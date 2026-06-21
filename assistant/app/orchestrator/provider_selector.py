from typing import Optional

from loguru import logger

from app.repositories.provider_config_repository import (
    ProviderConfigRecord,
    ProviderConfigRepository,
)
from app.orchestrator.health_cache import ProviderHealthCache
from app.orchestrator.circuit_breaker import CircuitBreaker


class ProviderSelector:
    def __init__(
        self,
        config_repo: ProviderConfigRepository,
        health_cache: ProviderHealthCache,
        circuit_breaker: Optional[CircuitBreaker] = None,
    ):
        self._config_repo = config_repo
        self._health_cache = health_cache
        self._circuit_breaker = circuit_breaker

    async def select(
        self, provider_name: str, provider_type: str = "chat"
    ) -> Optional[ProviderConfigRecord]:
        logger.info(
            f"[start] ProviderSelector - select provider={provider_name} type={provider_type}"
        )

        if self._circuit_breaker:
            state = self._circuit_breaker.state
            if state.value == "OPEN":
                logger.warning(f"[provider_selector] circuit OPEN for {provider_name}")
                return None

        healthy = await self._health_cache.is_healthy(provider_name)
        if not healthy:
            logger.warning(f"[provider_selector] cache says unhealthy: {provider_name}")
            return None

        config = await self._config_repo.get_by_name(provider_name)
        if config and config.is_active:
            logger.debug(f"[finish] ProviderSelector - selected {provider_name}")
            return config

        logger.warning(f"[provider_selector] no active config for {provider_name}")
        return None

    async def select_by_type(
        self, provider_type: str = "chat"
    ) -> Optional[ProviderConfigRecord]:
        providers = await self._config_repo.get_by_type(provider_type)
        for provider in providers:
            healthy = await self._health_cache.is_healthy(provider.provider_name)
            if healthy:
                logger.info(
                    f"[provider_selector] selected {provider.provider_name} "
                    f"for type={provider_type}"
                )
                return provider
        return None

    async def select_healthy(
        self, candidate_names: list[str]
    ) -> Optional[ProviderConfigRecord]:
        for name in candidate_names:
            healthy = await self._health_cache.is_healthy(name)
            if healthy:
                config = await self._config_repo.get_by_name(name)
                if config:
                    return config
        return None
