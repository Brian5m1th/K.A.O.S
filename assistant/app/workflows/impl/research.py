from typing import AsyncIterator

from loguru import logger

from app.domain.chat import ChatRequest, Message
from app.domain.execution_plan import ExecutionPlan
from app.registry.service_registry import ServiceRegistry
from app.workflows.base import BaseWorkflow


class ResearchWorkflow(BaseWorkflow):
    name = "research"
    version = "1.0"

    @property
    def required_capabilities(self) -> list[str]:
        return ["reasoning", "rag", "long_context"]

    async def execute(
        self, plan: ExecutionPlan, request: ChatRequest
    ) -> AsyncIterator[str]:
        logger.info(
            f"[start] ResearchWorkflow - execute plan={plan.execution_id} model={plan.selected_model}"
        )

        vector_store = ServiceRegistry.get_vector_store("qdrant")
        embed_provider = ServiceRegistry.get_embedding_provider("bge")
        query_vector = await embed_provider.embed(request.message)
        results = await vector_store.search(
            collection="knowledge", query_vector=query_vector, limit=15
        )

        context = "\n\n".join(
            f"[{r.path}] {r.excerpt}" for r in results
        ) if results else "Nenhum contexto encontrado."

        chat_provider_name = plan.provider_configs.get("provider", "ollama")
        chat_provider = ServiceRegistry.get_chat_provider(
            chat_provider_name, {"model": plan.selected_model}
        )

        system_msg = Message(
            role="system",
            content=(
                "Voce e um pesquisador. Analise profundamente o contexto, "
                "identifique padroes e produza uma resposta detalhada e bem fundamentada.\n\n"
                f"Contexto:\n{context}"
            ),
        )
        messages = [system_msg] + list(request.history)
        messages.append(Message(role="user", content=request.message))

        result = await chat_provider.chat(messages)
        yield result

        logger.debug("[finish] ResearchWorkflow - execute")

    async def healthcheck(self) -> bool:
        return True
