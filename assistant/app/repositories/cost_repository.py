"""
CostRepository — persistence and aggregation for cost tracking.

Uses SQLAlchemy async ORM with the CostEvent model.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cost_event import CostEvent


@dataclass
class CostEventData:
    """Input data for recording a cost event."""
    execution_id: UUID | None = None
    user_id: str | None = None
    provider: str = "unknown"
    workflow: str | None = None
    model: str | None = None
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0


@dataclass
class CostBreakdown:
    """Aggregated cost by provider and workflow."""
    provider: str
    workflow: str
    total_usd: float
    total_tokens: int
    request_count: int


@dataclass
class CostSummary:
    """Overall cost summary for a period."""
    total_usd: float
    period: str  # "day" | "week" | "month"
    breakdown: list[CostBreakdown]


class CostRepository:
    """Repository for persisting and querying cost events."""

    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, data: CostEventData) -> CostEvent:
        """Persist a cost event and return the ORM object."""
        orm = CostEvent(
            id=uuid4(),
            execution_id=data.execution_id,
            user_id=data.user_id,
            provider=data.provider,
            workflow=data.workflow,
            model=data.model,
            tokens_in=data.tokens_in,
            tokens_out=data.tokens_out,
            cost_usd=data.cost_usd,
        )
        self._session.add(orm)
        await self._session.commit()
        return orm

    async def aggregate(
        self,
        user_id: str | None = None,
        provider: str | None = None,
        workflow: str | None = None,
    ) -> list[CostBreakdown]:
        """Return cost breakdown grouped by provider and workflow."""
        filters = []
        if user_id:
            filters.append(CostEvent.user_id == user_id)
        if provider:
            filters.append(CostEvent.provider == provider)
        if workflow:
            filters.append(CostEvent.workflow == workflow)

        stmt = (
            select(
                CostEvent.provider,
                CostEvent.workflow,
                func.sum(CostEvent.cost_usd).label("total_usd"),
                func.sum(CostEvent.tokens_in + CostEvent.tokens_out).label("total_tokens"),
                func.count().label("request_count"),
            )
            .where(*filters)
            .group_by(CostEvent.provider, CostEvent.workflow)
            .order_by(CostEvent.provider, CostEvent.workflow)
        )
        result = await self._session.execute(stmt)
        return [
            CostBreakdown(
                provider=row.provider,
                workflow=row.workflow or "unknown",
                total_usd=float(row.total_usd or 0.0),
                total_tokens=int(row.total_tokens or 0),
                request_count=int(row.request_count),
            )
            for row in result
        ]

    async def summary(self, period: str = "day") -> CostSummary:
        """Return total cost for the period (day|week|month)."""
        now = datetime.now(timezone.utc)

        if period == "day":
            since = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif period == "week":
            since = now.replace(hour=0, minute=0, second=0, microsecond=0)
            since = since.replace(day=since.day - since.weekday())
        elif period == "month":
            since = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            raise ValueError(f"Invalid period: {period}. Use day, week, or month.")

        stmt = (
            select(
                CostEvent.provider,
                CostEvent.workflow,
                func.sum(CostEvent.cost_usd).label("total_usd"),
                func.sum(CostEvent.tokens_in + CostEvent.tokens_out).label("total_tokens"),
                func.count().label("request_count"),
            )
            .where(CostEvent.created_at >= since)
            .group_by(CostEvent.provider, CostEvent.workflow)
            .order_by(CostEvent.provider, CostEvent.workflow)
        )
        result = await self._session.execute(stmt)
        breakdown = [
            CostBreakdown(
                provider=row.provider,
                workflow=row.workflow or "unknown",
                total_usd=float(row.total_usd or 0.0),
                total_tokens=int(row.total_tokens or 0),
                request_count=int(row.request_count),
            )
            for row in result
        ]
        total = sum(b.total_usd for b in breakdown)

        return CostSummary(total_usd=total, period=period, breakdown=breakdown)
