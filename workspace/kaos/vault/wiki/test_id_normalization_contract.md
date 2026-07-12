# graphify\tests\test_id_normalization_contract.py

## Símbolos

- [[graphify_tests_test_id_normalization_contract]] — code: test_id_normalization_contract.py
- [[graphify_tests_test_id_normalization_contract_test_make_id_matches_normalize_id]] — code: test_make_id_matches_normalize_id()
- [[graphify_tests_test_id_normalization_contract_test_normalize_id_is_idempotent]] — code: test_normalize_id_is_idempotent()
- [[graphify_tests_test_id_normalization_contract_test_make_id_joins_then_normalizes]] — code: test_make_id_joins_then_normalizes()
- [[graphify_tests_test_id_normalization_contract_test_unicode_identifiers_do_not_collapse_to_empty]] — code: test_unicode_identifiers_do_not_collapse_to_empty()
- [[graphify_tests_test_id_normalization_contract_test_normalized_ids_are_safe_node_ids]] — code: test_normalized_ids_are_safe_node_ids()
- [[graphify_tests_test_id_normalization_contract_test_both_callers_share_one_implementation]] — code: test_both_callers_share_one_implementation()
- [[graphify_tests_test_id_normalization_contract_test_property_make_id_equals_normalize_id]] — code: test_property_make_id_equals_normalize_id()
- [[graphify_tests_test_id_normalization_contract_test_property_normalize_id_idempotent]] — code: test_property_normalize_id_idempotent()
- [[graphify_tests_test_id_normalization_contract_rationale_1]] — code: Drift guard for the node-ID normalization contract.  Three independent produce
- [[graphify_tests_test_id_normalization_contract_rationale_47]] — code: The AST id-maker and the builder's reconciler must agree, char for char.
- [[graphify_tests_test_id_normalization_contract_rationale_61]] — code: Multi-part make_id == normalize_id of the joined parts (the builder only     ev
- [[graphify_tests_test_id_normalization_contract_rationale_71]] — code: #811: non-ASCII identifiers must yield distinct, non-empty IDs rather than
- [[graphify_tests_test_id_normalization_contract_rationale_79]] — code: Output is lowercase and contains no path/punctuation separators.
- [[graphify_tests_test_id_normalization_contract_rationale_88]] — code: Guard against re-forking: the two public callers must resolve to the same     u

## Dependências

- [[graphify_tests_test_id_normalization_contract_test_make_id_matches_normalize_id]] → `calls` → [[assistant_scripts_bootstrap_feature_registry_normalize_id]]
- [[graphify_tests_test_id_normalization_contract_test_property_make_id_equals_normalize_id]] → `calls` → [[assistant_scripts_bootstrap_feature_registry_normalize_id]]
- [[graphify_tests_test_id_normalization_contract]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_id_normalization_contract]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_id_normalization_contract]] → `imports_from` → [[graphify_graphify_ids]]
- [[graphify_tests_test_id_normalization_contract_test_both_callers_share_one_implementation]] → `calls` → [[graphify_graphify_ids_normalize_id]]
- [[graphify_tests_test_id_normalization_contract_test_make_id_joins_then_normalizes]] → `calls` → [[graphify_graphify_ids_normalize_id]]
- [[graphify_tests_test_id_normalization_contract_test_normalize_id_is_idempotent]] → `calls` → [[graphify_graphify_ids_normalize_id]]
- [[graphify_tests_test_id_normalization_contract_test_normalized_ids_are_safe_node_ids]] → `calls` → [[graphify_graphify_ids_normalize_id]]
- [[graphify_tests_test_id_normalization_contract_test_property_normalize_id_idempotent]] → `calls` → [[graphify_graphify_ids_normalize_id]]
- [[graphify_tests_test_id_normalization_contract_test_both_callers_share_one_implementation]] → `calls` → [[graphify_graphify_ids_make_id]]
- [[graphify_tests_test_id_normalization_contract_test_make_id_joins_then_normalizes]] → `calls` → [[graphify_graphify_ids_make_id]]
- [[graphify_tests_test_id_normalization_contract_test_both_callers_share_one_implementation]] → `indirect_call` → [[graphify_graphify_symbol_resolution_bash_make_id]]
- [[graphify_tests_test_id_normalization_contract]] → `contains` → [[graphify_tests_test_id_normalization_contract_test_both_callers_share_one_implementation]]
- [[graphify_tests_test_id_normalization_contract]] → `contains` → [[graphify_tests_test_id_normalization_contract_test_make_id_joins_then_normalizes]]
- [[graphify_tests_test_id_normalization_contract]] → `contains` → [[graphify_tests_test_id_normalization_contract_test_make_id_matches_normalize_id]]
- [[graphify_tests_test_id_normalization_contract]] → `contains` → [[graphify_tests_test_id_normalization_contract_test_normalize_id_is_idempotent]]
- [[graphify_tests_test_id_normalization_contract]] → `contains` → [[graphify_tests_test_id_normalization_contract_test_normalized_ids_are_safe_node_ids]]
- [[graphify_tests_test_id_normalization_contract]] → `contains` → [[graphify_tests_test_id_normalization_contract_test_property_make_id_equals_normalize_id]]
- [[graphify_tests_test_id_normalization_contract]] → `contains` → [[graphify_tests_test_id_normalization_contract_test_property_normalize_id_idempotent]]
- [[graphify_tests_test_id_normalization_contract]] → `contains` → [[graphify_tests_test_id_normalization_contract_test_unicode_identifiers_do_not_collapse_to_empty]]
- [[graphify_tests_test_id_normalization_contract_rationale_1]] → `rationale_for` → [[graphify_tests_test_id_normalization_contract]]
- [[graphify_tests_test_id_normalization_contract_rationale_47]] → `rationale_for` → [[graphify_tests_test_id_normalization_contract_test_make_id_matches_normalize_id]]
- [[graphify_tests_test_id_normalization_contract_rationale_61]] → `rationale_for` → [[graphify_tests_test_id_normalization_contract_test_make_id_joins_then_normalizes]]
- [[graphify_tests_test_id_normalization_contract_rationale_71]] → `rationale_for` → [[graphify_tests_test_id_normalization_contract_test_unicode_identifiers_do_not_collapse_to_empty]]
- [[graphify_tests_test_id_normalization_contract_rationale_79]] → `rationale_for` → [[graphify_tests_test_id_normalization_contract_test_normalized_ids_are_safe_node_ids]]
- [[graphify_tests_test_id_normalization_contract_rationale_88]] → `rationale_for` → [[graphify_tests_test_id_normalization_contract_test_both_callers_share_one_implementation]]