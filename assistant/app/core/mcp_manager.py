"""
MCP Manager — singleton responsible for initialising, running, and
shutting down MCP server subprocesses.
"""

import os
import shutil
import subprocess
import sys
import time
from threading import Lock

from loguru import logger

from app.core.mcp_registry import MCPRegistry
from app.core.mcp_server_base import MCPServer


class _MCPServerProcess(MCPServer):
    """Concrete MCPServer wrapping a local STDIO subprocess."""

    def __init__(self, config: dict) -> None:
        self._config = config
        self._name: str = config.get("name", "unnamed")
        self._command: str = config.get("command", "")
        self._args: list[str] = config.get("args", [])
        self._env_overrides: dict = config.get("env", {})
        self._process: subprocess.Popen | None = None
        self._tools_cache: list[dict] = []
        self._last_health: dict = {"status": "unknown", "latency_ms": 0, "error": None}

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def initialize(self) -> bool:
        if not self._command:
            logger.error("[mcp] server '{}' has no command configured", self._name)
            return False

        # Validate executable exists
        resolved = shutil.which(self._command)
        if not resolved:
            logger.error(
                "[mcp] executable '{}' not found in PATH for server '{}'",
                self._command,
                self._name,
            )
            self._last_health = {
                "status": "error",
                "latency_ms": 0,
                "error": f"Executable '{self._command}' not found in PATH",
            }
            return False

        # Build environment: inherit system env + overrides
        env = os.environ.copy()
        if self._env_overrides:
            env.update(self._env_overrides)

        # Build subprocess kwargs
        kwargs: dict = {
            "stdin": subprocess.PIPE,
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "env": env,
        }

        # Windows: suppress flashing CMD window
        if sys.platform == "win32":
            kwargs["creationflags"] = 0x08000000  # CREATE_NO_WINDOW

        try:
            self._process = subprocess.Popen(
                [resolved, *self._args],
                **kwargs,
            )
            logger.info("[mcp] server '{}' started (pid={})", self._name, self._process.pid)
            self._last_health = {"status": "healthy", "latency_ms": 0, "error": None}
            return True
        except (OSError, subprocess.SubprocessError) as exc:
            logger.error("[mcp] failed to start server '{}': {}", self._name, exc)
            self._last_health = {
                "status": "error",
                "latency_ms": 0,
                "error": str(exc),
            }
            return False

    def shutdown(self) -> bool:
        if self._process is None:
            return True
        try:
            self._process.terminate()
            self._process.wait(timeout=5)
            logger.info("[mcp] server '{}' terminated (pid={})", self._name, self._process.pid)
            self._process = None
            return True
        except (OSError, subprocess.TimeoutExpired) as exc:
            logger.warning("[mcp] force-killing server '{}': {}", self._name, exc)
            try:
                self._process.kill()
                self._process.wait(timeout=3)
            except Exception:
                pass
            self._process = None
            return False

    # ------------------------------------------------------------------
    # Tools
    # ------------------------------------------------------------------

    def get_tools(self) -> list[dict]:
        return self._tools_cache

    def call_tool(self, tool_name: str, params: dict) -> dict:
        # TODO: Implement actual STDIO JSON-RPC exchange per MCP spec
        # For now, return a stub
        return {
            "status": "not_implemented",
            "tool": tool_name,
            "message": f"MCP STDIO transport not yet implemented for '{self._name}'",
        }

    # ------------------------------------------------------------------
    # Health
    # ------------------------------------------------------------------

    def get_health(self) -> dict:
        if self._process is None:
            return {"status": "stopped", "latency_ms": 0, "error": "Process not running"}
        # Ping process
        t0 = time.monotonic()
        ret = self._process.poll()
        latency_ms = int((time.monotonic() - t0) * 1000)
        if ret is not None:
            self._last_health = {
                "status": "error",
                "latency_ms": latency_ms,
                "error": f"Process exited with code {ret}",
            }
            self._process = None
        else:
            self._last_health = {
                "status": "healthy",
                "latency_ms": latency_ms,
                "error": None,
            }
        return dict(self._last_health)


class MCPManager:
    """Singleton that manages all configured MCP server subprocesses."""

    _instance: "MCPManager | None" = None
    _lock: Lock = Lock()

    def __new__(cls) -> "MCPManager":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._servers: dict[str, _MCPServerProcess] = {}
                    cls._instance._initialized = False
        return cls._instance

    # ------------------------------------------------------------------
    # Boot / shutdown
    # ------------------------------------------------------------------

    def start_all(self) -> int:
        """Read the registry and start all enabled MCP servers.

        Returns the number of successfully started servers.
        """
        registry = MCPRegistry.load()
        server_configs = MCPRegistry.get_enabled_servers()
        started = 0
        for cfg in server_configs:
            name = cfg.get("name", "unnamed")
            if name in self._servers:
                logger.warning("[mcp] server '{}' already registered, skipping", name)
                continue
            proc = _MCPServerProcess(cfg)
            if proc.initialize():
                self._servers[name] = proc
                started += 1
            else:
                logger.error("[mcp] server '{}' failed to start", name)
        self._initialized = True
        logger.info("[mcp] started {}/{} servers", started, len(server_configs))
        return started

    def shutdown_all(self) -> int:
        """Gracefully stop all running MCP servers.

        Returns the number of successfully stopped servers.
        """
        stopped = 0
        for name, proc in list(self._servers.items()):
            if proc.shutdown():
                stopped += 1
            del self._servers[name]
        self._initialized = False
        logger.info("[mcp] stopped {}/{} servers", stopped, stopped)
        return stopped

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def get_server(self, name: str) -> _MCPServerProcess | None:
        return self._servers.get(name)

    def list_servers(self) -> list[dict]:
        return [
            {
                "name": name,
                "health": proc.get_health(),
                "tools_count": len(proc.get_tools()),
            }
            for name, proc in self._servers.items()
        ]

    def is_initialized(self) -> bool:
        return self._initialized

    @property
    def servers(self) -> dict[str, _MCPServerProcess]:
        return dict(self._servers)
