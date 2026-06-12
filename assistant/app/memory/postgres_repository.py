import uuid
from datetime import datetime
from typing import Optional
from loguru import logger
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import selectinload

from app.config.settings import settings
from app.memory.models import Base, MemorySession, MemoryMessage, MemorySummary
from app.memory.repository import MemoryRepository


class PostgresMemoryRepository(MemoryRepository):
    def __init__(self, database_url: str | None = None):
        self._database_url = database_url or settings.DATABASE_URL
        self._engine = create_async_engine(self._database_url, echo=False)
        self._session_factory = async_sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False
        )
        logger.info("[info] PostgresMemoryRepository - initialized")

    async def init_db(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("[info] PostgresMemoryRepository - tables created")

    async def close(self) -> None:
        await self._engine.dispose()

    async def _get_session(self) -> AsyncSession:
        return self._session_factory()

    async def get_preferences(self, user_id: str) -> str:
        return ""

    async def save_preference(self, user_id: str, key: str, value: str) -> None:
        pass

    async def save_conversation(
        self,
        user_id: str,
        session_id: str,
        summary: str,
        user_message: str,
        assistant_response: str,
    ) -> str:
        logger.info(f"[start] PostgresMemoryRepository - save_conversation [user={user_id}]")
        
        async with self._session_factory() as session:
            session_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, session_id)
            
            existing = await session.get(MemorySession, session_uuid)
            if existing is None:
                mem_session = MemorySession(
                    id=session_uuid,
                    user_id=user_id,
                )
                session.add(mem_session)
            else:
                mem_session = existing
                mem_session.updated_at = datetime.utcnow()

            user_msg = MemoryMessage(
                session_id=session_uuid,
                role="user",
                content=user_message,
            )
            assistant_msg = MemoryMessage(
                session_id=session_uuid,
                role="assistant",
                content=assistant_response,
            )
            session.add_all([user_msg, assistant_msg])

            summary_obj = await session.get(MemorySummary, session_uuid)
            if summary_obj is None:
                summary_obj = MemorySummary(
                    session_id=session_uuid,
                    summary=summary,
                )
                session.add(summary_obj)
            else:
                summary_obj.summary = summary
                summary_obj.updated_at = datetime.utcnow()

            await session.commit()
            
            logger.info(f"[info] PostgresMemoryRepository - conversation saved [user={user_id}, session={session_uuid}]")
            return str(session_uuid)

    async def list_recent_conversations(self, user_id: str, limit: int = 5) -> list[str]:
        async with self._session_factory() as session:
            result = await session.execute(
                select(MemorySession)
                .where(MemorySession.user_id == user_id)
                .order_by(desc(MemorySession.updated_at))
                .limit(limit)
                .options(selectinload(MemorySession.summary))
            )
            sessions = result.scalars().all()
            
            return [
                f"{s.id} | {s.summary.summary if s.summary else 'Sem resumo'} | {s.updated_at.isoformat()}"
                for s in sessions
            ]

    async def get_conversation_history(self, session_id: str) -> list[dict]:
        session_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, session_id)
        async with self._session_factory() as session:
            result = await session.execute(
                select(MemoryMessage)
                .where(MemoryMessage.session_id == session_uuid)
                .order_by(MemoryMessage.created_at)
            )
            messages = result.scalars().all()
            
            return [
                {"role": m.role, "content": m.content, "timestamp": m.created_at.isoformat()}
                for m in messages
            ]


_postgres_repo: PostgresMemoryRepository | None = None


async def get_postgres_repository() -> PostgresMemoryRepository:
    global _postgres_repo
    if _postgres_repo is None:
        _postgres_repo = PostgresMemoryRepository()
        await _postgres_repo.init_db()
    return _postgres_repo