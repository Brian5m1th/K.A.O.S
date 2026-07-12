# assistant\app\core\secret_manager.py

## Símbolos

- [[assistant_app_core_secret_manager]] — code: secret_manager.py
- [[assistant_app_core_secret_manager_secretmanager]] — code: SecretManager
- [[assistant_app_core_secret_manager_secretmanager_get_fernet]] — code: ._get_fernet()
- [[assistant_app_core_secret_manager_secretmanager_encrypt]] — code: .encrypt()
- [[assistant_app_core_secret_manager_secretmanager_decrypt]] — code: .decrypt()
- [[assistant_app_core_secret_manager_secretmanager_rotate_key]] — code: .rotate_key()
- [[assistant_app_core_secret_manager_rationale_1]] — code: Secret Manager for K.A.O.S. Provides AES-GCM (Fernet) encryption and decryption
- [[assistant_app_core_secret_manager_rationale_37]] — code: Encrypts plain text and returns base64 url-safe cipher text.
- [[assistant_app_core_secret_manager_rationale_46]] — code: Decrypts base64 url-safe cipher text and returns the original plain text.
- [[assistant_app_core_secret_manager_rationale_63]] — code: Decrypts dictionary values with old_key and re-encrypts with new_key.

## Dependências

- [[assistant_app_core_secret_manager]] → `contains` → [[assistant_app_core_secret_manager_secretmanager]]
- [[assistant_app_core_secret_manager_rationale_1]] → `rationale_for` → [[assistant_app_core_secret_manager]]
- [[assistant_app_core_secret_manager_secretmanager]] → `method` → [[assistant_app_core_secret_manager_secretmanager_decrypt]]
- [[assistant_app_core_secret_manager_secretmanager]] → `method` → [[assistant_app_core_secret_manager_secretmanager_encrypt]]
- [[assistant_app_core_secret_manager_secretmanager]] → `method` → [[assistant_app_core_secret_manager_secretmanager_get_fernet]]
- [[assistant_app_core_secret_manager_secretmanager]] → `method` → [[assistant_app_core_secret_manager_secretmanager_rotate_key]]
- [[assistant_app_core_secret_manager_secretmanager_decrypt]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_get_fernet]]
- [[assistant_app_core_secret_manager_secretmanager_encrypt]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_get_fernet]]
- [[assistant_app_core_secret_manager_secretmanager_get_fernet]] → `references` → [[fernet]]
- [[assistant_app_core_secret_manager_secretmanager_rotate_key]] → `calls` → [[fernet]]
- [[assistant_app_core_secret_manager_rationale_37]] → `rationale_for` → [[assistant_app_core_secret_manager_secretmanager_encrypt]]
- [[assistant_app_core_secret_manager_secretmanager_rotate_key]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_encrypt]]
- [[assistant_app_core_secret_manager_rationale_46]] → `rationale_for` → [[assistant_app_core_secret_manager_secretmanager_decrypt]]
- [[assistant_app_core_secret_manager_secretmanager_rotate_key]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_decrypt]]
- [[assistant_app_core_secret_manager_rationale_63]] → `rationale_for` → [[assistant_app_core_secret_manager_secretmanager_rotate_key]]