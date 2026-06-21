from uuid import UUID

import pytest

from app.observability.cost_tracker import CostTracker
from app.observability.event_bus import Event


@pytest.fixture
def tracker():
    return CostTracker()


@pytest.mark.asyncio
async def test_tracks_llm_request(tracker):
    event = Event(
        name="llm_request",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"provider": "ollama", "model": "qwen3:4b"},
    )
    await tracker.on_event(event)
    summary = tracker.summary()
    assert summary["executions_count"] == 1


@pytest.mark.asyncio
async def test_tracks_workflow_started(tracker):
    event = Event(
        name="workflow_started",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"workflow": "chat"},
    )
    await tracker.on_event(event)
    assert tracker._executions[UUID(int=1)]["workflow"] == "chat"


@pytest.mark.asyncio
async def test_ollama_cost_is_zero(tracker):
    event = Event(
        name="workflow_completed",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={
            "provider": "ollama",
            "model": "qwen3:4b",
            "tokens_in": 100,
            "tokens_out": 50,
        },
    )
    await tracker.on_event(event)
    assert tracker._total_cost == 0.0


@pytest.mark.asyncio
async def test_openai_cost_accumulates(tracker):
    event = Event(
        name="workflow_completed",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={
            "provider": "openai",
            "model": "gpt-4",
            "tokens_in": 1000,
            "tokens_out": 500,
        },
    )
    await tracker.on_event(event)
    assert tracker._total_cost > 0
    assert "openai" in tracker._provider_costs


@pytest.mark.asyncio
async def test_summary_format(tracker):
    event = Event(
        name="workflow_completed",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={
            "provider": "ollama",
            "model": "qwen3:4b",
            "tokens_in": 100,
            "tokens_out": 50,
        },
    )
    await tracker.on_event(event)
    summary = tracker.summary()
    assert "total_cost" in summary
    assert "by_provider" in summary
    assert "by_workflow" in summary
    assert summary["executions_count"] >= 0


@pytest.mark.asyncio
async def test_reset_clears_all(tracker):
    event = Event(
        name="llm_request",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"provider": "ollama"},
    )
    await tracker.on_event(event)
    tracker.reset()
    assert tracker._total_cost == 0.0
    assert len(tracker._executions) == 0
