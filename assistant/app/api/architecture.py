from fastapi import APIRouter
from loguru import logger

from app.ai.vault_analyzer.analyzer_engine import AnalyzerEngine
from app.ai.vault_analyzer.drift_engine import DriftEngine
from app.ai.vault_analyzer.vault_reader import VaultReader
from app.ai.vault_analyzer.graph_builder import GraphBuilder

router = APIRouter(prefix="/api/architecture", tags=["Architecture"])


@router.post("/analyze")
async def analyze_architecture():
    """Executa analise arquitetural completa."""
    logger.info("[api/architecture] analyze requested")
    analysis = AnalyzerEngine.analyze()
    return {
        "coverage_score": round(analysis.coverage_score, 1),
        "drift_level": analysis.drift_level,
        "total_issues": len(analysis.issues),
        "suggestions": analysis.suggestions,
        "warnings": analysis.warnings,
        "generated_at": analysis.generated_at,
    }


@router.get("/analysis")
async def get_analysis():
    """Obtem ultima analise arquitetural."""
    analysis = AnalyzerEngine.load_latest()
    if not analysis:
        return {"error": "No analysis available. Run analysis first."}
    return analysis  # type: ignore


@router.get("/graph")
async def get_graph():
    """Obtem o grafo de arquitetura."""
    graph = GraphBuilder.load()
    if not graph:
        return {"error": "No graph available. Build graph first."}
    return graph.to_dict()


@router.post("/graph")
async def build_graph():
    """Constroi o grafo de arquitetura."""
    graph = GraphBuilder.build()
    return graph.to_dict()


@router.get("/issues")
async def get_issues():
    """Lista evidencias/issues arquiteturais."""
    from pathlib import Path
    import json
    path = Path("docs/runtime/architecture/issues.json")
    if not path.exists():
        return {"total": 0, "evidences": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@router.get("/suggestions")
async def get_suggestions():
    """Lista sugestoes arquiteturais."""
    from pathlib import Path
    import json
    path = Path("docs/runtime/architecture/suggestions.json")
    if not path.exists():
        return {"total": 0, "suggestions": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@router.get("/heatmap")
async def get_heatmap():
    """Obtem dados para o heatmap de drift."""
    score = DriftEngine.load_latest()
    if not score:
        return {"error": "No heatmap data available."}
    return score.to_dict()


@router.post("/scan-vault")
async def scan_vault():
    """Escaneia vault e retorna estatisticas."""
    nodes = VaultReader.scan_all()
    by_type = VaultReader.get_node_count_by_type()
    orphans = VaultReader.get_orphan_nodes()
    return {
        "total_nodes": len(nodes),
        "by_type": by_type,
        "orphan_count": len(orphans),
        "total_links": VaultReader.get_total_links(),
        "orphan_nodes": [{"id": n.id, "title": n.title, "type": n.type} for n in orphans],
    }
