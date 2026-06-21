from prometheus_client import Counter, Histogram

from app.observability.event_bus import Event, EventSubscriber

_event_counter = Counter(
    "kaos_events_total",
    "Total events by name and status",
    ["event_name", "status"],
)

_workflow_duration = Histogram(
    "kaos_workflow_duration_seconds",
    "Workflow execution duration in seconds",
    ["workflow"],
)

_llm_duration = Histogram(
    "kaos_llm_request_duration_seconds",
    "LLM request duration in seconds",
    ["provider"],
)


class MetricsSubscriber(EventSubscriber):
    async def on_event(self, event: Event) -> None:
        _event_counter.labels(event_name=event.name, status="received").inc()

        if event.name == "workflow_started":
            _event_counter.labels(event_name=event.name, status="started").inc()

        elif event.name == "workflow_completed":
            _event_counter.labels(event_name=event.name, status="completed").inc()
            duration = event.data.get("duration_seconds", 0)
            workflow = event.data.get("workflow", "unknown")
            _workflow_duration.labels(workflow=workflow).observe(duration)

        elif event.name == "orchestrator.execution_failed":
            _event_counter.labels(event_name=event.name, status="failed").inc()

        elif event.name == "llm_request":
            provider = event.data.get("provider", "unknown")
            _llm_duration.labels(provider=provider).observe(
                event.data.get("duration_seconds", 0)
            )
