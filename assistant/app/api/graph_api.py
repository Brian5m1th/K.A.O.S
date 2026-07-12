"""
Graph REST API — Structural code intelligence queries.

Endpoints:
  GET  /api/graph/explain/{concept}   — Explain a code symbol
  GET  /api/graph/path                — Find dependency path
  POST /api/graph/query               — Execute graph traversal search
  GET  /api/graph/health              — Service health check
"""

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel

from app.core.services.graph_service import GraphService
from app.domain.ports.graph_port import GraphQuery

router = APIRouter(prefix="/api/graph", tags=["Graph"])


class GraphQueryRequest(BaseModel):
    text: str
    max_depth: int = 3
    max_results: int = 20


def get_graph_service() -> GraphService:
    from app.providers.graph.graphify_adapter import GraphifyAdapter
    from app.providers.graph.networkx_fallback import NetworkXFallback

    svc = GraphService()
    svc.registry.register("graphify", GraphifyAdapter())
    svc.registry.register("networkx", NetworkXFallback())
    return svc


@router.get("/explain/{concept}")
async def explain_concept(
    concept: str,
    graph: GraphService = Depends(get_graph_service),
):
    """Explain a code symbol: location, connections, and community."""
    result = await graph.explain(concept)
    if result is None:
        return {"found": False, "concept": concept}
    return {
        "found": True,
        "id": result.id,
        "label": result.label,
        "source_file": result.source_file,
        "type": result.type,
        "degree": result.degree,
        "community": result.community,
    }


@router.get("/path")
async def find_path(
    source: str = Query(..., description="Source symbol name"),
    target: str = Query(..., description="Target symbol name"),
    graph: GraphService = Depends(get_graph_service),
):
    """Find the shortest dependency path between two symbols."""
    result = await graph.path(source, target)
    return {
        "source": result.source,
        "target": result.target,
        "hops": result.hops,
        "description": result.description,
    }


@router.post("/query")
async def query_graph(
    body: GraphQueryRequest,
    graph: GraphService = Depends(get_graph_service),
):
    """Execute a traversal search over the code graph."""
    query = GraphQuery(
        text=body.text,
        max_depth=body.max_depth,
        max_results=body.max_results,
    )
    result = await graph.query(query)
    return {
        "nodes": [
            {"id": n.id, "label": n.label, "source_file": n.source_file, "type": n.type}
            for n in result.nodes
        ],
        "total_found": result.total_found,
    }


@router.get("/health")
async def graph_health(graph: GraphService = Depends(get_graph_service)):
    """Check graph service health."""
    return await graph.health()
