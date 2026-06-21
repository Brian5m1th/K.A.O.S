from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.model_repository import ModelRecord, ModelRepository


class ModelRegistry:
    def __init__(self, session: AsyncSession):
        self._repo = ModelRepository(session)

    async def get_model(self, name: str) -> Optional[ModelRecord]:
        return await self._repo.get_by_name(name)

    async def list_by_capability(self, capability: str) -> list[ModelRecord]:
        return await self._repo.list_by_capability(capability)

    async def list_all(self) -> list[ModelRecord]:
        return await self._repo.list_all()
