# graphify\tests\test_affected_member_seed.py

## Símbolos

- [[graphify_tests_test_affected_member_seed]] — code: test_affected_member_seed.py
- [[graphify_tests_test_affected_member_seed_g]] — code: _g()
- [[graphify_tests_test_affected_member_seed_test_class_affected_reaches_method_bound_caller]] — code: test_class_affected_reaches_method_bound_caller()
- [[graphify_tests_test_affected_member_seed_test_member_method_node_not_reported_as_hit]] — code: test_member_method_node_not_reported_as_hit()
- [[graphify_tests_test_affected_member_seed_test_method_contains_still_excluded_from_general_walk]] — code: test_method_contains_still_excluded_from_general_walk()
- [[graphify_tests_test_affected_member_seed_test_class_level_caller_still_works]] — code: test_class_level_caller_still_works()
- [[graphify_tests_test_affected_member_seed_rationale_1]] — code: #1669 — affected <Class> must reach callers that bind to the class's method nod

## Dependências

- [[graphify_tests_test_affected_member_seed]] → `imports_from` → [[graphify_graphify_affected]]
- [[graphify_tests_test_affected_member_seed_test_class_affected_reaches_method_bound_caller]] → `calls` → [[graphify_graphify_affected_affected_nodes]]
- [[graphify_tests_test_affected_member_seed_test_class_level_caller_still_works]] → `calls` → [[graphify_graphify_affected_affected_nodes]]
- [[graphify_tests_test_affected_member_seed_test_member_method_node_not_reported_as_hit]] → `calls` → [[graphify_graphify_affected_affected_nodes]]
- [[graphify_tests_test_affected_member_seed_test_method_contains_still_excluded_from_general_walk]] → `calls` → [[graphify_graphify_affected_affected_nodes]]
- [[graphify_tests_test_affected_member_seed]] → `contains` → [[graphify_tests_test_affected_member_seed_g]]
- [[graphify_tests_test_affected_member_seed]] → `contains` → [[graphify_tests_test_affected_member_seed_test_class_affected_reaches_method_bound_caller]]
- [[graphify_tests_test_affected_member_seed]] → `contains` → [[graphify_tests_test_affected_member_seed_test_class_level_caller_still_works]]
- [[graphify_tests_test_affected_member_seed]] → `contains` → [[graphify_tests_test_affected_member_seed_test_member_method_node_not_reported_as_hit]]
- [[graphify_tests_test_affected_member_seed]] → `contains` → [[graphify_tests_test_affected_member_seed_test_method_contains_still_excluded_from_general_walk]]
- [[graphify_tests_test_affected_member_seed_rationale_1]] → `rationale_for` → [[graphify_tests_test_affected_member_seed]]
- [[graphify_tests_test_affected_member_seed_test_class_affected_reaches_method_bound_caller]] → `calls` → [[graphify_tests_test_affected_member_seed_g]]
- [[graphify_tests_test_affected_member_seed_test_member_method_node_not_reported_as_hit]] → `calls` → [[graphify_tests_test_affected_member_seed_g]]