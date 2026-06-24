from typing import AsyncIterator
from uuid import UUID, uuid4, uuid5

from loguru import logger

from app.config.settings import settings
from app.domain.chat import ChatRequest
from app.domain.execution_plan import ExecutionPlan
from app.models.model_router import ModelRouter, ModelSelection
from app.orchestrator.circuit_breaker import CircuitBreaker
from app.orchestrator.health_cache import ProviderHealthCache
from app.orchestrator.plan_executor import PlanExecutor
from app.observability.event_bus import (
    EVENT_ORCHESTRATOR_COMPLETED,
    EVENT_ORCHESTRATOR_FAILED,
    EVENT_ORCHESTRATOR_STARTED,
    Event,
    EventBus,
)


# Workflows que exigem role "admin" ou permissão explícita
_ADMIN_ONLY_WORKFLOWS = {"agent", "browser", "multi_agent"}


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

    async def _select_model(
        self,
        workflow: str,
        capabilities: list[str],
        user_id: UUID | None,
    ) -> ModelSelection:
        """Select model via ModelRouter if available, fallback to settings."""
        if self._model_router is not None and capabilities:
            try:
                return await self._model_router.select_model(
                    capabilities=capabilities,
                    user_id=str(user_id) if user_id else None,
                    workflow_type=workflow,
                )
            except Exception as exc:
                logger.warning(
                    "[orchestrator] ModelRouter failed, using fallback: {}",
                    exc,
                )

        # Fallback: usar model do settings baseado no workflow
        if workflow in ("fast", "chat"):
            model_name = settings.OLLAMA_FAST_MODEL
        else:
            model_name = settings.OLLAMA_MODEL

        return ModelSelection(
            model=model_name,
            provider="ollama",
            reason="settings_fallback",
            capabilities=capabilities,
        )

    async def execute(
        self,
        request: ChatRequest,
        workflow: str = "chat",
        capabilities: list[str] | None = None,
        user_id: UUID | None = None,
    ) -> AsyncIterator[str]:
        uid = user_id or UUID(int=0)
        user_role = request.role or "user"
        session_uuid = (
            uuid5(UUID(int=0), request.session_id) if request.session_id else uuid4()
        )

        # RF-A03: Validar capabilities contra role do usuário
        if user_role == "user" and workflow in _ADMIN_ONLY_WORKFLOWS:
            error_msg = (
                f"Workflow '{workflow}' requires admin role. "
                f"User role: '{user_role}'"
            )
            logger.warning("[orchestrator] access denied: {}", error_msg)
            raise PermissionError(error_msg)

        cap_list = capabilities or []

        # Selecionar modelo via ModelRouter ou fallback
        selection = await self._select_model(
            workflow=workflow,
            capabilities=cap_list,
            user_id=uid,
        )

        model_name = selection.model
        provider_name = selection.provider

        plan = ExecutionPlan.create(
            workflow=workflow,
            selected_model=model_name,
            user_id=uid,
            session_id=session_uuid,
            capabilities=cap_list,
        )

        logger.info(
            f"[start] UniversalOrchestrator - execute plan={plan.execution_id} "
            f"workflow={workflow} model={model_name} provider={provider_name} "
            f"user={uid} role={user_role}"
        )

        await EventBus.publish(
            Event(
                name=EVENT_ORCHESTRATOR_STARTED,
                execution_id=plan.execution_id,
                trace_id=plan.trace_id,
                data={
                    "workflow": workflow,
                    "model": model_name,
                    "provider": provider_name,
                    "user_id": str(uid),
                    "user_role": user_role,
                },
            )
        )

        try:
            async for chunk in self._executor.execute(plan, request):
                yield chunk

            await EventBus.publish(
                Event(
                    name=EVENT_ORCHESTRATOR_COMPLETED,
                    execution_id=plan.execution_id,
                    trace_id=plan.trace_id,
                    data={
                        "model": model_name,
                        "provider": provider_name,
                        "workflow": workflow,
                    },
                )
            )

        except Exception as exc:
            await EventBus.publish(
                Event(
                    name=EVENT_ORCHESTRATOR_FAILED,
                    execution_id=plan.execution_id,
                    trace_id=plan.trace_id,
                    data={"error": str(exc)},
                )
            )
            raise

        logger.debug("[finish] UniversalOrchestrator - execute")
