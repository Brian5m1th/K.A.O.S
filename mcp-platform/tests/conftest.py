"""
Shared pytest fixtures for mcp-platform unit tests.

Fixtures:
    temp_dir: Temporary directory with MCP_HOME set for config isolation
    mock_transport: MagicMock mimicking MCPTransport interface
    mock_subprocess: Patched subprocess.Popen / subprocess.run
    managed_server: ManagedServer with a basic registry entry
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory and set MCP_HOME to isolate file I/O.

    All config/save/load operations under test will write here instead of
    the real ~/.config/mcp/ location. Restores the previous MCP_HOME value
    (or absence) after the test.
    """
    old_home = os.environ.pop("MCP_HOME", None)
    with tempfile.TemporaryDirectory() as td:
        os.environ["MCP_HOME"] = td
        yield Path(td)
    if old_home is not None:
        os.environ["MCP_HOME"] = old_home
    else:
        os.environ.pop("MCP_HOME", None)


@pytest.fixture
def mock_transport():
    """Return an AsyncMock that fulfills the MCPTransport abstract interface.

    All async methods (connect, disconnect, health_check, send_request,
    send_notification) are AsyncMock instances so ``await`` works correctly.
    Default return values let callers exercise ManagedServer without a real
    subprocess or network connection.
    """
    transport = AsyncMock()
    transport.connect.return_value = True
    transport.disconnect.return_value = True
    transport.health_check.return_value = {
        "status": "healthy",
        "latency_ms": 5,
        "error": None,
    }
    transport.send_request.return_value = {
        "tools": [{"name": "test_tool", "description": "A test tool"}],
    }
    transport.send_notification.return_value = None
    transport.get_server_info.return_value = {
        "type": "stdio",
        "pid": 9999,
        "command": "test",
        "args": [],
        "connected_at": 1000.0,
    }
    return transport


@pytest.fixture
def mock_subprocess_run():
    """Patch subprocess.run to return a successful result by default.

    Test functions can mutate the returned MagicMock's attributes
    (e.g. ``mock_run.return_value.returncode = 1``) to simulate failures.
    """
    with patch("mcp_cli.commands.install.subprocess.run") as mock_run:
        mock_proc = MagicMock()
        mock_proc.returncode = 0
        mock_proc.stdout = "installed successfully"
        mock_proc.stderr = ""
        mock_run.return_value = mock_proc
        yield mock_run


@pytest.fixture
def patched_transport_factory(mock_transport):
    """Patch TransportFactory.create inside server_manager to return ``mock_transport``.

    Apply this fixture to any test that exercises ``ManagedServer.initialize()``
    so that the factory call returns a controllable mock instead of starting
    a real subprocess.
    """
    with patch(
        "mcp_cli.core.server_manager.TransportFactory.create",
        return_value=mock_transport,
    ):
        yield


@pytest.fixture
def managed_server():
    """Create a ManagedServer in INSTALLED state with a minimal registry entry.

    The ``initialize()`` method requires the server to be in INSTALLED state
    (INSTALLED → STARTING → RUNNING → HEALTHY).  This fixture pre-sets the
    state so lifecycle tests work correctly.
    """
    from mcp_cli.core.server_manager import ManagedServer, ServerState

    entry = {
        "id": "test-server",
        "name": "Test Server",
        "version": "1.0.0",
        "protocol": {
            "transports": [
                {"type": "stdio", "command": "test", "args": []},
            ],
        },
        "plan": "phase-1",
    }
    server = ManagedServer("test-server", entry)
    server.state = ServerState.INSTALLED
    return server


@pytest.fixture
def mock_platform_config():
    """Patch PlatformConfig inside server_manager to return controllable data.

    The mock returns a fixed list of enabled servers and supports
    get_server() lookups so ServerManager can operate without real YAML files.
    Also patches ManagedServer.initialize so ServerManager tests can exercise
    orchestration logic without hitting the full state machine.
    """
    import mcp_cli.core.server_manager as sm

    fake_servers = [
        {
            "id": "test-server",
            "name": "Test Server",
            "version": "1.0.0",
            "protocol": {
                "transports": [{"type": "stdio", "command": "test", "args": []}],
            },
            "plan": "phase-1",
        },
        {
            "id": "server-b",
            "name": "Server B",
            "version": "1.0.0",
            "protocol": {
                "transports": [{"type": "stdio", "command": "other", "args": []}],
            },
            "plan": "phase-1",
        },
    ]

    def get_server_side_effect(server_id):
        for s in fake_servers:
            if s["id"] == server_id:
                return s
        return None

    mock_config = MagicMock()
    mock_config.get_enabled_servers.return_value = fake_servers
    mock_config.get_server.side_effect = get_server_side_effect

    with patch.object(sm, "PlatformConfig", return_value=mock_config), patch.object(
        sm.ManagedServer, "initialize", AsyncMock(return_value=True)
    ), patch.object(sm.ManagedServer, "shutdown", AsyncMock(return_value=True)):
        yield mock_config
