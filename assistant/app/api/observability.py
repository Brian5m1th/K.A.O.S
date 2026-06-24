from datetime import datetime

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.cost_repository import CostRepository

router = APIRouter(prefix="/api/observability", tags=["Observability"])


# ── Response models ──────────────────────────────────────────────────


class CostBreakdownResponse(BaseModel):
    provider: str
    workflow: str
    total_usd: float
    total_tokens: int
    request_count: int


class CostsResponse(BaseModel):
    source: str
    total_usd: float
    breakdown: list[CostBreakdownResponse]
    updated_at: str


class CostSummaryResponse(BaseModel):
    total_usd: float
    period: str
    breakdown: list[CostBreakdownResponse]


# ── Endpoints ────────────────────────────────────────────────────────


@router.get("/health")
async def observability_health():
    services = {"prometheus": False, "loki": False, "grafana": False}
    for name, url in [
        ("prometheus", "http://prometheus:9090/-/ready"),
        ("loki", "http://loki:3100/ready"),
        ("grafana", "http://grafana:3001/api/health"),
    ]:
        try:
            async with httpx.AsyncClient(timeout=2) as c:
                r = await c.get(url)
                services[name] = r.is_success
        except Exception:
            pass
    return services


@router.get("/costs", response_model=CostsResponse)
async def get_costs(
    user_id: str | None = Query(None, description="Filtrar por usuário"),
    provider: str | None = Query(None, description="Filtrar por provider"),
    workflow: str | None = Query(None, description="Filtrar por workflow"),
    session: AsyncSession = Depends(get_session),
):
    """RF-F01: Breakdown de custos por provider e workflow."""
    repo = CostRepository(session)
    breakdown = await repo.aggregate(
        user_id=user_id, provider=provider, workflow=workflow
    )

    total_usd = sum(b.total_usd for b in breakdown)

    return CostsResponse(
        source="postgres",
        total_usd=round(total_usd, 6),
        breakdown=[
            CostBreakdownResponse(
                provider=b.provider,
                workflow=b.workflow,
                total_usd=round(b.total_usd, 6),
                total_tokens=b.total_tokens,
                request_count=b.request_count,
            )
            for b in breakdown
        ],
        updated_at=datetime.now().isoformat(),
    )


@router.get("/costs/summary", response_model=CostSummaryResponse)
async def get_costs_summary(
    period: str = Query("day", description="Período: day, week, month"),
    session: AsyncSession = Depends(get_session),
):
    """RF-F02: Total de custos para o período especificado."""
    if period not in ("day", "week", "month"):
        raise HTTPException(
            status_code=422,
            detail="Invalid period. Use: day, week, or month",
        )

    repo = CostRepository(session)
    summary = await repo.summary(period=period)

    return CostSummaryResponse(
        total_usd=round(summary.total_usd, 6),
        period=summary.period,
        breakdown=[
            CostBreakdownResponse(
                provider=b.provider,
                workflow=b.workflow,
                total_usd=round(b.total_usd, 6),
                total_tokens=b.total_tokens,
                request_count=b.request_count,
            )
            for b in summary.breakdown
        ],
    )
