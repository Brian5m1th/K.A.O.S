"""
MemoryService — Memory storage and retrieval orchestrator.
"""

from app.core.provider_registry import ProviderRegistry
from app.domain.ports.memory_port import MemoryPort, MemoryEntry, MemoryQuery, MemoryResult


class MemoryService:
    """Service for user and agent memory management."""

    def __init__(self):
        self.registry = ProviderRegistry[MemoryPort]("memory")

    async def store(self, entry: MemoryEntry) -> str:
        return await self.registry.active.store(entry)

    async def search(self, query: MemoryQuery) -> MemoryResult:
        return await self.registry.active.search(query)

    async def delete(self, memory_id: str) -> bool:
        return await self.registry.active.delete(memory_id)

    async def health(self) -> dict:
        provider = self.registry.active_key or "none"
        ok = await self.registry.active.health()
        return {
            "service": "memory",
            "healthy": ok,
            "active_provider": provider,
            "available_providers": self.registry.list_providers(),
        }
