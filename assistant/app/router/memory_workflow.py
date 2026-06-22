from loguru import logger

from app.domain.context import RequestContext
from app.domain.command import CommandType
from app.domain.memory import ConversationSnapshot
from app.memory.summarizer import ConversationSummarizer
from app.memory.storage.workspace_storage import WorkspaceStorage
from app.memory.storage.postgres_storage import PostgresStorage
from app.observability.event_bus import EventBus, Event
from app.observability.event_bus import (
    EVENT_MEMORY_WRITE_STARTED,
    EVENT_MEMORY_WRITE_COMPLETED,
    EVENT_MEMORY_WRITE_FAILED,
    EVENT_CONVERSATION_STORED,
)


class MemoryWorkflow:
    def __init__(self) -> None:
        self._workspace_storage = WorkspaceStorage()
        self._postgres_storage = PostgresStorage()

    async def execute(self, command: CommandType | None, context: RequestContext) -> str:
        if command == CommandType.SAVE_CONVERSATION:
            return await self._save_conversation(context)
        logger.warning(f"[warn] MemoryWorkflow - comando nao implementado: {command}")
        return f"Comando '{command}' ainda nao implementado."

    async def _save_conversation(self, context: RequestContext) -> str:
        await EventBus.publish(Event(
            name=EVENT_MEMORY_WRITE_STARTED,
            execution_id=context.execution_id,
            trace_id=context.trace_id,
            data={
                "user_id": str(context.user.user_id),
                "workspace_id": str(context.workspace.workspace_id),
                "session_id": str(context.session_id),
            },
        ))

        history = context.history or []
        summary = ConversationSummarizer.generate(history)
        title = ConversationSummarizer.generate_title(history)

        snapshot = ConversationSnapshot(
            version="1.0",
            history=history,
            summary=summary,
            title=title,
            tags=["conversation"],
            metadata={
                "user_id": str(context.user.user_id),
                "workspace_id": str(context.workspace.workspace_id),
                "session_id": str(context.session_id),
                "execution_id": str(context.execution_id),
            },
        )

        slug = context.workspace.slug
        vault_path = self._workspace_storage.save(snapshot, slug, context.user.slug)

        try:
            await self._postgres_storage.save(
                snapshot=snapshot,
                workspace_id=context.workspace.workspace_id,
                user_id=context.user.user_id,
                session_id=context.session_id,
                vault_path=vault_path,
            )
        except Exception as e:
            await EventBus.publish(Event(
                name=EVENT_MEMORY_WRITE_FAILED,
                execution_id=context.execution_id,
                trace_id=context.trace_id,
                data={"reason": str(e), "vault_path": vault_path},
            ))
            logger.warning(f"[warn] MemoryWorkflow - PostgreSQL save failed: {e}")

        await EventBus.publish(Event(
            name=EVENT_MEMORY_WRITE_COMPLETED,
            execution_id=context.execution_id,
            trace_id=context.trace_id,
            data={"vault_path": vault_path, "title": title},
        ))

        await EventBus.publish(Event(
            name=EVENT_CONVERSATION_STORED,
            execution_id=context.execution_id,
            trace_id=context.trace_id,
            data={
                "vault_path": vault_path,
                "session_id": str(context.session_id),
                "storage_type": "workspace_storage",
            },
        ))

        return f"Conversa salva em: {vault_path}"
