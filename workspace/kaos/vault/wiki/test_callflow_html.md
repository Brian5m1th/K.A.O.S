# graphify\tests\test_callflow_html.py

## Símbolos

- [[graphify_tests_test_callflow_html]] — code: test_callflow_html.py
- [[graphify_tests_test_callflow_html_make_graphify_out]] — code: _make_graphify_out()
- [[graphify_tests_test_callflow_html_test_write_callflow_html_creates_file_and_uses_report]] — code: test_write_callflow_html_creates_file_and_uses_report()
- [[graphify_tests_test_callflow_html_test_export_callflow_html_cli_creates_file]] — code: test_export_callflow_html_cli_creates_file()
- [[graphify_tests_test_callflow_html_test_export_callflow_html_cli_accepts_positional_graph_path]] — code: test_export_callflow_html_cli_accepts_positional_graph_path()
- [[graphify_tests_test_callflow_html_test_derive_sections_groups_by_architecture_keywords]] — code: test_derive_sections_groups_by_architecture_keywords()
- [[graphify_tests_test_callflow_html_test_load_graph_rejects_oversized_file]] — code: test_load_graph_rejects_oversized_file()
- [[graphify_tests_test_callflow_html_rationale_174]] — code: #F4: callflow_html.load_graph must refuse to read a graph.json that     exceeds

## Dependências

- [[graphify_tests_test_callflow_html]] → `imports_from` → [[graphify_graphify_callflow_html]]
- [[graphify_tests_test_callflow_html_test_derive_sections_groups_by_architecture_keywords]] → `calls` → [[graphify_graphify_callflow_html_derive_sections_from_communities]]
- [[graphify_tests_test_callflow_html_test_write_callflow_html_creates_file_and_uses_report]] → `calls` → [[graphify_graphify_callflow_html_write_callflow_html]]
- [[graphify_tests_test_callflow_html]] → `contains` → [[graphify_tests_test_callflow_html_make_graphify_out]]
- [[graphify_tests_test_callflow_html]] → `contains` → [[graphify_tests_test_callflow_html_test_derive_sections_groups_by_architecture_keywords]]
- [[graphify_tests_test_callflow_html]] → `contains` → [[graphify_tests_test_callflow_html_test_export_callflow_html_cli_accepts_positional_graph_path]]
- [[graphify_tests_test_callflow_html]] → `contains` → [[graphify_tests_test_callflow_html_test_export_callflow_html_cli_creates_file]]
- [[graphify_tests_test_callflow_html]] → `contains` → [[graphify_tests_test_callflow_html_test_load_graph_rejects_oversized_file]]
- [[graphify_tests_test_callflow_html]] → `contains` → [[graphify_tests_test_callflow_html_test_write_callflow_html_creates_file_and_uses_report]]
- [[graphify_tests_test_callflow_html_make_graphify_out]] → `references` → [[graphify_tests_test_callflow_html_py_path]]
- [[graphify_tests_test_callflow_html_test_export_callflow_html_cli_accepts_positional_graph_path]] → `calls` → [[graphify_tests_test_callflow_html_make_graphify_out]]
- [[graphify_tests_test_callflow_html_test_export_callflow_html_cli_creates_file]] → `calls` → [[graphify_tests_test_callflow_html_make_graphify_out]]
- [[graphify_tests_test_callflow_html_test_write_callflow_html_creates_file_and_uses_report]] → `calls` → [[graphify_tests_test_callflow_html_make_graphify_out]]
- [[graphify_tests_test_callflow_html_rationale_174]] → `rationale_for` → [[graphify_tests_test_callflow_html_test_load_graph_rejects_oversized_file]]