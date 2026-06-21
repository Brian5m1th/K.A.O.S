from uuid import UUID

import pytest

from app.domain.execution_plan import CapabilityProfile, ExecutionPlan
from app.providers.base.chat import BaseChatProvider
from app.providers.base.embedding import BaseEmbeddingProvider
from app.providers.base.memory import BaseMemoryProvider
from app.providers.base.vector_store import BaseVectorStore
from app.workflows.base import BaseWorkflow
from app.registry.service_registry import ServiceRegistry
from app.observability.event_bus import Event, EventBus, EventSubscriber


class TestCapabilityProfile:
    def test_default_empty(self):
        profile = CapabilityProfile()
        assert profile.capabilities == []
        assert len(profile) == 0

    def test_with_capabilities(self):
        profile = CapabilityProfile(capabilities=["fast_chat", "rag"])
        assert profile.has("fast_chat")
        assert profile.has("rag")
        assert not profile.has("reasoning")

    def test_has_any(self):
        profile = CapabilityProfile(capabilities=["fast_chat", "rag"])
        assert profile.has_any(["fast_chat"])
        assert profile.has_any(["reasoning", "rag"])
        assert not profile.has_any(["coding", "vision"])

    def test_has_all(self):
        profile = CapabilityProfile(capabilities=["fast_chat", "rag", "reasoning"])
        assert profile.has_all(["fast_chat", "rag"])
        assert not profile.has_all(["fast_chat", "vision"])

    def test_merge(self):
        p1 = CapabilityProfile(capabilities=["fast_chat", "rag"])
        p2 = CapabilityProfile(capabilities=["reasoning", "rag"])
        merged = p1.merge(p2)
        assert set(merged.capabilities) == {"fast_chat", "rag", "reasoning"}


class TestExecutionPlan:
    def test_create_with_defaults(self):
        plan = ExecutionPlan.create(
            workflow="chat",
            selected_model="qwen3:4b",
            user_id=UUID("00000000-0000-0000-0000-000000000001"),
            session_id=UUID("00000000-0000-0000-0000-000000000002"),
        )
        assert isinstance(plan.execution_id, UUID)
        assert isinstance(plan.trace_id, UUID)
        assert plan.workflow == "chat"
        assert plan.selected_model == "qwen3:4b"

    def test_create_with_capabilities(self):
        plan = ExecutionPlan.create(
            workflow="research",
            selected_model="claude-sonnet",
            user_id=UUID("00000000-0000-0000-0000-000000000001"),
            session_id=UUID("00000000-0000-0000-0000-000000000002"),
            capabilities=["reasoning", "long_context", "rag"],
        )
        assert len(plan.capabilities) == 3
        assert plan.capability_profile.has("reasoning")

    def test_create_with_explicit_ids(self):
        exec_id = UUID("11111111-1111-1111-1111-111111111111")
        trace_id = UUID("22222222-2222-2222-2222-222222222222")
        plan = ExecutionPlan.create(
            workflow="test",
            selected_model="test-model",
            user_id=UUID("00000000-0000-0000-0000-000000000001"),
            session_id=UUID("00000000-0000-0000-0000-000000000002"),
            execution_id=exec_id,
            trace_id=trace_id,
        )
        assert plan.execution_id == exec_id
        assert plan.trace_id == trace_id


class TestBaseContracts:
    def test_chat_provider_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            BaseChatProvider()  # type: ignore

    def test_embedding_provider_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            BaseEmbeddingProvider()  # type: ignore

    def test_vector_store_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            BaseVectorStore()  # type: ignore

    def test_memory_provider_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            BaseMemoryProvider()  # type: ignore

    def test_workflow_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            BaseWorkflow()  # type: ignore


class TestServiceRegistry:
    def test_register_and_get_workflow(self):
        class FakeWorkflow(BaseWorkflow):
            name = "test"
            version = "1.0"

            @property
            def required_capabilities(self):
                return ["fast_chat"]

            async def execute(self, plan, request):
                yield "test"

            async def healthcheck(self):
                return True

        ServiceRegistry.register_workflow("test", FakeWorkflow)
        wf = ServiceRegistry.get_workflow("test")
        assert isinstance(wf, FakeWorkflow)
        assert wf.name == "test"
        assert "test" in ServiceRegistry.list_workflows()

        ServiceRegistry._workflows.clear()

    def test_get_unregistered_workflow_raises(self):
        with pytest.raises(KeyError, match="Workflow not registered: nonexistent"):
            ServiceRegistry.get_workflow("nonexistent")

    def test_list_empty(self):
        ServiceRegistry._workflows.clear()
        assert ServiceRegistry.list_workflows() == []


class TestEventBus:
    class TestSubscriber(EventSubscriber):
        def __init__(self):
            self.events = []

        async def on_event(self, event: Event):
            self.events.append(event)

    @pytest.mark.asyncio
    async def test_publish_and_subscribe(self):
        subscriber = self.TestSubscriber()
        EventBus.subscribe("test_event", subscriber)

        event = Event(
            name="test_event",
            execution_id=UUID("00000000-0000-0000-0000-000000000001"),
            trace_id=UUID("00000000-0000-0000-0000-000000000002"),
            data={"key": "value"},
        )
        await EventBus.publish(event)

        assert len(subscriber.events) == 1
        assert subscriber.events[0].name == "test_event"
        assert subscriber.events[0].data["key"] == "value"

        EventBus.clear()

    @pytest.mark.asyncio
    async def test_subscriber_error_does_not_propagate(self):
        class FailingSubscriber(EventSubscriber):
            async def on_event(self, event: Event):
                raise ValueError("test error")

        subscriber = FailingSubscriber()
        EventBus.subscribe("failing_event", subscriber)

        event = Event(
            name="failing_event",
            execution_id=UUID("00000000-0000-0000-0000-000000000001"),
            trace_id=UUID("00000000-0000-0000-0000-000000000002"),
        )
        await EventBus.publish(event)

        EventBus.clear()
