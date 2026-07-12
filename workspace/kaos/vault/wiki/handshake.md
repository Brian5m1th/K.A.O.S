# assistant\app\auth\handshake.py

## Símbolos

- [[assistant_app_auth_handshake]] — code: handshake.py
- [[assistant_app_auth_handshake_handshakeservice]] — code: HandshakeService
- [[assistant_app_auth_handshake_handshakeservice_new]] — code: .__new__()
- [[assistant_app_auth_handshake_handshakeservice_init_keys]] — code: ._init_keys()
- [[assistant_app_auth_handshake_handshakeservice_get_public_key_hex]] — code: .get_public_key_hex()
- [[assistant_app_auth_handshake_handshakeservice_register_client_key]] — code: .register_client_key()
- [[assistant_app_auth_handshake_handshakeservice_decrypt]] — code: .decrypt()
- [[assistant_app_auth_handshake_handshakeservice_encrypt]] — code: .encrypt()

## Dependências

- [[assistant_app_auth_handshake]] → `contains` → [[assistant_app_auth_handshake_handshakeservice]]
- [[assistant_app_auth_handshake_handshakeservice]] → `method` → [[assistant_app_auth_handshake_handshakeservice_decrypt]]
- [[assistant_app_auth_handshake_handshakeservice]] → `method` → [[assistant_app_auth_handshake_handshakeservice_encrypt]]
- [[assistant_app_auth_handshake_handshakeservice]] → `method` → [[assistant_app_auth_handshake_handshakeservice_get_public_key_hex]]
- [[assistant_app_auth_handshake_handshakeservice]] → `method` → [[assistant_app_auth_handshake_handshakeservice_init_keys]]
- [[assistant_app_auth_handshake_handshakeservice_new]] → `indirect_call` → [[assistant_app_auth_handshake_handshakeservice]]
- [[assistant_app_auth_handshake_handshakeservice]] → `method` → [[assistant_app_auth_handshake_handshakeservice_register_client_key]]
- [[assistant_app_auth_handshake_handshakeservice_new]] → `calls` → [[assistant_app_auth_handshake_handshakeservice_init_keys]]
- [[assistant_app_auth_handshake_handshakeservice_init_keys]] → `calls` → [[assistant_app_auth_handshake_handshakeservice_get_public_key_hex]]