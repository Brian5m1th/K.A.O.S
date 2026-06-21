from dataclasses import dataclass
from typing import Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class FeatureFlagRecord:
    flag: str
    enabled: bool
    description: str = ""


class FeatureFlagRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, flag: str) -> Optional[FeatureFlagRecord]:
        result = await self._session.execute(
            text("SELECT * FROM feature_flags WHERE flag = :flag"),
            {"flag": flag},
        )
        row = result.fetchone()
        if not row:
            return None
        return FeatureFlagRecord(
            flag=row.flag,
            enabled=row.enabled,
            description=row.description or "",
        )

    async def is_enabled(self, flag: str) -> bool:
        result = await self._session.execute(
            text("SELECT enabled FROM feature_flags WHERE flag = :flag"),
            {"flag": flag},
        )
        row = result.fetchone()
        return row.enabled if row else False

    async def set(self, flag: str, enabled: bool) -> None:
        await self._session.execute(
            text("""
                INSERT INTO feature_flags (flag, enabled)
                VALUES (:flag, :enabled)
                ON CONFLICT (flag) DO UPDATE SET
                    enabled = EXCLUDED.enabled,
                    updated_at = NOW()
            """),
            {"flag": flag, "enabled": enabled},
        )
        await self._session.commit()

    async def list_all(self) -> list[FeatureFlagRecord]:
        result = await self._session.execute(
            text("SELECT * FROM feature_flags ORDER BY flag")
        )
        return [
            FeatureFlagRecord(
                flag=row.flag,
                enabled=row.enabled,
                description=row.description or "",
            )
            for row in result.fetchall()
        ]
