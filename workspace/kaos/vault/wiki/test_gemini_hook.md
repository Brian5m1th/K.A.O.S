# graphify\tests\test_gemini_hook.py

## Símbolos

- [[graphify_tests_test_gemini_hook]] — code: test_gemini_hook.py
- [[graphify_tests_test_gemini_hook_env]] — code: _env()
- [[graphify_tests_test_gemini_hook_run]] — code: _run()
- [[graphify_tests_test_gemini_hook_test_matcher_and_command_shape]] — code: test_matcher_and_command_shape()
- [[graphify_tests_test_gemini_hook_test_allows_and_nudges_with_graph]] — code: test_allows_and_nudges_with_graph()
- [[graphify_tests_test_gemini_hook_test_allows_without_nudge_when_no_graph]] — code: test_allows_without_nudge_when_no_graph()
- [[graphify_tests_test_gemini_hook_test_never_blocks]] — code: test_never_blocks()
- [[graphify_tests_test_gemini_hook_test_honors_graphify_out_override]] — code: test_honors_graphify_out_override()
- [[graphify_tests_test_gemini_hook_rationale_1]] — code: The Gemini CLI BeforeTool guard nudges toward the graph, shell-agnostically.

## Dependências

- [[graphify_tests_test_gemini_hook]] → `imports_from` → [[graphify_graphify_main]]
- [[graphify_tests_test_gemini_hook_test_matcher_and_command_shape]] → `calls` → [[graphify_graphify_install_gemini_hook]]
- [[graphify_tests_test_gemini_hook]] → `contains` → [[graphify_tests_test_gemini_hook_env]]
- [[graphify_tests_test_gemini_hook]] → `contains` → [[graphify_tests_test_gemini_hook_run]]
- [[graphify_tests_test_gemini_hook]] → `contains` → [[graphify_tests_test_gemini_hook_test_allows_and_nudges_with_graph]]
- [[graphify_tests_test_gemini_hook]] → `contains` → [[graphify_tests_test_gemini_hook_test_allows_without_nudge_when_no_graph]]
- [[graphify_tests_test_gemini_hook]] → `contains` → [[graphify_tests_test_gemini_hook_test_honors_graphify_out_override]]
- [[graphify_tests_test_gemini_hook]] → `contains` → [[graphify_tests_test_gemini_hook_test_matcher_and_command_shape]]
- [[graphify_tests_test_gemini_hook]] → `contains` → [[graphify_tests_test_gemini_hook_test_never_blocks]]
- [[graphify_tests_test_gemini_hook_rationale_1]] → `rationale_for` → [[graphify_tests_test_gemini_hook]]
- [[graphify_tests_test_gemini_hook_run]] → `calls` → [[graphify_tests_test_gemini_hook_env]]
- [[graphify_tests_test_gemini_hook_test_allows_and_nudges_with_graph]] → `calls` → [[graphify_tests_test_gemini_hook_run]]
- [[graphify_tests_test_gemini_hook_test_allows_without_nudge_when_no_graph]] → `calls` → [[graphify_tests_test_gemini_hook_run]]
- [[graphify_tests_test_gemini_hook_test_never_blocks]] → `calls` → [[graphify_tests_test_gemini_hook_run]]