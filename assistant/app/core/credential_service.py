"""Credential Service — Centralized Plugable Secrets Storage.

SDD-KAOS-EVOLUTION-001: Exposes CredentialManager and pluggable providers
                       (e.g., Encrypted File fallback, Database-backed).
"""

from abc import ABC, abstractmethod
from loguru import logger

from app.core.config_service import ConfigService
from app.core.secret_manager import SecretManager


class CredentialProvider(ABC):
    @abstractmethod
    def get(self, service: str, key: str) -> str | None:
        """Retrieve a credential."""
        ...

    @abstractmethod
    def set(self, service: str, key: str, value: str) -> None:
        """Store a credential."""
        ...

    @abstractmethod
    def delete(self, service: str, key: str) -> None:
        """Remove a credential."""
        ...


class EncryptedFileCredentialProvider(CredentialProvider):
    """Credential provider using ConfigService secrets file with Fernet encryption."""

    def __init__(self) -> None:
        self._secret_manager = SecretManager()

    def get(self, service: str, key: str) -> str | None:
        try:
            secrets = ConfigService.load_secrets()
            encrypted = secrets.get("credentials", {}).get(service, {}).get(key)
            if encrypted is None:
                return None
            return self._secret_manager.decrypt(encrypted)
        except Exception as e:
            logger.error(f"[CredentialService] Failed to load secret: {e}")
            return None

    def set(self, service: str, key: str, value: str) -> None:
        try:
            secrets = ConfigService.load_secrets()
            creds = secrets.setdefault("credentials", {})
            service_creds = creds.setdefault(service, {})
            service_creds[key] = self._secret_manager.encrypt(value)
            ConfigService.save_secrets(secrets)
            logger.info(f"[CredentialService] Secret set for '{service}:{key}'")
        except Exception as e:
            logger.error(f"[CredentialService] Failed to set secret: {e}")

    def delete(self, service: str, key: str) -> None:
        try:
            secrets = ConfigService.load_secrets()
            creds = secrets.get("credentials", {})
            if service in creds and key in creds[service]:
                del creds[service][key]
                ConfigService.save_secrets(secrets)
                logger.info(f"[CredentialService] Secret deleted for '{service}:{key}'")
        except Exception as e:
            logger.error(f"[CredentialService] Failed to delete secret: {e}")


class DatabaseCredentialProvider(CredentialProvider):
    """Credential provider backed by PostgreSQL with encryption."""

    def __init__(self) -> None:
        self._secret_manager = SecretManager()
        self._repo = None

    async def _ensure_repo(self):
        if self._repo is None:
            from app.memory.postgres_repository import get_postgres_repository

            self._repo = await get_postgres_repository()
        return self._repo

    def get(self, service: str, key: str) -> str | None:
        # Sync wrapper for async repo — uses event loop
        import asyncio

        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Cannot run sync when loop is running; fallback to file
                logger.debug("[credential:db] loop running, fallback to file provider")
                return None
        except RuntimeError as e:
            logger.debug("[credential:db] no event loop available: {}", e)

        try:
            repo_data = asyncio.run(self._get_credential_from_db(service, key))
            if repo_data:
                return self._secret_manager.decrypt(repo_data)
        except Exception as e:
            logger.warning(f"[credential:db] Failed to get credential: {e}")
        return None

    async def _get_credential_from_db(self, service: str, key: str) -> str | None:
        repo = await self._ensure_repo()
        # Store as UserPreference with key format "cred:{service}:{key}"
        pref_key = f"cred:{service}:{key}"
        prefs = await repo.get_preferences("__system__")
        if pref_key in prefs:
            # Parse from the preferences string
            for line in prefs.split("\n"):
                if f"**{pref_key}**:" in line:
                    return line.split(":", 1)[1].strip()
        return None

    def set(self, service: str, key: str, value: str) -> None:
        import asyncio

        try:
            encrypted = self._secret_manager.encrypt(value)
            asyncio.run(self._set_credential_in_db(service, key, encrypted))
        except Exception as e:
            logger.warning(f"[credential:db] Failed to set credential: {e}")

    async def _set_credential_in_db(
        self, service: str, key: str, encrypted: str
    ) -> None:
        repo = await self._ensure_repo()
        pref_key = f"cred:{service}:{key}"
        await repo.save_preference("__system__", pref_key, encrypted)

    def delete(self, service: str, key: str) -> None:
        import asyncio

        try:
            asyncio.run(self._delete_credential_from_db(service, key))
        except Exception as e:
            logger.warning(f"[credential:db] Failed to delete credential: {e}")

    async def _delete_credential_from_db(self, service: str, key: str) -> None:
        repo = await self._ensure_repo()
        pref_key = f"cred:{service}:{key}"
        await repo.save_preference("__system__", pref_key, "")


class CredentialManager:
    """Centralized manager to orchestrate pluggable credential providers."""

    _providers: list[CredentialProvider] = [
        EncryptedFileCredentialProvider(),
    ]

    @classmethod
    def register_provider(cls, provider: CredentialProvider) -> None:
        """Register a new credential provider (e.g. Keychain, Vault)."""
        cls._providers.insert(0, provider)
        logger.info(
            f"[CredentialService] Registered provider: {provider.__class__.__name__}"
        )

    @classmethod
    def get_credential(cls, service: str, key: str) -> str | None:
        """Retrieve a credential from the active providers."""
        for provider in cls._providers:
            val = provider.get(service, key)
            if val is not None:
                return val
        return None

    @classmethod
    def set_credential(cls, service: str, key: str, value: str) -> None:
        """Store a credential across all providers."""
        for provider in cls._providers:
            provider.set(service, key, value)

    @classmethod
    def delete_credential(cls, service: str, key: str) -> None:
        """Delete a credential across all providers."""
        for provider in cls._providers:
            provider.delete(service, key)
