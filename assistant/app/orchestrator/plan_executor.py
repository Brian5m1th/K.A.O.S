from typing import Any, AsyncIterator

from loguru import logger

from app.domain.chat import ChatRequest
from app.domain.execution_plan import ExecutionPlan
from app.orchestrator.circuit_breaker import (
    CircuitBreaker,
    CircuitState,
)
from app.orchestrator.dead_letter_queue import DeadLetterQueue, FailedExecution
from app.orchestrator.health_cache import ProviderHealthCache
from app.registry.service_registry import ServiceRegistry


class PlanExecutor:
    def __init__(
        self,
        circuit_breaker: CircuitBreaker | None = None,
        health_cache: ProviderHealthCache | None = None,
    ):
        self._circuit_breaker = circuit_breaker or CircuitBreaker(name="plan_executor")
        self._health_cache = health_cache or ProviderHealthCache()

    async def execute(
        self, plan: ExecutionPlan, request: ChatRequest
    ) -> AsyncIterator[str]:
        logger.info(
            f"[start] PlanExecutor - execute plan={plan.execution_id} "
            f"workflow={plan.workflow} model={plan.selected_model}"
        )

        if self._circuit_breaker.state == CircuitState.OPEN:
            if not await self._try_half_open():
                error_msg = "Circuit breaker is OPEN. Execution blocked."
                logger.warning(f"[blocked] {error_msg}")
                self._add_to_dlq(plan, error_msg)
                yield error_msg
                return

        try:
            workflow = ServiceRegistry.get_workflow(plan.workflow)
            async for chunk in workflow.execute(plan, request):
                yield chunk

            self._circuit_breaker._on_success()
            provider_name = plan.provider_configs.get("provider", "ollama")
            await self._health_cache.mark_healthy(provider_name)

        except Exception as exc:
            logger.error(
                f"[error] PlanExecutor - execution failed: {exc} "
                f"plan={plan.execution_id}"
            )
            self._circuit_breaker._on_failure(str(exc))
            provider_name = plan.provider_configs.get("provider", "ollama")
            await self._health_cache.mark_unhealthy(provider_name)

            self._add_to_dlq(
                plan,
                str(exc),
                {"model": plan.selected_model, "provider": provider_name},
            )

            yield f"Erro na execucao: {exc}"

        logger.debug("[finish] PlanExecutor - execute")

    async def _try_half_open(self) -> bool:
        if self._circuit_breaker.state != CircuitState.OPEN:
            return True
        import time as time_module

        if (
            time_module.monotonic() - self._circuit_breaker._last_failure_time
            >= self._circuit_breaker._recovery_timeout
        ):
            self._circuit_breaker.reset()
            return True
        return False

    def _add_to_dlq(
        self, plan: ExecutionPlan, error: str, context: dict[str, Any] | None = None
    ) -> None:
        DeadLetterQueue.add(
            FailedExecution(
                execution_id=plan.execution_id,
                trace_id=plan.trace_id,
                workflow=plan.workflow,
                user_id=plan.user_id,
                session_id=plan.session_id,
                error=error,
                context=context or {},
            )
        )
