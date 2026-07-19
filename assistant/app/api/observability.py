from datetime import datetime
import asyncio
import json
from collections import deque

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.cost_repository import CostRepository
from app.observability.event_bus import EventBus, Event, EventSubscriber

# Store last 100 logs
LOG_BUFFER = deque(maxlen=100)
LOG_LISTENERS = []

# Store last 100 events
EVENT_BUFFER = deque(maxlen=100)
EVENT_LISTENERS = []


def log_sink(message):
    record = message.record
    time_str = record["time"].strftime("%Y-%m-%d %H:%M:%S")
    level_str = record["level"].name
    msg = f"{time_str} | {level_str:<8} | {record['name']}:{record['function']}:{record['line']} - {record['message']}"
    LOG_BUFFER.append(msg)
    for q in list(LOG_LISTENERS):
        try:
            q.put_nowait(msg)
        except Exception as e:
            logger.debug("[observability] log listener queue full/disconnected: {}", e)


# Register the sink on import
logger.add(log_sink, format="{message}")


class SSEEventSubscriber(EventSubscriber):
    async def on_event(self, event: Event) -> None:
        source_map = {
            "memory": "database",
            "conversation": "database",
            "orchestrator": "webhook",
            "workflow": "webhook",
            "llm": "agent",
            "request": "system",
        }

        # Determine source
        source = "system"
        for prefix, src in source_map.items():
            if event.name.startswith(prefix):
                source = src
                break

        payload = {
            "id": f"{event.execution_id}_{event.timestamp.timestamp()}",
            "source": source,
            "type": event.name,
            "message": f"Event data: {event.data}"
            if event.data
            else f"Event '{event.name}' processed successfully.",
            "timestamp": event.timestamp.strftime("%H:%M:%S"),
        }

        EVENT_BUFFER.append(payload)

        for q in list(EVENT_LISTENERS):
            try:
                q.put_nowait(payload)
            except Exception as e:
                logger.debug("[observability] event listener queue full/disconnected: {}", e)


# Subscribe this subscriber to ALL event names on import
subscriber = SSEEventSubscriber()
for ev_name in [
    "request_started",
    "intent_classified",
    "model_selected",
    "workflow_started",
    "workflow_completed",
    "workflow_step",
    "llm_request",
    "llm_response",
    "fallback_triggered",
    "request_completed",
    "error",
    "orchestrator.execution_started",
    "orchestrator.execution_completed",
    "orchestrator.execution_failed",
    "memory.write.started",
    "memory.write.completed",
    "memory.write.failed",
    "memory.read.started",
    "memory.read.completed",
    "memory.deleted",
    "conversation.summarized",
    "conversation.stored",
]:
    EventBus.subscribe(ev_name, subscriber)

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
        ("grafana", "http://grafana:3000/api/health"),
    ]:
        try:
            async with httpx.AsyncClient(timeout=2) as c:
                r = await c.get(url)
                services[name] = r.is_success
        except Exception as e:
            logger.warning("[observability] {} health check failed: {}", name, e)
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


@router.get("/logs/stream")
async def stream_logs():
    """SSE endpoint to stream real-time system log records."""

    async def event_generator():
        # 1. Yield history from the logs buffer
        for log in list(LOG_BUFFER):
            yield f"data: {log}\n\n"

        # 2. Listen to future log records
        q = asyncio.Queue()
        LOG_LISTENERS.append(q)
        try:
            while True:
                log = await q.get()
                yield f"data: {log}\n\n"
        except asyncio.CancelledError:
            logger.debug("[observability] log stream cancelled (client disconnected)")
        finally:
            if q in LOG_LISTENERS:
                LOG_LISTENERS.remove(q)

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@router.get("/events/stream")
async def stream_events():
    """SSE endpoint to stream real-time EventBus events."""

    async def event_generator():
        # 1. Yield history from the event buffer
        for ev in list(EVENT_BUFFER):
            yield f"data: {json.dumps(ev)}\n\n"

        # 2. Listen to future events
        q = asyncio.Queue()
        EVENT_LISTENERS.append(q)
        try:
            while True:
                ev = await q.get()
                yield f"data: {json.dumps(ev)}\n\n"
        except asyncio.CancelledError:
            logger.debug("[observability] event stream cancelled (client disconnected)")
        finally:
            if q in EVENT_LISTENERS:
                EVENT_LISTENERS.remove(q)

    return StreamingResponse(event_generator(), media_type="text/event-stream")
