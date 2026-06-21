from unittest.mock import AsyncMock

import pytest

from app.models.model_registry import ModelRegistry
from app.repositories.model_repository import ModelRecord


@pytest.fixture
def mock_session():
    return AsyncMock()


@pytest.mark.asyncio
async def test_get_model(mock_session):
    registry = ModelRegistry(mock_session)
    registry._repo.get_by_name = AsyncMock(
        return_value=ModelRecord(
            id=1,
            name="qwen3:4b",
            provider_name="ollama",
            context_window=8192,
            cost_input=0.0,
            cost_output=0.0,
            capabilities=["fast_chat"],
            is_active=True,
        )
    )
    result = await registry.get_model("qwen3:4b")
    assert result is not None
    assert result.name == "qwen3:4b"


@pytest.mark.asyncio
async def test_get_model_not_found(mock_session):
    registry = ModelRegistry(mock_session)
    registry._repo.get_by_name = AsyncMock(return_value=None)
    result = await registry.get_model("nonexistent")
    assert result is None


@pytest.mark.asyncio
async def test_list_by_capability(mock_session):
    registry = ModelRegistry(mock_session)
    registry._repo.list_by_capability = AsyncMock(return_value=[])
    result = await registry.list_by_capability("fast_chat")
    assert result == []


@pytest.mark.asyncio
async def test_list_all(mock_session):
    registry = ModelRegistry(mock_session)
    registry._repo.list_all = AsyncMock(return_value=[])
    result = await registry.list_all()
    assert result == []
