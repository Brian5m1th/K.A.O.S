"""
LangGraphAdapter — Wraps existing LangGraph workflows for PlannerPort.

Provides plan generation and execution through the existing
LangGraph-based agent workflow state machines.
"""

import time
from datetime import datetime, timezone
from loguru import logger

from app.domain.ports.planner_port import (
    PlannerPort,
    PlanRequest,
    PlanResult,
    PlanStep,
    PlanStatus,
)

# In-memory plan store: plan_id -> {steps, status, started_at, updated_at}
_plan_store: dict[str, dict] = {}


class LangGraphAdapter(PlannerPort):
    """LangGraph-based planning and execution adapter."""

    @property
    def provider_name(self) -> str:
        return "langgraph"

    async def plan(self, request: PlanRequest) -> PlanResult:
        """Decompose intent into executable steps using existing agent graph."""
        plan_id = f"plan_{hash(request.intent) % 100000}_{int(time.time())}"
        steps = []

        # Use existing planner function from LangGraph agent
        try:
            from app.agent.nodes.planner import planner as planner_fn
            from app.agent.state import AgentState

            # Build a minimal AgentState to call the planner
            from langchain_core.messages import HumanMessage

            state: AgentState = {
                "messages": [HumanMessage(content=request.intent)],
                "retrieved_context": [],
                "tool_to_call": None,
                "tool_args": {},
                "tool_result": None,
                "session_id": request.user_id or "",
                "user_id": request.user_id or "",
                "username": "",
                "role": "user",
                "model": None,
                "ingest_source_path": None,
            }
            if request.context:
                state["retrieved_context"] = [
                    {"path": k, "content": v} for k, v in request.context.items()
                ]

            result = planner_fn(state)
            if result.get("tool_to_call"):
                steps.append(
                    PlanStep(
                        id=f"{plan_id}_step_0",
                        action=result["tool_to_call"],
                        inputs=result.get("tool_args", {}),
                        status=PlanStatus.PENDING,
                    )
                )
            else:
                # Planner responded directly — create a single completion step
                steps.append(
                    PlanStep(
                        id=f"{plan_id}_step_0",
                        action="respond",
                        inputs={"response": str(result.get("messages", []))},
                        status=PlanStatus.PENDING,
                    )
                )
        except Exception as exc:
            logger.warning(f"[planner] fallback to stub plan: {exc}")
            # Fallback: retrieve + execute
            steps = [
                PlanStep(
                    id=f"{plan_id}_step_0",
                    action="retrieve",
                    inputs={"query": request.intent},
                    status=PlanStatus.PENDING,
                ),
                PlanStep(
                    id=f"{plan_id}_step_1",
                    action="execute",
                    inputs={},
                    depends_on=[f"{plan_id}_step_0"],
                    status=PlanStatus.PENDING,
                ),
            ]

        now = datetime.now(timezone.utc).isoformat()
        _plan_store[plan_id] = {
            "plan_id": plan_id,
            "steps": steps,
            "status": PlanStatus.PENDING,
            "current_step": 0,
            "created_at": now,
            "updated_at": now,
        }

        return PlanResult(plan_id=plan_id, steps=steps, status=PlanStatus.PENDING)

    async def execute(self, plan_id: str) -> PlanResult:
        """Execute a plan through existing workflow engine."""
        plan = _plan_store.get(plan_id)
        if not plan:
            return PlanResult(
                plan_id=plan_id,
                steps=[],
                status=PlanStatus.FAILED,
            )

        plan["status"] = PlanStatus.RUNNING
        plan["updated_at"] = datetime.now(timezone.utc).isoformat()
        steps = plan["steps"]

        # Execute steps sequentially respecting depends_on
        for i, step in enumerate(steps):
            plan["current_step"] = i

            # Check dependencies
            deps_met = all(
                any(s.id == dep and s.status == PlanStatus.COMPLETED for s in steps)
                for dep in (step.depends_on or [])
            )
            if not deps_met:
                step.status = PlanStatus.FAILED
                step.error = f"Dependency not met: {step.depends_on}"
                plan["status"] = PlanStatus.FAILED
                plan["updated_at"] = datetime.now(timezone.utc).isoformat()
                return PlanResult(
                    plan_id=plan_id,
                    steps=steps,
                    status=PlanStatus.FAILED,
                )

            # Execute step action
            step.status = PlanStatus.RUNNING
            try:
                if step.action == "retrieve":
                    from app.providers.retrieval.qdrant_adapter import QdrantAdapter

                    adapter = QdrantAdapter()
                    query = step.inputs.get("query", "")
                    results = await adapter.search(query)
                    step.result = {"results": results}
                elif step.action == "execute":
                    # Invoke the main agent graph
                    from app.agent.graph import agent_graph

                    from langchain_core.messages import HumanMessage

                    invoke_input = {
                        "messages": [
                            HumanMessage(content=step.inputs.get("query", ""))
                        ],
                        "retrieved_context": [],
                        "tool_to_call": None,
                        "tool_args": {},
                        "tool_result": None,
                        "session_id": "",
                        "user_id": "",
                        "username": "",
                        "role": "user",
                        "model": None,
                        "ingest_source_path": None,
                    }
                    result = await agent_graph.ainvoke(invoke_input)
                    step.result = {"output": str(result.get("messages", []))}
                elif step.action == "respond":
                    step.result = {"output": step.inputs.get("response", "")}
                else:
                    # Generic tool call via executor
                    from app.agent.nodes.executor import TOOL_REGISTRY

                    tool_fn = TOOL_REGISTRY.get(step.action)
                    if tool_fn:
                        result = tool_fn.invoke(step.inputs)
                        step.result = {"output": str(result)}
                    else:
                        step.error = f"Unknown action: {step.action}"
                        step.status = PlanStatus.FAILED
                        plan["status"] = PlanStatus.FAILED
                        plan["updated_at"] = datetime.now(timezone.utc).isoformat()
                        return PlanResult(
                            plan_id=plan_id,
                            steps=steps,
                            status=PlanStatus.FAILED,
                        )

                step.status = PlanStatus.COMPLETED
            except Exception as exc:
                logger.error(f"[planner] step {step.id} failed: {exc}")
                step.status = PlanStatus.FAILED
                step.error = str(exc)
                plan["status"] = PlanStatus.FAILED
                plan["updated_at"] = datetime.now(timezone.utc).isoformat()
                return PlanResult(
                    plan_id=plan_id,
                    steps=steps,
                    status=PlanStatus.FAILED,
                )

        plan["status"] = PlanStatus.COMPLETED
        plan["updated_at"] = datetime.now(timezone.utc).isoformat()
        return PlanResult(plan_id=plan_id, steps=steps, status=PlanStatus.COMPLETED)

    async def status(self, plan_id: str) -> PlanResult:
        """Check the status of a plan."""
        plan = _plan_store.get(plan_id)
        if not plan:
            return PlanResult(plan_id=plan_id, status=PlanStatus.FAILED)

        return PlanResult(
            plan_id=plan_id,
            steps=plan["steps"],
            status=plan["status"],
        )

    async def health(self) -> bool:
        try:
            import importlib.util

            return importlib.util.find_spec("langgraph") is not None
        except Exception:
            return False
