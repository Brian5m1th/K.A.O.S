"""
Knowledge REST API — Unified knowledge coalescing queries.

Endpoints:
  POST /api/knowledge/query     — Query across all knowledge sources
  GET  /api/knowledge/health    — Health of all sub-services
"""

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.core.services.knowledge_service import KnowledgeService
from app.core.services.graph_service import GraphService
from app.core.services.memory_service import MemoryService
from app.core.services.retrieval_service import RetrievalService

router = APIRouter(prefix="/api/knowledge", tags=["Knowledge"])


class KnowledgeQueryRequest(BaseModel):
    text: str
    include_sources: list[str] = ["graph", "retrieval", "memory"]


def get_knowledge_service() -> KnowledgeService:
    from app.providers.graph.graphify_adapter import GraphifyAdapter
    from app.providers.memory.postgres_memory_adapter import PostgresMemoryAdapter
    from app.providers.retrieval.qdrant_adapter import QdrantAdapter

    gs = GraphService()
    gs.registry.register("graphify", GraphifyAdapter())

    ms = MemoryService()
    ms.registry.register("postgres", PostgresMemoryAdapter())

    rs = RetrievalService()
    rs.registry.register("qdrant", QdrantAdapter())

    return KnowledgeService(graph_service=gs, memory_service=ms, retrieval_service=rs)


@router.post("/query")
async def query_knowledge(
    body: KnowledgeQueryRequest,
    knowledge: KnowledgeService = Depends(get_knowledge_service),
):
    """Coalescing query across graph, retrieval, and memory sources."""
    result = await knowledge.query(body.text, body.include_sources)
    return result


@router.get("/health")
async def knowledge_health(
    knowledge: KnowledgeService = Depends(get_knowledge_service),
):
    return await knowledge.health()
