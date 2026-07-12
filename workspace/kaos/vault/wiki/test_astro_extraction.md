# graphify\tests\test_astro_extraction.py

## Símbolos

- [[graphify_tests_test_astro_extraction]] — code: test_astro_extraction.py
- [[graphify_tests_test_astro_extraction_write]] — code: _write()
- [[graphify_tests_test_astro_extraction_import_targets]] — code: _import_targets()
- [[graphify_tests_test_astro_extraction_test_astro_is_in_code_extensions]] — code: test_astro_is_in_code_extensions()
- [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_frontmatter_static_imports]] — code: test_extract_astro_picks_up_frontmatter_static_imports()
- [[graphify_tests_test_astro_extraction_test_extract_astro_handles_dynamic_import_in_frontmatter]] — code: test_extract_astro_handles_dynamic_import_in_frontmatter()
- [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_client_side_script_imports]] — code: test_extract_astro_picks_up_client_side_script_imports()
- [[graphify_tests_test_astro_extraction_test_extract_astro_no_frontmatter_does_not_crash]] — code: test_extract_astro_no_frontmatter_does_not_crash()
- [[graphify_tests_test_astro_extraction_test_extract_astro_handles_tsconfig_path_alias]] — code: test_extract_astro_handles_tsconfig_path_alias()
- [[graphify_tests_test_astro_extraction_rationale_1]] — code: Tests for `.astro` extraction (#850).  Astro files have a TypeScript frontmatt
- [[graphify_tests_test_astro_extraction_rationale_36]] — code: Without this, detect.py silently drops `.astro` from the AST pass (#850).
- [[graphify_tests_test_astro_extraction_rationale_108]] — code: Astro permits frontmatter-less files (pure-HTML pages). Must not raise.

## Dependências

- [[graphify_tests_test_astro_extraction]] → `imports_from` → [[graphify_graphify_detect]]
- [[graphify_tests_test_astro_extraction]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_handles_dynamic_import_in_frontmatter]] → `calls` → [[graphify_graphify_extract_extract_astro]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_handles_tsconfig_path_alias]] → `calls` → [[graphify_graphify_extract_extract_astro]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_no_frontmatter_does_not_crash]] → `calls` → [[graphify_graphify_extract_extract_astro]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_client_side_script_imports]] → `calls` → [[graphify_graphify_extract_extract_astro]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_frontmatter_static_imports]] → `calls` → [[graphify_graphify_extract_extract_astro]]
- [[graphify_tests_test_astro_extraction]] → `contains` → [[graphify_tests_test_astro_extraction_import_targets]]
- [[graphify_tests_test_astro_extraction]] → `contains` → [[graphify_tests_test_astro_extraction_test_astro_is_in_code_extensions]]
- [[graphify_tests_test_astro_extraction]] → `contains` → [[graphify_tests_test_astro_extraction_test_extract_astro_handles_dynamic_import_in_frontmatter]]
- [[graphify_tests_test_astro_extraction]] → `contains` → [[graphify_tests_test_astro_extraction_test_extract_astro_handles_tsconfig_path_alias]]
- [[graphify_tests_test_astro_extraction]] → `contains` → [[graphify_tests_test_astro_extraction_test_extract_astro_no_frontmatter_does_not_crash]]
- [[graphify_tests_test_astro_extraction]] → `contains` → [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_client_side_script_imports]]
- [[graphify_tests_test_astro_extraction]] → `contains` → [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_frontmatter_static_imports]]
- [[graphify_tests_test_astro_extraction]] → `contains` → [[graphify_tests_test_astro_extraction_write]]
- [[graphify_tests_test_astro_extraction_rationale_1]] → `rationale_for` → [[graphify_tests_test_astro_extraction]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_handles_dynamic_import_in_frontmatter]] → `calls` → [[graphify_tests_test_astro_extraction_write]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_handles_tsconfig_path_alias]] → `calls` → [[graphify_tests_test_astro_extraction_write]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_no_frontmatter_does_not_crash]] → `calls` → [[graphify_tests_test_astro_extraction_write]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_client_side_script_imports]] → `calls` → [[graphify_tests_test_astro_extraction_write]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_frontmatter_static_imports]] → `calls` → [[graphify_tests_test_astro_extraction_write]]
- [[graphify_tests_test_astro_extraction_write]] → `references` → [[graphify_tests_test_astro_extraction_py_path]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_handles_dynamic_import_in_frontmatter]] → `calls` → [[graphify_tests_test_astro_extraction_import_targets]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_handles_tsconfig_path_alias]] → `calls` → [[graphify_tests_test_astro_extraction_import_targets]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_no_frontmatter_does_not_crash]] → `calls` → [[graphify_tests_test_astro_extraction_import_targets]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_client_side_script_imports]] → `calls` → [[graphify_tests_test_astro_extraction_import_targets]]
- [[graphify_tests_test_astro_extraction_test_extract_astro_picks_up_frontmatter_static_imports]] → `calls` → [[graphify_tests_test_astro_extraction_import_targets]]
- [[graphify_tests_test_astro_extraction_rationale_36]] → `rationale_for` → [[graphify_tests_test_astro_extraction_test_astro_is_in_code_extensions]]
- [[graphify_tests_test_astro_extraction_rationale_108]] → `rationale_for` → [[graphify_tests_test_astro_extraction_test_extract_astro_no_frontmatter_does_not_crash]]