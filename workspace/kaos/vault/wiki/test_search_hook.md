# graphify\tests\test_search_hook.py

## Símbolos

- [[graphify_tests_test_search_hook]] — code: test_search_hook.py
- [[graphify_tests_test_search_hook_search_matcher]] — code: _search_matcher()
- [[graphify_tests_test_search_hook_env]] — code: _env()
- [[graphify_tests_test_search_hook_run]] — code: _run()
- [[graphify_tests_test_search_hook_test_matcher_targets_bash]] — code: test_matcher_targets_bash()
- [[graphify_tests_test_search_hook_test_command_has_no_shell_syntax]] — code: test_command_has_no_shell_syntax()
- [[graphify_tests_test_search_hook_test_nudges_on_search_commands_with_graph]] — code: test_nudges_on_search_commands_with_graph()
- [[graphify_tests_test_search_hook_test_silent_without_graph]] — code: test_silent_without_graph()
- [[graphify_tests_test_search_hook_test_silent_on_non_search_commands]] — code: test_silent_on_non_search_commands()
- [[graphify_tests_test_search_hook_test_nudge_payload_is_valid_pretooluse_json]] — code: test_nudge_payload_is_valid_pretooluse_json()
- [[graphify_tests_test_search_hook_test_fails_open_on_malformed_stdin]] — code: test_fails_open_on_malformed_stdin()
- [[graphify_tests_test_search_hook_test_never_blocks]] — code: test_never_blocks()
- [[graphify_tests_test_search_hook_test_honors_graphify_out_override]] — code: test_honors_graphify_out_override()
- [[graphify_tests_test_search_hook_rationale_1]] — code: The Bash PreToolUse guard nudges toward the graph before grep/find searches.
- [[graphify_tests_test_search_hook_rationale_101]] — code: The guard resolves the graph via GRAPHIFY_OUT, not a hardcoded path.

## Dependências

- [[graphify_tests_test_search_hook]] → `imports_from` → [[graphify_graphify_main]]
- [[graphify_tests_test_search_hook_search_matcher]] → `calls` → [[graphify_graphify_install_claude_pretooluse_hooks]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_env]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_run]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_search_matcher]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_command_has_no_shell_syntax]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_fails_open_on_malformed_stdin]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_honors_graphify_out_override]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_matcher_targets_bash]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_never_blocks]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_nudge_payload_is_valid_pretooluse_json]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_nudges_on_search_commands_with_graph]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_silent_on_non_search_commands]]
- [[graphify_tests_test_search_hook]] → `contains` → [[graphify_tests_test_search_hook_test_silent_without_graph]]
- [[graphify_tests_test_search_hook_rationale_1]] → `rationale_for` → [[graphify_tests_test_search_hook]]
- [[graphify_tests_test_search_hook_test_command_has_no_shell_syntax]] → `calls` → [[graphify_tests_test_search_hook_search_matcher]]
- [[graphify_tests_test_search_hook_test_matcher_targets_bash]] → `calls` → [[graphify_tests_test_search_hook_search_matcher]]
- [[graphify_tests_test_search_hook_run]] → `calls` → [[graphify_tests_test_search_hook_env]]
- [[graphify_tests_test_search_hook_test_fails_open_on_malformed_stdin]] → `calls` → [[graphify_tests_test_search_hook_env]]
- [[graphify_tests_test_search_hook_test_never_blocks]] → `calls` → [[graphify_tests_test_search_hook_run]]
- [[graphify_tests_test_search_hook_test_nudge_payload_is_valid_pretooluse_json]] → `calls` → [[graphify_tests_test_search_hook_run]]
- [[graphify_tests_test_search_hook_test_nudges_on_search_commands_with_graph]] → `calls` → [[graphify_tests_test_search_hook_run]]
- [[graphify_tests_test_search_hook_test_silent_on_non_search_commands]] → `calls` → [[graphify_tests_test_search_hook_run]]
- [[graphify_tests_test_search_hook_test_silent_without_graph]] → `calls` → [[graphify_tests_test_search_hook_run]]
- [[graphify_tests_test_search_hook_rationale_101]] → `rationale_for` → [[graphify_tests_test_search_hook_test_honors_graphify_out_override]]