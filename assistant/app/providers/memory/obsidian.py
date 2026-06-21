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

        user_msg = next(
            (m.content for m in messages if m.role == "user"), ""
        )
        assistant_msg = next(
            (m.content for m in messages if m.role == "assistant"), ""
        )
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
        conversations = self._service.list_recent_conversations(limit=10)
        logger.debug("[finish] ObsidianMemoryProvider - load")
        return [
            Message(role="user", content=f"See conversation: {conv}")
            for conv in conversations
        ]

    async def clear(self, session_id: str) -> None:
        logger.info(f"[start] ObsidianMemoryProvider - clear session={session_id}")
        logger.debug("[finish] ObsidianMemoryProvider - clear")

    async def healthcheck(self) -> bool:
        from pathlib import Path
        from app.config.settings import settings
        vault = Path(settings.OBSIDIAN_VAULT_PATH)
        return vault.exists()
