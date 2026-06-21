from typing import AsyncIterator

from loguru import logger

from app.domain.chat import ChatRequest, Message
from app.domain.execution_plan import ExecutionPlan
from app.registry.service_registry import ServiceRegistry
from app.workflows.base import BaseWorkflow


class ChatWorkflow(BaseWorkflow):
    name = "chat"
    version = "1.0"

    @property
    def required_capabilities(self) -> list[str]:
        return ["fast_chat"]

    async def execute(
        self, plan: ExecutionPlan, request: ChatRequest
    ) -> AsyncIterator[str]:
        logger.info(
            f"[start] ChatWorkflow - execute plan={plan.execution_id} model={plan.selected_model}"
        )

        provider_name = plan.provider_configs.get("provider", "ollama")
        provider = ServiceRegistry.get_chat_provider(
            provider_name, {"model": plan.selected_model}
        )

        messages = list(request.history)
        messages.append(Message(role="user", content=request.message))

        if request.role.lower() == "stream":
            async for chunk in provider.stream(messages):
                yield chunk
        else:
            result = await provider.chat(messages)
            yield result

        logger.debug("[finish] ChatWorkflow - execute")

    async def healthcheck(self) -> bool:
        return True
