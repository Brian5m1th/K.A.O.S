# graphify\tests\test_file_node_id_spec.py

## Símbolos

- [[graphify_tests_test_file_node_id_spec]] — code: test_file_node_id_spec.py
- [[graphify_tests_test_file_node_id_spec_file_nodes]] — code: _file_nodes()
- [[graphify_tests_test_file_node_id_spec_test_file_node_id_uses_parent_dir_and_stem_no_extension]] — code: test_file_node_id_uses_parent_dir_and_stem_no_extension()
- [[graphify_tests_test_file_node_id_spec_test_top_level_file_node_id_is_bare_stem]] — code: test_top_level_file_node_id_is_bare_stem()
- [[graphify_tests_test_file_node_id_spec_test_top_level_file_symbol_ids_use_bare_stem]] — code: test_top_level_file_SYMBOL_ids_use_bare_stem()
- [[graphify_tests_test_file_node_id_spec_test_nested_file_symbol_ids_unchanged]] — code: test_nested_file_symbol_ids_unchanged()
- [[graphify_tests_test_file_node_id_spec_test_symbol_and_file_ids_share_the_same_stem]] — code: test_symbol_and_file_ids_share_the_same_stem()
- [[graphify_tests_test_file_node_id_spec_test_cross_file_import_edges_stay_connected]] — code: test_cross_file_import_edges_stay_connected()
- [[graphify_tests_test_file_node_id_spec_rationale_1]] — code: Regression tests for issue #1033: AST file-level node IDs must match the skill.
- [[graphify_tests_test_file_node_id_spec_rationale_28]] — code: match/script/pipeline_step.py -> file node id 'match_script_pipeline_step'
- [[graphify_tests_test_file_node_id_spec_rationale_47]] — code: A file directly at the project root collapses to just its stem.
- [[graphify_tests_test_file_node_id_spec_rationale_59]] — code: A SYMBOL in a root-level file must use the bare-stem prefix (`setup_configure`),
- [[graphify_tests_test_file_node_id_spec_rationale_84]] — code: Regression guard: nested files (immediate parent identical in abs/rel form)
- [[graphify_tests_test_file_node_id_spec_rationale_98]] — code: Symbol ids already use {parent}_{stem}_{name}; the file node must share     tha
- [[graphify_tests_test_file_node_id_spec_rationale_123]] — code: Changing the file-id format must not orphan import edges: the import     target

## Dependências

- [[graphify_tests_test_file_node_id_spec]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_file_node_id_spec_test_cross_file_import_edges_stay_connected]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_file_node_id_spec_test_file_node_id_uses_parent_dir_and_stem_no_extension]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_file_node_id_spec_test_nested_file_symbol_ids_unchanged]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_file_node_id_spec_test_symbol_and_file_ids_share_the_same_stem]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_file_node_id_spec_test_top_level_file_node_id_is_bare_stem]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_file_node_id_spec_test_top_level_file_symbol_ids_use_bare_stem]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_file_node_id_spec]] → `contains` → [[graphify_tests_test_file_node_id_spec_file_nodes]]
- [[graphify_tests_test_file_node_id_spec]] → `contains` → [[graphify_tests_test_file_node_id_spec_test_cross_file_import_edges_stay_connected]]
- [[graphify_tests_test_file_node_id_spec]] → `contains` → [[graphify_tests_test_file_node_id_spec_test_file_node_id_uses_parent_dir_and_stem_no_extension]]
- [[graphify_tests_test_file_node_id_spec]] → `contains` → [[graphify_tests_test_file_node_id_spec_test_nested_file_symbol_ids_unchanged]]
- [[graphify_tests_test_file_node_id_spec]] → `contains` → [[graphify_tests_test_file_node_id_spec_test_symbol_and_file_ids_share_the_same_stem]]
- [[graphify_tests_test_file_node_id_spec]] → `contains` → [[graphify_tests_test_file_node_id_spec_test_top_level_file_node_id_is_bare_stem]]
- [[graphify_tests_test_file_node_id_spec]] → `contains` → [[graphify_tests_test_file_node_id_spec_test_top_level_file_symbol_ids_use_bare_stem]]
- [[graphify_tests_test_file_node_id_spec_rationale_1]] → `rationale_for` → [[graphify_tests_test_file_node_id_spec]]
- [[graphify_tests_test_file_node_id_spec_rationale_28]] → `rationale_for` → [[graphify_tests_test_file_node_id_spec_test_file_node_id_uses_parent_dir_and_stem_no_extension]]
- [[graphify_tests_test_file_node_id_spec_rationale_47]] → `rationale_for` → [[graphify_tests_test_file_node_id_spec_test_top_level_file_node_id_is_bare_stem]]
- [[graphify_tests_test_file_node_id_spec_rationale_59]] → `rationale_for` → [[graphify_tests_test_file_node_id_spec_test_top_level_file_symbol_ids_use_bare_stem]]
- [[graphify_tests_test_file_node_id_spec_rationale_84]] → `rationale_for` → [[graphify_tests_test_file_node_id_spec_test_nested_file_symbol_ids_unchanged]]
- [[graphify_tests_test_file_node_id_spec_rationale_98]] → `rationale_for` → [[graphify_tests_test_file_node_id_spec_test_symbol_and_file_ids_share_the_same_stem]]
- [[graphify_tests_test_file_node_id_spec_rationale_123]] → `rationale_for` → [[graphify_tests_test_file_node_id_spec_test_cross_file_import_edges_stay_connected]]