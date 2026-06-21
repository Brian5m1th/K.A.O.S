from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.capability_policy_repository import (
    CapabilityPolicyRepository,
)


@dataclass
class ResolvedPolicy:
    capability: str
    priority_order: int
    model_name: str


class CapabilityPolicyResolver:
    def __init__(self, session: AsyncSession):
        self._repo = CapabilityPolicyRepository(session)

    async def resolve(self, capability: str) -> list[ResolvedPolicy]:
        records = await self._repo.get_by_capability(capability)
        return [
            ResolvedPolicy(
                capability=r.capability,
                priority_order=r.priority_order,
                model_name=r.model_name,
            )
            for r in records
        ]

    async def resolve_best(self, capability: str) -> ResolvedPolicy | None:
        policies = await self.resolve(capability)
        return policies[0] if policies else None

    async def list_all(self) -> list[ResolvedPolicy]:
        records = await self._repo.list_all()
        return [
            ResolvedPolicy(
                capability=r.capability,
                priority_order=r.priority_order,
                model_name=r.model_name,
            )
            for r in records
        ]
