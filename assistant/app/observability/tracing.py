from typing import Any

from loguru import logger

from app.observability.event_bus import Event, EventSubscriber

try:
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
        OTLPSpanExporter,
    )
    from opentelemetry.sdk.resources import SERVICE_NAME, Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    _OTEL_AVAILABLE = True
except ImportError:
    _OTEL_AVAILABLE = False


_tracer: Any = None


def setup_tracing(service_name: str = "kaos-api", endpoint: str = "") -> None:
    global _tracer
    if not _OTEL_AVAILABLE:
        logger.warning(
            "[tracing] OpenTelemetry not installed; tracing disabled"
        )
        return
    if not endpoint:
        logger.info("[tracing] no endpoint configured; tracing disabled")
        return
    resource = Resource(attributes={SERVICE_NAME: service_name})
    provider = TracerProvider(resource=resource)
    exporter = OTLPSpanExporter(endpoint=endpoint)
    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    _tracer = trace.get_tracer(service_name)
    logger.info("[tracing] OpenTelemetry initialized: endpoint={}", endpoint)


def get_tracer() -> Any:
    return _tracer


class TracingSubscriber(EventSubscriber):
    async def on_event(self, event: Event) -> None:
        if not _tracer:
            return
        with _tracer.start_as_current_span(
            event.name,
            attributes={
                "execution_id": str(event.execution_id),
                "trace_id": str(event.trace_id),
                **{k: str(v) for k, v in event.data.items()},
            },
        ):
            pass
