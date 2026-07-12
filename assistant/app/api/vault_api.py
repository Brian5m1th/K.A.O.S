"""
Vault Analysis API — RF-B01, RF-B02, RF-B03 from SDD-Roadmap-Expansion-v2.

Endpoints for analyzing the Obsidian vault and retrieving results.
"""

from fastapi import APIRouter, HTTPException
from loguru import logger

from app.ai.vault_analyzer.analyzer_engine import AnalyzerEngine

router = APIRouter(prefix="/api/vault", tags=["Vault"])

# In-memory lock to prevent concurrent analysis
_analysis_in_progress = False


@router.post("/analyze")
async def analyze_vault(force: bool = False, include_suggestions: bool = True):
    """Dispara analise completa do vault (RF-B01).

    Args:
        force: Se True, ignora cache e executa novamente.
        include_suggestions: Se True, inclui sugestoes no resultado.

    Returns:
        ArchitectureAnalysis com coverage_score, drift_level, issues, suggestions.
    """
    global _analysis_in_progress

    if _analysis_in_progress:
        raise HTTPException(
            status_code=409,
            detail={
                "status": "running",
                "message": "Uma analise ja esta em andamento. Aguarde a conclusao.",
            },
        )

    _analysis_in_progress = True
    try:
        logger.info("[api/vault] Starting vault analysis...")
        analysis = await AnalyzerEngine.analyze_async()
        result = analysis.to_dict()

        if not include_suggestions:
            result.pop("suggestions", None)

        logger.info(
            f"[api/vault] Analysis complete: "
            f"coverage={result['coverage_score']}%, "
            f"drift={result['drift_level']}"
        )
        return result
    finally:
        _analysis_in_progress = False


@router.get("/analysis")
async def get_latest_analysis():
    """Retorna o ultimo relatorio de analise gerado (RF-B02)."""
    analysis = AnalyzerEngine.load_latest()
    if analysis is None:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "not_found",
                "message": "Nenhuma analise encontrada. Execute POST /api/vault/analyze primeiro.",
            },
        )

    return analysis.to_dict()


@router.get("/suggestions")
async def get_suggestions():
    """Retorna a lista de sugestoes do ultimo analysis (RF-B03)."""
    analysis = AnalyzerEngine.load_latest()
    if analysis is None:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "not_found",
                "message": "Nenhuma analise encontrada. Execute POST /api/vault/analyze primeiro.",
            },
        )

    return {
        "total": len(analysis.suggestions),
        "suggestions": analysis.suggestions,
        "generated_at": analysis.generated_at,
    }


@router.get("/analyze/status")
async def analysis_status():
    """Retorna o status atual da analise."""
    global _analysis_in_progress
    return {
        "running": _analysis_in_progress,
        "has_results": AnalyzerEngine.load_latest() is not None,
    }
