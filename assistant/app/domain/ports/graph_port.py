"""
GraphPort — Code intelligence capability.

Exposes structural queries over the codebase AST graph.
Current provider: Graphify (graphify-out/graph.json).
Fallback: NetworkX in-memory graph.
Future candidate: Neo4j/Cypher for property graph queries.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NodeInfo:
    """Information about a code symbol or file."""

    id: str
    label: str
    source_file: str
    type: str  # code | file | class | function
    degree: int = 0
    community: str = ""
    connections: list[dict] = field(default_factory=list)


@dataclass
class PathInfo:
    """Path between two code symbols."""

    source: str
    target: str
    hops: int
    path: list[str] = field(default_factory=list)
    description: str = ""


@dataclass
class GraphQuery:
    """A query against the code graph."""

    text: str
    max_depth: int = 3
    context_filter: Optional[str] = None  # "call" | "import" | "contains"
    max_results: int = 20


@dataclass
class GraphResult:
    """Result of a graph query."""

    nodes: list[NodeInfo] = field(default_factory=list)
    total_found: int = 0
    query_time_ms: float = 0.0


class GraphPort(ABC):
    """
    Interface for code intelligence graph queries.

    Concrete implementations:
      - GraphifyAdapter (reads graphify-out/graph.json)
      - NetworkXAdapter (in-memory fallback)
      - Neo4jAdapter  (future — property graph with Cypher)
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Unique provider identifier, e.g. 'graphify'."""
        ...

    @abstractmethod
    async def explain(self, concept: str) -> Optional[NodeInfo]:
        """Explain a code symbol: its location, connections, and community."""
        ...

    @abstractmethod
    async def path(self, source: str, target: str) -> Optional[PathInfo]:
        """Find the shortest dependency path between two symbols."""
        ...

    @abstractmethod
    async def query(self, query: GraphQuery) -> GraphResult:
        """Execute a traversal/neighborhood search from matching nodes."""
        ...

    @abstractmethod
    async def health(self) -> bool:
        """Check if the graph source is available and up-to-date."""
        ...
