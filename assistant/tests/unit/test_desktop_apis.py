from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from app.database import get_session
from app.repositories.capability_policy_repository import (
    CapabilityPolicyRecord,
)
from app.repositories.feature_flag_repository import FeatureFlagRecord
from app.repositories.model_repository import ModelRecord

from app.repositories.user_model_profile_repository import (
    UserModelProfileRecord,
)
from app.repositories.user_profile_repository import UserProfileRecord
from app.main import app


@pytest.fixture
def mock_session():
    session = AsyncMock()
    return session


@pytest.fixture
def client(mock_session):
    async def override_get_session():
        yield mock_session

    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


class TestUsersAPI:
    def test_get_user_exists(self, client, mock_session):
        mock_session.execute.return_value.scalar_one_or_none.return_value = (
            UserProfileRecord(user_id="test_user")
        )
        response = client.get("/api/users/test_user")
        assert response.status_code == 200
        assert response.json()["exists"] is True

    def test_get_user_not_found(self, client, mock_session):
        mock_session.execute.return_value.scalar_one_or_none.return_value = None
        response = client.get("/api/users/nonexistent")
        assert response.status_code == 200
        assert response.json()["exists"] is False

    def test_upsert_user(self, client, mock_session):
        response = client.put(
            "/api/users/new_user",
            params={"theme": "light", "language": "en"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == "saved"


class TestModelsAPI:
    def test_list_models(self, client, mock_session):
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
        response = client.get("/api/models")
        assert response.status_code == 200
        assert response.json()["total"] == 1

    def test_get_model(self, client, mock_session):
        mock_session.execute.return_value.scalar_one_or_none.return_value = ModelRecord(
            id=1,
            name="qwen3:4b",
            provider_name="ollama",
            context_window=8192,
            cost_input=0.0,
            cost_output=0.0,
            capabilities=["fast_chat"],
            is_active=True,
        )
        response = client.get("/api/models/qwen3:4b")
        assert response.status_code == 200
        assert response.json()["exists"] is True


class TestCapabilitiesAPI:
    def test_list_policies(self, client, mock_session):
        mock_session.execute.return_value.scalars.return_value.all.return_value = [
            CapabilityPolicyRecord(
                id=1,
                capability="fast_chat",
                priority_order=1,
                model_id=1,
                model_name="qwen3:4b",
            )
        ]
        response = client.get("/api/capabilities")
        assert response.status_code == 200
        assert response.json()["total"] == 1

    def test_create_policy(self, client, mock_session):
        mock_session.execute.return_value.scalar_one.return_value = 1
        response = client.post(
            "/api/capabilities/fast_chat",
            params={"priority_order": 1, "model_id": 1},
        )
        assert response.status_code == 200
        assert response.json()["status"] == "created"


class TestFeatureFlagsAPI:
    def test_list_flags(self, client, mock_session):
        mock_session.execute.return_value.scalars.return_value.all.return_value = [
            FeatureFlagRecord(flag="dark_mode", enabled=True, description="")
        ]
        response = client.get("/api/feature-flags")
        assert response.status_code == 200
        assert response.json()["total"] == 1

    def test_get_flag(self, client, mock_session):
        mock_session.execute.return_value.scalar_one_or_none.return_value = (
            FeatureFlagRecord(flag="dark_mode", enabled=True, description="")
        )
        response = client.get("/api/feature-flags/dark_mode")
        assert response.status_code == 200
        assert response.json()["enabled"] is True


class TestUserModelProfilesAPI:
    def test_list_profiles(self, client, mock_session):
        from uuid import UUID

        mock_session.execute.return_value.scalars.return_value.all.return_value = [
            UserModelProfileRecord(
                id=UUID(int=1),
                user_id="user1",
                workflow_type="chat",
                model_name="qwen3:4b",
            )
        ]
        response = client.get("/api/user-model-profiles/user1")
        assert response.status_code == 200
        assert response.json()["total"] == 1
