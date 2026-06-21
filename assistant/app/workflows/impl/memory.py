from typing import AsyncIterator

from loguru import logger

from app.domain.chat import ChatRequest
from app.domain.execution_plan import ExecutionPlan
from app.registry.service_registry import ServiceRegistry
from app.workflows.base import BaseWorkflow


class MemoryWorkflow(BaseWorkflow):
    name = "memory"
    version = "1.0"

    @property
    def required_capabilities(self) -> list[str]:
        return ["memory"]

    async def execute(
        self, plan: ExecutionPlan, request: ChatRequest
    ) -> AsyncIterator[str]:
        logger.info(
            f"[start] MemoryWorkflow - execute plan={plan.execution_id} user={plan.user_id}"
        )

        memory_provider = ServiceRegistry.get_memory_provider("obsidian")

        if request.message.startswith("/save"):
            from app.domain.chat import Message
            msg = Message(role="user", content=request.message)
            await memory_provider.save(str(plan.session_id), [msg])
            yield "Memoria salva."
        elif request.message.startswith("/load"):
            history = await memory_provider.load(str(plan.session_id))
            if history:
                for m in history:
                    yield f"[{m.role}] {m.content}\n"
            else:
                yield "Nenhuma memoria encontrada."
        elif request.message.startswith("/clear"):
            await memory_provider.clear(str(plan.session_id))
            yield "Memoria limpa."
        else:
            yield "Comandos: /save, /load, /clear"

        logger.debug("[finish] MemoryWorkflow - execute")

    async def healthcheck(self) -> bool:
        return True
