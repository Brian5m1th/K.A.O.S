from dataclasses import dataclass
from typing import Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class UserProfileRecord:
    user_id: str
    theme: str = "dark"
    language: str = "pt-BR"
    vault_path: str = ""
    auto_update: bool = True
    telemetry_enabled: bool = False


class UserProfileRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, user_id: str) -> Optional[UserProfileRecord]:
        result = await self._session.execute(
            text("SELECT * FROM user_profiles WHERE user_id = :user_id"),
            {"user_id": user_id},
        )
        row = result.fetchone()
        if not row:
            return None
        return UserProfileRecord(
            user_id=row.user_id,
            theme=row.theme,
            language=row.language,
            vault_path=row.vault_path,
            auto_update=row.auto_update,
            telemetry_enabled=row.telemetry_enabled,
        )

    async def upsert(self, record: UserProfileRecord) -> None:
        await self._session.execute(
            text("""
                INSERT INTO user_profiles (user_id, theme, language, vault_path, auto_update, telemetry_enabled)
                VALUES (:user_id, :theme, :language, :vault_path, :auto_update, :telemetry_enabled)
                ON CONFLICT (user_id) DO UPDATE SET
                    theme = EXCLUDED.theme,
                    language = EXCLUDED.language,
                    vault_path = EXCLUDED.vault_path,
                    auto_update = EXCLUDED.auto_update,
                    telemetry_enabled = EXCLUDED.telemetry_enabled,
                    updated_at = NOW()
            """),
            {
                "user_id": record.user_id,
                "theme": record.theme,
                "language": record.language,
                "vault_path": record.vault_path,
                "auto_update": record.auto_update,
                "telemetry_enabled": record.telemetry_enabled,
            },
        )
        await self._session.commit()
