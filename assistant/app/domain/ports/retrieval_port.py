"""
RetrievalPort — Semantic search and vector retrieval capability.

Searches across the vector index (Qdrant) and optionally across
knowledge graph nodes for multi-modal retrieval.
Current provider: QdrantAdapter.
Future candidate: FalkorDB (graph-native vector search).
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RetrievalQuery:
    """Semantic search query."""
    text: str
    collection: str = "kaos"
    max_results: int = 10
    score_threshold: float = 0.0
    filter: Optional[dict] = None  # Qdrant payload filter


@dataclass
class RetrievalResult:
    """Retrieved document chunk with score."""
    score: float
    payload: dict = field(default_factory=dict)
    chunk_id: Optional[str] = None
    source_file: Optional[str] = None
    text: str = ""


class RetrievalPort(ABC):
    """
    Interface for semantic search and vector retrieval.

    Concrete implementations:
      - QdrantAdapter    (current — vector similarity)
      - FalkorDBAdapter  (future — graph-native vectors with Cypher)
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        ...

    @abstractmethod
    async def search(self, query: RetrievalQuery) -> list[RetrievalResult]:
        """Search for semantically similar documents."""
        ...

    @abstractmethod
    async def index(self, documents: list[dict]) -> int:
        """Index documents into the vector store. Returns count indexed."""
        ...

    @abstractmethod
    async def count(self, collection: str = "kaos") -> int:
        """Return the number of indexed vectors."""
        ...

    @abstractmethod
    async def health(self) -> bool:
        ...
