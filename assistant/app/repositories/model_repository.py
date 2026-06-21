from dataclasses import dataclass
from typing import Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession



@dataclass
class ModelRecord:
    id: int
    name: str
    provider_name: str
    context_window: int
    cost_input: float
    cost_output: float
    capabilities: list[str]
    is_active: bool


class ModelRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_name(self, name: str) -> Optional[ModelRecord]:
        result = await self._session.execute(
            text("SELECT * FROM models WHERE name = :name"),
            {"name": name},
        )
        row = result.fetchone()
        if not row:
            return None
        return ModelRecord(
            id=row.id,
            name=row.name,
            provider_name=row.provider_name,
            context_window=row.context_window,
            cost_input=float(row.cost_input) if row.cost_input else 0.0,
            cost_output=float(row.cost_output) if row.cost_output else 0.0,
            capabilities=list(row.capabilities) if row.capabilities else [],
            is_active=row.is_active,
        )

    async def list_by_capability(self, capability: str) -> list[ModelRecord]:
        result = await self._session.execute(
            text(
                "SELECT * FROM models WHERE :capability = ANY(capabilities) AND is_active = TRUE"
            ),
            {"capability": capability},
        )
        return [
            ModelRecord(
                id=row.id,
                name=row.name,
                provider_name=row.provider_name,
                context_window=row.context_window,
                cost_input=float(row.cost_input) if row.cost_input else 0.0,
                cost_output=float(row.cost_output) if row.cost_output else 0.0,
                capabilities=list(row.capabilities) if row.capabilities else [],
                is_active=row.is_active,
            )
            for row in result.fetchall()
        ]

    async def list_all(self) -> list[ModelRecord]:
        result = await self._session.execute(
            text("SELECT * FROM models WHERE is_active = TRUE ORDER BY name")
        )
        return [
            ModelRecord(
                id=row.id,
                name=row.name,
                provider_name=row.provider_name,
                context_window=row.context_window,
                cost_input=float(row.cost_input) if row.cost_input else 0.0,
                cost_output=float(row.cost_output) if row.cost_output else 0.0,
                capabilities=list(row.capabilities) if row.capabilities else [],
                is_active=row.is_active,
            )
            for row in result.fetchall()
        ]

    async def upsert(self, record: ModelRecord) -> int:
        result = await self._session.execute(
            text("""
                INSERT INTO models (name, provider_name, context_window, cost_input, cost_output, capabilities, is_active)
                VALUES (:name, :provider_name, :context_window, :cost_input, :cost_output, :capabilities, :is_active)
                ON CONFLICT (name) DO UPDATE SET
                    provider_name = EXCLUDED.provider_name,
                    context_window = EXCLUDED.context_window,
                    cost_input = EXCLUDED.cost_input,
                    cost_output = EXCLUDED.cost_output,
                    capabilities = EXCLUDED.capabilities,
                    is_active = EXCLUDED.is_active,
                    updated_at = NOW()
                RETURNING id
            """),
            {
                "name": record.name,
                "provider_name": record.provider_name,
                "context_window": record.context_window,
                "cost_input": str(record.cost_input),
                "cost_output": str(record.cost_output),
                "capabilities": record.capabilities,
                "is_active": record.is_active,
            },
        )
        await self._session.commit()
        return result.fetchone().id
