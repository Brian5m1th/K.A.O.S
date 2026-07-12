# graphify\tests\test_case_sensitive_resolution.py

## Símbolos

- [[graphify_tests_test_case_sensitive_resolution]] — code: test_case_sensitive_resolution.py
- [[graphify_tests_test_case_sensitive_resolution_extract]] — code: _extract()
- [[graphify_tests_test_case_sensitive_resolution_labels]] — code: _labels()
- [[graphify_tests_test_case_sensitive_resolution_test_python_path_does_not_resolve_to_shell_path]] — code: test_python_Path_does_not_resolve_to_shell_PATH()
- [[graphify_tests_test_case_sensitive_resolution_test_case_sensitive_cross_file_ref_respects_case]] — code: test_case_sensitive_cross_file_ref_respects_case()
- [[graphify_tests_test_case_sensitive_resolution_test_exact_case_cross_file_still_resolves]] — code: test_exact_case_cross_file_still_resolves()
- [[graphify_tests_test_case_sensitive_resolution_test_php_case_insensitive_resolution_preserved]] — code: test_php_case_insensitive_resolution_preserved()
- [[graphify_tests_test_case_sensitive_resolution_rationale_1]] — code: Cross-file name resolution respects case in case-sensitive languages (#1581).

## Dependências

- [[graphify_tests_test_case_sensitive_resolution]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_case_sensitive_resolution_extract]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_case_sensitive_resolution]] → `contains` → [[graphify_tests_test_case_sensitive_resolution_extract]]
- [[graphify_tests_test_case_sensitive_resolution]] → `contains` → [[graphify_tests_test_case_sensitive_resolution_labels]]
- [[graphify_tests_test_case_sensitive_resolution]] → `contains` → [[graphify_tests_test_case_sensitive_resolution_test_case_sensitive_cross_file_ref_respects_case]]
- [[graphify_tests_test_case_sensitive_resolution]] → `contains` → [[graphify_tests_test_case_sensitive_resolution_test_exact_case_cross_file_still_resolves]]
- [[graphify_tests_test_case_sensitive_resolution]] → `contains` → [[graphify_tests_test_case_sensitive_resolution_test_php_case_insensitive_resolution_preserved]]
- [[graphify_tests_test_case_sensitive_resolution]] → `contains` → [[graphify_tests_test_case_sensitive_resolution_test_python_path_does_not_resolve_to_shell_path]]
- [[graphify_tests_test_case_sensitive_resolution_rationale_1]] → `rationale_for` → [[graphify_tests_test_case_sensitive_resolution]]
- [[graphify_tests_test_case_sensitive_resolution_test_case_sensitive_cross_file_ref_respects_case]] → `calls` → [[graphify_tests_test_case_sensitive_resolution_extract]]
- [[graphify_tests_test_case_sensitive_resolution_test_exact_case_cross_file_still_resolves]] → `calls` → [[graphify_tests_test_case_sensitive_resolution_extract]]
- [[graphify_tests_test_case_sensitive_resolution_test_php_case_insensitive_resolution_preserved]] → `calls` → [[graphify_tests_test_case_sensitive_resolution_extract]]
- [[graphify_tests_test_case_sensitive_resolution_test_python_path_does_not_resolve_to_shell_path]] → `calls` → [[graphify_tests_test_case_sensitive_resolution_extract]]
- [[graphify_tests_test_case_sensitive_resolution_test_case_sensitive_cross_file_ref_respects_case]] → `calls` → [[graphify_tests_test_case_sensitive_resolution_labels]]
- [[graphify_tests_test_case_sensitive_resolution_test_exact_case_cross_file_still_resolves]] → `calls` → [[graphify_tests_test_case_sensitive_resolution_labels]]
- [[graphify_tests_test_case_sensitive_resolution_test_php_case_insensitive_resolution_preserved]] → `calls` → [[graphify_tests_test_case_sensitive_resolution_labels]]
- [[graphify_tests_test_case_sensitive_resolution_test_python_path_does_not_resolve_to_shell_path]] → `calls` → [[graphify_tests_test_case_sensitive_resolution_labels]]