from loguru import logger
import httpx

from app.observability.event_bus import Event, EventSubscriber
from app.config.settings import settings


class N8NSubscriber(EventSubscriber):
    def __init__(self) -> None:
        self._webhook_url = settings.N8N_WEBHOOK_URL

    async def on_event(self, event: Event) -> None:
        if not self._webhook_url:
            return
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                payload = {
                    "event": event.name,
                    "execution_id": str(event.execution_id),
                    "trace_id": str(event.trace_id),
                    "timestamp": event.timestamp.isoformat(),
                    "data": event.data,
                }
                url = f"{self._webhook_url.rstrip('/')}/kaos-event"
                await client.post(url, json=payload)
        except Exception as e:
            logger.debug(f"[n8n] falha ao enviar evento {event.name}: {e}")
