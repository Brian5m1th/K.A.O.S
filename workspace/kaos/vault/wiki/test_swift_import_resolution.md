# graphify\tests\test_swift_import_resolution.py

## Símbolos

- [[graphify_tests_test_swift_import_resolution]] — code: test_swift_import_resolution.py
- [[graphify_tests_test_swift_import_resolution_write]] — code: _write()
- [[graphify_tests_test_swift_import_resolution_module_nodes]] — code: _module_nodes()
- [[graphify_tests_test_swift_import_resolution_import_edges]] — code: _import_edges()
- [[graphify_tests_test_swift_import_resolution_test_swift_import_resolves_to_module_node]] — code: test_swift_import_resolves_to_module_node()
- [[graphify_tests_test_swift_import_resolution_test_swift_same_module_imported_twice_collapses_to_one_node]] — code: test_swift_same_module_imported_twice_collapses_to_one_node()
- [[graphify_tests_test_swift_import_resolution_test_swift_import_edges_survive_build]] — code: test_swift_import_edges_survive_build()

## Dependências

- [[graphify_tests_test_swift_import_resolution]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_swift_import_resolution]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_swift_import_resolution_test_swift_import_edges_survive_build]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_swift_import_resolution_test_swift_import_resolves_to_module_node]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_swift_import_resolution_test_swift_same_module_imported_twice_collapses_to_one_node]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_swift_import_resolution]] → `contains` → [[graphify_tests_test_swift_import_resolution_import_edges]]
- [[graphify_tests_test_swift_import_resolution]] → `contains` → [[graphify_tests_test_swift_import_resolution_module_nodes]]
- [[graphify_tests_test_swift_import_resolution]] → `contains` → [[graphify_tests_test_swift_import_resolution_test_swift_import_edges_survive_build]]
- [[graphify_tests_test_swift_import_resolution]] → `contains` → [[graphify_tests_test_swift_import_resolution_test_swift_import_resolves_to_module_node]]
- [[graphify_tests_test_swift_import_resolution]] → `contains` → [[graphify_tests_test_swift_import_resolution_test_swift_same_module_imported_twice_collapses_to_one_node]]
- [[graphify_tests_test_swift_import_resolution]] → `contains` → [[graphify_tests_test_swift_import_resolution_write]]
- [[graphify_tests_test_swift_import_resolution_test_swift_import_edges_survive_build]] → `calls` → [[graphify_tests_test_swift_import_resolution_write]]
- [[graphify_tests_test_swift_import_resolution_test_swift_import_resolves_to_module_node]] → `calls` → [[graphify_tests_test_swift_import_resolution_write]]
- [[graphify_tests_test_swift_import_resolution_test_swift_same_module_imported_twice_collapses_to_one_node]] → `calls` → [[graphify_tests_test_swift_import_resolution_write]]
- [[graphify_tests_test_swift_import_resolution_write]] → `references` → [[graphify_tests_test_swift_import_resolution_py_path]]
- [[graphify_tests_test_swift_import_resolution_test_swift_import_edges_survive_build]] → `references` → [[graphify_tests_test_swift_import_resolution_py_path]]
- [[graphify_tests_test_swift_import_resolution_test_swift_import_resolves_to_module_node]] → `references` → [[graphify_tests_test_swift_import_resolution_py_path]]
- [[graphify_tests_test_swift_import_resolution_test_swift_same_module_imported_twice_collapses_to_one_node]] → `references` → [[graphify_tests_test_swift_import_resolution_py_path]]
- [[graphify_tests_test_swift_import_resolution_test_swift_import_resolves_to_module_node]] → `calls` → [[graphify_tests_test_swift_import_resolution_module_nodes]]
- [[graphify_tests_test_swift_import_resolution_test_swift_same_module_imported_twice_collapses_to_one_node]] → `calls` → [[graphify_tests_test_swift_import_resolution_module_nodes]]
- [[graphify_tests_test_swift_import_resolution_test_swift_import_resolves_to_module_node]] → `calls` → [[graphify_tests_test_swift_import_resolution_import_edges]]
- [[graphify_tests_test_swift_import_resolution_test_swift_same_module_imported_twice_collapses_to_one_node]] → `calls` → [[graphify_tests_test_swift_import_resolution_import_edges]]