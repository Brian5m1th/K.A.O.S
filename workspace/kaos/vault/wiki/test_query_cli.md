# graphify\tests\test_query_cli.py

## Símbolos

- [[graphify_tests_test_query_cli]] — code: test_query_cli.py
- [[graphify_tests_test_query_cli_write_graph]] — code: _write_graph()
- [[graphify_tests_test_query_cli_test_query_cli_explicit_context_filter]] — code: test_query_cli_explicit_context_filter()
- [[graphify_tests_test_query_cli_test_query_cli_heuristic_context_filter]] — code: test_query_cli_heuristic_context_filter()
- [[graphify_tests_test_query_cli_test_query_cli_rejects_oversized_graph]] — code: test_query_cli_rejects_oversized_graph()
- [[graphify_tests_test_query_cli_rationale_1]] — code: Tests for graphify query CLI context filtering.
- [[graphify_tests_test_query_cli_rationale_55]] — code: #F4: query CLI must refuse to parse a graph.json that exceeds the cap.

## Dependências

- [[graphify_tests_test_query_cli]] → `imports` → [[graphify_graphify_main]]
- [[graphify_tests_test_query_cli]] → `contains` → [[graphify_tests_test_query_cli_test_query_cli_explicit_context_filter]]
- [[graphify_tests_test_query_cli]] → `contains` → [[graphify_tests_test_query_cli_test_query_cli_heuristic_context_filter]]
- [[graphify_tests_test_query_cli]] → `contains` → [[graphify_tests_test_query_cli_test_query_cli_rejects_oversized_graph]]
- [[graphify_tests_test_query_cli]] → `contains` → [[graphify_tests_test_query_cli_write_graph]]
- [[graphify_tests_test_query_cli_rationale_1]] → `rationale_for` → [[graphify_tests_test_query_cli]]
- [[graphify_tests_test_query_cli_test_query_cli_explicit_context_filter]] → `calls` → [[graphify_tests_test_query_cli_write_graph]]
- [[graphify_tests_test_query_cli_test_query_cli_heuristic_context_filter]] → `calls` → [[graphify_tests_test_query_cli_write_graph]]
- [[graphify_tests_test_query_cli_test_query_cli_rejects_oversized_graph]] → `calls` → [[graphify_tests_test_query_cli_write_graph]]
- [[graphify_tests_test_query_cli_rationale_55]] → `rationale_for` → [[graphify_tests_test_query_cli_test_query_cli_rejects_oversized_graph]]