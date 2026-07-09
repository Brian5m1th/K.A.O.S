import json
import pytest
from fastapi.testclient import TestClient
from nacl.public import PrivateKey, PublicKey, Box
from app.main import app
from app.auth.handshake import HandshakeService


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


class TestSecureHandshake:
    def test_handshake_service_flow(self) -> None:
        service = HandshakeService()
        server_pubkey_hex = service.get_public_key_hex()
        assert len(server_pubkey_hex) == 64  # X25519 public keys are 32 bytes (64 hex characters)

        # Simulate client generating keypair
        client_privkey = PrivateKey.generate()
        client_pubkey = client_privkey.public_key
        client_pubkey_hex = client_pubkey.encode().hex()

        # Register client public key in HandshakeService
        client_id = "test-client-123"
        service.register_client_key(client_id, client_pubkey_hex)

        # Encrypt a secret on client side
        secret_plaintext = "Minha API Key Secreta 123"
        server_pubkey_obj = PublicKey(bytes.fromhex(server_pubkey_hex))
        client_box = Box(client_privkey, server_pubkey_obj)  # noqa: F841 — verify Box construction works

        encrypted_base64 = service.encrypt(client_id, secret_plaintext)
        decrypted = service.decrypt(client_id, encrypted_base64)
        assert decrypted == secret_plaintext

    def test_handshake_api_flow(self, client: TestClient) -> None:
        # 1. Get server public key
        resp_key = client.get("/auth/handshake/public-key")
        assert resp_key.status_code == 200
        server_pubkey_hex = resp_key.json()["public_key"]
        assert len(server_pubkey_hex) == 64

        # 2. Generate client keypair and exchange keys
        client_privkey = PrivateKey.generate()
        client_pubkey_hex = client_privkey.public_key.encode().hex()
        client_id = "api-test-client"

        resp_exchange = client.post(
            "/auth/handshake/exchange",
            json={"client_id": client_id, "client_public_key": client_pubkey_hex},
        )
        assert resp_exchange.status_code == 200
        assert resp_exchange.json() == {"status": "established"}

        # 3. Test secure setup endpoint
        server_pubkey_obj = PublicKey(bytes.fromhex(server_pubkey_hex))
        client_box = Box(client_privkey, server_pubkey_obj)

        test_config = {
            "openai": {"apiKey": "sk-12345", "url": "https://api.openai.com/v1"},
            "ollama": {"apiKey": "", "url": "http://localhost:11434"},
        }
        test_config_json = json.dumps(test_config)

        # Encrypt configuration using client_box
        import base64

        encrypted_bytes = client_box.encrypt(test_config_json.encode("utf-8"))
        encrypted_base64 = base64.b64encode(encrypted_bytes).decode("utf-8")

        resp_secure = client.post(
            "/api/setup/provider/secure",
            json={"client_id": client_id, "encrypted_data": encrypted_base64},
        )
        assert resp_secure.status_code == 200
        assert resp_secure.json()["status"] == "ok"
