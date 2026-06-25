"""
Secret Manager for K.A.O.S.
Provides AES-GCM (Fernet) encryption and decryption for sensitive third-party integration credentials.
Forces the presence of a valid KAOS_SECRET_KEY.
"""

import os
from cryptography.fernet import Fernet
from app.config.settings import settings
from loguru import logger


class SecretManager:
    _fernet: Fernet | None = None

    @classmethod
    def _get_fernet(cls) -> Fernet:
        if cls._fernet is None:
            key = settings.KAOS_SECRET_KEY or os.getenv("KAOS_SECRET_KEY")
            if not key:
                raise ValueError("KAOS_SECRET_KEY environment variable is required and must not be empty.")
            
            try:
                # Fernet keys must be 32 url-safe base64-encoded bytes
                cls._fernet = Fernet(key.encode("utf-8") if isinstance(key, str) else key)
            except Exception as e:
                logger.error(f"[SecretManager] KAOS_SECRET_KEY validation failed: {e}")
                raise ValueError(f"KAOS_SECRET_KEY is not a valid Fernet key: {e}")
        return cls._fernet

    @classmethod
    def encrypt(cls, plain_text: str) -> str:
        """Encrypts plain text and returns base64 url-safe cipher text."""
        if not plain_text:
            return ""
        fernet = cls._get_fernet()
        cipher_bytes = fernet.encrypt(plain_text.encode("utf-8"))
        return cipher_bytes.decode("utf-8")

    @classmethod
    def decrypt(cls, cipher_text: str) -> str:
        """Decrypts base64 url-safe cipher text and returns the original plain text."""
        if not cipher_text:
            return ""
        fernet = cls._get_fernet()
        try:
            plain_bytes = fernet.decrypt(cipher_text.encode("utf-8"))
            return plain_bytes.decode("utf-8")
        except Exception as e:
            logger.error(f"[SecretManager] Decryption failed: {e}")
            raise ValueError("Failed to decrypt secret data. The key may be incorrect or corrupted.")

    @classmethod
    def rotate_key(cls, old_key: str, new_key: str, data: dict[str, str]) -> dict[str, str]:
        """Decrypts dictionary values with old_key and re-encrypts with new_key."""
        try:
            old_fernet = Fernet(old_key.encode("utf-8") if isinstance(old_key, str) else old_key)
            new_fernet = Fernet(new_key.encode("utf-8") if isinstance(new_key, str) else new_key)
        except Exception as e:
            raise ValueError(f"Invalid key provided for rotation: {e}")

        rotated = {}
        for k, v in data.items():
            if v:
                plain = old_fernet.decrypt(v.encode("utf-8")).decode("utf-8")
                rotated[k] = new_fernet.encrypt(plain.encode("utf-8")).decode("utf-8")
            else:
                rotated[k] = ""
        return rotated
