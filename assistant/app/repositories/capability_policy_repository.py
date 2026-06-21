from dataclasses import dataclass

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class CapabilityPolicyRecord:
    id: int
    capability: str
    priority_order: int
    model_id: int
    model_name: str = ""


class CapabilityPolicyRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_capability(self, capability: str) -> list[CapabilityPolicyRecord]:
        result = await self._session.execute(
            text("""
                SELECT cp.*, m.name as model_name
                FROM capability_policies cp
                JOIN models m ON cp.model_id = m.id
                WHERE cp.capability = :capability
                ORDER BY cp.priority_order ASC
            """),
            {"capability": capability},
        )
        return [
            CapabilityPolicyRecord(
                id=row.id,
                capability=row.capability,
                priority_order=row.priority_order,
                model_id=row.model_id,
                model_name=row.model_name,
            )
            for row in result.fetchall()
        ]

    async def upsert(self, capability: str, priority_order: int, model_id: int) -> int:
        result = await self._session.execute(
            text("""
                INSERT INTO capability_policies (capability, priority_order, model_id)
                VALUES (:capability, :priority_order, :model_id)
                ON CONFLICT (capability, priority_order) DO UPDATE SET
                    model_id = EXCLUDED.model_id
                RETURNING id
            """),
            {
                "capability": capability,
                "priority_order": priority_order,
                "model_id": model_id,
            },
        )
        await self._session.commit()
        return result.fetchone().id

    async def delete(self, policy_id: int) -> bool:
        result = await self._session.execute(
            text("DELETE FROM capability_policies WHERE id = :id"),
            {"id": policy_id},
        )
        await self._session.commit()
        return result.rowcount > 0

    async def list_all(self) -> list[CapabilityPolicyRecord]:
        result = await self._session.execute(
            text("""
                SELECT cp.*, m.name as model_name
                FROM capability_policies cp
                JOIN models m ON cp.model_id = m.id
                ORDER BY cp.capability, cp.priority_order ASC
            """)
        )
        return [
            CapabilityPolicyRecord(
                id=row.id,
                capability=row.capability,
                priority_order=row.priority_order,
                model_id=row.model_id,
                model_name=row.model_name,
            )
            for row in result.fetchall()
        ]
