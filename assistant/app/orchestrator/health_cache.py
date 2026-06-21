import time
from enum import Enum

from loguru import logger


class HealthStatus(Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"


class ProviderHealthCache:
    def __init__(self, ttl_seconds: int = 30):
        self._cache: dict[str, tuple[HealthStatus, float]] = {}
        self._ttl = ttl_seconds

    async def is_healthy(self, provider_name: str) -> bool:
        status = await self.get_health(provider_name)
        return status == HealthStatus.HEALTHY

    async def get_health(self, provider_name: str) -> HealthStatus:
        now = time.monotonic()
        entry = self._cache.get(provider_name)

        if entry:
            status, timestamp = entry
            if now - timestamp < self._ttl:
                return status

        return HealthStatus.UNKNOWN

    async def set_health(self, provider_name: str, status: HealthStatus) -> None:
        self._cache[provider_name] = (status, time.monotonic())
        logger.debug(f"[health_cache] {provider_name} -> {status.value}")

    async def mark_healthy(self, provider_name: str) -> None:
        await self.set_health(provider_name, HealthStatus.HEALTHY)

    async def mark_unhealthy(self, provider_name: str) -> None:
        await self.set_health(provider_name, HealthStatus.UNHEALTHY)
        logger.warning(f"[health_cache] {provider_name} marked UNHEALTHY")

    async def refresh(self, provider_name: str, check_fn) -> HealthStatus:
        try:
            healthy = await check_fn()
            status = HealthStatus.HEALTHY if healthy else HealthStatus.UNHEALTHY
        except Exception:
            status = HealthStatus.UNHEALTHY

        await self.set_health(provider_name, status)
        return status

    @property
    def entries(self) -> int:
        return len(self._cache)

    def clear(self) -> None:
        self._cache.clear()
        logger.info("[health_cache] cleared")
