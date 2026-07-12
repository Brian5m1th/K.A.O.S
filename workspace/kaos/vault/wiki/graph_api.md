# assistant\app\api\graph_api.py

## Símbolos

- [[assistant_app_api_graph_api]] — code: graph_api.py
- [[assistant_app_api_graph_api_graphqueryrequest]] — code: GraphQueryRequest
- [[assistant_app_api_graph_api_get_graph_service]] — code: get_graph_service()
- [[assistant_app_api_graph_api_explain_concept]] — code: explain_concept()
- [[assistant_app_api_graph_api_find_path]] — code: find_path()
- [[assistant_app_api_graph_api_query_graph]] — code: query_graph()
- [[assistant_app_api_graph_api_graph_health]] — code: graph_health()
- [[assistant_app_api_graph_api_rationale_1]] — code: Graph REST API — Structural code intelligence queries.  Endpoints:   GET  /api/g
- [[assistant_app_api_graph_api_rationale_42]] — code: Explain a code symbol: location, connections, and community.
- [[assistant_app_api_graph_api_rationale_63]] — code: Find the shortest dependency path between two symbols.
- [[assistant_app_api_graph_api_rationale_78]] — code: Execute a traversal search over the code graph.
- [[assistant_app_api_graph_api_rationale_96]] — code: Check graph service health.

## Dependências

- [[assistant_app_api_graph_api]] → `contains` → [[assistant_app_api_graph_api_explain_concept]]
- [[assistant_app_api_graph_api]] → `contains` → [[assistant_app_api_graph_api_find_path]]
- [[assistant_app_api_graph_api]] → `contains` → [[assistant_app_api_graph_api_get_graph_service]]
- [[assistant_app_api_graph_api]] → `contains` → [[assistant_app_api_graph_api_graph_health]]
- [[assistant_app_api_graph_api]] → `contains` → [[assistant_app_api_graph_api_graphqueryrequest]]
- [[assistant_app_api_graph_api]] → `contains` → [[assistant_app_api_graph_api_query_graph]]
- [[assistant_app_api_graph_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_graph_api_rationale_1]] → `rationale_for` → [[assistant_app_api_graph_api]]
- [[assistant_app_api_graph_api_graphqueryrequest]] → `inherits` → [[assistant_app_api_graph_api_py_basemodel]]
- [[assistant_app_api_graph_api_graphqueryrequest]] → `uses` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_api_graph_api_graphqueryrequest]] → `uses` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_api_graph_api_graphqueryrequest]] → `uses` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]]
- [[assistant_app_api_graph_api_graphqueryrequest]] → `uses` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback]]
- [[assistant_app_api_graph_api_query_graph]] → `references` → [[assistant_app_api_graph_api_graphqueryrequest]]
- [[assistant_app_api_graph_api_get_graph_service]] → `references` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_api_graph_api_get_graph_service]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]]
- [[assistant_app_api_graph_api_get_graph_service]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback]]
- [[assistant_app_api_graph_api_explain_concept]] → `references` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_api_graph_api_rationale_42]] → `rationale_for` → [[assistant_app_api_graph_api_explain_concept]]
- [[assistant_app_api_graph_api_find_path]] → `references` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_api_graph_api_rationale_63]] → `rationale_for` → [[assistant_app_api_graph_api_find_path]]
- [[assistant_app_api_graph_api_query_graph]] → `references` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_api_graph_api_query_graph]] → `calls` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_api_graph_api_rationale_78]] → `rationale_for` → [[assistant_app_api_graph_api_query_graph]]
- [[assistant_app_api_graph_api_graph_health]] → `references` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_api_graph_api_rationale_96]] → `rationale_for` → [[assistant_app_api_graph_api_graph_health]]