"""
MCP Registry — manages the ``config/mcp.json`` file that lists configured
MCP server definitions.
"""

import json
from pathlib import Path

from loguru import logger

from app.core.runtime_path_resolver import RuntimePathResolver

MCP_CONFIG_FILE = "mcp.json"

DEFAULT_REGISTRY: dict = {
    "servers": [
        {
            "name": "example",
            "command": "python",
            "args": ["-m", "mcp_example_server"],
            "enabled": False,
            "env": {},
        }
    ]
}


class MCPRegistry:
    """Reads and writes the MCP server registry file (``config/mcp.json``)."""

    @classmethod
    def _path(cls) -> Path:
        return RuntimePathResolver.get_config_path() / MCP_CONFIG_FILE

    @classmethod
    def load(cls) -> dict:
        """Load the MCP registry from disk.

        Returns the registry dict, or a default template if the file
        does not exist or is corrupted.
        """
        path = cls._path()
        if not path.exists():
            logger.info("[mcp] registry file not found at {}, using defaults", path)
            return dict(DEFAULT_REGISTRY)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or "servers" not in data:
                logger.warning("[mcp] invalid registry format, resetting to defaults")
                return dict(DEFAULT_REGISTRY)
            return data
        except (json.JSONDecodeError, PermissionError) as exc:
            logger.warning("[mcp] failed to read registry: {}", exc)
            return dict(DEFAULT_REGISTRY)

    @classmethod
    def save(cls, registry: dict) -> None:
        """Persist the MCP registry to disk."""
        path = cls._path()
        path.parent.mkdir(parents=True, exist_ok=True)
        content = json.dumps(registry, indent=2, ensure_ascii=False)
        path.write_text(content, encoding="utf-8")
        logger.info("[mcp] registry saved to {}", path)

    @classmethod
    def get_enabled_servers(cls) -> list[dict]:
        """Return only the enabled server entries from the registry."""
        registry = cls.load()
        return [s for s in registry.get("servers", []) if s.get("enabled", False)]
