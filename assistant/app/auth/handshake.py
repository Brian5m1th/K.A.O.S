import base64
from nacl.public import PrivateKey, PublicKey, Box
from loguru import logger


class HandshakeService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HandshakeService, cls).__new__(
                cls, *args, **kwargs
            )
            cls._instance._init_keys()
        return cls._instance

    def _init_keys(self):
        # Generate backend's ephemeral keypair
        self._private_key = PrivateKey.generate()
        self._public_key = self._private_key.public_key
        # In-memory store mapping client_id/session_id to client public key
        self._sessions: dict[str, PublicKey] = {}
        # derived shared secrets (Boxes)
        self._boxes: dict[str, Box] = {}
        logger.info(
            f"[info] HandshakeService - Ephemeral keypair generated. Public Key (hex): {self.get_public_key_hex()}"
        )

    def get_public_key_hex(self) -> str:
        return self._public_key.encode().hex()

    def register_client_key(self, client_id: str, client_pubkey_hex: str) -> None:
        client_pubkey_bytes = bytes.fromhex(client_pubkey_hex)
        client_pubkey = PublicKey(client_pubkey_bytes)
        self._sessions[client_id] = client_pubkey
        # Pre-compute Box for Diffie-Hellman shared key exchange
        self._boxes[client_id] = Box(self._private_key, client_pubkey)
        logger.info(
            f"[info] HandshakeService - Shared Box derived successfully for client_id={client_id}"
        )

    def decrypt(self, client_id: str, encrypted_base64: str) -> str:
        if client_id not in self._boxes:
            logger.error(
                f"[error] HandshakeService - Handshake not established for client_id={client_id}"
            )
            raise ValueError(
                f"Handshake nao estabelecido para o client_id: {client_id}"
            )
        box = self._boxes[client_id]
        try:
            encrypted_bytes = base64.b64decode(encrypted_base64)
            decrypted_bytes = box.decrypt(encrypted_bytes)
            return decrypted_bytes.decode("utf-8")
        except Exception as e:
            logger.error(
                f"[error] HandshakeService - Decryption failed for client_id={client_id}: {e}"
            )
            raise ValueError(f"Falha na decodificacao/descriptografia: {e}")

    def encrypt(self, client_id: str, plaintext: str) -> str:
        if client_id not in self._boxes:
            logger.error(
                f"[error] HandshakeService - Handshake not established for client_id={client_id}"
            )
            raise ValueError(
                f"Handshake nao estabelecido para o client_id: {client_id}"
            )
        box = self._boxes[client_id]
        encrypted_bytes = box.encrypt(plaintext.encode("utf-8"))
        return base64.b64encode(encrypted_bytes).decode("utf-8")
