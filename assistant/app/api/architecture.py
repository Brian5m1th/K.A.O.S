from fastapi import APIRouter
from loguru import logger

from app.ai.vault_analyzer.analyzer_engine import AnalyzerEngine
from app.ai.vault_analyzer.drift_engine import DriftEngine
from app.ai.vault_analyzer.vault_reader import VaultReader
from app.ai.vault_analyzer.graph_builder import GraphBuilder
from app.ai.vault_analyzer.knowledge_graph import KnowledgeGraphBuilder
from app.audit.runtime_resolver import RuntimePathResolver

router = APIRouter(prefix="/api/architecture", tags=["Architecture"])


@router.post("/analyze")
async def analyze_architecture():
    """Executa analise arquitetural completa e emite evento no EventBus (RF-B05)."""
    logger.info("[api/architecture] analyze requested")
    analysis = await AnalyzerEngine.analyze_async()
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
    import json

    path = RuntimePathResolver.issues_path()
    if not path.exists():
        return {"total": 0, "evidences": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@router.get("/suggestions")
async def get_suggestions():
    """Lista sugestoes arquiteturais."""
    import json

    path = RuntimePathResolver.suggestions_path()
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
        "orphan_nodes": [
            {"id": n.id, "title": n.title, "type": n.type} for n in orphans
        ],
    }


@router.post("/knowledge-graph")
async def build_knowledge_graph():
    """Constroi grafo de conhecimento consolidado."""
    kg = KnowledgeGraphBuilder.build()
    return kg.to_dict()


@router.get("/knowledge-graph")
async def get_knowledge_graph():
    """Obtem grafo de conhecimento."""
    kg = KnowledgeGraphBuilder.load()
    if not kg:
        return {"error": "No knowledge graph available. Build first."}
    return kg.to_dict()


@router.get("/history")
async def get_drift_history():
    """Lista historico temporal de drift."""
    import json

    history_dir = RuntimePathResolver.architecture_history_dir()
    if not history_dir.exists():
        return {"total": 0, "history": []}
    entries = []
    for f in sorted(history_dir.glob("*.json")):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            entries.append(
                {
                    "date": f.stem,
                    "score": data.get("score", 0),
                    "level": data.get("level", "low"),
                    "missing_links": data.get("missing_links", 0),
                    "sdd_mismatch": data.get("sdd_mismatch", 0),
                    "code_vs_vault_diff": data.get("code_vs_vault_diff", 0),
                }
            )
        except Exception:
            pass
    return {"total": len(entries), "history": entries}
