import pytest
from unittest.mock import patch, MagicMock
from app.core.opencode_executor import OpenCodeExecutor


class TestOpenCodeExecutor:
    def test_validate_command_whitelisted(self) -> None:
        assert OpenCodeExecutor.validate_command("git status") is True
        assert OpenCodeExecutor.validate_command("python main.py") is True
        assert OpenCodeExecutor.validate_command("pytest tests/") is True

    def test_validate_command_blacklisted(self) -> None:
        assert OpenCodeExecutor.validate_command("rm -rf /") is False
        assert OpenCodeExecutor.validate_command("format-volume D:") is False
        assert OpenCodeExecutor.validate_command("shutdown now") is False

    def test_validate_command_unknown(self) -> None:
        assert OpenCodeExecutor.validate_command("curl https://malicious.com") is False
        assert OpenCodeExecutor.validate_command("powershell.exe Set-ExecutionPolicy") is False

    def test_execute_without_approval_fails(self) -> None:
        res = OpenCodeExecutor.execute("git status", user_approved=False)
        assert res["status"] == "error"
        assert "Consentimento" in res["message"]

    def test_execute_invalid_command_fails(self) -> None:
        res = OpenCodeExecutor.execute("rm -rf /", user_approved=True)
        assert res["status"] == "error"
        assert "segurança" in res["message"]

    @patch("subprocess.run")
    @patch("shutil.which")
    def test_execute_in_docker_sandbox(self, mock_which, mock_run) -> None:
        mock_which.return_value = "/usr/bin/docker"  # Docker is available
        mock_res = MagicMock()
        mock_res.returncode = 0
        mock_res.stdout = "Everything is clean"
        mock_res.stderr = ""
        mock_run.return_value = mock_res

        res = OpenCodeExecutor.execute("git status", user_approved=True)

        assert res["status"] == "success"
        assert res["sandbox"] == "docker"
        assert res["stdout"] == "Everything is clean"

    @patch("subprocess.run")
    @patch("shutil.which")
    def test_execute_in_local_fallback(self, mock_which, mock_run) -> None:
        mock_which.return_value = None  # Docker is not available
        mock_res = MagicMock()
        mock_res.returncode = 0
        mock_res.stdout = "Local git status"
        mock_res.stderr = ""
        mock_run.return_value = mock_res

        res = OpenCodeExecutor.execute("git status", user_approved=True)

        assert res["status"] == "success"
        assert res["sandbox"] == "local-fallback"
        assert res["stdout"] == "Local git status"
