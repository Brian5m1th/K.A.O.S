from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.settings import settings

_engine = create_async_engine(settings.DATABASE_URL, echo=False)
_session_factory = async_sessionmaker(
    _engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with _session_factory() as session:
        yield session
