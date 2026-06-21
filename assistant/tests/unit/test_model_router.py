import asyncio
from unittest.mock import AsyncMock

import pytest

from app.models.model_router import ModelSelection
from app.models.capability_policy import (
    ResolvedPolicy,
)
from app.orchestrator.health_cache import (
    HealthStatus,
    ProviderHealthCache,
)
from app.orchestrator.circuit_breaker import (
    CircuitBreaker,
    CircuitState,
)
from app.orchestrator.provider_selector import ProviderSelector
from app.repositories.provider_config_repository import ProviderConfigRecord


class TestProviderHealthCache:
    @pytest.mark.asyncio
    async def test_default_is_unknown(self):
        cache = ProviderHealthCache(ttl_seconds=30)
        status = await cache.get_health("unknown-provider")
        assert status == HealthStatus.UNKNOWN

    @pytest.mark.asyncio
    async def test_mark_healthy(self):
        cache = ProviderHealthCache(ttl_seconds=30)
        await cache.mark_healthy("ollama")
        assert await cache.is_healthy("ollama") is True

    @pytest.mark.asyncio
    async def test_mark_unhealthy(self):
        cache = ProviderHealthCache(ttl_seconds=30)
        await cache.mark_unhealthy("ollama")
        assert await cache.is_healthy("ollama") is False

    @pytest.mark.asyncio
    async def test_ttl_expiry(self):
        cache = ProviderHealthCache(ttl_seconds=0)
        await cache.mark_healthy("ollama")
        status = await cache.get_health("ollama")
        assert status == HealthStatus.UNKNOWN

    @pytest.mark.asyncio
    async def test_entries_count(self):
        cache = ProviderHealthCache(ttl_seconds=30)
        await cache.mark_healthy("ollama")
        await cache.mark_unhealthy("openai")
        assert cache.entries == 2

    def test_clear(self):
        cache = ProviderHealthCache(ttl_seconds=30)
        cache._cache["test"] = (HealthStatus.HEALTHY, 0.0)
        cache.clear()
        assert cache.entries == 0

    @pytest.mark.asyncio
    async def test_refresh_healthy(self):
        cache = ProviderHealthCache(ttl_seconds=30)
        async def check():
            return True
        status = await cache.refresh("ollama", check)
        assert status == HealthStatus.HEALTHY
        assert await cache.is_healthy("ollama") is True

    @pytest.mark.asyncio
    async def test_refresh_unhealthy(self):
        cache = ProviderHealthCache(ttl_seconds=30)
        async def check():
            raise ConnectionError("down")
        status = await cache.refresh("ollama", check)
        assert status == HealthStatus.UNHEALTHY


class TestCircuitBreaker:
    @pytest.mark.asyncio
    async def test_initial_state_closed(self):
        cb = CircuitBreaker(name="test", failure_threshold=3)
        assert cb.state == CircuitState.CLOSED

    @pytest.mark.asyncio
    async def test_opens_after_threshold(self):
        cb = CircuitBreaker(name="test", failure_threshold=3)
        async def fail():
            raise ValueError("fail")

        for i in range(3):
            success, _ = await cb.call(fail)
            assert success is False

        assert cb.state == CircuitState.OPEN

    @pytest.mark.asyncio
    async def test_success_resets(self):
        cb = CircuitBreaker(name="test", failure_threshold=3)
        async def fail():
            raise ValueError("fail")
        async def succeed():
            return "ok"

        await cb.call(fail)
        assert cb.failure_count == 1

        success, _ = await cb.call(succeed)
        assert success is True
        assert cb.state == CircuitState.CLOSED
        assert cb.failure_count == 0

    @pytest.mark.asyncio
    async def test_half_open_transition(self):
        cb = CircuitBreaker(
            name="test",
            failure_threshold=2,
            recovery_timeout=-1,
        )
        async def fail():
            raise ValueError("fail")

        await cb.call(fail)
        await cb.call(fail)
        assert cb.state == CircuitState.OPEN

        if cb.state == CircuitState.OPEN:
            success, _ = await cb.call(fail)
            assert cb.state == CircuitState.OPEN

    @pytest.mark.asyncio
    async def test_recovery(self):
        cb = CircuitBreaker(
            name="test", failure_threshold=2, recovery_timeout=-0.1
        )
        async def fail():
            raise ValueError("fail")

        await cb.call(fail)
        await cb.call(fail)
        assert cb.state == CircuitState.OPEN

        await asyncio.sleep(0.01)

        async def succeed():
            return "ok"
        success, _ = await cb.call(succeed)
        assert cb.state == CircuitState.CLOSED

    def test_to_dict(self):
        cb = CircuitBreaker(name="test", failure_threshold=5)
        d = cb.to_dict()
        assert d["name"] == "test"
        assert d["state"] == "CLOSED"
        assert d["failure_count"] == 0

    def test_reset(self):
        cb = CircuitBreaker(name="test", failure_threshold=2)
        cb._state = CircuitState.OPEN
        cb._failure_count = 5
        cb.reset()
        assert cb.state == CircuitState.CLOSED
        assert cb.failure_count == 0


