import json
from unittest.mock import patch, MagicMock
from app.tools.github_tool import call_tool
from app.core.mcp_manager import MCPManager
from app.core.mcp_registry import MCPRegistry


class TestGithubMCP:
    def test_call_tool_read_code_fallback(self) -> None:
        # Without real internet/credentials, it returns a clear fallback message
        res = call_tool("github_read_code", {"repo": "test/repo", "path": "test.py"})
        assert "content" in res
        text = res["content"][0]["text"]
        assert "test/repo" in text or "Failed" in text

    def test_call_tool_create_pr_fallback(self) -> None:
        res = call_tool(
            "github_create_pull_request",
            {
                "repo": "test/repo",
                "title": "Fix something",
                "head": "patch-1",
            },
        )
        assert "content" in res
        text = res["content"][0]["text"]
        assert "Fix something" in text or "Success" in text or "created" in text

    def test_call_tool_unsupported(self) -> None:
        res = call_tool("unknown_tool", {})
        assert res.get("isError") is True

    @patch("subprocess.Popen")
    def test_mcp_manager_handshake(self, mock_popen) -> None:
        # Mock the subprocess stdin/stdout to check initialize & tools/list
        mock_proc = MagicMock()
        mock_proc.pid = 9999
        mock_proc.stdin = MagicMock()
        mock_proc.stdout = MagicMock()

        # Responses:
        # 1. initialize response
        # 2. tools/list response
        responses = [
            # initialize response
            json.dumps(
                {
                    "jsonrpc": "2.0",
                    "id": 12345,  # will be dynamic, mock will return this to match
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {},
                        "serverInfo": {"name": "github-mcp", "version": "1.0.0"},
                    },
                }
            ).encode("utf-8")
            + b"\n",
            # tools/list response
            json.dumps(
                {
                    "jsonrpc": "2.0",
                    "id": 12345,
                    "result": {"tools": [{"name": "github_read_code"}]},
                }
            ).encode("utf-8")
            + b"\n",
        ]

        def mock_readline():
            if responses:
                resp = responses.pop(0)
                # Override the dynamic request ID in the mock read to match
                # whatever was written to stdin
                return resp
            return b""

        mock_proc.stdout.readline.side_effect = mock_readline
        mock_popen.return_value = mock_proc

        # Mock writing to stdin to capture request id
        written_data = []

        def mock_write(b_data):
            written_data.append(b_data)
            try:
                payload = json.loads(b_data.decode("utf-8").strip())
                req_id = payload.get("id")
                # update the response lists to have the matching request id
                if responses:
                    curr_resp = json.loads(responses[0].decode("utf-8"))
                    curr_resp["id"] = req_id
                    responses[0] = json.dumps(curr_resp).encode("utf-8") + b"\n"
            except Exception:
                pass

        mock_proc.stdin.write.side_effect = mock_write

        # Initialize the MCPManager process wrapper
        server_config = {
            "name": "github",
            "command": "python",
            "args": ["-m", "app.tools.github_tool"],
            "enabled": True,
        }

        # Clear active servers
        MCPManager._instances = {}
        manager = MCPManager()

        # Test loading registry and configuring
        with patch.object(
            MCPRegistry, "get_enabled_servers", return_value=[server_config]
        ):
            # Start/initialize servers
            success = manager.start_all()
            assert success == 1

            # Verify we registered tools in manager
            server = manager.get_server("github")
            assert server is not None
            tools = server.get_tools()
            assert len(tools) == 1
            assert tools[0]["name"] == "github_read_code"

            # Shutdown
            manager.shutdown_all()
