from typing import AsyncIterator

from loguru import logger

from app.domain.chat import ChatRequest, Message
from app.domain.execution_plan import ExecutionPlan
from app.registry.service_registry import ServiceRegistry
from app.workflows.base import BaseWorkflow


class CodingWorkflow(BaseWorkflow):
    name = "coding"
    version = "1.0"

    @property
    def required_capabilities(self) -> list[str]:
        return ["coding", "reasoning"]

    async def execute(
        self, plan: ExecutionPlan, request: ChatRequest
    ) -> AsyncIterator[str]:
        logger.info(
            f"[start] CodingWorkflow - execute plan={plan.execution_id} model={plan.selected_model}"
        )

        provider_name = plan.provider_configs.get("provider", "ollama")
        provider = ServiceRegistry.get_chat_provider(
            provider_name, {"model": plan.selected_model}
        )

        system_msg = Message(
            role="system",
            content="Voce e um engenheiro de software. Gere codigo claro, eficiente e bem estruturado. Explique suas decisoes tecnicas.",
        )
        messages = [system_msg] + list(request.history)
        messages.append(Message(role="user", content=request.message))

        result = await provider.chat(messages)
        yield result

        logger.debug("[finish] CodingWorkflow - execute")

    async def healthcheck(self) -> bool:
        return True
