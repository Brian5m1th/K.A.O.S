# graphify\tests\test_explain_cli.py

## Símbolos

- [[graphify_tests_test_explain_cli]] — code: test_explain_cli.py
- [[graphify_tests_test_explain_cli_write_graph]] — code: _write_graph()
- [[graphify_tests_test_explain_cli_run]] — code: _run()
- [[graphify_tests_test_explain_cli_test_callee_shows_callers_as_inbound]] — code: test_callee_shows_callers_as_inbound()
- [[graphify_tests_test_explain_cli_test_caller_shows_callee_as_outbound]] — code: test_caller_shows_callee_as_outbound()
- [[graphify_tests_test_explain_cli_test_explain_source_file_path_prefers_file_level_node]] — code: test_explain_source_file_path_prefers_file_level_node()
- [[graphify_tests_test_explain_cli_write_sidecar]] — code: _write_sidecar()
- [[graphify_tests_test_explain_cli_test_explain_shows_preferred_lesson_line]] — code: test_explain_shows_preferred_lesson_line()
- [[graphify_tests_test_explain_cli_test_explain_shows_contested_and_stale_lesson]] — code: test_explain_shows_contested_and_stale_lesson()
- [[graphify_tests_test_explain_cli_test_explain_no_lesson_line_for_unannotated_node]] — code: test_explain_no_lesson_line_for_unannotated_node()
- [[graphify_tests_test_explain_cli_rationale_1]] — code: Regression tests for `graphify explain` arrow direction (#853).
- [[graphify_tests_test_explain_cli_rationale_122]] — code: No sidecar => no Lesson line; output identical to pre-feature.

## Dependências

- [[graphify_tests_test_explain_cli]] → `imports` → [[graphify_graphify_main]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_run]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_test_callee_shows_callers_as_inbound]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_test_caller_shows_callee_as_outbound]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_test_explain_no_lesson_line_for_unannotated_node]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_test_explain_shows_contested_and_stale_lesson]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_test_explain_shows_preferred_lesson_line]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_test_explain_source_file_path_prefers_file_level_node]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_write_graph]]
- [[graphify_tests_test_explain_cli]] → `contains` → [[graphify_tests_test_explain_cli_write_sidecar]]
- [[graphify_tests_test_explain_cli_rationale_1]] → `rationale_for` → [[graphify_tests_test_explain_cli]]
- [[graphify_tests_test_explain_cli_test_callee_shows_callers_as_inbound]] → `calls` → [[graphify_tests_test_explain_cli_write_graph]]
- [[graphify_tests_test_explain_cli_test_caller_shows_callee_as_outbound]] → `calls` → [[graphify_tests_test_explain_cli_write_graph]]
- [[graphify_tests_test_explain_cli_test_explain_no_lesson_line_for_unannotated_node]] → `calls` → [[graphify_tests_test_explain_cli_write_graph]]
- [[graphify_tests_test_explain_cli_test_explain_shows_contested_and_stale_lesson]] → `calls` → [[graphify_tests_test_explain_cli_write_graph]]
- [[graphify_tests_test_explain_cli_test_explain_shows_preferred_lesson_line]] → `calls` → [[graphify_tests_test_explain_cli_write_graph]]
- [[graphify_tests_test_explain_cli_test_callee_shows_callers_as_inbound]] → `calls` → [[graphify_tests_test_explain_cli_run]]
- [[graphify_tests_test_explain_cli_test_caller_shows_callee_as_outbound]] → `calls` → [[graphify_tests_test_explain_cli_run]]
- [[graphify_tests_test_explain_cli_test_explain_no_lesson_line_for_unannotated_node]] → `calls` → [[graphify_tests_test_explain_cli_run]]
- [[graphify_tests_test_explain_cli_test_explain_shows_contested_and_stale_lesson]] → `calls` → [[graphify_tests_test_explain_cli_run]]
- [[graphify_tests_test_explain_cli_test_explain_shows_preferred_lesson_line]] → `calls` → [[graphify_tests_test_explain_cli_run]]
- [[graphify_tests_test_explain_cli_test_explain_source_file_path_prefers_file_level_node]] → `calls` → [[graphify_tests_test_explain_cli_run]]
- [[graphify_tests_test_explain_cli_test_explain_shows_contested_and_stale_lesson]] → `calls` → [[graphify_tests_test_explain_cli_write_sidecar]]
- [[graphify_tests_test_explain_cli_test_explain_shows_preferred_lesson_line]] → `calls` → [[graphify_tests_test_explain_cli_write_sidecar]]
- [[graphify_tests_test_explain_cli_rationale_122]] → `rationale_for` → [[graphify_tests_test_explain_cli_test_explain_no_lesson_line_for_unannotated_node]]