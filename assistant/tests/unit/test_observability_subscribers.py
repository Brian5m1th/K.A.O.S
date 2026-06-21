from uuid import UUID

import pytest
from prometheus_client import REGISTRY

from app.observability.event_bus import Event, EventBus, EventSubscriber
from app.observability.subscribers.audit_subscriber import AuditSubscriber
from app.observability.subscribers.logger_subscriber import LoggerSubscriber
from app.observability.subscribers.metrics_subscriber import MetricsSubscriber


@pytest.fixture(autouse=True)
def clear_eventbus():
    EventBus.clear()
    yield


@pytest.mark.asyncio
async def test_logger_subscriber_logs_event():
    subscriber = LoggerSubscriber()
    event = Event(
        name="test_event",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"workflow": "chat"},
    )
    await subscriber.on_event(event)


@pytest.mark.asyncio
async def test_metrics_subscriber_counts_events():
    subscriber = MetricsSubscriber()
    for name in ("workflow_started", "workflow_completed"):
        event = Event(
            name=name,
            execution_id=UUID(int=1),
            trace_id=UUID(int=2),
            data={"workflow": "chat", "duration_seconds": 1.5},
        )
        await subscriber.on_event(event)

    samples = []
    for metric in REGISTRY.collect():
        if metric.name == "kaos_events":
            for sample in metric.samples:
                if sample.name.endswith("_total"):
                    samples.append((sample.labels["event_name"], sample.labels["status"], sample.value))

    assert ("workflow_started", "received", 1.0) in samples
    assert ("workflow_started", "started", 1.0) in samples
    assert ("workflow_completed", "received", 1.0) in samples
    assert ("workflow_completed", "completed", 1.0) in samples


@pytest.mark.asyncio
async def test_metrics_subscriber_workflow_duration():
    subscriber = MetricsSubscriber()
    event = Event(
        name="workflow_completed",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"workflow": "chat", "duration_seconds": 2.5},
    )
    await subscriber.on_event(event)

    found = False
    for metric in REGISTRY.collect():
        if metric.name == "kaos_workflow_duration_seconds":
            for sample in metric.samples:
                if sample.labels.get("workflow") == "chat":
                    found = True
    assert found


@pytest.mark.asyncio
async def test_metrics_subscriber_llm_duration():
    subscriber = MetricsSubscriber()
    event = Event(
        name="llm_request",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"provider": "ollama", "duration_seconds": 0.5},
    )
    await subscriber.on_event(event)

    found = False
    for metric in REGISTRY.collect():
        if metric.name == "kaos_llm_request_duration_seconds":
            for sample in metric.samples:
                if sample.labels.get("provider") == "ollama":
                    found = True
    assert found


@pytest.mark.asyncio
async def test_metrics_subscriber_failed_event():
    subscriber = MetricsSubscriber()
    event = Event(
        name="orchestrator.execution_failed",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"error": "timeout"},
    )
    await subscriber.on_event(event)

    samples = []
    for metric in REGISTRY.collect():
        if metric.name == "kaos_events":
            for sample in metric.samples:
                if sample.name.endswith("_total"):
                    samples.append((sample.labels["event_name"], sample.labels["status"], sample.value))

    assert ("orchestrator.execution_failed", "received", 1.0) in samples
    assert ("orchestrator.execution_failed", "failed", 1.0) in samples


@pytest.mark.asyncio
async def test_audit_subscriber_logs_event():
    subscriber = AuditSubscriber()
    event = Event(
        name="orchestrator.execution_started",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"workflow": "chat"},
    )
    await subscriber.on_event(event)


@pytest.mark.asyncio
async def test_subscribers_work_with_eventbus():
    logger_sub = LoggerSubscriber()
    metrics_sub = MetricsSubscriber()
    EventBus.subscribe("test.subscriber_workflow", logger_sub)
    EventBus.subscribe("test.subscriber_workflow", metrics_sub)

    event = Event(
        name="test.subscriber_workflow",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
        data={"key": "value"},
    )
    await EventBus.publish(event)


@pytest.mark.asyncio
async def test_eventbus_subscriber_error_does_not_break_publish():
    class BrokenSubscriber(EventSubscriber):
        async def on_event(self, event: Event) -> None:
            raise RuntimeError("subscriber failure")

    broken = BrokenSubscriber()
    logger_sub = LoggerSubscriber()
    EventBus.subscribe("test.broken", broken)
    EventBus.subscribe("test.broken", logger_sub)

    event = Event(
        name="test.broken",
        execution_id=UUID(int=1),
        trace_id=UUID(int=2),
    )
    await EventBus.publish(event)
