"""
Evidence REST API — Architecture health and decision support.

Endpoints:
  GET  /api/evidence/report      — Full evidence report
  GET  /api/evidence/metric/{name} — Single metric
  GET  /api/evidence/history/{name} — Historical trend
  GET  /api/evidence/health      — Service health check
"""

from fastapi import APIRouter, Depends, Query

from app.core.services.evidence_service import EvidenceService

router = APIRouter(prefix="/api/evidence", tags=["Evidence"])


def get_evidence_service() -> EvidenceService:
    from app.providers.evidence.engine import EvidenceEngine

    svc = EvidenceService()
    svc.registry.register("engine", EvidenceEngine())
    return svc


@router.get("/report")
async def evidence_report(ev: EvidenceService = Depends(get_evidence_service)):
    """Full architectural evidence report from all sources."""
    report = await ev.collect()
    return {
        "generated_at": report.generated_at,
        "overall_score": round(report.overall_score, 1),
        "level": report.level,
        "sources_checked": report.sources_checked,
        "metrics": [
            {
                "name": m.name,
                "value": m.value,
                "level": m.level,
                "description": m.description,
                "source": m.source,
            }
            for m in report.metrics
        ],
        "recommendations": report.recommendations,
    }


@router.get("/metric/{name}")
async def evidence_metric(
    name: str,
    ev: EvidenceService = Depends(get_evidence_service),
):
    """Get a specific evidence metric by name."""
    metric = await ev.get_metric(name)
    if metric is None:
        return {"found": False}
    return {
        "name": metric.name,
        "value": metric.value,
        "level": metric.level,
        "description": metric.description,
        "source": metric.source,
    }


@router.get("/history/{name}")
async def evidence_history(
    name: str,
    days: int = Query(30, ge=1, le=365),
    ev: EvidenceService = Depends(get_evidence_service),
):
    """Get historical trend for a metric."""
    history = await ev.get_history(name, days)
    return {
        "metric": name,
        "days": days,
        "data_points": [
            {"date": m.source, "value": m.value, "level": m.level} for m in history
        ],
    }


@router.get("/health")
async def evidence_health(ev: EvidenceService = Depends(get_evidence_service)):
    return await ev.health()
