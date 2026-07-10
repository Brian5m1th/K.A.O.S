"""Runtime Registry — Orchestrator for all runtime modules.

SDD-KAOS-EVOLUTION-001: Provides dynamic runtime discovery (AI, Communication, Memory, etc.).
"""

from typing import Any, Dict
from loguru import logger


class RuntimeRegistry:
    """Registry to discover and obtain references to active K.A.O.S runtimes."""

    _runtimes: Dict[str, Any] = {}

    @classmethod
    def register(cls, name: str, runtime: Any) -> None:
        """Register a runtime implementation in the registry."""
        cls._runtimes[name] = runtime
        logger.info(f"[RuntimeRegistry] Runtime registered: '{name}'")

    @classmethod
    def get(cls, name: str) -> Any | None:
        """Retrieve a registered runtime by its name."""
        return cls._runtimes.get(name)

    @classmethod
    def list_all(cls) -> list[str]:
        """List all active runtime identifiers."""
        return list(cls._runtimes.keys())
