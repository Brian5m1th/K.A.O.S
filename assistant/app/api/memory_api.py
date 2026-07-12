"""
Memory REST API — Agent and user memory storage.

Endpoints:
  POST   /api/memory/store       — Store a memory entry
  GET    /api/memory/search      — Search memories
  GET    /api/memory/{id}        — Get specific memory
  DELETE /api/memory/{id}        — Delete a memory
  GET    /api/memory/health      — Service health check
"""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional

from app.core.services.memory_service import MemoryService
from app.domain.ports.memory_port import MemoryEntry, MemoryQuery
from datetime import datetime, timezone

router = APIRouter(prefix="/api/memory", tags=["Memory"])


class StoreRequest(BaseModel):
    user_id: str = ""
    type: str = "episodic"
    content: str
    metadata: dict = {}
    ttl_seconds: Optional[int] = None


class SearchRequest(BaseModel):
    text: str
    user_id: Optional[str] = None
    type_filter: Optional[list[str]] = None
    max_results: int = 10


def get_memory_service() -> MemoryService:
    from app.providers.memory.postgres_memory_adapter import PostgresMemoryAdapter
    svc = MemoryService()
    svc.registry.register("postgres", PostgresMemoryAdapter())
    return svc


@router.post("/store")
async def store_memory(
    body: StoreRequest,
    mem: MemoryService = Depends(get_memory_service),
):
    """Store a memory entry. Returns the assigned ID."""
    entry = MemoryEntry(
        user_id=body.user_id,
        type=body.type,
        content=body.content,
        metadata=body.metadata,
        created_at=datetime.now(timezone.utc),
        ttl_seconds=body.ttl_seconds,
    )
    memory_id = await mem.store(entry)
    return {"id": memory_id, "stored": True}


@router.post("/search")
async def search_memory(
    body: SearchRequest,
    mem: MemoryService = Depends(get_memory_service),
):
    """Search memories by semantic similarity or metadata."""
    query = MemoryQuery(
        text=body.text,
        user_id=body.user_id,
        type_filter=body.type_filter,
        max_results=body.max_results,
    )
    result = await mem.search(query)
    return {
        "matches": [
            {"id": m.id, "type": m.type, "content": m.content[:200], "metadata": m.metadata}
            for m in result.matches
        ],
        "total_found": result.total_found,
    }


@router.get("/{memory_id}")
async def get_memory(
    memory_id: str,
    mem: MemoryService = Depends(get_memory_service),
):
    """Retrieve a specific memory by ID."""
    result = await mem.registry.active.get(memory_id)
    if result is None:
        return {"found": False}
    return {"found": True, "id": result.id, "type": result.type, "content": result.content}


@router.delete("/{memory_id}")
async def delete_memory(
    memory_id: str,
    mem: MemoryService = Depends(get_memory_service),
):
    """Delete a memory entry."""
    deleted = await mem.delete(memory_id)
    return {"deleted": deleted}


@router.get("/health")
async def memory_health(mem: MemoryService = Depends(get_memory_service)):
    return await mem.health()
