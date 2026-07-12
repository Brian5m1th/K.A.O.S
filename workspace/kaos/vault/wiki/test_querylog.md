# graphify\tests\test_querylog.py

## Símbolos

- [[graphify_tests_test_querylog]] — code: test_querylog.py
- [[graphify_tests_test_querylog_test_nodes_from_result_parses_header]] — code: test_nodes_from_result_parses_header()
- [[graphify_tests_test_querylog_test_nodes_from_result_singular]] — code: test_nodes_from_result_singular()
- [[graphify_tests_test_querylog_test_nodes_from_result_missing]] — code: test_nodes_from_result_missing()
- [[graphify_tests_test_querylog_test_nodes_from_result_empty]] — code: test_nodes_from_result_empty()
- [[graphify_tests_test_querylog_test_log_query_writes_jsonl]] — code: test_log_query_writes_jsonl()
- [[graphify_tests_test_querylog_test_log_query_appends]] — code: test_log_query_appends()
- [[graphify_tests_test_querylog_test_disable_env]] — code: test_disable_env()
- [[graphify_tests_test_querylog_test_disable_env_true]] — code: test_disable_env_true()
- [[graphify_tests_test_querylog_test_responses_not_logged_by_default]] — code: test_responses_not_logged_by_default()
- [[graphify_tests_test_querylog_test_responses_optin]] — code: test_responses_optin()
- [[graphify_tests_test_querylog_test_log_never_raises]] — code: test_log_never_raises()
- [[graphify_tests_test_querylog_test_log_creates_parent_dirs]] — code: test_log_creates_parent_dirs()
- [[graphify_tests_test_querylog_test_nodes_returned_inferred_from_result]] — code: test_nodes_returned_inferred_from_result()
- [[graphify_tests_test_querylog_test_explicit_nodes_returned_takes_precedence]] — code: test_explicit_nodes_returned_takes_precedence()
- [[graphify_tests_test_querylog_test_kind_mcp_query]] — code: test_kind_mcp_query()
- [[graphify_tests_test_querylog_rationale_1]] — code: Tests for graphify.querylog.

## Dependências

- [[graphify_tests_test_querylog]] → `imports_from` → [[graphify_graphify_querylog]]
- [[graphify_tests_test_querylog_test_nodes_from_result_empty]] → `calls` → [[graphify_graphify_querylog_nodes_from_result]]
- [[graphify_tests_test_querylog_test_nodes_from_result_missing]] → `calls` → [[graphify_graphify_querylog_nodes_from_result]]
- [[graphify_tests_test_querylog_test_nodes_from_result_parses_header]] → `calls` → [[graphify_graphify_querylog_nodes_from_result]]
- [[graphify_tests_test_querylog_test_nodes_from_result_singular]] → `calls` → [[graphify_graphify_querylog_nodes_from_result]]
- [[graphify_tests_test_querylog_test_disable_env]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_disable_env_true]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_explicit_nodes_returned_takes_precedence]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_kind_mcp_query]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_log_creates_parent_dirs]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_log_never_raises]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_log_query_appends]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_log_query_writes_jsonl]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_nodes_returned_inferred_from_result]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_responses_not_logged_by_default]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog_test_responses_optin]] → `calls` → [[graphify_graphify_querylog_log_query]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_disable_env]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_disable_env_true]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_explicit_nodes_returned_takes_precedence]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_kind_mcp_query]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_log_creates_parent_dirs]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_log_never_raises]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_log_query_appends]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_log_query_writes_jsonl]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_nodes_from_result_empty]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_nodes_from_result_missing]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_nodes_from_result_parses_header]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_nodes_from_result_singular]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_nodes_returned_inferred_from_result]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_responses_not_logged_by_default]]
- [[graphify_tests_test_querylog]] → `contains` → [[graphify_tests_test_querylog_test_responses_optin]]
- [[graphify_tests_test_querylog_rationale_1]] → `rationale_for` → [[graphify_tests_test_querylog]]