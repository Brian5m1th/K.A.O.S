from typing import AsyncIterator

from loguru import logger

from app.domain.chat import ChatRequest
from app.domain.execution_plan import ExecutionPlan
from app.workflows.base import BaseWorkflow


class IngestWorkflow(BaseWorkflow):
    name = "ingest"
    version = "1.0"

    @property
    def required_capabilities(self) -> list[str]:
        return ["rag"]

    async def execute(
        self, plan: ExecutionPlan, request: ChatRequest
    ) -> AsyncIterator[str]:
        logger.info(f"[start] IngestWorkflow - execute plan={plan.execution_id}")

        from app.rag.indexer.vault_indexer import VaultIndexer

        indexer = VaultIndexer()
        result = indexer.index_vault()
        yield (
            f"Ingestao concluida: {result.get('files', 0)} arquivos, "
            f"{result.get('chunks', 0)} chunks indexados."
        )

        logger.debug("[finish] IngestWorkflow - execute")

    async def healthcheck(self) -> bool:
        return True
