# graphify\tests\test_extraction_spec_ids.py

## Símbolos

- [[graphify_tests_test_extraction_spec_ids]] — code: test_extraction_spec_ids.py
- [[graphify_tests_test_extraction_spec_ids_spec_files]] — code: _spec_files()
- [[graphify_tests_test_extraction_spec_ids_examples]] — code: _examples()
- [[graphify_tests_test_extraction_spec_ids_ast_symbol_id]] — code: _ast_symbol_id()
- [[graphify_tests_test_extraction_spec_ids_test_spec_files_are_discoverable]] — code: test_spec_files_are_discoverable()
- [[graphify_tests_test_extraction_spec_ids_test_spec_node_id_examples_match_ast_extractor]] — code: test_spec_node_id_examples_match_ast_extractor()
- [[graphify_tests_test_extraction_spec_ids_test_cautionary_wrong_forms_are_actually_wrong]] — code: test_cautionary_wrong_forms_are_actually_wrong()
- [[graphify_tests_test_extraction_spec_ids_rationale_1]] — code: Drift guard for the node-ID spec shown to LLM semantic subagents.  `tools/skil
- [[graphify_tests_test_extraction_spec_ids_rationale_57]] — code: Reproduce the symbol ID the AST extractor emits for a file + symbol, using
- [[graphify_tests_test_extraction_spec_ids_rationale_63]] — code: Guard the guard: if the spec moves or the example format changes so nothing
- [[graphify_tests_test_extraction_spec_ids_rationale_89]] — code: The canonical spec warns against the filename-only and full-path ID forms.

## Dependências

- [[graphify_tests_test_extraction_spec_ids]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_extraction_spec_ids_ast_symbol_id]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_tests_test_extraction_spec_ids]] → `contains` → [[graphify_tests_test_extraction_spec_ids_ast_symbol_id]]
- [[graphify_tests_test_extraction_spec_ids]] → `contains` → [[graphify_tests_test_extraction_spec_ids_examples]]
- [[graphify_tests_test_extraction_spec_ids]] → `contains` → [[graphify_tests_test_extraction_spec_ids_spec_files]]
- [[graphify_tests_test_extraction_spec_ids]] → `contains` → [[graphify_tests_test_extraction_spec_ids_test_cautionary_wrong_forms_are_actually_wrong]]
- [[graphify_tests_test_extraction_spec_ids]] → `contains` → [[graphify_tests_test_extraction_spec_ids_test_spec_files_are_discoverable]]
- [[graphify_tests_test_extraction_spec_ids]] → `contains` → [[graphify_tests_test_extraction_spec_ids_test_spec_node_id_examples_match_ast_extractor]]
- [[graphify_tests_test_extraction_spec_ids_rationale_1]] → `rationale_for` → [[graphify_tests_test_extraction_spec_ids]]
- [[graphify_tests_test_extraction_spec_ids_examples]] → `calls` → [[graphify_tests_test_extraction_spec_ids_spec_files]]
- [[graphify_tests_test_extraction_spec_ids_spec_files]] → `references` → [[graphify_tests_test_extraction_spec_ids_py_path]]
- [[graphify_tests_test_extraction_spec_ids_test_spec_files_are_discoverable]] → `calls` → [[graphify_tests_test_extraction_spec_ids_spec_files]]
- [[graphify_tests_test_extraction_spec_ids_ast_symbol_id]] → `calls` → [[graphify_tests_test_extraction_spec_ids_py_path]]
- [[graphify_tests_test_extraction_spec_ids_examples]] → `references` → [[graphify_tests_test_extraction_spec_ids_py_path]]
- [[graphify_tests_test_extraction_spec_ids_test_spec_files_are_discoverable]] → `calls` → [[graphify_tests_test_extraction_spec_ids_examples]]
- [[graphify_tests_test_extraction_spec_ids_rationale_57]] → `rationale_for` → [[graphify_tests_test_extraction_spec_ids_ast_symbol_id]]
- [[graphify_tests_test_extraction_spec_ids_test_cautionary_wrong_forms_are_actually_wrong]] → `calls` → [[graphify_tests_test_extraction_spec_ids_ast_symbol_id]]
- [[graphify_tests_test_extraction_spec_ids_test_spec_node_id_examples_match_ast_extractor]] → `calls` → [[graphify_tests_test_extraction_spec_ids_ast_symbol_id]]
- [[graphify_tests_test_extraction_spec_ids_rationale_63]] → `rationale_for` → [[graphify_tests_test_extraction_spec_ids_test_spec_files_are_discoverable]]
- [[graphify_tests_test_extraction_spec_ids_rationale_89]] → `rationale_for` → [[graphify_tests_test_extraction_spec_ids_test_cautionary_wrong_forms_are_actually_wrong]]