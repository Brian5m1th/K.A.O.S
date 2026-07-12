# assistant\tests\unit\test_audit_code_scanner.py

## Símbolos

- [[assistant_tests_unit_test_audit_code_scanner]] — code: test_audit_code_scanner.py
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot]] — code: TestCodeSnapshot
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot_test_create_empty]] — code: .test_create_empty()
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot_test_create_with_data]] — code: .test_create_with_data()
- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner]] — code: TestCodeScanner
- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner_test_scan_returns_snapshot]] — code: .test_scan_returns_snapshot()
- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner_test_exclude_dirs_present]] — code: .test_exclude_dirs_present()

## Dependências

- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner]] → `uses` → [[assistant_app_audit_code_scanner_codesnapshot]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner_test_scan_returns_snapshot]] → `indirect_call` → [[assistant_app_audit_code_scanner_codesnapshot]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot]] → `uses` → [[assistant_app_audit_code_scanner_codesnapshot]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot_test_create_empty]] → `calls` → [[assistant_app_audit_code_scanner_codesnapshot]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot_test_create_with_data]] → `calls` → [[assistant_app_audit_code_scanner_codesnapshot]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner]] → `uses` → [[assistant_app_audit_code_scanner_codescanner]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot]] → `uses` → [[assistant_app_audit_code_scanner_codescanner]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner_test_scan_returns_snapshot]] → `calls` → [[assistant_app_audit_code_scanner_codescanner_scan_all]]
- [[assistant_tests_unit_test_audit_code_scanner]] → `contains` → [[assistant_tests_unit_test_audit_code_scanner_testcodescanner]]
- [[assistant_tests_unit_test_audit_code_scanner]] → `contains` → [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot]] → `method` → [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot_test_create_empty]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot]] → `method` → [[assistant_tests_unit_test_audit_code_scanner_testcodesnapshot_test_create_with_data]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner]] → `method` → [[assistant_tests_unit_test_audit_code_scanner_testcodescanner_test_exclude_dirs_present]]
- [[assistant_tests_unit_test_audit_code_scanner_testcodescanner]] → `method` → [[assistant_tests_unit_test_audit_code_scanner_testcodescanner_test_scan_returns_snapshot]]