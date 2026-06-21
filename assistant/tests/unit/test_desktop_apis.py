from unittest.mock import patch

import pytest
from httpx import ASGITransport, AsyncClient

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
def client():
    app.state.api_key = "test-api-key"
    transport = ASGITransport(app=app)
    return AsyncClient(
        transport=transport,
        base_url="http://test",
        headers={"x-api-key": "test-api-key"},
    )


@pytest.mark.asyncio
async def test_get_user_exists(client):
    with patch(
        "app.api.users.UserProfileRepository.get",
        return_value=UserProfileRecord(user_id="test_user"),
    ):
        response = await client.get("/api/users/test_user")
    assert response.status_code == 200
    assert response.json()["exists"] is True


@pytest.mark.asyncio
async def test_get_user_not_found(client):
    with patch(
        "app.api.users.UserProfileRepository.get",
        return_value=None,
    ):
        response = await client.get("/api/users/nonexistent")
    assert response.status_code == 200
    assert response.json()["exists"] is False


@pytest.mark.asyncio
async def test_upsert_user(client):
    with patch(
        "app.api.users.UserProfileRepository.upsert",
        return_value=None,
    ):
        response = await client.put(
            "/api/users/new_user",
            params={"theme": "light", "language": "en"},
        )
    assert response.status_code == 200
    assert response.json()["status"] == "saved"


@pytest.mark.asyncio
async def test_list_models(client):
    fake_models = [
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
    with patch(
        "app.api.models.ModelRepository.list_all",
        return_value=fake_models,
    ):
        response = await client.get("/api/models")
    assert response.status_code == 200
    assert response.json()["total"] == 1


@pytest.mark.asyncio
async def test_get_model(client):
    with patch(
        "app.api.models.ModelRepository.get_by_name",
        return_value=ModelRecord(
            id=1,
            name="qwen3:4b",
            provider_name="ollama",
            context_window=8192,
            cost_input=0.0,
            cost_output=0.0,
            capabilities=["fast_chat"],
            is_active=True,
        ),
    ):
        response = await client.get("/api/models/qwen3:4b")
    assert response.status_code == 200
    assert response.json()["exists"] is True


@pytest.mark.asyncio
async def test_list_capability_policies(client):
    with patch(
        "app.api.capabilities.CapabilityPolicyRepository.list_all",
        return_value=[
            CapabilityPolicyRecord(
                id=1, capability="fast_chat", priority_order=1, model_id=1, model_name="qwen3:4b"
            )
        ],
    ):
        response = await client.get("/api/capabilities")
    assert response.status_code == 200
    assert response.json()["total"] == 1


@pytest.mark.asyncio
async def test_create_capability_policy(client):
    with patch(
        "app.api.capabilities.CapabilityPolicyRepository.upsert",
        return_value=1,
    ):
        response = await client.post(
            "/api/capabilities/fast_chat",
            params={"priority_order": 1, "model_id": 1},
        )
    assert response.status_code == 200
    assert response.json()["status"] == "created"


@pytest.mark.asyncio
async def test_list_feature_flags(client):
    with patch(
        "app.api.feature_flags.FeatureFlagRepository.list_all",
        return_value=[
            FeatureFlagRecord(flag="dark_mode", enabled=True, description="")
        ],
    ):
        response = await client.get("/api/feature-flags")
    assert response.status_code == 200
    assert response.json()["total"] == 1


@pytest.mark.asyncio
async def test_get_feature_flag(client):
    with patch(
        "app.api.feature_flags.FeatureFlagRepository.is_enabled",
        return_value=True,
    ):
        response = await client.get("/api/feature-flags/dark_mode")
    assert response.status_code == 200
    assert response.json()["enabled"] is True


@pytest.mark.asyncio
async def test_list_user_model_profiles(client):
    from uuid import UUID

    with patch(
        "app.api.user_model_profiles.UserModelProfileRepository.list_by_user",
        return_value=[
            UserModelProfileRecord(
                id=UUID(int=1), user_id="user1", workflow_type="chat", model_name="qwen3:4b"
            )
        ],
    ):
        response = await client.get("/api/user-model-profiles/user1")
    assert response.status_code == 200
    assert response.json()["total"] == 1
