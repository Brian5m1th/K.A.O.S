# assistant\app\core\credential_service.py

## Símbolos

- [[assistant_app_core_credential_service]] — code: credential_service.py
- [[assistant_app_core_credential_service_credentialprovider]] — code: CredentialProvider
- [[assistant_app_core_credential_service_credentialprovider_get]] — code: .get()
- [[assistant_app_core_credential_service_credentialprovider_set]] — code: .set()
- [[assistant_app_core_credential_service_credentialprovider_delete]] — code: .delete()
- [[assistant_app_core_credential_service_filesecretscredentialprovider]] — code: FileSecretsCredentialProvider
- [[assistant_app_core_credential_service_filesecretscredentialprovider_get]] — code: .get()
- [[assistant_app_core_credential_service_filesecretscredentialprovider_set]] — code: .set()
- [[assistant_app_core_credential_service_filesecretscredentialprovider_delete]] — code: .delete()
- [[assistant_app_core_credential_service_credentialmanager]] — code: CredentialManager
- [[assistant_app_core_credential_service_credentialmanager_register_provider]] — code: .register_provider()
- [[assistant_app_core_credential_service_credentialmanager_get_credential]] — code: .get_credential()
- [[assistant_app_core_credential_service_credentialmanager_set_credential]] — code: .set_credential()
- [[assistant_app_core_credential_service_credentialmanager_delete_credential]] — code: .delete_credential()
- [[assistant_app_core_credential_service_rationale_1]] — code: Credential Service — Centralized Plugable Secrets Storage.  SDD-KAOS-EVOLUTION
- [[assistant_app_core_credential_service_rationale_16]] — code: Retrieve a credential.
- [[assistant_app_core_credential_service_rationale_31]] — code: Fallback credential provider using ConfigService secrets file.
- [[assistant_app_core_credential_service_rationale_65]] — code: Centralized manager to orchestrate pluggable credential providers.
- [[assistant_app_core_credential_service_rationale_71]] — code: Register a new credential provider (e.g. Keychain, Vault).
- [[assistant_app_core_credential_service_rationale_79]] — code: Retrieve a credential from the active providers.
- [[assistant_app_core_credential_service_rationale_88]] — code: Store a credential across all providers.
- [[assistant_app_core_credential_service_rationale_94]] — code: Delete a credential across all providers.

## Dependências

- [[assistant_app_core_credential_service_credentialmanager]] → `uses` → [[assistant_app_core_config_service_configservice]]
- [[assistant_app_core_credential_service_credentialprovider]] → `uses` → [[assistant_app_core_config_service_configservice]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider]] → `uses` → [[assistant_app_core_config_service_configservice]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider_delete]] → `calls` → [[assistant_app_core_config_service_configservice_load_secrets]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider_get]] → `calls` → [[assistant_app_core_config_service_configservice_load_secrets]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider_set]] → `calls` → [[assistant_app_core_config_service_configservice_load_secrets]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider_delete]] → `calls` → [[assistant_app_core_config_service_configservice_save_secrets]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider_set]] → `calls` → [[assistant_app_core_config_service_configservice_save_secrets]]
- [[assistant_app_core_credential_service]] → `contains` → [[assistant_app_core_credential_service_credentialmanager]]
- [[assistant_app_core_credential_service]] → `contains` → [[assistant_app_core_credential_service_credentialprovider]]
- [[assistant_app_core_credential_service]] → `contains` → [[assistant_app_core_credential_service_filesecretscredentialprovider]]
- [[assistant_app_core_credential_service]] → `imports_from` → [[assistant_app_core_credential_service_py_abc]]
- [[assistant_app_core_credential_service_rationale_1]] → `rationale_for` → [[assistant_app_core_credential_service]]
- [[assistant_app_core_credential_service_credentialmanager_register_provider]] → `references` → [[assistant_app_core_credential_service_credentialprovider]]
- [[assistant_app_core_credential_service_credentialprovider]] → `method` → [[assistant_app_core_credential_service_credentialprovider_delete]]
- [[assistant_app_core_credential_service_credentialprovider]] → `method` → [[assistant_app_core_credential_service_credentialprovider_get]]
- [[assistant_app_core_credential_service_credentialprovider]] → `method` → [[assistant_app_core_credential_service_credentialprovider_set]]
- [[assistant_app_core_credential_service_credentialprovider]] → `inherits` → [[assistant_app_core_credential_service_py_abc]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider]] → `inherits` → [[assistant_app_core_credential_service_credentialprovider]]
- [[assistant_app_core_credential_service_rationale_16]] → `rationale_for` → [[assistant_app_core_credential_service_credentialprovider_get]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider]] → `method` → [[assistant_app_core_credential_service_filesecretscredentialprovider_delete]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider]] → `method` → [[assistant_app_core_credential_service_filesecretscredentialprovider_get]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider]] → `method` → [[assistant_app_core_credential_service_filesecretscredentialprovider_set]]
- [[assistant_app_core_credential_service_rationale_31]] → `rationale_for` → [[assistant_app_core_credential_service_filesecretscredentialprovider]]
- [[assistant_app_core_credential_service_credentialmanager_get_credential]] → `calls` → [[assistant_app_core_credential_service_filesecretscredentialprovider_get]]
- [[assistant_app_core_credential_service_filesecretscredentialprovider_delete]] → `calls` → [[assistant_app_core_credential_service_filesecretscredentialprovider_get]]
- [[assistant_app_core_credential_service_credentialmanager_delete_credential]] → `calls` → [[assistant_app_core_credential_service_filesecretscredentialprovider_delete]]
- [[assistant_app_core_credential_service_credentialmanager]] → `method` → [[assistant_app_core_credential_service_credentialmanager_delete_credential]]
- [[assistant_app_core_credential_service_credentialmanager]] → `method` → [[assistant_app_core_credential_service_credentialmanager_get_credential]]
- [[assistant_app_core_credential_service_credentialmanager]] → `method` → [[assistant_app_core_credential_service_credentialmanager_register_provider]]
- [[assistant_app_core_credential_service_credentialmanager]] → `method` → [[assistant_app_core_credential_service_credentialmanager_set_credential]]
- [[assistant_app_core_credential_service_rationale_65]] → `rationale_for` → [[assistant_app_core_credential_service_credentialmanager]]
- [[assistant_app_core_credential_service_rationale_71]] → `rationale_for` → [[assistant_app_core_credential_service_credentialmanager_register_provider]]
- [[assistant_app_core_credential_service_rationale_79]] → `rationale_for` → [[assistant_app_core_credential_service_credentialmanager_get_credential]]
- [[assistant_app_core_credential_service_rationale_88]] → `rationale_for` → [[assistant_app_core_credential_service_credentialmanager_set_credential]]
- [[assistant_app_core_credential_service_rationale_94]] → `rationale_for` → [[assistant_app_core_credential_service_credentialmanager_delete_credential]]