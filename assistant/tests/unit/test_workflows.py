from app.workflows.impl.chat import ChatWorkflow
from app.workflows.impl.rag import RagWorkflow
from app.workflows.impl.agent import AgentWorkflow
from app.workflows.impl.research import ResearchWorkflow
from app.workflows.impl.coding import CodingWorkflow
from app.workflows.impl.memory import MemoryWorkflow
from app.workflows.impl.ingest import IngestWorkflow
from app.workflows.base import BaseWorkflow
from app.workflows.impl.registry import register_workflows
from app.registry.service_registry import ServiceRegistry


class TestChatWorkflow:
    def test_name(self):
        assert ChatWorkflow.name == "chat"
        assert ChatWorkflow.version == "1.0"

    def test_required_capabilities(self):
        wf = ChatWorkflow()
        assert wf.required_capabilities == ["fast_chat"]

    def test_is_workflow(self):
        assert issubclass(ChatWorkflow, BaseWorkflow)


class TestRagWorkflow:
    def test_name(self):
        assert RagWorkflow.name == "rag"

    def test_required_capabilities(self):
        wf = RagWorkflow()
        assert wf.required_capabilities == ["fast_chat", "rag"]

    def test_is_workflow(self):
        assert issubclass(RagWorkflow, BaseWorkflow)


class TestAgentWorkflow:
    def test_name(self):
        assert AgentWorkflow.name == "agent"

    def test_required_capabilities(self):
        wf = AgentWorkflow()
        assert wf.required_capabilities == ["reasoning", "fast_chat"]

    def test_is_workflow(self):
        assert issubclass(AgentWorkflow, BaseWorkflow)


class TestResearchWorkflow:
    def test_name(self):
        assert ResearchWorkflow.name == "research"

    def test_required_capabilities(self):
        wf = ResearchWorkflow()
        assert wf.required_capabilities == ["reasoning", "rag", "long_context"]

    def test_is_workflow(self):
        assert issubclass(ResearchWorkflow, BaseWorkflow)


class TestCodingWorkflow:
    def test_name(self):
        assert CodingWorkflow.name == "coding"

    def test_required_capabilities(self):
        wf = CodingWorkflow()
        assert wf.required_capabilities == ["coding", "reasoning"]

    def test_is_workflow(self):
        assert issubclass(CodingWorkflow, BaseWorkflow)


class TestMemoryWorkflow:
    def test_name(self):
        assert MemoryWorkflow.name == "memory"

    def test_required_capabilities(self):
        wf = MemoryWorkflow()
        assert wf.required_capabilities == ["memory"]

    def test_is_workflow(self):
        assert issubclass(MemoryWorkflow, BaseWorkflow)


class TestIngestWorkflow:
    def test_name(self):
        assert IngestWorkflow.name == "ingest"

    def test_required_capabilities(self):
        wf = IngestWorkflow()
        assert wf.required_capabilities == ["rag"]

    def test_is_workflow(self):
        assert issubclass(IngestWorkflow, BaseWorkflow)


class TestRegisterWorkflows:
    def test_register_all(self):
        ServiceRegistry._workflows.clear()
        register_workflows()

        assert "chat" in ServiceRegistry.list_workflows()
        assert "rag" in ServiceRegistry.list_workflows()
        assert "agent" in ServiceRegistry.list_workflows()
        assert "research" in ServiceRegistry.list_workflows()
        assert "coding" in ServiceRegistry.list_workflows()
        assert "memory" in ServiceRegistry.list_workflows()
        assert "ingest" in ServiceRegistry.list_workflows()

    def test_get_workflow_instances(self):
        register_workflows()

        assert isinstance(ServiceRegistry.get_workflow("chat"), ChatWorkflow)
        assert isinstance(ServiceRegistry.get_workflow("rag"), RagWorkflow)
        assert isinstance(ServiceRegistry.get_workflow("agent"), AgentWorkflow)
        assert isinstance(ServiceRegistry.get_workflow("research"), ResearchWorkflow)
        assert isinstance(ServiceRegistry.get_workflow("coding"), CodingWorkflow)
        assert isinstance(ServiceRegistry.get_workflow("memory"), MemoryWorkflow)
        assert isinstance(ServiceRegistry.get_workflow("ingest"), IngestWorkflow)

    def test_healthcheck(self):
        register_workflows()

        for name in ServiceRegistry.list_workflows():
            wf = ServiceRegistry.get_workflow(name)
            assert wf.healthcheck() is True
