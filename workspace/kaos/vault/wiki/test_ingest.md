# graphify\tests\test_ingest.py

## Símbolos

- [[graphify_tests_test_ingest]] — code: test_ingest.py
- [[graphify_tests_test_ingest_test_file_created]] — code: test_file_created()
- [[graphify_tests_test_ingest_test_filename_format]] — code: test_filename_format()
- [[graphify_tests_test_ingest_test_frontmatter_question]] — code: test_frontmatter_question()
- [[graphify_tests_test_ingest_test_frontmatter_type]] — code: test_frontmatter_type()
- [[graphify_tests_test_ingest_test_source_nodes_included]] — code: test_source_nodes_included()
- [[graphify_tests_test_ingest_test_source_nodes_capped_at_10]] — code: test_source_nodes_capped_at_10()
- [[graphify_tests_test_ingest_test_memory_dir_created]] — code: test_memory_dir_created()
- [[graphify_tests_test_ingest_test_answer_in_body]] — code: test_answer_in_body()
- [[graphify_tests_test_ingest_test_outcome_in_frontmatter_and_body]] — code: test_outcome_in_frontmatter_and_body()
- [[graphify_tests_test_ingest_test_correction_in_frontmatter_and_body]] — code: test_correction_in_frontmatter_and_body()
- [[graphify_tests_test_ingest_test_no_outcome_means_no_outcome_section]] — code: test_no_outcome_means_no_outcome_section()
- [[graphify_tests_test_ingest_test_invalid_outcome_rejected]] — code: test_invalid_outcome_rejected()
- [[graphify_tests_test_ingest_rationale_1]] — code: Tests for graphify.ingest.save_query_result
- [[graphify_tests_test_ingest_rationale_71]] — code: An outcome signal is written to both frontmatter (for `reflect`) and an     ##
- [[graphify_tests_test_ingest_rationale_91]] — code: Backward compatible: a result without an outcome looks exactly as before.

## Dependências

- [[graphify_tests_test_ingest]] → `imports_from` → [[graphify_graphify_ingest]]
- [[graphify_tests_test_ingest_test_answer_in_body]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_correction_in_frontmatter_and_body]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_file_created]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_filename_format]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_frontmatter_question]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_frontmatter_type]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_invalid_outcome_rejected]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_memory_dir_created]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_no_outcome_means_no_outcome_section]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_outcome_in_frontmatter_and_body]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_source_nodes_capped_at_10]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest_test_source_nodes_included]] → `calls` → [[graphify_graphify_ingest_save_query_result]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_answer_in_body]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_correction_in_frontmatter_and_body]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_file_created]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_filename_format]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_frontmatter_question]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_frontmatter_type]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_invalid_outcome_rejected]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_memory_dir_created]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_no_outcome_means_no_outcome_section]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_outcome_in_frontmatter_and_body]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_source_nodes_capped_at_10]]
- [[graphify_tests_test_ingest]] → `contains` → [[graphify_tests_test_ingest_test_source_nodes_included]]
- [[graphify_tests_test_ingest_rationale_1]] → `rationale_for` → [[graphify_tests_test_ingest]]
- [[graphify_tests_test_ingest_rationale_71]] → `rationale_for` → [[graphify_tests_test_ingest_test_outcome_in_frontmatter_and_body]]
- [[graphify_tests_test_ingest_rationale_91]] → `rationale_for` → [[graphify_tests_test_ingest_test_no_outcome_means_no_outcome_section]]