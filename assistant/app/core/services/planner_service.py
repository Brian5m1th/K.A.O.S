"""
PlannerService — Task planning orchestrator.
"""

from app.core.provider_registry import ProviderRegistry
from app.domain.ports.planner_port import PlannerPort, PlanRequest, PlanResult


class PlannerService:
    """Service for task decomposition and agent orchestration."""

    def __init__(self):
        self.registry = ProviderRegistry[PlannerPort]("planner")

    async def plan(self, request: PlanRequest) -> PlanResult:
        return await self.registry.active.plan(request)

    async def execute(self, plan_id: str) -> PlanResult:
        return await self.registry.active.execute(plan_id)

    async def status(self, plan_id: str) -> PlanResult:
        return await self.registry.active.status(plan_id)

    async def health(self) -> dict:
        provider = self.registry.active_key or "none"
        ok = await self.registry.active.health()
        return {
            "service": "planner",
            "healthy": ok,
            "active_provider": provider,
            "available_providers": self.registry.list_providers(),
        }
