# graphify\tests\test_extract_code_only_cli.py

## Símbolos

- [[graphify_tests_test_extract_code_only_cli]] — code: test_extract_code_only_cli.py
- [[graphify_tests_test_extract_code_only_cli_mixed_repo]] — code: _mixed_repo()
- [[graphify_tests_test_extract_code_only_cli_run]] — code: _run()
- [[graphify_tests_test_extract_code_only_cli_test_code_only_succeeds_without_key]] — code: test_code_only_succeeds_without_key()
- [[graphify_tests_test_extract_code_only_cli_test_mixed_repo_without_key_errors_and_points_at_code_only]] — code: test_mixed_repo_without_key_errors_and_points_at_code_only()
- [[graphify_tests_test_extract_code_only_cli_rationale_1]] — code: `graphify extract --code-only` indexes code without an LLM key (#1734).  A mix

## Dependências

- [[graphify_tests_test_extract_code_only_cli]] → `contains` → [[graphify_tests_test_extract_code_only_cli_mixed_repo]]
- [[graphify_tests_test_extract_code_only_cli]] → `contains` → [[graphify_tests_test_extract_code_only_cli_run]]
- [[graphify_tests_test_extract_code_only_cli]] → `contains` → [[graphify_tests_test_extract_code_only_cli_test_code_only_succeeds_without_key]]
- [[graphify_tests_test_extract_code_only_cli]] → `contains` → [[graphify_tests_test_extract_code_only_cli_test_mixed_repo_without_key_errors_and_points_at_code_only]]
- [[graphify_tests_test_extract_code_only_cli_rationale_1]] → `rationale_for` → [[graphify_tests_test_extract_code_only_cli]]
- [[graphify_tests_test_extract_code_only_cli_mixed_repo]] → `references` → [[graphify_tests_test_extract_code_only_cli_py_path]]
- [[graphify_tests_test_extract_code_only_cli_test_code_only_succeeds_without_key]] → `calls` → [[graphify_tests_test_extract_code_only_cli_mixed_repo]]
- [[graphify_tests_test_extract_code_only_cli_test_mixed_repo_without_key_errors_and_points_at_code_only]] → `calls` → [[graphify_tests_test_extract_code_only_cli_mixed_repo]]
- [[graphify_tests_test_extract_code_only_cli_run]] → `references` → [[graphify_tests_test_extract_code_only_cli_py_path]]
- [[graphify_tests_test_extract_code_only_cli_test_code_only_succeeds_without_key]] → `calls` → [[graphify_tests_test_extract_code_only_cli_run]]
- [[graphify_tests_test_extract_code_only_cli_test_mixed_repo_without_key_errors_and_points_at_code_only]] → `calls` → [[graphify_tests_test_extract_code_only_cli_run]]