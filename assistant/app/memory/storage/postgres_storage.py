from loguru import logger


class PostgresStorage:
    async def save(self, snapshot, user_id: str, session_id: str) -> None:
        logger.info(f"[start] PostgresStorage - save [user={user_id}]")
        from app.memory.postgres_repository import get_postgres_repository
        repo = await get_postgres_repository()
        await repo.save_conversation(
            user_id=user_id,
            session_id=session_id,
            summary=snapshot.summary,
            user_message=snapshot.history[-1].content if snapshot.history else "",
            assistant_response="",
        )
        logger.debug("[finish] PostgresStorage - save")
