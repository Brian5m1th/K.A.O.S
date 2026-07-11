"""
Dependency Injection — FastAPI service wiring.

Centralizes service instantiation with ProviderRegistry setup.
All API routes use these dependency functions via `Depends()`.

Architecture: Desktop → REST API → Service → Port → Adapter → Framework
"""

from app.core.services.graph_service import GraphService
from app.core.services.memory_service import MemoryService
from app.core.services.retrieval_service import RetrievalService
from app.core.services.inference_service import InferenceService
from app.core.services.planner_service import PlannerService
from app.core.services.evidence_service import EvidenceService
from app.core.services.knowledge_service import KnowledgeService


# ── Singleton service instances (initialized once) ──────────────────────

_graph_service: GraphService | None = None
_memory_service: MemoryService | None = None
_retrieval_service: RetrievalService | None = None
_inference_service: InferenceService | None = None
_planner_service: PlannerService | None = None
_evidence_service: EvidenceService | None = None
_knowledge_service: KnowledgeService | None = None


def init_services():
    """Initialize all services with default provider registries."""
    global _graph_service, _memory_service, _retrieval_service
    global _inference_service, _planner_service, _evidence_service, _knowledge_service

    from app.providers.graph.graphify_adapter import GraphifyAdapter
    from app.providers.graph.networkx_fallback import NetworkXFallback
    from app.providers.memory.postgres_memory_adapter import PostgresMemoryAdapter
    from app.providers.retrieval.qdrant_adapter import QdrantAdapter
    from app.providers.inference.ollama_adapter import OllamaAdapter
    from app.providers.inference.airllm_adapter import AirLLMAdapter
    from app.providers.inference.openai_adapter import OpenAIAdapter, GeminiAdapter, ClaudeAdapter
    from app.providers.planner.langgraph_adapter import LangGraphAdapter
    from app.providers.evidence.engine import EvidenceEngine

    # Graph
    _graph_service = GraphService()
    _graph_service.registry.register("graphify", GraphifyAdapter())
    _graph_service.registry.register("networkx", NetworkXFallback())

    # Memory
    _memory_service = MemoryService()
    _memory_service.registry.register("postgres", PostgresMemoryAdapter())

    # Retrieval
    _retrieval_service = RetrievalService()
    _retrieval_service.registry.register("qdrant", QdrantAdapter())

    # Inference
    _inference_service = InferenceService()
    _inference_service.registry.register("ollama", OllamaAdapter())
    _inference_service.registry.register("airllm", AirLLMAdapter())
    _inference_service.registry.register("openai", OpenAIAdapter())
    _inference_service.registry.register("gemini", GeminiAdapter())
    _inference_service.registry.register("claude", ClaudeAdapter())

    # Planner
    _planner_service = PlannerService()
    _planner_service.registry.register("langgraph", LangGraphAdapter())

    # Evidence
    _evidence_service = EvidenceService()
    _evidence_service.registry.register("engine", EvidenceEngine())

    # Knowledge (coalescing)
    _knowledge_service = KnowledgeService(
        graph_service=_graph_service,
        memory_service=_memory_service,
        retrieval_service=_retrieval_service,
    )


def get_graph_service() -> GraphService:
    """Dependency injection: GraphService singleton."""
    global _graph_service
    if _graph_service is None:
        init_services()
    return _graph_service


def get_memory_service() -> MemoryService:
    global _memory_service
    if _memory_service is None:
        init_services()
    return _memory_service


def get_retrieval_service() -> RetrievalService:
    global _retrieval_service
    if _retrieval_service is None:
        init_services()
    return _retrieval_service


def get_inference_service() -> InferenceService:
    global _inference_service
    if _inference_service is None:
        init_services()
    return _inference_service


def get_planner_service() -> PlannerService:
    global _planner_service
    if _planner_service is None:
        init_services()
    return _planner_service


def get_evidence_service() -> EvidenceService:
    global _evidence_service
    if _evidence_service is None:
        init_services()
    return _evidence_service


def get_knowledge_service() -> KnowledgeService:
    global _knowledge_service
    if _knowledge_service is None:
        init_services()
    return _knowledge_service
