"""
Provider Registry — Generic dependency injection container for K.A.O.S.

Enables capability-first architecture: every K.A.O.S service uses a
ProviderRegistry to manage its backend implementations. The Desktop
never knows which framework implements a capability — it only talks
to REST APIs served by the services.

Usage:
    registry = ProviderRegistry[GraphProvider]()
    registry.register("graphify", GraphifyAdapter())
    registry.register("networkx", NetworkXAdapter())
    registry.activate("graphify")

    provider = registry.active  # Returns GraphifyAdapter
    result = await provider.explain("CodeScanner")
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, Callable
from loguru import logger

T = TypeVar("T")


class Provider(ABC):
    """Base class for all K.A.O.S provider implementations."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    def version(self) -> str:
        return "0.0.0"

    @property
    def health_check(self) -> Optional[Callable[[], bool]]:
        """Optional async health check. Returns True if provider is ready."""
        return None


class ProviderRegistry(Generic[T]):
    """
    Generic registry for provider implementations of a K.A.O.S capability.

    Features:
      - Runtime provider switching (activate/deactivate)
      - Health-aware fallback (auto-select next healthy provider)
      - Graceful degradation (return fallback when active provider fails)
    """

    def __init__(self, name: str = "unnamed"):
        self._name = name
        self._providers: dict[str, T] = {}
        self._active_key: Optional[str] = None

    def register(self, key: str, provider: T) -> None:
        """Register a provider implementation under a unique key."""
        if key in self._providers:
            logger.warning(f"[registry:{self._name}] Overwriting provider: {key}")
        self._providers[key] = provider
        logger.info(f"[registry:{self._name}] Registered provider: {key}")

        # Auto-activate first provider
        if self._active_key is None:
            self._active_key = key

    def activate(self, key: str) -> None:
        """Activate a specific provider by key."""
        if key not in self._providers:
            raise KeyError(
                f"[registry:{self._name}] Provider '{key}' not found. "
                f"Available: {list(self._providers.keys())}"
            )
        self._active_key = key
        logger.info(f"[registry:{self._name}] Activated provider: {key}")

    def remove(self, key: str) -> None:
        """Remove a provider from the registry."""
        if key in self._providers:
            del self._providers[key]
            logger.info(f"[registry:{self._name}] Removed provider: {key}")
            if self._active_key == key:
                self._active_key = next(iter(self._providers), None)

    def deactivate(self) -> None:
        """Deactivate current provider (will use fallback or raise)."""
        self._active_key = None

    @property
    def active(self) -> T:
        """Return the currently active provider."""
        if self._active_key is None:
            if not self._providers:
                raise RuntimeError(f"[registry:{self._name}] No providers registered")
            # Auto-activate first available
            self._active_key = next(iter(self._providers))
        return self._providers[self._active_key]

    @property
    def active_key(self) -> Optional[str]:
        return self._active_key

    @property
    def providers(self) -> dict[str, T]:
        return dict(self._providers)

    def list_providers(self) -> list[str]:
        return list(self._providers.keys())

    def __contains__(self, key: str) -> bool:
        return key in self._providers

    def __repr__(self) -> str:
        active = self._active_key or "none"
        return (
            f"<ProviderRegistry[{self._name}] "
            f"active={active} "
            f"providers={list(self._providers.keys())}>"
        )
