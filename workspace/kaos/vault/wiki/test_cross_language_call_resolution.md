# graphify\tests\test_cross_language_call_resolution.py

## Símbolos

- [[graphify_tests_test_cross_language_call_resolution]] — code: test_cross_language_call_resolution.py
- [[graphify_tests_test_cross_language_call_resolution_write]] — code: _write()
- [[graphify_tests_test_cross_language_call_resolution_call_edges]] — code: _call_edges()
- [[graphify_tests_test_cross_language_call_resolution_test_tsx_callback_does_not_bind_to_kotlin_method]] — code: test_tsx_callback_does_not_bind_to_kotlin_method()
- [[graphify_tests_test_cross_language_call_resolution_test_python_call_does_not_bind_to_kotlin_function]] — code: test_python_call_does_not_bind_to_kotlin_function()
- [[graphify_tests_test_cross_language_call_resolution_test_same_language_callback_still_resolves]] — code: test_same_language_callback_still_resolves()
- [[graphify_tests_test_cross_language_call_resolution_test_jvm_interop_kotlin_call_to_java_still_resolves]] — code: test_jvm_interop_kotlin_call_to_java_still_resolves()
- [[graphify_tests_test_cross_language_call_resolution_rationale_1]] — code: Cross-language call resolution — a call in one language must never bind by name

## Dependências

- [[graphify_tests_test_cross_language_call_resolution]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_cross_language_call_resolution_call_edges]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_cross_language_call_resolution]] → `contains` → [[graphify_tests_test_cross_language_call_resolution_call_edges]]
- [[graphify_tests_test_cross_language_call_resolution]] → `contains` → [[graphify_tests_test_cross_language_call_resolution_test_jvm_interop_kotlin_call_to_java_still_resolves]]
- [[graphify_tests_test_cross_language_call_resolution]] → `contains` → [[graphify_tests_test_cross_language_call_resolution_test_python_call_does_not_bind_to_kotlin_function]]
- [[graphify_tests_test_cross_language_call_resolution]] → `contains` → [[graphify_tests_test_cross_language_call_resolution_test_same_language_callback_still_resolves]]
- [[graphify_tests_test_cross_language_call_resolution]] → `contains` → [[graphify_tests_test_cross_language_call_resolution_test_tsx_callback_does_not_bind_to_kotlin_method]]
- [[graphify_tests_test_cross_language_call_resolution]] → `contains` → [[graphify_tests_test_cross_language_call_resolution_write]]
- [[graphify_tests_test_cross_language_call_resolution_rationale_1]] → `rationale_for` → [[graphify_tests_test_cross_language_call_resolution]]
- [[graphify_tests_test_cross_language_call_resolution_test_jvm_interop_kotlin_call_to_java_still_resolves]] → `calls` → [[graphify_tests_test_cross_language_call_resolution_write]]
- [[graphify_tests_test_cross_language_call_resolution_test_python_call_does_not_bind_to_kotlin_function]] → `calls` → [[graphify_tests_test_cross_language_call_resolution_write]]
- [[graphify_tests_test_cross_language_call_resolution_test_same_language_callback_still_resolves]] → `calls` → [[graphify_tests_test_cross_language_call_resolution_write]]
- [[graphify_tests_test_cross_language_call_resolution_test_tsx_callback_does_not_bind_to_kotlin_method]] → `calls` → [[graphify_tests_test_cross_language_call_resolution_write]]
- [[graphify_tests_test_cross_language_call_resolution_write]] → `references` → [[graphify_tests_test_cross_language_call_resolution_py_path]]
- [[graphify_tests_test_cross_language_call_resolution_call_edges]] → `references` → [[graphify_tests_test_cross_language_call_resolution_py_path]]
- [[graphify_tests_test_cross_language_call_resolution_test_jvm_interop_kotlin_call_to_java_still_resolves]] → `references` → [[graphify_tests_test_cross_language_call_resolution_py_path]]
- [[graphify_tests_test_cross_language_call_resolution_test_python_call_does_not_bind_to_kotlin_function]] → `references` → [[graphify_tests_test_cross_language_call_resolution_py_path]]
- [[graphify_tests_test_cross_language_call_resolution_test_same_language_callback_still_resolves]] → `references` → [[graphify_tests_test_cross_language_call_resolution_py_path]]
- [[graphify_tests_test_cross_language_call_resolution_test_tsx_callback_does_not_bind_to_kotlin_method]] → `references` → [[graphify_tests_test_cross_language_call_resolution_py_path]]
- [[graphify_tests_test_cross_language_call_resolution_test_jvm_interop_kotlin_call_to_java_still_resolves]] → `calls` → [[graphify_tests_test_cross_language_call_resolution_call_edges]]
- [[graphify_tests_test_cross_language_call_resolution_test_python_call_does_not_bind_to_kotlin_function]] → `calls` → [[graphify_tests_test_cross_language_call_resolution_call_edges]]
- [[graphify_tests_test_cross_language_call_resolution_test_same_language_callback_still_resolves]] → `calls` → [[graphify_tests_test_cross_language_call_resolution_call_edges]]
- [[graphify_tests_test_cross_language_call_resolution_test_tsx_callback_does_not_bind_to_kotlin_method]] → `calls` → [[graphify_tests_test_cross_language_call_resolution_call_edges]]