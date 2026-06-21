from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class FailedExecutionRecord:
    id: UUID
    trace_id: Optional[UUID]
    execution_id: Optional[UUID]
    workflow: str
    payload: dict
    error: str
    created_at: datetime
    reprocessed_at: Optional[datetime] = None


class FailedExecutionRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(
        self,
        trace_id: Optional[UUID],
        execution_id: Optional[UUID],
        workflow: str,
        payload: dict,
        error: str,
    ) -> UUID:
        import uuid

        record_id = uuid.uuid4()
        await self._session.execute(
            text("""
                INSERT INTO failed_executions (id, trace_id, execution_id, workflow, payload, error)
                VALUES (:id, :trace_id, :execution_id, :workflow, :payload, :error)
            """),
            {
                "id": record_id,
                "trace_id": trace_id,
                "execution_id": execution_id,
                "workflow": workflow,
                "payload": payload,
                "error": error[:1000],
            },
        )
        await self._session.commit()
        return record_id

    async def list_pending(self, limit: int = 50) -> list[FailedExecutionRecord]:
        result = await self._session.execute(
            text("""
                SELECT * FROM failed_executions
                WHERE reprocessed_at IS NULL
                ORDER BY created_at DESC
                LIMIT :limit
            """),
            {"limit": limit},
        )
        return [
            FailedExecutionRecord(
                id=row.id,
                trace_id=row.trace_id,
                execution_id=row.execution_id,
                workflow=row.workflow,
                payload=dict(row.payload) if row.payload else {},
                error=row.error,
                created_at=row.created_at,
                reprocessed_at=row.reprocessed_at,
            )
            for row in result.fetchall()
        ]

    async def mark_reprocessed(self, record_id: UUID) -> bool:
        result = await self._session.execute(
            text("""
                UPDATE failed_executions
                SET reprocessed_at = NOW()
                WHERE id = :id AND reprocessed_at IS NULL
            """),
            {"id": record_id},
        )
        await self._session.commit()
        return result.rowcount > 0

    async def count_pending(self) -> int:
        result = await self._session.execute(
            text("SELECT COUNT(*) FROM failed_executions WHERE reprocessed_at IS NULL")
        )
        return result.fetchone()[0]
