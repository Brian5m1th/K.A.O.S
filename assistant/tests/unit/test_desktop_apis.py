from unittest.mock import AsyncMock
from uuid import UUID

import pytest
from httpx import ASGITransport, AsyncClient

from app.database import get_session
from app.main import app
from app.repositories.capability_policy_repository import (
    CapabilityPolicyRecord,
)
from app.repositories.feature_flag_repository import FeatureFlagRecord
from app.repositories.model_repository import ModelRecord
from app.repositories.user_model_profile_repository import (
    UserModelProfileRecord,
)
from app.repositories.user_profile_repository import UserProfileRecord


@pytest.fixture
def mock_session():
    return AsyncMock()


@pytest.fixture
def client(mock_session):
    app.state.api_key = "test-api-key"

    async def override_get_session():
        yield mock_session

    app.dependency_overrides[get_session] = override_get_session
    transport = ASGITransport(app=app)
    client = AsyncClient(
        transport=transport,
        base_url="http://test",
        headers={"x-api-key": "test-api-key"},
    )
    return client


@pytest.mark.asyncio
async def test_get_user_exists(client, mock_session):
    mock_session.execute.return_value.scalar_one_or_none.return_value = (
        UserProfileRecord(user_id="test_user")
    )
    response = await client.get("/api/users/test_user")
    assert response.status_code == 200
    assert response.json()["exists"] is True


@pytest.mark.asyncio
async def test_get_user_not_found(client, mock_session):
    mock_session.execute.return_value.scalar_one_or_none.return_value = None
    response = await client.get("/api/users/nonexistent")
    assert response.status_code == 200
    assert response.json()["exists"] is False


@pytest.mark.asyncio
async def test_upsert_user(client, mock_session):
    response = await client.put(
        "/api/users/new_user",
        params={"theme": "light", "language": "en"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "saved"


@pytest.mark.asyncio
async def test_list_models(client, mock_session):
    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        ModelRecord(
            id=1,
            name="qwen3:4b",
            provider_name="ollama",
            context_window=8192,
            cost_input=0.0,
            cost_output=0.0,
            capabilities=["fast_chat"],
            is_active=True,
        )
    ]
    response = await client.get("/api/models")
    assert response.status_code == 200
    assert response.json()["total"] == 1


@pytest.mark.asyncio
async def test_get_model(client, mock_session):
    mock_session.execute.return_value.scalar_one_or_none.return_value = (
        ModelRecord(
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
    response = await client.get("/api/models/qwen3:4b")
    assert response.status_code == 200
    assert response.json()["exists"] is True


@pytest.mark.asyncio
async def test_list_capability_policies(client, mock_session):
    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        CapabilityPolicyRecord(
            id=1, capability="fast_chat", priority_order=1, model_id=1, model_name="qwen3:4b"
        )
    ]
    response = await client.get("/api/capabilities")
    assert response.status_code == 200
    assert response.json()["total"] == 1


@pytest.mark.asyncio
async def test_create_capability_policy(client, mock_session):
    mock_session.execute.return_value.scalar_one.return_value = 1
    response = await client.post(
        "/api/capabilities/fast_chat",
        params={"priority_order": 1, "model_id": 1},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "created"


@pytest.mark.asyncio
async def test_list_feature_flags(client, mock_session):
    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        FeatureFlagRecord(flag="dark_mode", enabled=True, description="")
    ]
    response = await client.get("/api/feature-flags")
    assert response.status_code == 200
    assert response.json()["total"] == 1


@pytest.mark.asyncio
async def test_get_feature_flag(client, mock_session):
    mock_session.execute.return_value.scalar_one_or_none.return_value = (
        FeatureFlagRecord(flag="dark_mode", enabled=True, description="")
    )
    response = await client.get("/api/feature-flags/dark_mode")
    assert response.status_code == 200
    assert response.json()["enabled"] is True


@pytest.mark.asyncio
async def test_list_user_model_profiles(client, mock_session):
    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        UserModelProfileRecord(
            id=UUID(int=1), user_id="user1", workflow_type="chat", model_name="qwen3:4b"
        )
    ]
    response = await client.get("/api/user-model-profiles/user1")
    assert response.status_code == 200
    assert response.json()["total"] == 1
