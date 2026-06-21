from loguru import logger

from app.observability.event_bus import Event, EventSubscriber


class AuditSubscriber(EventSubscriber):
    async def on_event(self, event: Event) -> None:
        logger.bind(
            event_name=event.name,
            execution_id=str(event.execution_id),
            trace_id=str(event.trace_id),
            timestamp=event.timestamp.isoformat(),
            audit=True,
            **event.data,
        ).info("audit")
