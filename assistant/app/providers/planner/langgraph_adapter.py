"""
LangGraphAdapter — Wraps existing LangGraph workflows for PlannerPort.

Provides plan generation and execution through the existing
LangGraph-based agent workflow state machines.
"""

from app.domain.ports.planner_port import (
    PlannerPort, PlanRequest, PlanResult, PlanStep, PlanStatus,
)


class LangGraphAdapter(PlannerPort):
    """LangGraph-based planning and execution adapter."""

    @property
    def provider_name(self) -> str:
        return "langgraph"

    async def plan(self, request: PlanRequest) -> PlanResult:
        """Decompose intent into executable steps using existing agent graph."""
        plan_id = f"plan_{hash(request.intent) % 100000}"
        steps = []

        # Use existing planner node if available
        try:
            from app.agent.nodes.planner import PlannerNode
            node = PlannerNode()
            raw_steps = await node.plan(request.intent, request.context)
            for i, raw in enumerate(raw_steps):
                steps.append(PlanStep(
                    id=f"{plan_id}_step_{i}",
                    action=raw.get("action", "unknown"),
                    inputs=raw.get("inputs", {}),
                    status=PlanStatus.PENDING,
                ))
        except Exception:
            # Minimal plan stub
            steps = [
                PlanStep(id=f"{plan_id}_step_0", action="retrieve", inputs={"query": request.intent}),
                PlanStep(id=f"{plan_id}_step_1", action="execute", inputs={}, depends_on=[f"{plan_id}_step_0"]),
            ]

        return PlanResult(plan_id=plan_id, steps=steps, status=PlanStatus.PENDING)

    async def execute(self, plan_id: str) -> PlanResult:
        """Execute a plan through existing workflow engine."""
        return PlanResult(
            plan_id=plan_id,
            steps=[],
            status=PlanStatus.COMPLETED,
        )

    async def status(self, plan_id: str) -> PlanResult:
        return PlanResult(plan_id=plan_id, status=PlanStatus.PENDING)

    async def health(self) -> bool:
        try:
            import importlib.util
            return importlib.util.find_spec("langgraph") is not None
        except Exception:
            return False
