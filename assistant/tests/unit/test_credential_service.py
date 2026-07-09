import pytest
from app.core.credential_service import CredentialManager, CredentialProvider


class MockCredentialProvider(CredentialProvider):
    def __init__(self):
        self.store = {}

    def get(self, service: str, key: str) -> str | None:
        return self.store.get(f"{service}:{key}")

    def set(self, service: str, key: str, value: str) -> None:
        self.store[f"{service}:{key}"] = value

    def delete(self, service: str, key: str) -> None:
        self.store.pop(f"{service}:{key}", None)


def test_credential_manager_flow():
    mock_prov = MockCredentialProvider()
    CredentialManager.register_provider(mock_prov)

    # Test set
    CredentialManager.set_credential("test_service", "api_key", "secret123")
    assert mock_prov.get("test_service", "api_key") == "secret123"

    # Test get
    assert CredentialManager.get_credential("test_service", "api_key") == "secret123"

    # Test delete
    CredentialManager.delete_credential("test_service", "api_key")
    assert CredentialManager.get_credential("test_service", "api_key") is None
