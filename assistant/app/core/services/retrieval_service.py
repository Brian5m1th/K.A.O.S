"""
RetrievalService — Semantic search orchestrator.
"""

from app.core.provider_registry import ProviderRegistry
from app.domain.ports.retrieval_port import (
    RetrievalPort,
    RetrievalQuery,
    RetrievalResult,
)


class RetrievalService:
    """Service for vector and semantic search."""

    def __init__(self):
        self.registry = ProviderRegistry[RetrievalPort]("retrieval")

    async def search(self, query: RetrievalQuery) -> list[RetrievalResult]:
        return await self.registry.active.search(query)

    async def count(self) -> int:
        return await self.registry.active.count()

    async def health(self) -> dict:
        provider = self.registry.active_key or "none"
        ok = await self.registry.active.health()
        return {
            "service": "retrieval",
            "healthy": ok,
            "active_provider": provider,
            "available_providers": self.registry.list_providers(),
        }
