# graphify\tests\test_phantom_cross_package_call.py

## Símbolos

- [[graphify_tests_test_phantom_cross_package_call]] — code: test_phantom_cross_package_call.py
- [[graphify_tests_test_phantom_cross_package_call_write]] — code: _write()
- [[graphify_tests_test_phantom_cross_package_call_calls]] — code: _calls()
- [[graphify_tests_test_phantom_cross_package_call_test_unimported_cross_package_call_emits_no_edge]] — code: test_unimported_cross_package_call_emits_no_edge()
- [[graphify_tests_test_phantom_cross_package_call_test_many_files_do_not_collapse_onto_one_export]] — code: test_many_files_do_not_collapse_onto_one_export()
- [[graphify_tests_test_phantom_cross_package_call_test_imported_cross_file_call_still_resolves]] — code: test_imported_cross_file_call_still_resolves()
- [[graphify_tests_test_phantom_cross_package_call_test_same_file_call_unaffected]] — code: test_same_file_call_unaffected()
- [[graphify_tests_test_phantom_cross_package_call_test_non_js_single_candidate_cross_file_still_resolves]] — code: test_non_js_single_candidate_cross_file_still_resolves()
- [[graphify_tests_test_phantom_cross_package_call_rationale_1]] — code: #1659 — a JS/TS call with no local definition and no import must not bind to a

## Dependências

- [[graphify_tests_test_phantom_cross_package_call]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_phantom_cross_package_call_calls]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_phantom_cross_package_call]] → `contains` → [[graphify_tests_test_phantom_cross_package_call_calls]]
- [[graphify_tests_test_phantom_cross_package_call]] → `contains` → [[graphify_tests_test_phantom_cross_package_call_test_imported_cross_file_call_still_resolves]]
- [[graphify_tests_test_phantom_cross_package_call]] → `contains` → [[graphify_tests_test_phantom_cross_package_call_test_many_files_do_not_collapse_onto_one_export]]
- [[graphify_tests_test_phantom_cross_package_call]] → `contains` → [[graphify_tests_test_phantom_cross_package_call_test_non_js_single_candidate_cross_file_still_resolves]]
- [[graphify_tests_test_phantom_cross_package_call]] → `contains` → [[graphify_tests_test_phantom_cross_package_call_test_same_file_call_unaffected]]
- [[graphify_tests_test_phantom_cross_package_call]] → `contains` → [[graphify_tests_test_phantom_cross_package_call_test_unimported_cross_package_call_emits_no_edge]]
- [[graphify_tests_test_phantom_cross_package_call]] → `contains` → [[graphify_tests_test_phantom_cross_package_call_write]]
- [[graphify_tests_test_phantom_cross_package_call_rationale_1]] → `rationale_for` → [[graphify_tests_test_phantom_cross_package_call]]
- [[graphify_tests_test_phantom_cross_package_call_test_imported_cross_file_call_still_resolves]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_write]]
- [[graphify_tests_test_phantom_cross_package_call_test_many_files_do_not_collapse_onto_one_export]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_write]]
- [[graphify_tests_test_phantom_cross_package_call_test_non_js_single_candidate_cross_file_still_resolves]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_write]]
- [[graphify_tests_test_phantom_cross_package_call_test_same_file_call_unaffected]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_write]]
- [[graphify_tests_test_phantom_cross_package_call_test_unimported_cross_package_call_emits_no_edge]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_write]]
- [[graphify_tests_test_phantom_cross_package_call_write]] → `references` → [[graphify_tests_test_phantom_cross_package_call_py_path]]
- [[graphify_tests_test_phantom_cross_package_call_calls]] → `references` → [[graphify_tests_test_phantom_cross_package_call_py_path]]
- [[graphify_tests_test_phantom_cross_package_call_test_imported_cross_file_call_still_resolves]] → `references` → [[graphify_tests_test_phantom_cross_package_call_py_path]]
- [[graphify_tests_test_phantom_cross_package_call_test_many_files_do_not_collapse_onto_one_export]] → `references` → [[graphify_tests_test_phantom_cross_package_call_py_path]]
- [[graphify_tests_test_phantom_cross_package_call_test_non_js_single_candidate_cross_file_still_resolves]] → `references` → [[graphify_tests_test_phantom_cross_package_call_py_path]]
- [[graphify_tests_test_phantom_cross_package_call_test_same_file_call_unaffected]] → `references` → [[graphify_tests_test_phantom_cross_package_call_py_path]]
- [[graphify_tests_test_phantom_cross_package_call_test_unimported_cross_package_call_emits_no_edge]] → `references` → [[graphify_tests_test_phantom_cross_package_call_py_path]]
- [[graphify_tests_test_phantom_cross_package_call_test_imported_cross_file_call_still_resolves]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_calls]]
- [[graphify_tests_test_phantom_cross_package_call_test_many_files_do_not_collapse_onto_one_export]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_calls]]
- [[graphify_tests_test_phantom_cross_package_call_test_non_js_single_candidate_cross_file_still_resolves]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_calls]]
- [[graphify_tests_test_phantom_cross_package_call_test_same_file_call_unaffected]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_calls]]
- [[graphify_tests_test_phantom_cross_package_call_test_unimported_cross_package_call_emits_no_edge]] → `calls` → [[graphify_tests_test_phantom_cross_package_call_calls]]