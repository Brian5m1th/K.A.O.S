"""
Tests for the ManagedServer state machine and ServerManager orchestrator.

Priority #1 (highest risk) — tests cover:
    - ServerState enum values and transitions
    - ManagedServer lifecycle (initialize, shutdown, health_check)
    - Error states and recovery logic
    - State-change callback notifications
    - ServerManager multi-server orchestration

State machine reference (simplified):
    REGISTERED → INSTALLING → INSTALLED → STARTING → RUNNING → HEALTHY
                                                              ↘ DEGRADED
    The ``managed_server`` fixture sets initial state to INSTALLED so that
    ``initialize()`` (INSTALLED → STARTING → …) can be exercised directly.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from mcp_cli.core.server_manager import (
    ManagedServer,
    ServerManager,
    ServerState,
    LifecycleError,
)


# ── Helpers ──────────────────────────────────────────────────────────


def _all_transitions() -> list[tuple[ServerState, ServerState]]:
    """Return every allowed (from, to) pair defined in STATE_TRANSITIONS."""
    from mcp_cli.core.server_manager import STATE_TRANSITIONS

    pairs: list[tuple[ServerState, ServerState]] = []
    for src, targets in STATE_TRANSITIONS.items():
        for tgt in targets:
            pairs.append((src, tgt))
    return pairs


# ── ServerState enum ─────────────────────────────────────────────────


class TestServerStateEnum:
    """Verify the 11 state enum values and their string representations."""

    def test_state_values(self):
        """All ServerState members have the expected string values."""
        assert ServerState.REGISTERED.value == "registered"
        assert ServerState.INSTALLING.value == "installing"
        assert ServerState.INSTALLED.value == "installed"
        assert ServerState.STARTING.value == "starting"
        assert ServerState.RUNNING.value == "running"
        assert ServerState.HEALTHY.value == "healthy"
        assert ServerState.DEGRADED.value == "degraded"
        assert ServerState.STOPPING.value == "stopping"
        assert ServerState.STOPPED.value == "stopped"
        assert ServerState.UNINSTALLED.value == "uninstalled"
        assert ServerState.FAILED.value == "failed"

    def test_all_states_present(self):
        """Ensure exactly 11 states exist."""
        assert len(list(ServerState)) == 11

    def test_every_state_has_transitions(self):
        """Every state appears as a source in STATE_TRANSITIONS."""
        from mcp_cli.core.server_manager import STATE_TRANSITIONS

        for state in ServerState:
            assert state in STATE_TRANSITIONS, f"{state} missing from STATE_TRANSITIONS"


# ── ManagedServer initial state ──────────────────────────────────────


class TestManagedServerInitialState:
    """A freshly constructed ManagedServer starts in REGISTERED."""

    def test_fresh_constructor_is_registered(self):
        """Default state after __init__ is REGISTERED."""
        server = ManagedServer("fresh", {})
        assert server.state == ServerState.REGISTERED

    def test_initial_start_attempts_zero(self, managed_server):
        """_start_attempts counter starts at 0."""
        assert managed_server._start_attempts == 0

    def test_initial_tools_cache_empty(self, managed_server):
        """No tools are cached before initialization."""
        assert managed_server._tools_cache == []

    def test_initial_health_unknown(self, managed_server):
        """Last health result starts with 'unknown' status."""
        assert managed_server._last_health["status"] == "unknown"

    def test_default_max_restarts(self, managed_server):
        """Default max restart attempts is 3."""
        assert managed_server._max_restarts == 3


# ── ManagedServer state transitions ──────────────────────────────────


class TestManagedServerTransitions:
    """Verify the state machine enforces allowed transitions."""

    def test_transition_valid(self, managed_server):
        """INSTALLED → STARTING is a valid transition."""
        managed_server._transition(ServerState.STARTING)
        assert managed_server.state == ServerState.STARTING

    def test_transition_invalid_raises(self, managed_server):
        """INSTALLED → RUNNING (without going through STARTING) raises."""
        with pytest.raises(LifecycleError, match="Cannot transition from"):
            managed_server._transition(ServerState.RUNNING)

    def test_transition_from_stopped_to_starting(self):
        """STOPPED → STARTING is valid."""
        server = ManagedServer("s", {})
        server.state = ServerState.STOPPED
        server._transition(ServerState.STARTING)
        assert server.state == ServerState.STARTING

    def test_transition_from_failed_to_stopped(self):
        """FAILED → STOPPED is valid (recovery path)."""
        server = ManagedServer("s", {})
        server.state = ServerState.FAILED
        server._transition(ServerState.STOPPED)
        assert server.state == ServerState.STOPPED

    def test_transition_from_failed_to_registered(self):
        """FAILED → REGISTERED is valid (re-registration path)."""
        server = ManagedServer("s", {})
        server.state = ServerState.FAILED
        server._transition(ServerState.REGISTERED)
        assert server.state == ServerState.REGISTERED

    @pytest.mark.parametrize(
        "src, tgt",
        [
            (ServerState.REGISTERED, ServerState.INSTALLING),
            (ServerState.INSTALLING, ServerState.INSTALLED),
            (ServerState.INSTALLED, ServerState.STARTING),
            (ServerState.STARTING, ServerState.RUNNING),
            (ServerState.RUNNING, ServerState.HEALTHY),
            (ServerState.RUNNING, ServerState.DEGRADED),
            (ServerState.HEALTHY, ServerState.DEGRADED),
            (ServerState.DEGRADED, ServerState.HEALTHY),
            (ServerState.RUNNING, ServerState.STOPPING),
            (ServerState.STOPPING, ServerState.STOPPED),
            (ServerState.INSTALLING, ServerState.FAILED),
            (ServerState.INSTALLED, ServerState.UNINSTALLED),
            (ServerState.FAILED, ServerState.REGISTERED),
        ],
    )
    def test_various_valid_transitions(self, src, tgt):
        """Parameterised: a selection of known-valid transitions succeed."""
        server = ManagedServer("s", {})
        server.state = src
        server._transition(tgt)
        assert server.state == tgt


# ── ManagedServer state-change callbacks ─────────────────────────────


class TestManagedServerCallbacks:
    """State-change callbacks fire correctly."""

    def test_on_state_change_called(self, managed_server):
        """Register a callback; it must be invoked on transition."""
        calls: list[tuple[str, ServerState, ServerState]] = []
        managed_server.on_state_change(
            lambda sid, old, new: calls.append((sid, old, new))
        )
        managed_server._transition(ServerState.STARTING)

        assert len(calls) == 1
        server_id, old, new = calls[0]
        assert server_id == "test-server"
        assert old == ServerState.INSTALLED  # fixture pre-sets this
        assert new == ServerState.STARTING

    def test_multiple_callbacks(self, managed_server):
        """All registered callbacks fire on a single transition."""
        results: list[int] = []

        def cb_a(*_):
            results.append(1)

        def cb_b(*_):
            results.append(2)

        managed_server.on_state_change(cb_a)
        managed_server.on_state_change(cb_b)
        managed_server._transition(ServerState.STARTING)

        assert results == [1, 2]

    def test_callback_receives_correct_old_state(self, managed_server):
        """The ``old`` argument reflects the state *before* transition."""
        old_states: list[ServerState] = []
        managed_server.on_state_change(
            lambda _, old, __: old_states.append(old)
        )
        managed_server._transition(ServerState.STARTING)
        assert old_states[0] == ServerState.INSTALLED


# ── ManagedServer initialize() ───────────────────────────────────────


class TestManagedServerInitialize:
    """initialize() — full start-up through MCP handshake.

    The ``managed_server`` fixture starts in INSTALLED state, which is the
    correct pre-condition for the INSTALLED → STARTING → … transition.
    """

    @pytest.mark.asyncio
    async def test_initialize_success_transitions_to_healthy(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """Successful init: INSTALLED → STARTING → RUNNING → HEALTHY."""
        result = await managed_server.initialize()

        assert result is True
        assert managed_server.state == ServerState.HEALTHY
        mock_transport.connect.assert_called_once()

    @pytest.mark.asyncio
    async def test_initialize_sends_mcp_handshake(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """MCP initialize request and tools/list are sent."""
        await managed_server.initialize()

        # The first send_request must be "initialize"
        init_call = mock_transport.send_request.call_args_list[0]
        assert init_call[0][0] == "initialize"
        assert init_call[0][1]["protocolVersion"] == "2024-11-05"

        # A notification must have been sent
        mock_transport.send_notification.assert_called_once_with(
            "notifications/initialized", {}
        )

        # The second send_request is tools/list
        tools_call = mock_transport.send_request.call_args_list[1]
        assert tools_call[0][0] == "tools/list"

    @pytest.mark.asyncio
    async def test_initialize_caches_tools(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """Tools returned by tools/list are cached."""
        await managed_server.initialize()
        tools = managed_server.get_tools()
        assert len(tools) == 1
        assert tools[0]["name"] == "test_tool"

    @pytest.mark.asyncio
    async def test_initialize_failure_transitions_to_failed(
        self, managed_server
    ):
        """When transport creation fails, state becomes FAILED."""
        with patch(
            "mcp_cli.core.server_manager.TransportFactory.create",
            side_effect=RuntimeError("Connection refused"),
        ):
            result = await managed_server.initialize()

        assert result is False
        assert managed_server.state == ServerState.FAILED
        assert managed_server._last_health["status"] == "error"
        assert "Connection refused" in managed_server._last_health["error"]

    @pytest.mark.asyncio
    async def test_initialize_increments_start_attempts(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """Each call to initialize() increments the retry counter."""
        assert managed_server._start_attempts == 0
        await managed_server.initialize()
        assert managed_server._start_attempts == 1


# ── ManagedServer shutdown() ─────────────────────────────────────────


class TestManagedServerShutdown:
    """shutdown() — graceful tear-down."""

    @pytest.mark.asyncio
    async def test_shutdown_success(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """Server that was initialised can shut down cleanly."""
        await managed_server.initialize()
        result = await managed_server.shutdown()

        assert result is True
        assert managed_server.state == ServerState.STOPPED
        mock_transport.disconnect.assert_called_once()

    @pytest.mark.asyncio
    async def test_shutdown_when_stopped_raises(self, managed_server):
        """Calling shutdown() on a STOPPED server is invalid."""
        managed_server.state = ServerState.STOPPED
        with pytest.raises(LifecycleError):
            await managed_server.shutdown()

    @pytest.mark.asyncio
    async def test_shutdown_disconnect_failure(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """If transport.disconnect raises, shutdown returns False and goes FAILED."""
        await managed_server.initialize()
        mock_transport.disconnect.side_effect = RuntimeError("Kill failed")
        result = await managed_server.shutdown()
        assert result is False
        assert managed_server.state == ServerState.FAILED


# ── ManagedServer health_check() ─────────────────────────────────────


class TestManagedServerHealthCheck:
    """health_check() — status probing and state reactions."""

    @pytest.mark.asyncio
    async def test_health_check_no_transport_returns_stopped(
        self, managed_server
    ):
        """When transport is None, result status is 'stopped'."""
        managed_server.transport = None
        health = await managed_server.health_check()
        assert health["status"] == "stopped"
        assert health["error"] == "Not started"

    @pytest.mark.asyncio
    async def test_health_check_healthy(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """A successful health check from DEGRADED transitions to HEALTHY."""
        await managed_server.initialize()
        managed_server.state = ServerState.DEGRADED

        health = await managed_server.health_check()
        assert health["status"] == "healthy"
        assert managed_server.state == ServerState.HEALTHY

    @pytest.mark.asyncio
    async def test_health_check_down_triggers_failed(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """When health reports 'down', state transitions to FAILED."""
        await managed_server.initialize()
        mock_transport.health_check.return_value = {
            "status": "down",
            "latency_ms": 100,
            "error": "Process exited with code 1",
        }

        # The method goes FAILED → tries retry via initialize()
        # Since FAILED → STARTING is not a valid transition, LifecycleError
        # propagates — this documents the current behaviour.
        with pytest.raises(LifecycleError):
            await managed_server.health_check()

        assert managed_server.state == ServerState.FAILED

    @pytest.mark.asyncio
    async def test_health_check_degraded_from_healthy(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """Unknown health status from HEALTHY transitions to DEGRADED."""
        await managed_server.initialize()
        mock_transport.health_check.return_value = {
            "status": "unknown",
            "latency_ms": 200,
            "error": None,
        }

        await managed_server.health_check()
        assert managed_server.state == ServerState.DEGRADED

    @pytest.mark.asyncio
    async def test_health_check_stays_degraded(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """Unknown health while already DEGRADED keeps state as DEGRADED."""
        await managed_server.initialize()
        managed_server.state = ServerState.DEGRADED
        mock_transport.health_check.return_value = {
            "status": "unknown",
            "latency_ms": 200,
            "error": None,
        }

        await managed_server.health_check()
        # HEALTHY → DEGRADED is valid, but DEGRADED → DEGRADED is not
        # So it stays in the current "degraded" state without re-transition
        assert managed_server.state == ServerState.DEGRADED


# ── ManagedServer get_tools() / get_status() ─────────────────────────


class TestManagedServerStatus:
    """get_tools() and get_status() — introspection methods."""

    @pytest.mark.asyncio
    async def test_get_status_after_initialize(
        self, managed_server, mock_transport, patched_transport_factory
    ):
        """Status contains id, state, tools_count, health, and start_attempts."""
        await managed_server.initialize()
        status = managed_server.get_status()

        assert status["id"] == "test-server"
        assert status["state"] == ServerState.HEALTHY.value
        assert status["tools_count"] == 1
        assert status["start_attempts"] == 1
        assert status["health"]["status"] is not None

    def test_get_status_before_initialize(self):
        """Status before any lifecycle: INSTALLED state, zero tools."""
        server = ManagedServer("fresh", {"id": "fresh"})
        server.state = ServerState.INSTALLED
        status = server.get_status()
        assert status["id"] == "fresh"
        assert status["state"] == ServerState.INSTALLED.value
        assert status["tools_count"] == 0
        assert status["start_attempts"] == 0

    def test_get_tools_empty_initially(self, managed_server):
        """Tools cache is empty before initialize()."""
        assert managed_server.get_tools() == []


# ── ServerManager orchestration ──────────────────────────────────────


class TestServerManager:
    """ServerManager aggregates ManagedServer instances.

    These tests patch both PlatformConfig and ManagedServer.initialize /
    ManagedServer.shutdown so the orchestration layer can be exercised
    independently of the real state machine (which has its own dedicated
    tests above).
    """

    @pytest.mark.asyncio
    async def test_initial_state_empty(self, mock_platform_config):
        """A fresh ServerManager has no servers."""
        manager = ServerManager()
        assert manager._servers == {}

    @pytest.mark.asyncio
    async def test_start_all_returns_count(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """start_all() starts all enabled servers and returns the count."""
        manager = ServerManager()
        count = await manager.start_all()

        assert count == 2  # Two servers in mock_platform_config
        assert len(manager._servers) == 2
        assert "test-server" in manager._servers
        assert "server-b" in manager._servers

    @pytest.mark.asyncio
    async def test_start_all_skips_already_managed(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """start_all() warns and skips servers already in _servers."""
        manager = ServerManager()
        await manager.start_all()
        # Second call should not re-add
        count2 = await manager.start_all()
        assert count2 == 0
        assert len(manager._servers) == 2

    @pytest.mark.asyncio
    async def test_start_one(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """start_one(server_id) starts a single server by ID."""
        manager = ServerManager()
        ok = await manager.start_one("test-server")
        assert ok is True
        assert "test-server" in manager._servers

    @pytest.mark.asyncio
    async def test_start_one_not_found(self, mock_platform_config):
        """start_one() returns False for an unknown server ID."""
        manager = ServerManager()
        ok = await manager.start_one("does-not-exist")
        assert ok is False

    @pytest.mark.asyncio
    async def test_start_one_already_running(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """start_one() returns True immediately if already managed."""
        manager = ServerManager()
        await manager.start_one("test-server")
        ok = await manager.start_one("test-server")
        assert ok is True

    @pytest.mark.asyncio
    async def test_stop_one(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """stop_one() shuts down a server and removes it from _servers."""
        manager = ServerManager()
        await manager.start_one("test-server")
        ok = await manager.stop_one("test-server")
        assert ok is True
        assert "test-server" not in manager._servers

    @pytest.mark.asyncio
    async def test_stop_one_not_found(self, mock_platform_config):
        """stop_one() returns False for a server not in _servers."""
        manager = ServerManager()
        ok = await manager.stop_one("ghost")
        assert ok is False

    @pytest.mark.asyncio
    async def test_stop_all(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """stop_all() shuts down every server and clears the dict."""
        manager = ServerManager()
        await manager.start_all()
        stopped = await manager.stop_all()
        assert stopped == 2
        assert manager._servers == {}

    @pytest.mark.asyncio
    async def test_restart_one(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """restart_one() is a stop followed by a start of the same server."""
        manager = ServerManager()
        await manager.start_one("test-server")
        # ManagedServer.shutdown and .initialize are both patched to return True
        ok = await manager.restart_one("test-server")
        assert ok is True
        assert "test-server" in manager._servers

    @pytest.mark.asyncio
    async def test_emergency_stop(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """emergency_stop() clears all servers immediately."""
        manager = ServerManager()
        await manager.start_all()
        await manager.emergency_stop()
        assert manager._servers == {}

    @pytest.mark.asyncio
    async def test_get_status_all(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """get_status_all() returns a list of status dicts."""
        manager = ServerManager()
        await manager.start_all()
        statuses = manager.get_status_all()
        assert len(statuses) == 2
        ids = {s["id"] for s in statuses}
        assert ids == {"test-server", "server-b"}

    @pytest.mark.asyncio
    async def test_get_server(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """get_server() returns the ManagedServer or None."""
        manager = ServerManager()
        await manager.start_one("test-server")
        server = manager.get_server("test-server")
        assert server is not None
        assert server.id == "test-server"
        assert manager.get_server("nope") is None

    @pytest.mark.asyncio
    async def test_health_check_all(
        self, mock_platform_config, mock_transport, patched_transport_factory
    ):
        """health_check_all() returns health for each managed server."""
        manager = ServerManager()
        await manager.start_all()
        results = await manager.health_check_all()
        assert len(results) == 2
        for r in results:
            assert "id" in r
            assert "status" in r
