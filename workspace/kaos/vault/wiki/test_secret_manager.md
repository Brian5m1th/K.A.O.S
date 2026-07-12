# assistant\tests\unit\test_secret_manager.py

## Símbolos

- [[assistant_tests_unit_test_secret_manager]] — code: test_secret_manager.py
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_encryption_decryption]] — code: test_secret_manager_encryption_decryption()
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_missing_key]] — code: test_secret_manager_missing_key()
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_invalid_key]] — code: test_secret_manager_invalid_key()
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_rotation]] — code: test_secret_manager_rotation()

## Dependências

- [[assistant_tests_unit_test_secret_manager_test_secret_manager_rotation]] → `calls` → [[fernet]]
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_encryption_decryption]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_encrypt]]
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_invalid_key]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_encrypt]]
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_missing_key]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_encrypt]]
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_encryption_decryption]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_decrypt]]
- [[assistant_tests_unit_test_secret_manager_test_secret_manager_rotation]] → `calls` → [[assistant_app_core_secret_manager_secretmanager_rotate_key]]
- [[assistant_tests_unit_test_secret_manager]] → `contains` → [[assistant_tests_unit_test_secret_manager_test_secret_manager_encryption_decryption]]
- [[assistant_tests_unit_test_secret_manager]] → `contains` → [[assistant_tests_unit_test_secret_manager_test_secret_manager_invalid_key]]
- [[assistant_tests_unit_test_secret_manager]] → `contains` → [[assistant_tests_unit_test_secret_manager_test_secret_manager_missing_key]]
- [[assistant_tests_unit_test_secret_manager]] → `contains` → [[assistant_tests_unit_test_secret_manager_test_secret_manager_rotation]]