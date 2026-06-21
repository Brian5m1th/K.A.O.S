from typing import AsyncIterator
from uuid import UUID, uuid4, uuid5

from loguru import logger

from app.domain.chat import ChatRequest
from app.domain.execution_plan import ExecutionPlan
from app.models.model_router import ModelRouter
from app.orchestrator.circuit_breaker import CircuitBreaker
from app.orchestrator.health_cache import ProviderHealthCache
from app.orchestrator.plan_executor import PlanExecutor
from app.observability.event_bus import Event, EventBus


class UniversalOrchestrator:
    def __init__(
        self,
        model_router: ModelRouter | None = None,
        circuit_breaker: CircuitBreaker | None = None,
        health_cache: ProviderHealthCache | None = None,
    ):
        self._model_router = model_router
        self._executor = PlanExecutor(
            circuit_breaker=circuit_breaker,
            health_cache=health_cache,
        )

    async def execute(
        self,
        request: ChatRequest,
        workflow: str = "chat",
        capabilities: list[str] | None = None,
        user_id: UUID | None = None,
    ) -> AsyncIterator[str]:
        uid = user_id or UUID(int=0)
        session_uuid = (
            uuid5(UUID(int=0), request.session_id) if request.session_id else uuid4()
        )

        model_name = "qwen3:4b"
        plan = ExecutionPlan.create(
            workflow=workflow,
            selected_model=model_name,
            user_id=uid,
            session_id=session_uuid,
            capabilities=capabilities or [],
        )

        logger.info(
            f"[start] UniversalOrchestrator - execute plan={plan.execution_id} "
            f"workflow={workflow} user={uid}"
        )

        await EventBus.publish(
            Event(
                name="orchestrator.execution_started",
                execution_id=plan.execution_id,
                trace_id=plan.trace_id,
                data={
                    "workflow": workflow,
                    "model": model_name,
                    "user_id": str(uid),
                },
            )
        )

        try:
            async for chunk in self._executor.execute(plan, request):
                yield chunk

            await EventBus.publish(
                Event(
                    name="orchestrator.execution_completed",
                    execution_id=plan.execution_id,
                    trace_id=plan.trace_id,
                )
            )

        except Exception as exc:
            await EventBus.publish(
                Event(
                    name="orchestrator.execution_failed",
                    execution_id=plan.execution_id,
                    trace_id=plan.trace_id,
                    data={"error": str(exc)},
                )
            )
            raise

        logger.debug("[finish] UniversalOrchestrator - execute")
