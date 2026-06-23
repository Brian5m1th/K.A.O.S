from collections.abc import AsyncIterator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.settings import settings


class Base(DeclarativeBase):
    pass


_engine = None
_session_factory = None


def _get_session_factory() -> async_sessionmaker[AsyncSession]:
    global _engine, _session_factory
    if _session_factory is None:
        _engine = create_async_engine(settings.DATABASE_URL, echo=False)
        _session_factory = async_sessionmaker(
            _engine, class_=AsyncSession, expire_on_commit=False
        )
    return _session_factory


async def get_session() -> AsyncIterator[AsyncSession]:
    factory = _get_session_factory()
    async with factory() as session:
        yield session


# Re-export for external consumers that expect async_session_factory
async_session_factory = _get_session_factory


async def create_tables() -> None:
    """Create all tables registered on Base.metadata."""
    global _engine
    if _engine is None:
        _get_session_factory()
    async with _engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
