# graphify\tests\test_language_resolvers.py

## Símbolos

- [[graphify_tests_test_language_resolvers]] — code: test_language_resolvers.py
- [[graphify_tests_test_language_resolvers_make_resolver]] — code: _make_resolver()
- [[graphify_tests_test_language_resolvers_test_default_registry_contains_swift_then_python]] — code: test_default_registry_contains_swift_then_python()
- [[graphify_tests_test_language_resolvers_test_resolver_runs_only_when_suffix_present]] — code: test_resolver_runs_only_when_suffix_present()
- [[graphify_tests_test_language_resolvers_test_resolvers_run_in_given_order]] — code: test_resolvers_run_in_given_order()
- [[graphify_tests_test_language_resolvers_test_failing_resolver_is_isolated]] — code: test_failing_resolver_is_isolated()
- [[graphify_tests_test_language_resolvers_test_resolver_mutates_edges_in_place]] — code: test_resolver_mutates_edges_in_place()
- [[graphify_tests_test_language_resolvers_rationale_1]] — code: Tests for the language resolver registry (graphify.resolver_registry).  The re

## Dependências

- [[graphify_tests_test_language_resolvers_test_resolver_mutates_edges_in_place]] → `indirect_call` → [[graphify_graphify_mcp_ingest_add_edge]]
- [[graphify_tests_test_language_resolvers]] → `imports_from` → [[graphify_graphify_resolver_registry]]
- [[graphify_tests_test_language_resolvers_make_resolver]] → `references` → [[graphify_graphify_resolver_registry_languageresolver]]
- [[graphify_tests_test_language_resolvers_test_failing_resolver_is_isolated]] → `calls` → [[graphify_graphify_resolver_registry_languageresolver]]
- [[graphify_tests_test_language_resolvers_test_resolver_mutates_edges_in_place]] → `calls` → [[graphify_graphify_resolver_registry_languageresolver]]
- [[graphify_tests_test_language_resolvers_test_default_registry_contains_swift_then_python]] → `calls` → [[graphify_graphify_resolver_registry_registered_resolvers]]
- [[graphify_tests_test_language_resolvers_test_failing_resolver_is_isolated]] → `calls` → [[graphify_graphify_resolver_registry_run_language_resolvers]]
- [[graphify_tests_test_language_resolvers_test_resolver_mutates_edges_in_place]] → `calls` → [[graphify_graphify_resolver_registry_run_language_resolvers]]
- [[graphify_tests_test_language_resolvers_test_resolver_runs_only_when_suffix_present]] → `calls` → [[graphify_graphify_resolver_registry_run_language_resolvers]]
- [[graphify_tests_test_language_resolvers_test_resolvers_run_in_given_order]] → `calls` → [[graphify_graphify_resolver_registry_run_language_resolvers]]
- [[graphify_tests_test_language_resolvers]] → `contains` → [[graphify_tests_test_language_resolvers_make_resolver]]
- [[graphify_tests_test_language_resolvers]] → `contains` → [[graphify_tests_test_language_resolvers_test_default_registry_contains_swift_then_python]]
- [[graphify_tests_test_language_resolvers]] → `contains` → [[graphify_tests_test_language_resolvers_test_failing_resolver_is_isolated]]
- [[graphify_tests_test_language_resolvers]] → `contains` → [[graphify_tests_test_language_resolvers_test_resolver_mutates_edges_in_place]]
- [[graphify_tests_test_language_resolvers]] → `contains` → [[graphify_tests_test_language_resolvers_test_resolver_runs_only_when_suffix_present]]
- [[graphify_tests_test_language_resolvers]] → `contains` → [[graphify_tests_test_language_resolvers_test_resolvers_run_in_given_order]]
- [[graphify_tests_test_language_resolvers_rationale_1]] → `rationale_for` → [[graphify_tests_test_language_resolvers]]
- [[graphify_tests_test_language_resolvers_test_failing_resolver_is_isolated]] → `calls` → [[graphify_tests_test_language_resolvers_make_resolver]]
- [[graphify_tests_test_language_resolvers_test_resolver_runs_only_when_suffix_present]] → `calls` → [[graphify_tests_test_language_resolvers_make_resolver]]
- [[graphify_tests_test_language_resolvers_test_resolvers_run_in_given_order]] → `calls` → [[graphify_tests_test_language_resolvers_make_resolver]]