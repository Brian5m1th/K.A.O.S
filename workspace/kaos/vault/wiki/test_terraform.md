# graphify\tests\test_terraform.py

## Símbolos

- [[graphify_tests_test_terraform]] — code: test_terraform.py
- [[graphify_tests_test_terraform_write]] — code: _write()
- [[graphify_tests_test_terraform_labels]] — code: _labels()
- [[graphify_tests_test_terraform_rel_pairs]] — code: _rel_pairs()
- [[graphify_tests_test_terraform_test_no_error_and_all_block_types_become_nodes]] — code: test_no_error_and_all_block_types_become_nodes()
- [[graphify_tests_test_terraform_test_reference_edges]] — code: test_reference_edges()
- [[graphify_tests_test_terraform_test_depends_on_edge]] — code: test_depends_on_edge()
- [[graphify_tests_test_terraform_test_file_contains_blocks]] — code: test_file_contains_blocks()
- [[graphify_tests_test_terraform_test_meta_heads_not_emitted]] — code: test_meta_heads_not_emitted()
- [[graphify_tests_test_terraform_test_cross_file_references_resolve_after_merge]] — code: test_cross_file_references_resolve_after_merge()
- [[graphify_tests_test_terraform_test_empty_and_commentonly_files_are_safe]] — code: test_empty_and_commentonly_files_are_safe()
- [[graphify_tests_test_terraform_test_tfvars_key_value_is_safe]] — code: test_tfvars_key_value_is_safe()
- [[graphify_tests_test_terraform_rationale_1]] — code: Tests for the Terraform/HCL extractor (graphify/extract.py, issue #187).

## Dependências

- [[graphify_tests_test_terraform]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_terraform]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_terraform_test_cross_file_references_resolve_after_merge]] → `calls` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_tests_test_terraform_test_depends_on_edge]] → `calls` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_tests_test_terraform_test_empty_and_commentonly_files_are_safe]] → `calls` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_tests_test_terraform_test_file_contains_blocks]] → `calls` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_tests_test_terraform_test_meta_heads_not_emitted]] → `calls` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_tests_test_terraform_test_no_error_and_all_block_types_become_nodes]] → `calls` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_tests_test_terraform_test_reference_edges]] → `calls` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_tests_test_terraform_test_tfvars_key_value_is_safe]] → `calls` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_labels]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_rel_pairs]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_test_cross_file_references_resolve_after_merge]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_test_depends_on_edge]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_test_empty_and_commentonly_files_are_safe]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_test_file_contains_blocks]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_test_meta_heads_not_emitted]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_test_no_error_and_all_block_types_become_nodes]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_test_reference_edges]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_test_tfvars_key_value_is_safe]]
- [[graphify_tests_test_terraform]] → `contains` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_rationale_1]] → `rationale_for` → [[graphify_tests_test_terraform]]
- [[graphify_tests_test_terraform_test_cross_file_references_resolve_after_merge]] → `calls` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_test_depends_on_edge]] → `calls` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_test_empty_and_commentonly_files_are_safe]] → `calls` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_test_file_contains_blocks]] → `calls` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_test_meta_heads_not_emitted]] → `calls` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_test_no_error_and_all_block_types_become_nodes]] → `calls` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_test_reference_edges]] → `calls` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_test_tfvars_key_value_is_safe]] → `calls` → [[graphify_tests_test_terraform_write]]
- [[graphify_tests_test_terraform_write]] → `references` → [[graphify_tests_test_terraform_py_path]]
- [[graphify_tests_test_terraform_test_no_error_and_all_block_types_become_nodes]] → `calls` → [[graphify_tests_test_terraform_labels]]
- [[graphify_tests_test_terraform_test_depends_on_edge]] → `calls` → [[graphify_tests_test_terraform_rel_pairs]]
- [[graphify_tests_test_terraform_test_file_contains_blocks]] → `calls` → [[graphify_tests_test_terraform_rel_pairs]]
- [[graphify_tests_test_terraform_test_meta_heads_not_emitted]] → `calls` → [[graphify_tests_test_terraform_rel_pairs]]
- [[graphify_tests_test_terraform_test_reference_edges]] → `calls` → [[graphify_tests_test_terraform_rel_pairs]]