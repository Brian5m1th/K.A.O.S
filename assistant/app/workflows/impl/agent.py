from typing import AsyncIterator

from loguru import logger

from app.domain.chat import ChatRequest, Message
from app.domain.execution_plan import ExecutionPlan
from app.registry.service_registry import ServiceRegistry
from app.workflows.base import BaseWorkflow


class AgentWorkflow(BaseWorkflow):
    name = "agent"
    version = "1.0"

    @property
    def required_capabilities(self) -> list[str]:
        return ["reasoning", "fast_chat"]

    async def execute(
        self, plan: ExecutionPlan, request: ChatRequest
    ) -> AsyncIterator[str]:
        logger.info(
            f"[start] AgentWorkflow - execute plan={plan.execution_id} model={plan.selected_model}"
        )

        provider_name = plan.provider_configs.get("provider", "ollama")
        provider = ServiceRegistry.get_chat_provider(
            provider_name, {"model": plan.selected_model}
        )

        system_msg = Message(
            role="system",
            content="Voce e um agente autonomo. Pense passo a passo e responda com acoes.",
        )
        messages = [system_msg] + list(request.history)
        messages.append(Message(role="user", content=request.message))

        result = await provider.chat(messages)
        yield result

        logger.debug("[finish] AgentWorkflow - execute")

    async def healthcheck(self) -> bool:
        return True
