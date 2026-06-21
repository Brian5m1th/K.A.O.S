from app.repositories.model_repository import ModelRecord, ModelRepository
from app.repositories.capability_policy_repository import (
    CapabilityPolicyRecord,
    CapabilityPolicyRepository,
)
from app.repositories.provider_config_repository import (
    ProviderConfigRecord,
    ProviderConfigRepository,
)
from app.repositories.user_profile_repository import (
    UserProfileRecord,
    UserProfileRepository,
)
from app.repositories.user_model_profile_repository import (
    UserModelProfileRecord,
    UserModelProfileRepository,
)
from app.repositories.feature_flag_repository import (
    FeatureFlagRecord,
    FeatureFlagRepository,
)
from app.repositories.failed_execution_repository import (
    FailedExecutionRecord,
    FailedExecutionRepository,
)


class TestModelRecord:
    def test_create_record(self):
        record = ModelRecord(
            id=1,
            name="test-model",
            provider_name="ollama",
            context_window=8192,
            cost_input=0.0,
            cost_output=0.0,
            capabilities=["fast_chat", "rag"],
            is_active=True,
        )
        assert record.name == "test-model"
        assert "fast_chat" in record.capabilities
        assert record.is_active is True

    def test_defaults(self):
        record = ModelRecord(
            id=0,
            name="test",
            provider_name="ollama",
            context_window=4096,
            cost_input=0.0,
            cost_output=0.0,
            capabilities=[],
            is_active=True,
        )
        assert len(record.capabilities) == 0


class TestCapabilityPolicyRecord:
    def test_create_record(self):
        record = CapabilityPolicyRecord(
            id=1,
            capability="fast_chat",
            priority_order=0,
            model_id=1,
            model_name="qwen3:4b",
        )
        assert record.capability == "fast_chat"
        assert record.model_name == "qwen3:4b"

    def test_default_model_name(self):
        record = CapabilityPolicyRecord(
            id=1,
            capability="reasoning",
            priority_order=0,
            model_id=2,
        )
        assert record.model_name == ""


class TestProviderConfigRecord:
    def test_create_record(self):
        record = ProviderConfigRecord(
            id=1,
            provider_type="chat",
            provider_name="ollama",
            base_url="http://localhost:11434",
            is_active=True,
            extra_config={"timeout": 30},
        )
        assert record.provider_type == "chat"
        assert record.provider_name == "ollama"
        assert record.extra_config["timeout"] == 30

    def test_extra_config_default(self):
        record = ProviderConfigRecord(
            id=1,
            provider_type="chat",
            provider_name="ollama",
        )
        assert record.extra_config == {}


class TestUserProfileRecord:
    def test_create_record(self):
        record = UserProfileRecord(
            user_id="test-user",
            theme="light",
            language="en-US",
            vault_path="/vault",
        )
        assert record.user_id == "test-user"
        assert record.theme == "light"
        assert record.auto_update is True

    def test_defaults(self):
        record = UserProfileRecord(user_id="default")
        assert record.theme == "dark"
        assert record.language == "pt-BR"
        assert record.telemetry_enabled is False


class TestUserModelProfileRecord:
    def test_create_record(self):
        import uuid

        record = UserModelProfileRecord(
            id=uuid.uuid4(),
            user_id="test-user",
            workflow_type="chat",
            model_name="qwen3:4b",
        )
        assert record.workflow_type == "chat"
        assert record.model_name == "qwen3:4b"


class TestFeatureFlagRecord:
    def test_create_record(self):
        record = FeatureFlagRecord(
            flag="research_workflow",
            enabled=True,
            description="Enable research workflow",
        )
        assert record.flag == "research_workflow"
        assert record.enabled is True

    def test_defaults(self):
        record = FeatureFlagRecord(flag="test", enabled=False)
        assert record.description == ""


class TestFailedExecutionRecord:
    def test_create_record(self):
        import uuid
        from datetime import datetime

        record = FailedExecutionRecord(
            id=uuid.uuid4(),
            trace_id=uuid.uuid4(),
            execution_id=uuid.uuid4(),
            workflow="research",
            payload={"message": "test"},
            error="TimeoutError",
            created_at=datetime.utcnow(),
        )
        assert record.workflow == "research"
        assert record.error == "TimeoutError"
        assert record.reprocessed_at is None


class TestRepositoryFactories:
    def test_all_repositories_have_session_param(self):
        repos = [
            ModelRepository,
            CapabilityPolicyRepository,
            ProviderConfigRepository,
            UserProfileRepository,
            UserModelProfileRepository,
            FeatureFlagRepository,
            FailedExecutionRepository,
        ]
        import inspect

        for repo in repos:
            sig = inspect.signature(repo.__init__)
            params = list(sig.parameters.keys())
            assert "session" in params, f"{repo.__name__} missing session param"
