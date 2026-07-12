# graphify\tests\test_pipeline.py

## Símbolos

- [[graphify_tests_test_pipeline]] — code: test_pipeline.py
- [[graphify_tests_test_pipeline_run_pipeline]] — code: run_pipeline()
- [[graphify_tests_test_pipeline_test_pipeline_runs_end_to_end]] — code: test_pipeline_runs_end_to_end()
- [[graphify_tests_test_pipeline_test_pipeline_graph_has_edges]] — code: test_pipeline_graph_has_edges()
- [[graphify_tests_test_pipeline_test_pipeline_all_nodes_have_community]] — code: test_pipeline_all_nodes_have_community()
- [[graphify_tests_test_pipeline_test_pipeline_report_mentions_top_god_node]] — code: test_pipeline_report_mentions_top_god_node()
- [[graphify_tests_test_pipeline_test_pipeline_detection_finds_code_and_docs]] — code: test_pipeline_detection_finds_code_and_docs()
- [[graphify_tests_test_pipeline_test_pipeline_incremental_update]] — code: test_pipeline_incremental_update()
- [[graphify_tests_test_pipeline_test_pipeline_extraction_confidence_labels]] — code: test_pipeline_extraction_confidence_labels()
- [[graphify_tests_test_pipeline_test_pipeline_no_self_loops]] — code: test_pipeline_no_self_loops()
- [[graphify_tests_test_pipeline_rationale_1]] — code: End-to-end pipeline test: detect → extract → build → cluster → analyze → report
- [[graphify_tests_test_pipeline_rationale_24]] — code: Run the full pipeline on the fixtures directory. Returns a dict of outputs.
- [[graphify_tests_test_pipeline_rationale_139]] — code: Second run on unchanged corpus should produce identical node/edge counts.

## Dependências

- [[graphify_tests_test_pipeline]] → `imports_from` → [[graphify_graphify_analyze]]
- [[graphify_tests_test_pipeline]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_pipeline]] → `imports_from` → [[graphify_graphify_cluster]]
- [[graphify_tests_test_pipeline]] → `imports_from` → [[graphify_graphify_detect]]
- [[graphify_tests_test_pipeline_run_pipeline]] → `calls` → [[graphify_graphify_detect_detect]]
- [[graphify_tests_test_pipeline]] → `imports_from` → [[graphify_graphify_export]]
- [[graphify_tests_test_pipeline_run_pipeline]] → `calls` → [[graphify_graphify_export_to_json]]
- [[graphify_tests_test_pipeline_run_pipeline]] → `calls` → [[graphify_graphify_export_to_obsidian]]
- [[graphify_tests_test_pipeline_run_pipeline]] → `calls` → [[graphify_graphify_exporters_html_to_html]]
- [[graphify_tests_test_pipeline]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_pipeline_run_pipeline]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_pipeline]] → `imports_from` → [[graphify_graphify_report]]
- [[graphify_tests_test_pipeline_run_pipeline]] → `calls` → [[graphify_graphify_report_generate]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_test_pipeline_all_nodes_have_community]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_test_pipeline_detection_finds_code_and_docs]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_test_pipeline_extraction_confidence_labels]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_test_pipeline_graph_has_edges]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_test_pipeline_incremental_update]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_test_pipeline_no_self_loops]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_test_pipeline_report_mentions_top_god_node]]
- [[graphify_tests_test_pipeline]] → `contains` → [[graphify_tests_test_pipeline_test_pipeline_runs_end_to_end]]
- [[graphify_tests_test_pipeline_rationale_1]] → `rationale_for` → [[graphify_tests_test_pipeline]]
- [[graphify_tests_test_pipeline_rationale_24]] → `rationale_for` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_run_pipeline]] → `references` → [[graphify_tests_test_pipeline_py_path]]
- [[graphify_tests_test_pipeline_test_pipeline_all_nodes_have_community]] → `calls` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_test_pipeline_detection_finds_code_and_docs]] → `calls` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_test_pipeline_extraction_confidence_labels]] → `calls` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_test_pipeline_graph_has_edges]] → `calls` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_test_pipeline_incremental_update]] → `calls` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_test_pipeline_no_self_loops]] → `calls` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_test_pipeline_report_mentions_top_god_node]] → `calls` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_test_pipeline_runs_end_to_end]] → `calls` → [[graphify_tests_test_pipeline_run_pipeline]]
- [[graphify_tests_test_pipeline_rationale_139]] → `rationale_for` → [[graphify_tests_test_pipeline_test_pipeline_incremental_update]]