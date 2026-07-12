# assistant\app\providers\graph\graphify_adapter.py

## Símbolos

- [[assistant_app_providers_graph_graphify_adapter]] — code: graphify_adapter.py
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] — code: GraphifyAdapter
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_init]] — code: .__init__()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_provider_name]] — code: .provider_name()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_version]] — code: .version()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_load_graph]] — code: ._load_graph()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_explain]] — code: .explain()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_explain_cli]] — code: ._parse_explain_cli()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_node_to_info]] — code: ._node_to_info()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_path]] — code: .path()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_path_cli]] — code: ._parse_path_cli()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_query]] — code: .query()
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_health]] — code: .health()
- [[assistant_app_providers_graph_graphify_adapter_rationale_1]] — code: GraphifyAdapter — Wraps Graphify CLI and graph.json for GraphPort.  Implements G
- [[assistant_app_providers_graph_graphify_adapter_rationale_18]] — code: Adapter that wraps Graphify CLI and graph.json for code intelligence queries.
- [[assistant_app_providers_graph_graphify_adapter_rationale_35]] — code: Lazy-load graph.json with node index.
- [[assistant_app_providers_graph_graphify_adapter_rationale_52]] — code: Explain a code symbol using Graphify CLI or graph.json parsing.
- [[assistant_app_providers_graph_graphify_adapter_rationale_75]] — code: Parse 'graphify explain' CLI output into NodeInfo.
- [[assistant_app_providers_graph_graphify_adapter_rationale_94]] — code: Convert a graph.json node to NodeInfo.
- [[assistant_app_providers_graph_graphify_adapter_rationale_111]] — code: Find dependency path between two symbols.
- [[assistant_app_providers_graph_graphify_adapter_rationale_125]] — code: Parse 'graphify path' CLI output.
- [[assistant_app_providers_graph_graphify_adapter_rationale_137]] — code: Execute a traversal search using graph.json.
- [[assistant_app_providers_graph_graphify_adapter_rationale_178]] — code: Check if graph.json exists and is recent.

## Dependências

- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `uses` → [[assistant_app_domain_ports_graph_port_nodeinfo]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `uses` → [[assistant_app_domain_ports_graph_port_pathinfo]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `uses` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_query]] → `references` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `uses` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_query]] → `references` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `uses` → [[assistant_app_domain_ports_graph_port_graphport]]
- [[assistant_app_providers_graph_graphify_adapter]] → `contains` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_1]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_explain]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_health]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_init]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_load_graph]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_node_to_info]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_explain_cli]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_path_cli]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_path]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_provider_name]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_query]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]] → `method` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_version]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_18]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_explain]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_load_graph]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_query]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_load_graph]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_35]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_load_graph]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_explain]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_node_to_info]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_explain]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_explain_cli]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_explain]] → `references` → [[assistant_app_providers_graph_graphify_adapter_py_nodeinfo]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_52]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_explain]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_node_to_info]] → `references` → [[assistant_app_providers_graph_graphify_adapter_py_nodeinfo]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_explain_cli]] → `references` → [[assistant_app_providers_graph_graphify_adapter_py_nodeinfo]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_75]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_explain_cli]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_query]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_node_to_info]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_94]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_node_to_info]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_path]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_path_cli]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_path]] → `references` → [[assistant_app_providers_graph_graphify_adapter_py_pathinfo]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_111]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_path]]
- [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_path_cli]] → `references` → [[assistant_app_providers_graph_graphify_adapter_py_pathinfo]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_125]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_parse_path_cli]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_137]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_query]]
- [[assistant_app_providers_graph_graphify_adapter_rationale_178]] → `rationale_for` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter_health]]