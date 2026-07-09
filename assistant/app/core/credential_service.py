"""Credential Service — Centralized Plugable Secrets Storage.

SDD-KAOS-EVOLUTION-001: Exposes CredentialManager and pluggable providers
                       (e.g., Encrypted File fallback).
"""
from abc import ABC, abstractmethod
from typing import Any, Dict
from loguru import logger

from app.core.config_service import ConfigService


class CredentialProvider(ABC):
    @abstractmethod
    def get(self, service: str, key: str) -> str | None:
        """Retrieve a credential."""
        pass

    @abstractmethod
    def set(self, service: str, key: str, value: str) -> None:
        """Store a credential."""
        pass

    @abstractmethod
    def delete(self, service: str, key: str) -> None:
        """Remove a credential."""
        pass


class FileSecretsCredentialProvider(CredentialProvider):
    """Fallback credential provider using ConfigService secrets file."""

    def get(self, service: str, key: str) -> str | None:
        try:
            secrets = ConfigService.load_secrets()
            return secrets.get("credentials", {}).get(service, {}).get(key)
        except Exception as e:
            logger.error(f"[CredentialService] Failed to load secret: {e}")
            return None

    def set(self, service: str, key: str, value: str) -> None:
        try:
            secrets = ConfigService.load_secrets()
            creds = secrets.setdefault("credentials", {})
            service_creds = creds.setdefault(service, {})
            service_creds[key] = value
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


class CredentialManager:
    """Centralized manager to orchestrate pluggable credential providers."""

    _providers: list[CredentialProvider] = [FileSecretsCredentialProvider()]

    @classmethod
    def register_provider(cls, provider: CredentialProvider) -> None:
        """Register a new credential provider (e.g. Keychain, Vault)."""
        cls._providers.insert(0, provider)  # Newer/Specific providers take precedence
        logger.info(f"[CredentialService] Registered provider: {provider.__class__.__name__}")

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
