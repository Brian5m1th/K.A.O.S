# graphify\graphify\exporters\html.py

## Símbolos

- [[graphify_graphify_exporters_html]] — code: html.py
- [[graphify_graphify_exporters_html_viz_node_limit]] — code: _viz_node_limit()
- [[graphify_graphify_exporters_html_html_styles]] — code: _html_styles()
- [[graphify_graphify_exporters_html_hyperedge_script]] — code: _hyperedge_script()
- [[graphify_graphify_exporters_html_html_script]] — code: _html_script()
- [[graphify_graphify_exporters_html_to_html]] — code: to_html()
- [[graphify_graphify_exporters_html_rationale_1]] — code: html — moved verbatim from graphify/export.py.
- [[graphify_graphify_exporters_html_rationale_16]] — code: Return the effective viz node limit, honoring GRAPHIFY_VIZ_NODE_LIMIT env var.
- [[graphify_graphify_exporters_html_rationale_321]] — code: Generate an interactive vis.js HTML visualization of the graph.      Features:

## Dependências

- [[graphify_graphify_exporters_html]] → `imports_from` → [[graphify_graphify_analyze]]
- [[graphify_graphify_exporters_html]] → `contains` → [[graphify_graphify_exporters_html_html_script]]
- [[graphify_graphify_exporters_html]] → `contains` → [[graphify_graphify_exporters_html_html_styles]]
- [[graphify_graphify_exporters_html]] → `contains` → [[graphify_graphify_exporters_html_hyperedge_script]]
- [[graphify_graphify_exporters_html]] → `contains` → [[graphify_graphify_exporters_html_to_html]]
- [[graphify_graphify_exporters_html]] → `contains` → [[graphify_graphify_exporters_html_viz_node_limit]]
- [[graphify_graphify_exporters_html]] → `imports_from` → [[graphify_security]]
- [[graphify_graphify_exporters_html]] → `imports` → [[graphify_graphify_exporters_html]]
- [[graphify_graphify_exporters_html_rationale_1]] → `rationale_for` → [[graphify_graphify_exporters_html]]
- [[graphify_graphify_exporters_html_rationale_16]] → `rationale_for` → [[graphify_graphify_exporters_html_viz_node_limit]]
- [[graphify_graphify_exporters_html_to_html]] → `calls` → [[graphify_graphify_exporters_html_viz_node_limit]]
- [[graphify_graphify_exporters_html_to_html]] → `calls` → [[graphify_graphify_exporters_html_html_styles]]
- [[graphify_graphify_exporters_html_to_html]] → `calls` → [[graphify_graphify_exporters_html_hyperedge_script]]
- [[graphify_graphify_exporters_html_to_html]] → `calls` → [[graphify_graphify_exporters_html_html_script]]
- [[graphify_graphify_exporters_html_rationale_321]] → `rationale_for` → [[graphify_graphify_exporters_html_to_html]]
- [[graphify_graphify_exporters_html_to_html]] → `calls` → [[graphify_graphify_security_sanitize_label]]
- [[graphify_graphify_exporters_html_to_html]] → `calls` → [[graphify_tests_fixtures_sample_graph]]