from app.workflows.impl.chat import ChatWorkflow
from app.workflows.impl.rag import RagWorkflow
from app.workflows.impl.agent import AgentWorkflow
from app.workflows.impl.research import ResearchWorkflow
from app.workflows.impl.coding import CodingWorkflow
from app.workflows.impl.memory import MemoryWorkflow
from app.workflows.impl.ingest import IngestWorkflow
from app.registry.service_registry import ServiceRegistry


def register_workflows() -> None:
    ServiceRegistry.register_workflow("chat", ChatWorkflow)
    ServiceRegistry.register_workflow("rag", RagWorkflow)
    ServiceRegistry.register_workflow("agent", AgentWorkflow)
    ServiceRegistry.register_workflow("research", ResearchWorkflow)
    ServiceRegistry.register_workflow("coding", CodingWorkflow)
    ServiceRegistry.register_workflow("memory", MemoryWorkflow)
    ServiceRegistry.register_workflow("ingest", IngestWorkflow)
