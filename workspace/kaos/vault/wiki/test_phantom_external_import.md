# graphify\tests\test_phantom_external_import.py

## Símbolos

- [[graphify_tests_test_phantom_external_import]] — code: test_phantom_external_import.py
- [[graphify_tests_test_phantom_external_import_write]] — code: _write()
- [[graphify_tests_test_phantom_external_import_test_unresolved_bare_import_is_ref_namespaced]] — code: test_unresolved_bare_import_is_ref_namespaced()
- [[graphify_tests_test_phantom_external_import_test_scoped_package_import_is_ref_namespaced]] — code: test_scoped_package_import_is_ref_namespaced()
- [[graphify_tests_test_phantom_external_import_test_no_phantom_edge_from_tsx_to_unrelated_python_file]] — code: test_no_phantom_edge_from_tsx_to_unrelated_python_file()
- [[graphify_tests_test_phantom_external_import_test_multiple_tsx_files_do_not_all_alias_onto_one_python_file]] — code: test_multiple_tsx_files_do_not_all_alias_onto_one_python_file()
- [[graphify_tests_test_phantom_external_import_rationale_1]] — code: #1638 — an unresolved bare npm import must not alias onto an unrelated same-nam

## Dependências

- [[graphify_tests_test_phantom_external_import]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_phantom_external_import]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_phantom_external_import_test_multiple_tsx_files_do_not_all_alias_onto_one_python_file]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_phantom_external_import_test_no_phantom_edge_from_tsx_to_unrelated_python_file]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_phantom_external_import_test_scoped_package_import_is_ref_namespaced]] → `calls` → [[graphify_graphify_extractors_resolution_resolve_js_import_target]]
- [[graphify_tests_test_phantom_external_import_test_unresolved_bare_import_is_ref_namespaced]] → `calls` → [[graphify_graphify_extractors_resolution_resolve_js_import_target]]
- [[graphify_tests_test_phantom_external_import]] → `contains` → [[graphify_tests_test_phantom_external_import_test_multiple_tsx_files_do_not_all_alias_onto_one_python_file]]
- [[graphify_tests_test_phantom_external_import]] → `contains` → [[graphify_tests_test_phantom_external_import_test_no_phantom_edge_from_tsx_to_unrelated_python_file]]
- [[graphify_tests_test_phantom_external_import]] → `contains` → [[graphify_tests_test_phantom_external_import_test_scoped_package_import_is_ref_namespaced]]
- [[graphify_tests_test_phantom_external_import]] → `contains` → [[graphify_tests_test_phantom_external_import_test_unresolved_bare_import_is_ref_namespaced]]
- [[graphify_tests_test_phantom_external_import]] → `contains` → [[graphify_tests_test_phantom_external_import_write]]
- [[graphify_tests_test_phantom_external_import_rationale_1]] → `rationale_for` → [[graphify_tests_test_phantom_external_import]]
- [[graphify_tests_test_phantom_external_import_test_multiple_tsx_files_do_not_all_alias_onto_one_python_file]] → `calls` → [[graphify_tests_test_phantom_external_import_write]]
- [[graphify_tests_test_phantom_external_import_test_no_phantom_edge_from_tsx_to_unrelated_python_file]] → `calls` → [[graphify_tests_test_phantom_external_import_write]]
- [[graphify_tests_test_phantom_external_import_write]] → `references` → [[graphify_tests_test_phantom_external_import_py_path]]
- [[graphify_tests_test_phantom_external_import_test_multiple_tsx_files_do_not_all_alias_onto_one_python_file]] → `references` → [[graphify_tests_test_phantom_external_import_py_path]]
- [[graphify_tests_test_phantom_external_import_test_no_phantom_edge_from_tsx_to_unrelated_python_file]] → `references` → [[graphify_tests_test_phantom_external_import_py_path]]