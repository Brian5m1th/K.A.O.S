"""
GraphService — Code intelligence orchestrator.

Wraps GraphPort with ProviderRegistry for runtime provider switching.
"""

from typing import Optional
from loguru import logger
from app.core.provider_registry import ProviderRegistry
from app.domain.ports.graph_port import GraphPort, NodeInfo, PathInfo, GraphQuery, GraphResult


class GraphService:
    """Service for code intelligence graph queries."""

    def __init__(self):
        self.registry = ProviderRegistry[GraphPort]("graph")

    async def explain(self, concept: str) -> Optional[NodeInfo]:
        return await self.registry.active.explain(concept)

    async def path(self, source: str, target: str) -> Optional[PathInfo]:
        return await self.registry.active.path(source, target)

    async def query(self, query: GraphQuery) -> GraphResult:
        return await self.registry.active.query(query)

    async def health(self) -> dict:
        provider = self.registry.active_key or "none"
        ok = await self.registry.active.health()
        return {
            "service": "graph",
            "healthy": ok,
            "active_provider": provider,
            "available_providers": self.registry.list_providers(),
        }
