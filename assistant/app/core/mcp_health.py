"""
MCP Health Monitor — aggregates health information for all registered
MCP servers, providing latency measurements and connectivity status.
"""

import time
from threading import Lock

from loguru import logger

from app.core.mcp_manager import MCPManager


class MCPHealthMonitor:
    """Periodically collects health data from MCP servers.

    Uses a simple TTL cache to avoid hammering subprocess health checks.
    """

    _cache: dict[str, dict] = {}
    _cache_ts: float = 0.0
    _cache_ttl: float = 15.0  # seconds
    _lock: Lock = Lock()

    @classmethod
    def get_health_summary(cls) -> list[dict]:
        """Return a list of health statuses for all running MCP servers.

        Results are cached for ``_cache_ttl`` seconds to avoid overhead.
        """
        now = time.monotonic()
        if cls._cache and (now - cls._cache_ts) < cls._cache_ttl:
            return list(cls._cache.values())

        with cls._lock:
            # Double-check after acquiring lock
            if cls._cache and (now - cls._cache_ts) < cls._cache_ttl:
                return list(cls._cache.values())

            manager = MCPManager()
            servers = manager.list_servers()
            summary = []
            for entry in servers:
                health = entry["health"]
                summary.append(
                    {
                        "name": entry["name"],
                        "status": health.get("status", "unknown"),
                        "latency_ms": health.get("latency_ms", 0),
                        "error": health.get("error"),
                        "tools_count": entry["tools_count"],
                    }
                )

            cls._cache = {s["name"]: s for s in summary}
            cls._cache_ts = now
            return summary

    @classmethod
    def invalidate_cache(cls) -> None:
        """Force cache refresh on next call."""
        with cls._lock:
            cls._cache = {}
            cls._cache_ts = 0.0
            logger.debug("[mcp] health cache invalidated")
