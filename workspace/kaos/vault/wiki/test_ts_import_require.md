# graphify\tests\test_ts_import_require.py

## Símbolos

- [[graphify_tests_test_ts_import_require]] — code: test_ts_import_require.py
- [[graphify_tests_test_ts_import_require_write]] — code: _write()
- [[graphify_tests_test_ts_import_require_has_edge]] — code: _has_edge()
- [[graphify_tests_test_ts_import_require_test_import_require_relative_emits_file_edge]] — code: test_import_require_relative_emits_file_edge()
- [[graphify_tests_test_ts_import_require_test_import_require_single_quotes]] — code: test_import_require_single_quotes()
- [[graphify_tests_test_ts_import_require_test_import_require_bare_module_targets_ref_stub]] — code: test_import_require_bare_module_targets_ref_stub()
- [[graphify_tests_test_ts_import_require_test_import_require_parity_with_namespace_import]] — code: test_import_require_parity_with_namespace_import()
- [[graphify_tests_test_ts_import_require_test_esm_imports_unaffected]] — code: test_esm_imports_unaffected()
- [[graphify_tests_test_ts_import_require_rationale_1]] — code: Regression tests for the TypeScript import-equals form: `import x = require("./m
- [[graphify_tests_test_ts_import_require_rationale_82]] — code: `import x = require("./m")` must produce the same file-level edge as     `impor
- [[graphify_tests_test_ts_import_require_rationale_103]] — code: Regression guard: the restructured string scan must not change ESM handling

## Dependências

- [[graphify_tests_test_ts_import_require]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_ts_import_require_has_edge]] → `calls` → [[graphify_graphify_extract_file_node_id]]
- [[graphify_tests_test_ts_import_require_test_esm_imports_unaffected]] → `calls` → [[graphify_graphify_extract_file_node_id]]
- [[graphify_tests_test_ts_import_require_test_import_require_bare_module_targets_ref_stub]] → `calls` → [[graphify_graphify_extract_file_node_id]]
- [[graphify_tests_test_ts_import_require_test_esm_imports_unaffected]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_import_require_test_import_require_bare_module_targets_ref_stub]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_import_require_test_import_require_parity_with_namespace_import]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_import_require_test_import_require_relative_emits_file_edge]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_import_require_test_import_require_single_quotes]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_import_require]] → `contains` → [[graphify_tests_test_ts_import_require_has_edge]]
- [[graphify_tests_test_ts_import_require]] → `contains` → [[graphify_tests_test_ts_import_require_test_esm_imports_unaffected]]
- [[graphify_tests_test_ts_import_require]] → `contains` → [[graphify_tests_test_ts_import_require_test_import_require_bare_module_targets_ref_stub]]
- [[graphify_tests_test_ts_import_require]] → `contains` → [[graphify_tests_test_ts_import_require_test_import_require_parity_with_namespace_import]]
- [[graphify_tests_test_ts_import_require]] → `contains` → [[graphify_tests_test_ts_import_require_test_import_require_relative_emits_file_edge]]
- [[graphify_tests_test_ts_import_require]] → `contains` → [[graphify_tests_test_ts_import_require_test_import_require_single_quotes]]
- [[graphify_tests_test_ts_import_require]] → `contains` → [[graphify_tests_test_ts_import_require_write]]
- [[graphify_tests_test_ts_import_require_rationale_1]] → `rationale_for` → [[graphify_tests_test_ts_import_require]]
- [[graphify_tests_test_ts_import_require_test_esm_imports_unaffected]] → `calls` → [[graphify_tests_test_ts_import_require_write]]
- [[graphify_tests_test_ts_import_require_test_import_require_bare_module_targets_ref_stub]] → `calls` → [[graphify_tests_test_ts_import_require_write]]
- [[graphify_tests_test_ts_import_require_test_import_require_parity_with_namespace_import]] → `calls` → [[graphify_tests_test_ts_import_require_write]]
- [[graphify_tests_test_ts_import_require_test_import_require_relative_emits_file_edge]] → `calls` → [[graphify_tests_test_ts_import_require_write]]
- [[graphify_tests_test_ts_import_require_test_import_require_single_quotes]] → `calls` → [[graphify_tests_test_ts_import_require_write]]
- [[graphify_tests_test_ts_import_require_write]] → `references` → [[graphify_tests_test_ts_import_require_py_path]]
- [[graphify_tests_test_ts_import_require_has_edge]] → `calls` → [[graphify_tests_test_ts_import_require_py_path]]
- [[graphify_tests_test_ts_import_require_test_esm_imports_unaffected]] → `references` → [[graphify_tests_test_ts_import_require_py_path]]
- [[graphify_tests_test_ts_import_require_test_import_require_bare_module_targets_ref_stub]] → `references` → [[graphify_tests_test_ts_import_require_py_path]]
- [[graphify_tests_test_ts_import_require_test_import_require_parity_with_namespace_import]] → `references` → [[graphify_tests_test_ts_import_require_py_path]]
- [[graphify_tests_test_ts_import_require_test_import_require_relative_emits_file_edge]] → `references` → [[graphify_tests_test_ts_import_require_py_path]]
- [[graphify_tests_test_ts_import_require_test_import_require_single_quotes]] → `references` → [[graphify_tests_test_ts_import_require_py_path]]
- [[graphify_tests_test_ts_import_require_test_esm_imports_unaffected]] → `calls` → [[graphify_tests_test_ts_import_require_has_edge]]
- [[graphify_tests_test_ts_import_require_test_import_require_parity_with_namespace_import]] → `calls` → [[graphify_tests_test_ts_import_require_has_edge]]
- [[graphify_tests_test_ts_import_require_test_import_require_relative_emits_file_edge]] → `calls` → [[graphify_tests_test_ts_import_require_has_edge]]
- [[graphify_tests_test_ts_import_require_test_import_require_single_quotes]] → `calls` → [[graphify_tests_test_ts_import_require_has_edge]]
- [[graphify_tests_test_ts_import_require_rationale_82]] → `rationale_for` → [[graphify_tests_test_ts_import_require_test_import_require_parity_with_namespace_import]]
- [[graphify_tests_test_ts_import_require_rationale_103]] → `rationale_for` → [[graphify_tests_test_ts_import_require_test_esm_imports_unaffected]]