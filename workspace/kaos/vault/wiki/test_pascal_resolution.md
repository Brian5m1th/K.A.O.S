# graphify\tests\test_pascal_resolution.py

## Símbolos

- [[graphify_tests_test_pascal_resolution]] — code: test_pascal_resolution.py
- [[graphify_tests_test_pascal_resolution_find_raw_call]] — code: _find_raw_call()
- [[graphify_tests_test_pascal_resolution_labels]] — code: _labels()
- [[graphify_tests_test_pascal_resolution_call_edge]] — code: _call_edge()
- [[graphify_tests_test_pascal_resolution_test_single_file_extraction_reports_unresolved_inherited_call]] — code: test_single_file_extraction_reports_unresolved_inherited_call()
- [[graphify_tests_test_pascal_resolution_test_calls_resolve_across_files_via_inherits_chain]] — code: test_calls_resolve_across_files_via_inherits_chain()
- [[graphify_tests_test_pascal_resolution_test_cross_file_calls_do_not_cross_unrelated_classes]] — code: test_cross_file_calls_do_not_cross_unrelated_classes()
- [[graphify_tests_test_pascal_resolution_test_pascal_resolver_registered]] — code: test_pascal_resolver_registered()
- [[graphify_tests_test_pascal_resolution_rationale_1]] — code: Tests for cross-file Pascal/Delphi inherited-method-call resolution.  The per-
- [[graphify_tests_test_pascal_resolution_rationale_57]] — code: Sanity check for the gap this resolver closes: the per-file extractor     alone
- [[graphify_tests_test_pascal_resolution_rationale_80]] — code: TDerivedGadget inherits only from TBaseGadget. TOtherGadget declares an     unr

## Dependências

- [[graphify_tests_test_pascal_resolution]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_pascal_resolution_test_calls_resolve_across_files_via_inherits_chain]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_pascal_resolution_test_cross_file_calls_do_not_cross_unrelated_classes]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_pascal_resolution_test_single_file_extraction_reports_unresolved_inherited_call]] → `calls` → [[graphify_graphify_extractors_pascal_extract_pascal]]
- [[graphify_tests_test_pascal_resolution_test_pascal_resolver_registered]] → `calls` → [[graphify_graphify_resolver_registry_registered_resolvers]]
- [[graphify_tests_test_pascal_resolution]] → `contains` → [[graphify_tests_test_pascal_resolution_call_edge]]
- [[graphify_tests_test_pascal_resolution]] → `contains` → [[graphify_tests_test_pascal_resolution_find_raw_call]]
- [[graphify_tests_test_pascal_resolution]] → `contains` → [[graphify_tests_test_pascal_resolution_labels]]
- [[graphify_tests_test_pascal_resolution]] → `contains` → [[graphify_tests_test_pascal_resolution_test_calls_resolve_across_files_via_inherits_chain]]
- [[graphify_tests_test_pascal_resolution]] → `contains` → [[graphify_tests_test_pascal_resolution_test_cross_file_calls_do_not_cross_unrelated_classes]]
- [[graphify_tests_test_pascal_resolution]] → `contains` → [[graphify_tests_test_pascal_resolution_test_pascal_resolver_registered]]
- [[graphify_tests_test_pascal_resolution]] → `contains` → [[graphify_tests_test_pascal_resolution_test_single_file_extraction_reports_unresolved_inherited_call]]
- [[graphify_tests_test_pascal_resolution_rationale_1]] → `rationale_for` → [[graphify_tests_test_pascal_resolution]]
- [[graphify_tests_test_pascal_resolution_test_single_file_extraction_reports_unresolved_inherited_call]] → `calls` → [[graphify_tests_test_pascal_resolution_find_raw_call]]
- [[graphify_tests_test_pascal_resolution_call_edge]] → `calls` → [[graphify_tests_test_pascal_resolution_labels]]
- [[graphify_tests_test_pascal_resolution_test_calls_resolve_across_files_via_inherits_chain]] → `calls` → [[graphify_tests_test_pascal_resolution_call_edge]]
- [[graphify_tests_test_pascal_resolution_test_cross_file_calls_do_not_cross_unrelated_classes]] → `calls` → [[graphify_tests_test_pascal_resolution_call_edge]]
- [[graphify_tests_test_pascal_resolution_test_single_file_extraction_reports_unresolved_inherited_call]] → `calls` → [[graphify_tests_test_pascal_resolution_call_edge]]
- [[graphify_tests_test_pascal_resolution_rationale_57]] → `rationale_for` → [[graphify_tests_test_pascal_resolution_test_single_file_extraction_reports_unresolved_inherited_call]]
- [[graphify_tests_test_pascal_resolution_rationale_80]] → `rationale_for` → [[graphify_tests_test_pascal_resolution_test_cross_file_calls_do_not_cross_unrelated_classes]]