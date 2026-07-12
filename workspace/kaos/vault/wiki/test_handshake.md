# assistant\tests\unit\test_handshake.py

## Símbolos

- [[assistant_tests_unit_test_handshake]] — code: test_handshake.py
- [[assistant_tests_unit_test_handshake_client]] — code: client()
- [[assistant_tests_unit_test_handshake_testsecurehandshake]] — code: TestSecureHandshake
- [[assistant_tests_unit_test_handshake_testsecurehandshake_test_handshake_service_flow]] — code: .test_handshake_service_flow()
- [[assistant_tests_unit_test_handshake_testsecurehandshake_test_handshake_api_flow]] — code: .test_handshake_api_flow()

## Dependências

- [[assistant_tests_unit_test_handshake_testsecurehandshake]] → `uses` → [[assistant_app_auth_handshake_handshakeservice]]
- [[assistant_tests_unit_test_handshake_testsecurehandshake_test_handshake_service_flow]] → `calls` → [[assistant_app_auth_handshake_handshakeservice]]
- [[assistant_tests_unit_test_handshake]] → `imports_from` → [[assistant_app_main]]
- [[assistant_tests_unit_test_handshake]] → `contains` → [[assistant_tests_unit_test_handshake_client]]
- [[assistant_tests_unit_test_handshake]] → `contains` → [[assistant_tests_unit_test_handshake_testsecurehandshake]]
- [[assistant_tests_unit_test_handshake_client]] → `references` → [[assistant_tests_unit_test_handshake_py_testclient]]
- [[assistant_tests_unit_test_handshake_testsecurehandshake_test_handshake_api_flow]] → `references` → [[assistant_tests_unit_test_handshake_py_testclient]]
- [[assistant_tests_unit_test_handshake_testsecurehandshake]] → `method` → [[assistant_tests_unit_test_handshake_testsecurehandshake_test_handshake_api_flow]]
- [[assistant_tests_unit_test_handshake_testsecurehandshake]] → `method` → [[assistant_tests_unit_test_handshake_testsecurehandshake_test_handshake_service_flow]]