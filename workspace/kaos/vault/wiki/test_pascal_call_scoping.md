# graphify\tests\test_pascal_call_scoping.py

## Símbolos

- [[graphify_tests_test_pascal_call_scoping]] — code: test_pascal_call_scoping.py
- [[graphify_tests_test_pascal_call_scoping_extractors]] — code: _extractors()
- [[graphify_tests_test_pascal_call_scoping_class_node_id]] — code: _class_node_id()
- [[graphify_tests_test_pascal_call_scoping_method_node_id]] — code: _method_node_id()
- [[graphify_tests_test_pascal_call_scoping_has_call]] — code: _has_call()
- [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_to_own_class]] — code: test_calls_scoped_to_own_class()
- [[graphify_tests_test_pascal_call_scoping_test_calls_do_not_cross_unrelated_classes]] — code: test_calls_do_not_cross_unrelated_classes()
- [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_other_direction]] — code: test_calls_scoped_other_direction()
- [[graphify_tests_test_pascal_call_scoping_test_calls_resolve_via_ancestor_chain]] — code: test_calls_resolve_via_ancestor_chain()
- [[graphify_tests_test_pascal_call_scoping_rationale_1]] — code: Regression tests for scoped call resolution in the Pascal/Delphi extractor.  B

## Dependências

- [[graphify_tests_test_pascal_call_scoping_extractors]] → `indirect_call` → [[graphify_graphify_extractors_pascal_extract_pascal_regex]]
- [[graphify_tests_test_pascal_call_scoping_extractors]] → `indirect_call` → [[graphify_graphify_extractors_pascal_extract_pascal]]
- [[graphify_tests_test_pascal_call_scoping]] → `contains` → [[graphify_tests_test_pascal_call_scoping_class_node_id]]
- [[graphify_tests_test_pascal_call_scoping]] → `contains` → [[graphify_tests_test_pascal_call_scoping_extractors]]
- [[graphify_tests_test_pascal_call_scoping]] → `contains` → [[graphify_tests_test_pascal_call_scoping_has_call]]
- [[graphify_tests_test_pascal_call_scoping]] → `contains` → [[graphify_tests_test_pascal_call_scoping_method_node_id]]
- [[graphify_tests_test_pascal_call_scoping]] → `contains` → [[graphify_tests_test_pascal_call_scoping_test_calls_do_not_cross_unrelated_classes]]
- [[graphify_tests_test_pascal_call_scoping]] → `contains` → [[graphify_tests_test_pascal_call_scoping_test_calls_resolve_via_ancestor_chain]]
- [[graphify_tests_test_pascal_call_scoping]] → `contains` → [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_other_direction]]
- [[graphify_tests_test_pascal_call_scoping]] → `contains` → [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_to_own_class]]
- [[graphify_tests_test_pascal_call_scoping_rationale_1]] → `rationale_for` → [[graphify_tests_test_pascal_call_scoping]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_do_not_cross_unrelated_classes]] → `calls` → [[graphify_tests_test_pascal_call_scoping_extractors]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_resolve_via_ancestor_chain]] → `calls` → [[graphify_tests_test_pascal_call_scoping_extractors]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_other_direction]] → `calls` → [[graphify_tests_test_pascal_call_scoping_extractors]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_to_own_class]] → `calls` → [[graphify_tests_test_pascal_call_scoping_extractors]]
- [[graphify_tests_test_pascal_call_scoping_method_node_id]] → `calls` → [[graphify_tests_test_pascal_call_scoping_class_node_id]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_do_not_cross_unrelated_classes]] → `calls` → [[graphify_tests_test_pascal_call_scoping_method_node_id]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_resolve_via_ancestor_chain]] → `calls` → [[graphify_tests_test_pascal_call_scoping_method_node_id]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_other_direction]] → `calls` → [[graphify_tests_test_pascal_call_scoping_method_node_id]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_to_own_class]] → `calls` → [[graphify_tests_test_pascal_call_scoping_method_node_id]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_do_not_cross_unrelated_classes]] → `calls` → [[graphify_tests_test_pascal_call_scoping_has_call]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_resolve_via_ancestor_chain]] → `calls` → [[graphify_tests_test_pascal_call_scoping_has_call]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_other_direction]] → `calls` → [[graphify_tests_test_pascal_call_scoping_has_call]]
- [[graphify_tests_test_pascal_call_scoping_test_calls_scoped_to_own_class]] → `calls` → [[graphify_tests_test_pascal_call_scoping_has_call]]