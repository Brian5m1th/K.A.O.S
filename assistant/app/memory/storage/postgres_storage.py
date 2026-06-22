from uuid import UUID
from loguru import logger
from app.memory.models import ConversationMemory


class PostgresStorage:
    async def save(
        self,
        snapshot,
        workspace_id: UUID,
        user_id: UUID,
        session_id: UUID,
        vault_path: str = "",
    ) -> None:
        logger.info(f"[start] PostgresStorage - save [user={user_id}]")
        from app.memory.postgres_repository import get_postgres_repository

        repo = await get_postgres_repository()
        async with repo._session_factory() as session:
            history_dicts = []
            if snapshot.history:
                history_dicts = [
                    {"role": m.role, "content": m.content} for m in snapshot.history
                ]
            record = ConversationMemory(
                workspace_id=workspace_id,
                user_id=user_id,
                session_id=session_id,
                version=snapshot.version or "1.0",
                title=snapshot.title or "",
                tags=snapshot.tags or [],
                summary=snapshot.summary or "",
                conversation_json={
                    "history": history_dicts,
                    "summary": snapshot.summary,
                    "title": snapshot.title,
                    "tags": snapshot.tags or [],
                    "metadata": snapshot.metadata or {},
                },
                vault_path=vault_path,
            )
            session.add(record)
            await session.commit()
            logger.debug("[finish] PostgresStorage - save")
