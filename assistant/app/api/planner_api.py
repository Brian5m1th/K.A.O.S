"""
Planner REST API — Task planning and agent orchestration.

Endpoints:
  POST /api/planner/plan         — Generate execution plan from intent
  POST /api/planner/execute      — Execute a plan
  GET  /api/planner/status/{id}  — Check plan status
  GET  /api/planner/health       — Service health check
"""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional

from app.core.services.planner_service import PlannerService
from app.domain.ports.planner_port import PlanRequest

router = APIRouter(prefix="/api/planner", tags=["Planner"])


class PlanRequest(BaseModel):
    intent: str
    context: dict = {}
    user_id: Optional[str] = None
    max_steps: int = 10


class ExecuteRequest(BaseModel):
    plan_id: str


def get_planner_service() -> PlannerService:
    from app.providers.planner.langgraph_adapter import LangGraphAdapter
    svc = PlannerService()
    svc.registry.register("langgraph", LangGraphAdapter())
    return svc


@router.post("/plan")
async def create_plan(
    body: PlanRequest,
    planner: PlannerService = Depends(get_planner_service),
):
    """Generate an execution plan from an intent."""
    request = PlanRequest(
        intent=body.intent,
        context=body.context,
        user_id=body.user_id,
        max_steps=body.max_steps,
    )
    result = await planner.plan(request)
    return {
        "plan_id": result.plan_id,
        "steps": [
            {"id": s.id, "action": s.action, "status": s.status}
            for s in result.steps
        ],
        "status": result.status,
    }


@router.post("/execute")
async def execute_plan(
    body: ExecuteRequest,
    planner: PlannerService = Depends(get_planner_service),
):
    """Execute a previously generated plan."""
    result = await planner.execute(body.plan_id)
    return {"plan_id": result.plan_id, "status": result.status}


@router.get("/status/{plan_id}")
async def plan_status(
    plan_id: str,
    planner: PlannerService = Depends(get_planner_service),
):
    """Check the status of a plan."""
    result = await planner.status(plan_id)
    return {"plan_id": result.plan_id, "status": result.status}


@router.get("/health")
async def planner_health(planner: PlannerService = Depends(get_planner_service)):
    return await planner.health()
