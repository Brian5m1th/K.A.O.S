"""
Smoke tests for CLI command helpers.

Priority #3 — tests cover:
    - _install_server with various install methods (npx, pip, unknown)
    - Subprocess error handling (timeout, command not found)
    - _install_all batching helper
"""

import sys
from unittest.mock import patch, MagicMock

import pytest

from mcp_cli.commands.install import _install_server, _install_all


# ── _install_server smoke tests ──────────────────────────────────────


class TestInstallServer:
    """_install_server() dispatches to the correct package manager."""

    # ── npx method ───────────────────────────────────────────────

    @pytest.mark.asyncio
    async def test_npx_success(self, temp_dir, mock_subprocess_run):
        """npx-based install runs 'npx -y <package>'."""
        entry = {
            "id": "test-server",
            "version": "1.0.0",
            "install": {"method": "npx", "command": "npx @scope/test-server"},
        }
        result = await _install_server(entry)
        assert result is True

        mock_subprocess_run.assert_called_once()
        args = mock_subprocess_run.call_args[0][0]
        assert args[0] == "npx"
        assert args[1] == "-y"
        assert "@scope/test-server" in args

    @pytest.mark.asyncio
    async def test_npx_saves_config(self, temp_dir, mock_subprocess_run):
        """After successful npx install, a server config YAML is written."""
        entry = {
            "id": "saved-server",
            "version": "2.0.0",
            "install": {"method": "npx", "command": "npx some-package"},
        }
        result = await _install_server(entry)
        assert result is True

        # Config should be saved to MCP_HOME/servers/saved-server.yaml
        config_path = temp_dir / "servers" / "saved-server.yaml"
        assert config_path.exists()

        import yaml
        with open(config_path, "r") as f:
            data = yaml.safe_load(f)
        assert data["id"] == "saved-server"
        assert data["version"] == "2.0.0"
        assert data["installed"] is True
        assert data["install_method"] == "npx"

    # ── pip method ───────────────────────────────────────────────

    @pytest.mark.asyncio
    async def test_pip_success(self, temp_dir, mock_subprocess_run):
        """pip-based install runs 'python -m pip install <package>'."""
        entry = {
            "id": "pip-server",
            "version": "0.1.0",
            "install": {"method": "pip", "command": "pip install mcp-something"},
        }
        result = await _install_server(entry)
        assert result is True

        mock_subprocess_run.assert_called_once()
        args = mock_subprocess_run.call_args[0][0]
        assert args[0] == sys.executable
        assert args[1] == "-m"
        assert args[2] == "pip"
        assert args[3] == "install"
        assert "mcp-something" in args

    # ── uvx method ───────────────────────────────────────────────

    @pytest.mark.asyncio
    async def test_uvx_success(self, temp_dir, mock_subprocess_run):
        """uvx-based install runs 'uvx <tool>'."""
        entry = {
            "id": "uvx-server",
            "version": "1.0.0",
            "install": {"method": "uvx", "command": "uvx @modelcontextprotocol/server-github"},
        }
        result = await _install_server(entry)
        assert result is True

        args = mock_subprocess_run.call_args[0][0]
        assert args[0] == "uvx"
        assert "@modelcontextprotocol/server-github" in args

    # ── npm method ───────────────────────────────────────────────

    @pytest.mark.asyncio
    async def test_npm_success(self, temp_dir, mock_subprocess_run):
        """npm-based install runs 'npm install -g <package>'."""
        entry = {
            "id": "npm-server",
            "version": "1.0.0",
            "install": {"method": "npm", "command": "npm install -g @scope/tool"},
        }
        result = await _install_server(entry)
        assert result is True

        args = mock_subprocess_run.call_args[0][0]
        assert args[0] == "npm"
        assert args[1] == "install"
        assert args[2] == "-g"
        assert "@scope/tool" in args

    # ── docker method ────────────────────────────────────────────

    @pytest.mark.asyncio
    async def test_docker_returns_true_without_subprocess(self, temp_dir):
        """Docker-based install returns True without invoking subprocess."""
        entry = {
            "id": "docker-server",
            "version": "1.0.0",
            "install": {"method": "docker", "command": "docker pull my-image"},
        }
        result = await _install_server(entry)
        assert result is True

    # ── unknown method ───────────────────────────────────────────

    @pytest.mark.asyncio
    async def test_unknown_method_returns_false(self, temp_dir):
        """An install method that isn't recognised returns False."""
        entry = {
            "id": "weird-server",
            "install": {"method": "helm", "command": "helm install foo"},
        }
        result = await _install_server(entry)
        assert result is False

    # ── subprocess failure modes ─────────────────────────────────

    @pytest.mark.asyncio
    async def test_install_failure_nonzero_exit(self, temp_dir, mock_subprocess_run):
        """A non-zero return code from subprocess returns False."""
        mock_subprocess_run.return_value.returncode = 1
        mock_subprocess_run.return_value.stderr = "Installation error"

        entry = {
            "id": "fail-server",
            "install": {"method": "npx", "command": "npx broken-package"},
        }
        result = await _install_server(entry)
        assert result is False

    @pytest.mark.asyncio
    async def test_install_timeout(self, temp_dir, mock_subprocess_run):
        """A subprocess.TimeoutExpired exception returns False."""
        import subprocess
        mock_subprocess_run.side_effect = subprocess.TimeoutExpired(
            cmd="npx foo", timeout=120
        )

        entry = {
            "id": "timeout-server",
            "install": {"method": "npx", "command": "npx slow-package"},
        }
        result = await _install_server(entry)
        assert result is False

    @pytest.mark.asyncio
    async def test_install_command_not_found(self, temp_dir, mock_subprocess_run):
        """A FileNotFoundError exception returns False."""
        mock_subprocess_run.side_effect = FileNotFoundError("npx not found")

        entry = {
            "id": "missing-cmd-server",
            "install": {"method": "npx", "command": "npx some-package"},
        }
        result = await _install_server(entry)
        assert result is False


# ── _install_all helper ──────────────────────────────────────────────


class TestInstallAll:
    """_install_all() batches multiple installs sequentially."""

    @pytest.mark.asyncio
    async def test_all_succeed(self, temp_dir, mock_subprocess_run):
        """When all installs succeed, the result list is all True."""
        servers = [
            {"id": "a", "install": {"method": "npx", "command": "npx pkg-a"}},
            {"id": "b", "install": {"method": "npx", "command": "npx pkg-b"}},
            {"id": "c", "install": {"method": "npx", "command": "npx pkg-c"}},
        ]
        results = await _install_all(servers)
        assert results == [True, True, True]

    @pytest.mark.asyncio
    async def test_partial_failure(self, temp_dir, mock_subprocess_run):
        """When one install fails, only that result is False."""
        call_count = 0

        def side_effect(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            proc = MagicMock()
            if call_count == 2:  # Second install fails
                proc.returncode = 1
                proc.stderr = "error"
            else:
                proc.returncode = 0
            return proc

        mock_subprocess_run.side_effect = side_effect

        servers = [
            {"id": "s1", "install": {"method": "npx", "command": "npx ok"}},
            {"id": "s2", "install": {"method": "npx", "command": "npx fail"}},
            {"id": "s3", "install": {"method": "npx", "command": "npx ok2"}},
        ]
        results = await _install_all(servers)
        assert results == [True, False, True]

    @pytest.mark.asyncio
    async def test_empty_list(self, temp_dir):
        """An empty server list returns an empty result list."""
        results = await _install_all([])
        assert results == []
