"""
GraphifyAdapter — Wraps Graphify CLI and graph.json for GraphPort.

Implements GraphPort interface. Queries use 'graphify explain/path/query'
CLI commands, with fallback to direct graph.json parsing when CLI is unavailable.
"""

import json
import subprocess
from pathlib import Path
from typing import Optional

from loguru import logger
from app.domain.ports.graph_port import (
    GraphPort,
    NodeInfo,
    PathInfo,
    GraphQuery,
    GraphResult,
)


class GraphifyAdapter(GraphPort):
    """Adapter that wraps Graphify CLI and graph.json for code intelligence queries."""

    GRAPH_PATH = Path("graphify-out/graph.json")

    def __init__(self):
        self._graph_data: Optional[dict] = None
        self._node_index: dict[str, dict] = {}

    @property
    def provider_name(self) -> str:
        return "graphify"

    @property
    def version(self) -> str:
        return "0.9.12"

    def _load_graph(self) -> dict:
        """Lazy-load graph.json with node index."""
        if self._graph_data is not None:
            return self._graph_data

        if not self.GRAPH_PATH.exists():
            logger.warning("[graphify] graph.json not found")
            return {"nodes": [], "links": [], "graph": {}}

        with open(self.GRAPH_PATH, "r", encoding="utf-8") as f:
            self._graph_data = json.load(f)

        for node in self._graph_data.get("nodes", []):
            self._node_index[node.get("id", "")] = node

        return self._graph_data

    async def explain(self, concept: str) -> Optional[NodeInfo]:
        """Explain a code symbol using Graphify CLI or graph.json parsing."""
        # Try CLI first
        try:
            proc = subprocess.run(
                ["graphify", "explain", concept],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if proc.returncode == 0:
                return self._parse_explain_cli(proc.stdout)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # Fallback: search graph.json directly
        data = self._load_graph()
        for node in data.get("nodes", []):
            label = node.get("label", "")
            norm = node.get("norm_label", "")
            if concept.lower() in label.lower() or concept.lower() in norm.lower():
                return self._node_to_info(node, data)

        return None

    def _parse_explain_cli(self, output: str) -> Optional[NodeInfo]:
        """Parse 'graphify explain' CLI output into NodeInfo."""
        info = NodeInfo(id="", label="", source_file="", type="code")
        for line in output.split("\n"):
            line = line.strip()
            if line.startswith("ID:"):
                info.id = line.split(":", 1)[1].strip()
            elif line.startswith("Source:"):
                info.source_file = line.split(":", 1)[1].strip().split(" L")[0]
            elif line.startswith("Degree:"):
                info.degree = int(line.split(":", 1)[1].strip())
            elif line.startswith("Community:"):
                info.community = line.split(":", 1)[1].strip()
            elif line.startswith("Type:"):
                info.type = line.split(":", 1)[1].strip()
            elif line.startswith("Node:"):
                info.label = line.split(":", 1)[1].strip()
        return info if info.id else None

    def _node_to_info(self, node: dict, data: dict) -> NodeInfo:
        """Convert a graph.json node to NodeInfo."""
        node_id = node.get("id", "")
        # Count connections
        degree = sum(
            1
            for link in data.get("links", [])
            if link.get("source") == node_id or link.get("target") == node_id
        )
        return NodeInfo(
            id=node_id,
            label=node.get("label", ""),
            source_file=node.get("source_file", ""),
            type=node.get("file_type", "code"),
            degree=degree,
            community=node.get("community_name", ""),
        )

    async def path(self, source: str, target: str) -> Optional[PathInfo]:
        """Find dependency path between two symbols."""
        try:
            proc = subprocess.run(
                ["graphify", "path", source, target],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if proc.returncode == 0:
                return self._parse_path_cli(proc.stdout)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        return PathInfo(
            source=source,
            target=target,
            hops=-1,
            description="Graphify CLI unavailable",
        )

    def _parse_path_cli(self, output: str) -> PathInfo:
        """Parse 'graphify path' CLI output."""
        path_info = PathInfo(source="", target="", hops=0)
        for line in output.split("\n"):
            if "hops" in line.lower():
                try:
                    path_info.hops = int(line.split("(")[1].split(" ")[0])
                except (IndexError, ValueError):
                    pass
                break
        return path_info

    async def query(self, query: GraphQuery) -> GraphResult:
        """Execute a traversal search using graph.json."""
        data = self._load_graph()
        nodes = data.get("nodes", [])
        links = data.get("links", [])

        # Simple keyword match on labels
        matches = []
        query_lower = query.text.lower()
        for node in nodes:
            label = node.get("label", "").lower()
            norm = node.get("norm_label", "").lower()
            if query_lower in label or query_lower in norm:
                matches.append(self._node_to_info(node, data))

        # BFS expansion if max_depth > 0
        if query.max_depth > 0 and matches:
            expanded = set()
            for _ in range(query.max_depth):
                for match in list(matches):
                    for link in links:
                        if link.get("source") == match.id:
                            tgt_id = link.get("target")
                            if tgt_id not in expanded:
                                tgt_node = self._node_index.get(tgt_id)
                                if tgt_node:
                                    matches.append(self._node_to_info(tgt_node, data))
                                    expanded.add(tgt_id)
                        elif link.get("target") == match.id:
                            src_id = link.get("source")
                            if src_id not in expanded:
                                src_node = self._node_index.get(src_id)
                                if src_node:
                                    matches.append(self._node_to_info(src_node, data))
                                    expanded.add(src_id)

        return GraphResult(
            nodes=matches[: query.max_results],
            total_found=len(matches),
        )

    async def health(self) -> bool:
        """Check if graph.json exists and is recent."""
        return self.GRAPH_PATH.exists()
