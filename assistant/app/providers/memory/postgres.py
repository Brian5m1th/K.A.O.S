from loguru import logger

from app.memory.postgres_repository import (
    PostgresMemoryRepository,
    get_postgres_repository,
)
from app.providers.base.memory import BaseMemoryProvider
from app.domain.chat import Message


class PostgresMemoryProvider(BaseMemoryProvider):
    provider_name = "postgres"

    def __init__(self):
        self._repo: PostgresMemoryRepository | None = None

    async def _ensure_repo(self) -> PostgresMemoryRepository:
        if self._repo is None:
            self._repo = await get_postgres_repository()
        return self._repo

    async def save(self, session_id: str, messages: list[Message]) -> None:
        logger.info(f"[start] PostgresMemoryProvider - save session={session_id}")
        repo = await self._ensure_repo()

        user_msg = next((m.content for m in messages if m.role == "user"), "")
        assistant_msg = next((m.content for m in messages if m.role == "assistant"), "")
        summary = f"Conversation with {len(messages)} messages"

        await repo.save_conversation(
            user_id="",
            session_id=session_id,
            summary=summary,
            user_message=user_msg,
            assistant_response=assistant_msg,
        )
        logger.debug("[finish] PostgresMemoryProvider - save")

    async def load(self, session_id: str) -> list[Message]:
        logger.info(f"[start] PostgresMemoryProvider - load session={session_id}")
        repo = await self._ensure_repo()
        history = await repo.get_conversation_history(session_id)
        logger.debug("[finish] PostgresMemoryProvider - load")
        return [Message(role=msg["role"], content=msg["content"]) for msg in history]

    async def clear(self, session_id: str) -> None:
        logger.info(f"[start] PostgresMemoryProvider - clear session={session_id}")
        logger.debug("[finish] PostgresMemoryProvider - clear")

    async def healthcheck(self) -> bool:
        try:
            repo = await self._ensure_repo()
            _ = await repo.get_preferences("healthcheck")
            return True
        except Exception:
            return False
