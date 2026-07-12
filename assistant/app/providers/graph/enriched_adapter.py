"""
EnrichedGraphAdapter — Wraps the enriched Knowledge Graph for GraphPort.

Replaces the legacy GraphifyAdapter with semantically-enriched queries using
the enriched graph (graph.enriched.json) with descriptions, quality metrics,
risks, and doc/test links.

Usage:
    adapter = EnrichedGraphAdapter()
    info = await adapter.explain("MemoryService")
    results = await adapter.search("authentication service")
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from loguru import logger
from app.domain.ports.graph_port import GraphPort, NodeInfo, PathInfo, GraphQuery, GraphResult


class EnrichedGraphAdapter(GraphPort):
    """Adapter that wraps the enriched Knowledge Graph for AI agent queries.

    Loads graphify-out/enriched/graph.enriched.json (with fallback to
    graphify-out/graph.json) and provides semantically-rich responses
    including descriptions, responsibilities, risks, and connections.
    """

    ENRICHED_PATH = Path("graphify-out/enriched/graph.enriched.json")
    LEGACY_PATH = Path("graphify-out/graph.json")

    def __init__(self):
        self._adapter = None
        self._loaded = False

    @property
    def provider_name(self) -> str:
        return "enriched_graph"

    @property
    def version(self) -> str:
        return "1.0.0"

    def _ensure_loaded(self) -> bool:
        """Lazy-load the enriched graph adapter."""
        if self._loaded and self._adapter is not None:
            return True

        try:
            from graphify.graph_sync.graph_port_v2 import EnrichedGraphAdapter as CoreAdapter

            enriched = str(self.ENRICHED_PATH.resolve()) if self.ENRICHED_PATH.exists() else None
            legacy = str(self.LEGACY_PATH.resolve()) if self.LEGACY_PATH.exists() else None

            self._adapter = CoreAdapter(
                enriched_path=enriched,
                legacy_path=legacy,
            )
            # Force load
            import asyncio
            health = asyncio.run(self._adapter.health())
            self._loaded = health.status != "unavailable"
            return self._loaded

        except ImportError as exc:
            logger.warning(f"[enriched] graphify.graph_sync not available: {exc}")
            return False
        except Exception as exc:
            logger.warning(f"[enriched] Failed to load enriched graph: {exc}")
            return False

    # ── GraphPort Interface ───────────────────────────────────────────────

    async def explain(self, concept: str) -> Optional[NodeInfo]:
        """Explain a code symbol with enriched metadata."""
        if not self._ensure_loaded():
            return None

        try:
            detail = await self._adapter.explain(concept)
            if not detail.id:
                return None

            return NodeInfo(
                id=detail.id,
                label=detail.label,
                source_file=detail.source_file or "",
                type=f"{detail.file_type}/{detail.symbol_type}",
                degree=detail.degree or 0,
                community=str(detail.community or ""),
                connections=detail.connections[:20],
            )
        except Exception as exc:
            logger.warning(f"[enriched] explain failed: {exc}")
            return None

    async def path(self, source: str, target: str) -> Optional[PathInfo]:
        """Find shortest path between two nodes."""
        if not self._ensure_loaded():
            return None

        try:
            result = await self._adapter.path(source, target)
            if result.hops == 0 and not result.path:
                return None

            return PathInfo(
                source=result.source,
                target=result.target,
                hops=result.hops,
                path=[f"{p['from']} --[{p['relation']}]--> {p['to']}" for p in result.path],
                description=result.description,
            )
        except Exception as exc:
            logger.warning(f"[enriched] path failed: {exc}")
            return None

    async def query(self, query: GraphQuery) -> GraphResult:
        """Execute a semantic search across the enriched graph."""
        if not self._ensure_loaded():
            return GraphResult()

        try:
            result = await self._adapter.query(
                text=query.text,
                max_depth=query.max_depth,
                context_filter=query.context_filter,
                max_results=query.max_results,
            )
            return GraphResult(
                nodes=[
                    NodeInfo(
                        id=n.id,
                        label=n.label,
                        source_file=n.source_file or "",
                        type=f"{n.file_type}/{n.symbol_type}",
                        degree=0,
                        community="",
                    )
                    for n in result.nodes
                ],
                total_found=result.total_found,
                query_time_ms=result.query_time_ms,
            )
        except Exception as exc:
            logger.warning(f"[enriched] query failed: {exc}")
            return GraphResult()

    async def health(self) -> bool:
        """Check if the enriched graph is available."""
        if not self._ensure_loaded():
            return False
        try:
            health = await self._adapter.health()
            return health.status == "healthy"
        except Exception:
            return False

    # ── Enhanced Methods ──────────────────────────────────────────────────

    async def search(self, text: str, limit: int = 20) -> list[dict]:
        """Semantic search across node labels, descriptions, and tags."""
        if not self._ensure_loaded():
            return []

        try:
            results = await self._adapter.search(text, limit=limit)
            return [
                {
                    "id": r.id,
                    "label": r.label,
                    "file_type": r.file_type,
                    "layer": r.layer,
                    "domain": r.domain,
                    "description": (r.description or "")[:200],
                    "tags": r.tags,
                    "risk_level": r.risk_level,
                }
                for r in results
            ]
        except Exception as exc:
            logger.warning(f"[enriched] search failed: {exc}")
            return []

    async def similar(self, node_id: str, n: int = 10) -> list[dict]:
        """Find similar nodes based on domain, layer, and tags."""
        if not self._ensure_loaded():
            return []

        try:
            results = await self._adapter.similar(node_id, n=n)
            return [
                {
                    "id": r.id,
                    "label": r.label,
                    "layer": r.layer,
                    "domain": r.domain,
                    "description": (r.description or "")[:200],
                }
                for r in results
            ]
        except Exception as exc:
            logger.warning(f"[enriched] similar failed: {exc}")
            return []

    async def analyze_impact(self, node_id: str, depth: int = 3) -> Optional[dict]:
        """Analyze impact of changing a node."""
        if not self._ensure_loaded():
            return None

        try:
            impact = await self._adapter.affected(node_id, depth=depth)
            return {
                "node_id": impact.node_id,
                "total_affected": impact.total_affected,
                "risk_level": impact.risk_level,
                "description": impact.description,
                "direct_dependents": [
                    {"id": d["node_id"], "label": d["label"], "relation": d["relation"]}
                    for d in impact.direct_dependents
                ],
                "transitive_count": len(impact.transitive_dependents),
            }
        except Exception as exc:
            logger.warning(f"[enriched] analyze_impact failed: {exc}")
            return None
