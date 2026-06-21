from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class UserModelProfileRecord:
    id: UUID
    user_id: str
    workflow_type: str
    model_name: str


class UserModelProfileRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(
        self, user_id: str, workflow_type: str
    ) -> Optional[UserModelProfileRecord]:
        result = await self._session.execute(
            text("""
                SELECT * FROM user_model_profiles
                WHERE user_id = :user_id AND workflow_type = :workflow_type
                LIMIT 1
            """),
            {"user_id": user_id, "workflow_type": workflow_type},
        )
        row = result.fetchone()
        if not row:
            return None
        return UserModelProfileRecord(
            id=row.id,
            user_id=row.user_id,
            workflow_type=row.workflow_type,
            model_name=row.model_name,
        )

    async def upsert(self, user_id: str, workflow_type: str, model_name: str) -> UUID:
        result = await self._session.execute(
            text("""
                INSERT INTO user_model_profiles (user_id, workflow_type, model_name)
                VALUES (:user_id, :workflow_type, :model_name)
                ON CONFLICT (user_id, workflow_type) DO UPDATE SET
                    model_name = EXCLUDED.model_name
                RETURNING id
            """),
            {
                "user_id": user_id,
                "workflow_type": workflow_type,
                "model_name": model_name,
            },
        )
        await self._session.commit()
        return result.fetchone().id

    async def list_by_user(self, user_id: str) -> list[UserModelProfileRecord]:
        result = await self._session.execute(
            text("""
                SELECT * FROM user_model_profiles
                WHERE user_id = :user_id
                ORDER BY workflow_type
            """),
            {"user_id": user_id},
        )
        return [
            UserModelProfileRecord(
                id=row.id,
                user_id=row.user_id,
                workflow_type=row.workflow_type,
                model_name=row.model_name,
            )
            for row in result.fetchall()
        ]

    async def delete(self, profile_id: UUID) -> bool:
        result = await self._session.execute(
            text("DELETE FROM user_model_profiles WHERE id = :id"),
            {"id": profile_id},
        )
        await self._session.commit()
        return result.rowcount > 0
