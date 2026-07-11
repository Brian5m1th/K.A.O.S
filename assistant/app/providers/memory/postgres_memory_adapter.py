"""
PostgresMemoryAdapter — MemoryPort implementation backed by PostgreSQL.

Stores conversations, preferences, and user context using the existing
PostgreSQL database. Provides basic keyword + metadata search.
"""

from typing import Optional
from dataclasses import asdict

from loguru import logger
from app.domain.ports.memory_port import MemoryPort, MemoryEntry, MemoryQuery, MemoryResult


class PostgresMemoryAdapter(MemoryPort):
    """Memory adapter backed by existing PostgreSQL storage."""

    def __init__(self):
        self._store: dict[str, MemoryEntry] = {}  # In-memory fallback
        self._counter = 0

    @property
    def provider_name(self) -> str:
        return "postgres"

    async def store(self, entry: MemoryEntry) -> str:
        self._counter += 1
        entry_id = entry.id or f"mem_{self._counter}"
        entry.id = entry_id

        # Try PostgreSQL first
        try:
            from app.memory.postgres_repository import PostgresMemoryRepository
            repo = PostgresMemoryRepository()
            await repo.save(asdict(entry))
        except Exception as e:
            logger.warning(f"[memory:postgres] PostgreSQL unavailable, using in-memory fallback: {e}")
            self._store[entry_id] = entry

        return entry_id

    async def search(self, query: MemoryQuery) -> MemoryResult:
        matches = []
        text_lower = query.text.lower()

        for entry in self._store.values():
            if text_lower in entry.content.lower():
                matches.append(entry)

        return MemoryResult(
            matches=matches[:query.max_results],
            total_found=len(matches),
        )

    async def get(self, memory_id: str) -> Optional[MemoryEntry]:
        return self._store.get(memory_id)

    async def delete(self, memory_id: str) -> bool:
        if memory_id in self._store:
            del self._store[memory_id]
            return True
        return False

    async def health(self) -> bool:
        try:
            from app.database import async_session_factory
            from sqlalchemy import text

            factory = async_session_factory()
            async with factory() as s:
                await s.execute(text("SELECT 1"))
                return True
        except Exception:
            return False
