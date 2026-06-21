from dataclasses import dataclass, field
from typing import Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession



@dataclass
class ProviderConfigRecord:
    id: int
    provider_type: str
    provider_name: str
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    is_active: bool = True
    extra_config: dict = field(default_factory=dict)


class ProviderConfigRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_type(
        self, provider_type: str
    ) -> list[ProviderConfigRecord]:
        result = await self._session.execute(
            text("""
                SELECT * FROM provider_configs
                WHERE provider_type = :provider_type AND is_active = TRUE
                ORDER BY provider_name
            """),
            {"provider_type": provider_type},
        )
        return [
            ProviderConfigRecord(
                id=row.id,
                provider_type=row.provider_type,
                provider_name=row.provider_name,
                api_key=row.api_key,
                base_url=row.base_url,
                is_active=row.is_active,
                extra_config=dict(row.extra_config) if row.extra_config else {},
            )
            for row in result.fetchall()
        ]

    async def get_by_name(self, provider_name: str) -> Optional[ProviderConfigRecord]:
        result = await self._session.execute(
            text("""
                SELECT * FROM provider_configs
                WHERE provider_name = :provider_name AND is_active = TRUE
                LIMIT 1
            """),
            {"provider_name": provider_name},
        )
        row = result.fetchone()
        if not row:
            return None
        return ProviderConfigRecord(
            id=row.id,
            provider_type=row.provider_type,
            provider_name=row.provider_name,
            api_key=row.api_key,
            base_url=row.base_url,
            is_active=row.is_active,
            extra_config=dict(row.extra_config) if row.extra_config else {},
        )

    async def upsert(self, record: ProviderConfigRecord) -> int:
        result = await self._session.execute(
            text("""
                INSERT INTO provider_configs (provider_type, provider_name, api_key, base_url, is_active, extra_config)
                VALUES (:provider_type, :provider_name, :api_key, :base_url, :is_active, :extra_config)
                ON CONFLICT (provider_type, provider_name) DO UPDATE SET
                    api_key = EXCLUDED.api_key,
                    base_url = EXCLUDED.base_url,
                    is_active = EXCLUDED.is_active,
                    extra_config = EXCLUDED.extra_config,
                    updated_at = NOW()
                RETURNING id
            """),
            {
                "provider_type": record.provider_type,
                "provider_name": record.provider_name,
                "api_key": record.api_key,
                "base_url": record.base_url,
                "is_active": record.is_active,
                "extra_config": record.extra_config,
            },
        )
        await self._session.commit()
        return result.fetchone().id

    async def delete(self, provider_id: int) -> bool:
        result = await self._session.execute(
            text("DELETE FROM provider_configs WHERE id = :id"),
            {"id": provider_id},
        )
        await self._session.commit()
        return result.rowcount > 0

    async def list_all(self) -> list[ProviderConfigRecord]:
        result = await self._session.execute(
            text("SELECT * FROM provider_configs ORDER BY provider_type, provider_name")
        )
        return [
            ProviderConfigRecord(
                id=row.id,
                provider_type=row.provider_type,
                provider_name=row.provider_name,
                api_key=row.api_key,
                base_url=row.base_url,
                is_active=row.is_active,
                extra_config=dict(row.extra_config) if row.extra_config else {},
            )
            for row in result.fetchall()
        ]
