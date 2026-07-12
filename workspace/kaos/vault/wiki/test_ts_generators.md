# graphify\tests\test_ts_generators.py

## Símbolos

- [[graphify_tests_test_ts_generators]] — code: test_ts_generators.py
- [[graphify_tests_test_ts_generators_write]] — code: _write()
- [[graphify_tests_test_ts_generators_has_node]] — code: _has_node()
- [[graphify_tests_test_ts_generators_contains]] — code: _contains()
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_ts]] — code: test_generator_declaration_is_node_ts()
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_js]] — code: test_generator_declaration_is_node_js()
- [[graphify_tests_test_ts_generators_test_generator_expression_is_node]] — code: test_generator_expression_is_node()
- [[graphify_tests_test_ts_generators_test_generator_body_calls_are_attributed]] — code: test_generator_body_calls_are_attributed()
- [[graphify_tests_test_ts_generators_test_async_generator_declaration_is_node]] — code: test_async_generator_declaration_is_node()
- [[graphify_tests_test_ts_generators_rationale_1]] — code: Regression tests: TypeScript/JavaScript generator functions as nodes.  Before
- [[graphify_tests_test_ts_generators_rationale_56]] — code: A call inside a generator's body should be attributed to the generator,     pro

## Dependências

- [[graphify_tests_test_ts_generators]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_ts_generators_test_async_generator_declaration_is_node]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_generators_test_generator_body_calls_are_attributed]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_js]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_ts]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_generators_test_generator_expression_is_node]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_generators_contains]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_tests_test_ts_generators_has_node]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_tests_test_ts_generators_test_generator_body_calls_are_attributed]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_tests_test_ts_generators]] → `contains` → [[graphify_tests_test_ts_generators_contains]]
- [[graphify_tests_test_ts_generators]] → `contains` → [[graphify_tests_test_ts_generators_has_node]]
- [[graphify_tests_test_ts_generators]] → `contains` → [[graphify_tests_test_ts_generators_test_async_generator_declaration_is_node]]
- [[graphify_tests_test_ts_generators]] → `contains` → [[graphify_tests_test_ts_generators_test_generator_body_calls_are_attributed]]
- [[graphify_tests_test_ts_generators]] → `contains` → [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_js]]
- [[graphify_tests_test_ts_generators]] → `contains` → [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_ts]]
- [[graphify_tests_test_ts_generators]] → `contains` → [[graphify_tests_test_ts_generators_test_generator_expression_is_node]]
- [[graphify_tests_test_ts_generators]] → `contains` → [[graphify_tests_test_ts_generators_write]]
- [[graphify_tests_test_ts_generators_rationale_1]] → `rationale_for` → [[graphify_tests_test_ts_generators]]
- [[graphify_tests_test_ts_generators_test_async_generator_declaration_is_node]] → `calls` → [[graphify_tests_test_ts_generators_write]]
- [[graphify_tests_test_ts_generators_test_generator_body_calls_are_attributed]] → `calls` → [[graphify_tests_test_ts_generators_write]]
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_js]] → `calls` → [[graphify_tests_test_ts_generators_write]]
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_ts]] → `calls` → [[graphify_tests_test_ts_generators_write]]
- [[graphify_tests_test_ts_generators_test_generator_expression_is_node]] → `calls` → [[graphify_tests_test_ts_generators_write]]
- [[graphify_tests_test_ts_generators_write]] → `references` → [[graphify_tests_test_ts_generators_py_path]]
- [[graphify_tests_test_ts_generators_contains]] → `calls` → [[graphify_tests_test_ts_generators_py_path]]
- [[graphify_tests_test_ts_generators_has_node]] → `calls` → [[graphify_tests_test_ts_generators_py_path]]
- [[graphify_tests_test_ts_generators_test_generator_body_calls_are_attributed]] → `calls` → [[graphify_tests_test_ts_generators_py_path]]
- [[graphify_tests_test_ts_generators_test_async_generator_declaration_is_node]] → `calls` → [[graphify_tests_test_ts_generators_has_node]]
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_js]] → `calls` → [[graphify_tests_test_ts_generators_has_node]]
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_ts]] → `calls` → [[graphify_tests_test_ts_generators_has_node]]
- [[graphify_tests_test_ts_generators_test_generator_expression_is_node]] → `calls` → [[graphify_tests_test_ts_generators_has_node]]
- [[graphify_tests_test_ts_generators_test_generator_declaration_is_node_ts]] → `calls` → [[graphify_tests_test_ts_generators_contains]]
- [[graphify_tests_test_ts_generators_rationale_56]] → `rationale_for` → [[graphify_tests_test_ts_generators_test_generator_body_calls_are_attributed]]