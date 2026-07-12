# graphify\tests\test_python_import_resolution.py

## Símbolos

- [[graphify_tests_test_python_import_resolution]] — code: test_python_import_resolution.py
- [[graphify_tests_test_python_import_resolution_write]] — code: _write()
- [[graphify_tests_test_python_import_resolution_node_id]] — code: _node_id()
- [[graphify_tests_test_python_import_resolution_has_edge]] — code: _has_edge()
- [[graphify_tests_test_python_import_resolution_test_python_package_reexport_resolves_import_and_call_to_origin_symbol]] — code: test_python_package_reexport_resolves_import_and_call_to_origin_symbol()
- [[graphify_tests_test_python_import_resolution_test_python_parameter_return_and_generic_contexts]] — code: test_python_parameter_return_and_generic_contexts()

## Dependências

- [[graphify_tests_test_python_import_resolution]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_python_import_resolution_test_python_package_reexport_resolves_import_and_call_to_origin_symbol]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_python_import_resolution_test_python_parameter_return_and_generic_contexts]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_python_import_resolution]] → `contains` → [[graphify_tests_test_python_import_resolution_has_edge]]
- [[graphify_tests_test_python_import_resolution]] → `contains` → [[graphify_tests_test_python_import_resolution_node_id]]
- [[graphify_tests_test_python_import_resolution]] → `contains` → [[graphify_tests_test_python_import_resolution_test_python_package_reexport_resolves_import_and_call_to_origin_symbol]]
- [[graphify_tests_test_python_import_resolution]] → `contains` → [[graphify_tests_test_python_import_resolution_test_python_parameter_return_and_generic_contexts]]
- [[graphify_tests_test_python_import_resolution]] → `contains` → [[graphify_tests_test_python_import_resolution_write]]
- [[graphify_tests_test_python_import_resolution_test_python_package_reexport_resolves_import_and_call_to_origin_symbol]] → `calls` → [[graphify_tests_test_python_import_resolution_write]]
- [[graphify_tests_test_python_import_resolution_write]] → `references` → [[graphify_tests_test_python_import_resolution_py_path]]
- [[graphify_tests_test_python_import_resolution_test_python_package_reexport_resolves_import_and_call_to_origin_symbol]] → `references` → [[graphify_tests_test_python_import_resolution_py_path]]
- [[graphify_tests_test_python_import_resolution_test_python_parameter_return_and_generic_contexts]] → `references` → [[graphify_tests_test_python_import_resolution_py_path]]
- [[graphify_tests_test_python_import_resolution_test_python_package_reexport_resolves_import_and_call_to_origin_symbol]] → `calls` → [[graphify_tests_test_python_import_resolution_node_id]]
- [[graphify_tests_test_python_import_resolution_test_python_package_reexport_resolves_import_and_call_to_origin_symbol]] → `calls` → [[graphify_tests_test_python_import_resolution_has_edge]]