class TestProviderSelector:
    @pytest.mark.asyncio
    async def test_select_nonexistent(self):
        config_repo = AsyncMock()
        config_repo.get_by_name = AsyncMock(return_value=None)
        health_cache = ProviderHealthCache(ttl_seconds=30)

        selector = ProviderSelector(config_repo, health_cache)
        result = await selector.select("nonexistent")
        assert result is None

    @pytest.mark.asyncio
    async def test_select_with_circuit_open(self):
        config_repo = AsyncMock()
        health_cache = ProviderHealthCache(ttl_seconds=30)
        cb = CircuitBreaker(name="test", failure_threshold=1)
        cb._state = CircuitState.OPEN

        selector = ProviderSelector(config_repo, health_cache, circuit_breaker=cb)
        result = await selector.select("ollama")
        assert result is None
        config_repo.get_by_name.assert_not_called()

    @pytest.mark.asyncio
    async def test_select_healthy(self):
        config = ProviderConfigRecord(
            id=1, provider_type="chat", provider_name="ollama",
            base_url="http://localhost:11434", is_active=True,
        )
        config_repo = AsyncMock()
        config_repo.get_by_name = AsyncMock(return_value=config)
        health_cache = ProviderHealthCache(ttl_seconds=30)
        await health_cache.mark_healthy("ollama")

        selector = ProviderSelector(config_repo, health_cache)
        result = await selector.select("ollama")
        assert result is not None
        assert result.provider_name == "ollama"

    @pytest.mark.asyncio
    async def test_select_unhealthy_in_cache(self):
        config_repo = AsyncMock(spec_set=["get_by_name"])
        health_cache = ProviderHealthCache(ttl_seconds=30)
        await health_cache.mark_unhealthy("ollama")

        selector = ProviderSelector(config_repo, health_cache)
        result = await selector.select("ollama")
        assert result is None
        config_repo.get_by_name.assert_not_called()


class TestModelSelection:
    def test_create(self):
        sel = ModelSelection(
            model="qwen3:4b",
            provider="ollama",
            reason="capability_policy",
            candidates=[{"model": "qwen3:4b", "provider": "ollama", "score": 1.0}],
            capabilities=["fast_chat"],
        )
        assert sel.model == "qwen3:4b"
        assert sel.reason == "capability_policy"
        assert len(sel.candidates) == 1

    def test_empty_candidates(self):
        sel = ModelSelection(
            model="unknown",
            provider="unknown",
            reason="no_match",
        )
        assert sel.candidates == []
        assert sel.capabilities == []


class TestResolvedPolicy:
    def test_create(self):
        policy = ResolvedPolicy(
            capability="fast_chat",
            priority_order=0,
            model_name="qwen3:4b",
        )
        assert policy.capability == "fast_chat"
        assert policy.model_name == "qwen3:4b"
