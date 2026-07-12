# graphify\tests\test_path_cli.py

## Símbolos

- [[graphify_tests_test_path_cli]] — code: test_path_cli.py
- [[graphify_tests_test_path_cli_write_graph]] — code: _write_graph()
- [[graphify_tests_test_path_cli_run]] — code: _run()
- [[graphify_tests_test_path_cli_test_forward_arrow]] — code: test_forward_arrow()
- [[graphify_tests_test_path_cli_test_reverse_arrow]] — code: test_reverse_arrow()
- [[graphify_tests_test_path_cli_write_misranking_graph]] — code: _write_misranking_graph()
- [[graphify_tests_test_path_cli_test_endpoint_prefers_full_token_match]] — code: test_endpoint_prefers_full_token_match()
- [[graphify_tests_test_path_cli_test_endpoint_falls_back_to_score_head]] — code: test_endpoint_falls_back_to_score_head()
- [[graphify_tests_test_path_cli_rationale_1]] — code: Regression tests for `graphify path` arrow direction (#849).
- [[graphify_tests_test_path_cli_rationale_53]] — code: Graph where IDF scoring ranks a partial-token decoy above the full match.
- [[graphify_tests_test_path_cli_rationale_85]] — code: A token-subset query resolves to the full-match node, not the IDF head.
- [[graphify_tests_test_path_cli_rationale_94]] — code: No full-token candidate -> behavior identical to the old scored[0] pick.

## Dependências

- [[graphify_tests_test_path_cli]] → `imports` → [[graphify_graphify_main]]
- [[graphify_tests_test_path_cli]] → `contains` → [[graphify_tests_test_path_cli_run]]
- [[graphify_tests_test_path_cli]] → `contains` → [[graphify_tests_test_path_cli_test_endpoint_falls_back_to_score_head]]
- [[graphify_tests_test_path_cli]] → `contains` → [[graphify_tests_test_path_cli_test_endpoint_prefers_full_token_match]]
- [[graphify_tests_test_path_cli]] → `contains` → [[graphify_tests_test_path_cli_test_forward_arrow]]
- [[graphify_tests_test_path_cli]] → `contains` → [[graphify_tests_test_path_cli_test_reverse_arrow]]
- [[graphify_tests_test_path_cli]] → `contains` → [[graphify_tests_test_path_cli_write_graph]]
- [[graphify_tests_test_path_cli]] → `contains` → [[graphify_tests_test_path_cli_write_misranking_graph]]
- [[graphify_tests_test_path_cli_rationale_1]] → `rationale_for` → [[graphify_tests_test_path_cli]]
- [[graphify_tests_test_path_cli_test_forward_arrow]] → `calls` → [[graphify_tests_test_path_cli_write_graph]]
- [[graphify_tests_test_path_cli_test_reverse_arrow]] → `calls` → [[graphify_tests_test_path_cli_write_graph]]
- [[graphify_tests_test_path_cli_test_endpoint_prefers_full_token_match]] → `calls` → [[graphify_tests_test_path_cli_run]]
- [[graphify_tests_test_path_cli_test_forward_arrow]] → `calls` → [[graphify_tests_test_path_cli_run]]
- [[graphify_tests_test_path_cli_test_reverse_arrow]] → `calls` → [[graphify_tests_test_path_cli_run]]
- [[graphify_tests_test_path_cli_rationale_53]] → `rationale_for` → [[graphify_tests_test_path_cli_write_misranking_graph]]
- [[graphify_tests_test_path_cli_test_endpoint_falls_back_to_score_head]] → `calls` → [[graphify_tests_test_path_cli_write_misranking_graph]]
- [[graphify_tests_test_path_cli_test_endpoint_prefers_full_token_match]] → `calls` → [[graphify_tests_test_path_cli_write_misranking_graph]]
- [[graphify_tests_test_path_cli_rationale_85]] → `rationale_for` → [[graphify_tests_test_path_cli_test_endpoint_prefers_full_token_match]]
- [[graphify_tests_test_path_cli_rationale_94]] → `rationale_for` → [[graphify_tests_test_path_cli_test_endpoint_falls_back_to_score_head]]