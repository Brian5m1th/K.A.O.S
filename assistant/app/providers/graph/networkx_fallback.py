"""
NetworkX Fallback Adapter — In-memory graph for GraphPort.

Used when Graphify CLI or graph.json is unavailable.
Provides basic explain/path/query from a pre-built NetworkX graph.
"""

from typing import Optional

from app.domain.ports.graph_port import GraphPort, NodeInfo, PathInfo, GraphQuery, GraphResult


class NetworkXFallback(GraphPort):
    """Minimal in-memory graph fallback when Graphify is unavailable."""

    def __init__(self):
        self._nodes: dict[str, NodeInfo] = {}

    @property
    def provider_name(self) -> str:
        return "networkx-fallback"

    def add_node(self, node_id: str, label: str, source_file: str = "", node_type: str = "code"):
        self._nodes[node_id] = NodeInfo(
            id=node_id, label=label, source_file=source_file, type=node_type
        )

    async def explain(self, concept: str) -> Optional[NodeInfo]:
        for nid, node in self._nodes.items():
            if concept.lower() in node.label.lower():
                return node
        return None

    async def path(self, source: str, target: str) -> Optional[PathInfo]:
        return PathInfo(
            source=source, target=target, hops=-1,
            description="NetworkX fallback: no edges available"
        )

    async def query(self, query: GraphQuery) -> GraphResult:
        matches = [
            n for n in self._nodes.values()
            if query.text.lower() in n.label.lower()
        ]
        return GraphResult(nodes=matches[:query.max_results], total_found=len(matches))

    async def health(self) -> bool:
        return True  # Always available as fallback
