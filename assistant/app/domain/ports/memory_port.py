"""
MemoryPort — Agent and user memory capability.

Stores and retrieves episodic, semantic, and procedural memories.
Current provider: PostgreSQL (conversations, preferences).
Future candidates: Mem0 (persistent identity), Graphiti (temporal evolution).
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class MemoryEntry:
    """A single memory record."""

    id: Optional[str] = None
    user_id: str = ""
    type: str = ""  # episodic | semantic | procedural | preference
    content: str = ""
    metadata: dict = field(default_factory=dict)
    created_at: Optional[datetime] = None
    ttl_seconds: Optional[int] = None  # None = permanent


@dataclass
class MemoryQuery:
    """Search parameters for memory retrieval."""

    text: str
    user_id: Optional[str] = None
    type_filter: Optional[list[str]] = None  # ["episodic", "semantic"]
    max_results: int = 10
    min_relevance: float = 0.5


@dataclass
class MemoryResult:
    """Search result wrapper."""

    matches: list[MemoryEntry] = field(default_factory=list)
    total_found: int = 0
    query_time_ms: float = 0.0


class MemoryPort(ABC):
    """
    Interface for memory storage and retrieval.

    Concrete implementations:
      - PostgresMemoryAdapter (current — conversations + preferences)
      - Mem0Adapter           (future — persistent user identity)
      - GraphitiAdapter       (future — temporal knowledge evolution)
    """

    @property
    @abstractmethod
    def provider_name(self) -> str: ...

    @abstractmethod
    async def store(self, entry: MemoryEntry) -> str:
        """Store a memory entry. Returns the assigned ID."""
        ...

    @abstractmethod
    async def search(self, query: MemoryQuery) -> MemoryResult:
        """Search memories by semantic similarity or metadata."""
        ...

    @abstractmethod
    async def get(self, memory_id: str) -> Optional[MemoryEntry]:
        """Retrieve a specific memory by ID."""
        ...

    @abstractmethod
    async def delete(self, memory_id: str) -> bool:
        """Delete a memory entry. Returns True if deleted."""
        ...

    @abstractmethod
    async def health(self) -> bool: ...
