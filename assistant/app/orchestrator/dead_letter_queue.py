from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID

from loguru import logger


@dataclass
class FailedExecution:
    execution_id: UUID
    trace_id: UUID
    workflow: str
    user_id: UUID
    session_id: UUID
    error: str
    context: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    retry_count: int = 0


class DeadLetterQueue:
    _failed: list[FailedExecution] = []

    @classmethod
    def add(cls, failed: FailedExecution) -> None:
        cls._failed.append(failed)
        logger.warning(
            f"[dlq] failed execution added: {failed.execution_id} "
            f"workflow={failed.workflow} error={failed.error}"
        )

    @classmethod
    def list_all(cls) -> list[FailedExecution]:
        return list(cls._failed)

    @classmethod
    def count(cls) -> int:
        return len(cls._failed)

    @classmethod
    def clear(cls) -> None:
        cls._failed.clear()
        logger.info("[dlq] cleared all failed executions")
