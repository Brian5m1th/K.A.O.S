# graphify\tests\test_ts_namespace.py

## Símbolos

- [[graphify_tests_test_ts_namespace]] — code: test_ts_namespace.py
- [[graphify_tests_test_ts_namespace_write]] — code: _write()
- [[graphify_tests_test_ts_namespace_node_label]] — code: _node_label()
- [[graphify_tests_test_ts_namespace_has_node]] — code: _has_node()
- [[graphify_tests_test_ts_namespace_test_namespace_is_node]] — code: test_namespace_is_node()
- [[graphify_tests_test_ts_namespace_test_module_keyword_is_node]] — code: test_module_keyword_is_node()
- [[graphify_tests_test_ts_namespace_test_nested_namespace_name]] — code: test_nested_namespace_name()
- [[graphify_tests_test_ts_namespace_test_namespace_members_still_extracted]] — code: test_namespace_members_still_extracted()
- [[graphify_tests_test_ts_namespace_test_ambient_string_module_quotes_stripped]] — code: test_ambient_string_module_quotes_stripped()
- [[graphify_tests_test_ts_namespace_test_namespace_node_not_emitted_in_js]] — code: test_namespace_node_not_emitted_in_js()
- [[graphify_tests_test_ts_namespace_rationale_1]] — code: Regression tests: TypeScript namespace/module container nodes.  `namespace Foo
- [[graphify_tests_test_ts_namespace_rationale_50]] — code: The container node must not cost us the members the default recurse reached.
- [[graphify_tests_test_ts_namespace_rationale_70]] — code: The handler is TS-only; plain JS has no namespace syntax to confuse it.

## Dependências

- [[graphify_tests_test_ts_namespace]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_ts_namespace_test_ambient_string_module_quotes_stripped]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_namespace_test_module_keyword_is_node]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_namespace_test_namespace_is_node]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_namespace_test_namespace_members_still_extracted]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_namespace_test_namespace_node_not_emitted_in_js]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_namespace_test_nested_namespace_name]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_namespace_node_label]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_has_node]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_node_label]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_test_ambient_string_module_quotes_stripped]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_test_module_keyword_is_node]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_test_namespace_is_node]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_test_namespace_members_still_extracted]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_test_namespace_node_not_emitted_in_js]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_test_nested_namespace_name]]
- [[graphify_tests_test_ts_namespace]] → `contains` → [[graphify_tests_test_ts_namespace_write]]
- [[graphify_tests_test_ts_namespace_rationale_1]] → `rationale_for` → [[graphify_tests_test_ts_namespace]]
- [[graphify_tests_test_ts_namespace_test_ambient_string_module_quotes_stripped]] → `calls` → [[graphify_tests_test_ts_namespace_write]]
- [[graphify_tests_test_ts_namespace_test_module_keyword_is_node]] → `calls` → [[graphify_tests_test_ts_namespace_write]]
- [[graphify_tests_test_ts_namespace_test_namespace_is_node]] → `calls` → [[graphify_tests_test_ts_namespace_write]]
- [[graphify_tests_test_ts_namespace_test_namespace_members_still_extracted]] → `calls` → [[graphify_tests_test_ts_namespace_write]]
- [[graphify_tests_test_ts_namespace_test_namespace_node_not_emitted_in_js]] → `calls` → [[graphify_tests_test_ts_namespace_write]]
- [[graphify_tests_test_ts_namespace_test_nested_namespace_name]] → `calls` → [[graphify_tests_test_ts_namespace_write]]
- [[graphify_tests_test_ts_namespace_write]] → `references` → [[graphify_tests_test_ts_namespace_py_path]]
- [[graphify_tests_test_ts_namespace_node_label]] → `calls` → [[graphify_tests_test_ts_namespace_py_path]]
- [[graphify_tests_test_ts_namespace_has_node]] → `calls` → [[graphify_tests_test_ts_namespace_node_label]]
- [[graphify_tests_test_ts_namespace_test_ambient_string_module_quotes_stripped]] → `calls` → [[graphify_tests_test_ts_namespace_node_label]]
- [[graphify_tests_test_ts_namespace_test_nested_namespace_name]] → `calls` → [[graphify_tests_test_ts_namespace_node_label]]
- [[graphify_tests_test_ts_namespace_test_module_keyword_is_node]] → `calls` → [[graphify_tests_test_ts_namespace_has_node]]
- [[graphify_tests_test_ts_namespace_test_namespace_is_node]] → `calls` → [[graphify_tests_test_ts_namespace_has_node]]
- [[graphify_tests_test_ts_namespace_test_namespace_members_still_extracted]] → `calls` → [[graphify_tests_test_ts_namespace_has_node]]
- [[graphify_tests_test_ts_namespace_test_namespace_node_not_emitted_in_js]] → `calls` → [[graphify_tests_test_ts_namespace_has_node]]
- [[graphify_tests_test_ts_namespace_rationale_50]] → `rationale_for` → [[graphify_tests_test_ts_namespace_test_namespace_members_still_extracted]]
- [[graphify_tests_test_ts_namespace_rationale_70]] → `rationale_for` → [[graphify_tests_test_ts_namespace_test_namespace_node_not_emitted_in_js]]