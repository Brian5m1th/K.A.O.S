from loguru import logger

from app.memory.memory_service import MemoryService
from app.providers.base.memory import BaseMemoryProvider
from app.domain.chat import Message


class ObsidianMemoryProvider(BaseMemoryProvider):
    provider_name = "obsidian"

    def __init__(self):
        self._service = MemoryService()

    async def save(self, session_id: str, messages: list[Message]) -> None:
        logger.info(f"[start] ObsidianMemoryProvider - save session={session_id}")

        user_msg = next((m.content for m in messages if m.role == "user"), "")
        assistant_msg = next((m.content for m in messages if m.role == "assistant"), "")
        summary = f"Conversation with {len(messages)} messages"

        self._service.save_conversation(
            user_id="",
            session_id=session_id,
            summary=summary,
            user_message=user_msg,
            assistant_response=assistant_msg,
        )
        logger.debug("[finish] ObsidianMemoryProvider - save")

    async def load(self, session_id: str) -> list[Message]:
        logger.info(f"[start] ObsidianMemoryProvider - load session={session_id}")
        messages: list[Message] = []

        # Try to find conversation files matching this session_id
        conversations = self._service.list_recent_conversations(limit=50)
        matching = [c for c in conversations if session_id[:8] in c]

        if matching:
            # Read the actual content from the matching file
            from pathlib import Path
            from app.config.settings import settings

            vault = Path(settings.OBSIDIAN_VAULT_PATH)
            for rel_path in matching[:3]:  # Read last 3 matching files
                filepath = vault / rel_path
                if filepath.exists():
                    content = filepath.read_text(encoding="utf-8")
                    # Parse the conversation structure from the markdown
                    lines = content.split("\n")
                    current_role = "user"
                    current_content: list[str] = []
                    for line in lines:
                        stripped = line.strip()
                        if stripped == "## Usuario":
                            if current_content:
                                messages.append(
                                    Message(
                                        role=current_role,
                                        content="\n".join(current_content),
                                    )
                                )
                            current_role = "user"
                            current_content = []
                        elif stripped == "## Assistente":
                            if current_content:
                                messages.append(
                                    Message(
                                        role=current_role,
                                        content="\n".join(current_content),
                                    )
                                )
                            current_role = "assistant"
                            current_content = []
                        elif (
                            stripped
                            and not stripped.startswith("#")
                            and not stripped.startswith("**")
                        ):
                            current_content.append(line)

                    if current_content:
                        messages.append(
                            Message(
                                role=current_role, content="\n".join(current_content)
                            )
                        )

        if not messages:
            # Fallback: try loading from PostgreSQL
            try:
                repo = await self._get_postgres_repo()
                history = await repo.get_conversation_history(session_id)
                messages = [
                    Message(role=msg["role"], content=msg["content"]) for msg in history
                ]
            except Exception as exc:
                logger.warning(f"[obsidian:load] postgres fallback failed: {exc}")

        logger.debug(
            f"[finish] ObsidianMemoryProvider - load ({len(messages)} messages)"
        )
        return messages

    async def clear(self, session_id: str) -> None:
        logger.info(f"[start] ObsidianMemoryProvider - clear session={session_id}")
        self._service.delete_conversation_files(session_id)
        # Also clear from postgres via MemoryService
        try:
            repo = await self._get_postgres_repo()
            await repo.delete_session(session_id)
        except Exception as exc:
            logger.warning(
                f"[warn] ObsidianMemoryProvider - postgres clear failed: {exc}"
            )
        logger.debug("[finish] ObsidianMemoryProvider - clear")

    async def _get_postgres_repo(self):
        from app.memory.postgres_repository import get_postgres_repository

        return await get_postgres_repository()

    async def healthcheck(self) -> bool:
        from pathlib import Path
        from app.config.settings import settings

        vault = Path(settings.OBSIDIAN_VAULT_PATH)
        return vault.exists()
