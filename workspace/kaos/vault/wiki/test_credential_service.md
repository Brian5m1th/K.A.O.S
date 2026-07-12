# assistant\tests\unit\test_credential_service.py

## Símbolos

- [[assistant_tests_unit_test_credential_service]] — code: test_credential_service.py
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider]] — code: MockCredentialProvider
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider_init]] — code: .__init__()
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider_get]] — code: .get()
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider_set]] — code: .set()
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider_delete]] — code: .delete()
- [[assistant_tests_unit_test_credential_service_test_credential_manager_flow]] — code: test_credential_manager_flow()

## Dependências

- [[assistant_tests_unit_test_credential_service_mockcredentialprovider]] → `uses` → [[assistant_app_core_credential_service_credentialprovider]]
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider]] → `uses` → [[assistant_app_core_credential_service_credentialmanager]]
- [[assistant_tests_unit_test_credential_service_test_credential_manager_flow]] → `calls` → [[assistant_app_core_credential_service_credentialmanager_register_provider]]
- [[assistant_tests_unit_test_credential_service_test_credential_manager_flow]] → `calls` → [[assistant_app_core_credential_service_credentialmanager_get_credential]]
- [[assistant_tests_unit_test_credential_service_test_credential_manager_flow]] → `calls` → [[assistant_app_core_credential_service_credentialmanager_set_credential]]
- [[assistant_tests_unit_test_credential_service_test_credential_manager_flow]] → `calls` → [[assistant_app_core_credential_service_credentialmanager_delete_credential]]
- [[assistant_tests_unit_test_credential_service]] → `contains` → [[assistant_tests_unit_test_credential_service_mockcredentialprovider]]
- [[assistant_tests_unit_test_credential_service]] → `contains` → [[assistant_tests_unit_test_credential_service_test_credential_manager_flow]]
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider]] → `method` → [[assistant_tests_unit_test_credential_service_mockcredentialprovider_delete]]
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider]] → `method` → [[assistant_tests_unit_test_credential_service_mockcredentialprovider_get]]
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider]] → `method` → [[assistant_tests_unit_test_credential_service_mockcredentialprovider_init]]
- [[assistant_tests_unit_test_credential_service_mockcredentialprovider]] → `method` → [[assistant_tests_unit_test_credential_service_mockcredentialprovider_set]]
- [[assistant_tests_unit_test_credential_service_test_credential_manager_flow]] → `calls` → [[assistant_tests_unit_test_credential_service_mockcredentialprovider]]
- [[assistant_tests_unit_test_credential_service_test_credential_manager_flow]] → `calls` → [[assistant_tests_unit_test_credential_service_mockcredentialprovider_get]]