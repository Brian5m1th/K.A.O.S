from uuid import uuid4
from loguru import logger

from app.domain.context import RequestContext
from app.domain.command import CommandType
from app.domain.memory import ConversationSnapshot
from app.memory.summarizer import ConversationSummarizer
from app.desktop.workspace.manager import WorkspaceManager
from app.memory.memory_service import MemoryService


class MemoryWorkflow:
    def __init__(self) -> None:
        self._workspace = WorkspaceManager()
        self._memory = MemoryService()

    async def execute(self, command: CommandType | None, context: RequestContext) -> str:
        if command == CommandType.SAVE_CONVERSATION:
            return await self._save_conversation(context)
        logger.warning(f"[warn] MemoryWorkflow - comando nao implementado: {command}")
        return f"Comando '{command}' ainda nao implementado."

    async def _save_conversation(self, context: RequestContext) -> str:
        logger.bind(
            event="memory.write.started",
            trace_id=str(context.trace_id),
            execution_id=str(context.execution_id),
            user_id=str(context.user.user_id),
            session_id=str(context.session_id),
        ).info("memory write started")

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
        filepath = self._workspace.conversation_filepath(slug, title)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        vault_content = self._build_markdown(snapshot, slug)
        filepath.write_text(vault_content, encoding="utf-8")
        logger.info(f"[info] MemoryWorkflow - conversa salva em: {filepath}")

        try:
            await self._memory.save_snapshot(snapshot, str(context.user.user_id), str(context.session_id))
            logger.info("[info] MemoryWorkflow - memoria salva no PostgreSQL")
        except Exception as e:
            logger.warning(f"[warn] MemoryWorkflow - PostgreSQL save failed: {e}")

        logger.bind(
            event="memory.write.completed",
            trace_id=str(context.trace_id),
            execution_id=str(context.execution_id),
            vault_path=str(filepath),
        ).info("memory write completed")

        return f"Conversa salva em: {filepath.name}"

    def _build_markdown(self, snapshot: ConversationSnapshot, slug: str) -> str:
        lines = [f"# {snapshot.title or 'Conversa'}", "", f"**Resumo:** {snapshot.summary}", ""]
        if snapshot.tags:
            lines.append(f"**Tags:** {', '.join(snapshot.tags)}")
            lines.append("")
        if snapshot.history:
            for msg in snapshot.history:
                prefix = f"## {msg.role.title()}"
                lines.append(prefix)
                lines.append("")
                lines.append(msg.content)
                lines.append("")
        return "\n".join(lines)
