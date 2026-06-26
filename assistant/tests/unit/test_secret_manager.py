import pytest
from cryptography.fernet import Fernet
from app.core.secret_manager import SecretManager
from app.config.settings import settings


def test_secret_manager_encryption_decryption(monkeypatch):
    # Generate a random valid Fernet key
    test_key = Fernet.generate_key().decode("utf-8")
    monkeypatch.setattr(settings, "KAOS_SECRET_KEY", test_key)

    # Reset any cached Fernet instance
    SecretManager._fernet = None

    plain = "SuperSecretAPIKey123!"
    cipher = SecretManager.encrypt(plain)

    assert cipher != plain
    assert SecretManager.decrypt(cipher) == plain


def test_secret_manager_missing_key(monkeypatch):
    monkeypatch.setattr(settings, "KAOS_SECRET_KEY", "")
    monkeypatch.delenv("KAOS_SECRET_KEY", raising=False)

    SecretManager._fernet = None

    with pytest.raises(
        ValueError, match="KAOS_SECRET_KEY environment variable is required"
    ):
        SecretManager.encrypt("test")


def test_secret_manager_invalid_key(monkeypatch):
    monkeypatch.setattr(settings, "KAOS_SECRET_KEY", "not-a-valid-key-at-all")
    SecretManager._fernet = None

    with pytest.raises(ValueError, match="is not a valid Fernet key"):
        SecretManager.encrypt("test")


def test_secret_manager_rotation():
    old_key = Fernet.generate_key().decode("utf-8")
    new_key = Fernet.generate_key().decode("utf-8")

    old_fernet = Fernet(old_key.encode("utf-8"))

    data = {
        "github_token": old_fernet.encrypt(b"token_val").decode("utf-8"),
        "slack_webhook": old_fernet.encrypt(b"slack_val").decode("utf-8"),
    }

    rotated = SecretManager.rotate_key(old_key, new_key, data)

    new_fernet = Fernet(new_key.encode("utf-8"))
    assert (
        new_fernet.decrypt(rotated["github_token"].encode("utf-8")).decode("utf-8")
        == "token_val"
    )
    assert (
        new_fernet.decrypt(rotated["slack_webhook"].encode("utf-8")).decode("utf-8")
        == "slack_val"
    )
