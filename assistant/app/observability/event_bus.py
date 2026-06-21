from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID

from loguru import logger


@dataclass
class Event:
    name: str
    execution_id: UUID
    trace_id: UUID
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    data: dict[str, Any] = field(default_factory=dict)


class EventSubscriber(ABC):
    @abstractmethod
    async def on_event(self, event: Event) -> None: ...


class EventBus:
    _subscribers: dict[str, list[EventSubscriber]] = {}

    @classmethod
    def subscribe(cls, event_name: str, subscriber: EventSubscriber) -> None:
        if event_name not in cls._subscribers:
            cls._subscribers[event_name] = []
        cls._subscribers[event_name].append(subscriber)
        logger.info(f"[event_bus] subscriber registered: {subscriber.__class__.__name__} for {event_name}")

    @classmethod
    def unsubscribe(cls, event_name: str, subscriber: EventSubscriber) -> None:
        if event_name in cls._subscribers:
            cls._subscribers[event_name] = [
                s for s in cls._subscribers[event_name] if s is not subscriber
            ]

    @classmethod
    async def publish(cls, event: Event) -> None:
        subscribers = cls._subscribers.get(event.name, [])
        for subscriber in subscribers:
            try:
                await subscriber.on_event(event)
            except Exception as e:
                logger.error(
                    f"[event_bus] subscriber failed: "
                    f"{subscriber.__class__.__name__} for {event.name}: {e}"
                )

    @classmethod
    def clear(cls) -> None:
        cls._subscribers.clear()


EVENT_REQUEST_STARTED = "request_started"
EVENT_INTENT_CLASSIFIED = "intent_classified"
EVENT_MODEL_SELECTED = "model_selected"
EVENT_WORKFLOW_STARTED = "workflow_started"
EVENT_WORKFLOW_STEP = "workflow_step"
EVENT_LLM_REQUEST = "llm_request"
EVENT_LLM_RESPONSE = "llm_response"
EVENT_FALLBACK_TRIGGERED = "fallback_triggered"
EVENT_REQUEST_COMPLETED = "request_completed"
EVENT_ERROR = "error"
