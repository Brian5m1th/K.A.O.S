# assistant\app\providers\graph\networkx_fallback.py

## Símbolos

- [[assistant_app_providers_graph_networkx_fallback]] — code: networkx_fallback.py
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] — code: NetworkXFallback
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_init]] — code: .__init__()
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_provider_name]] — code: .provider_name()
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]] — code: .add_node()
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_explain]] — code: .explain()
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_path]] — code: .path()
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_query]] — code: .query()
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_health]] — code: .health()
- [[assistant_app_providers_graph_networkx_fallback_rationale_1]] — code: NetworkX Fallback Adapter — In-memory graph for GraphPort.  Used when Graphify C
- [[assistant_app_providers_graph_networkx_fallback_rationale_14]] — code: Minimal in-memory graph fallback when Graphify is unavailable.

## Dependências

- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `uses` → [[assistant_app_domain_ports_graph_port_nodeinfo]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `uses` → [[assistant_app_domain_ports_graph_port_pathinfo]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `uses` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_query]] → `references` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `uses` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_query]] → `references` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `uses` → [[assistant_app_domain_ports_graph_port_graphport]]
- [[assistant_app_providers_graph_networkx_fallback]] → `contains` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback]]
- [[assistant_app_providers_graph_networkx_fallback_rationale_1]] → `rationale_for` → [[assistant_app_providers_graph_networkx_fallback]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `method` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `method` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_explain]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `method` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_health]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `method` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_init]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `method` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_path]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `method` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_provider_name]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback]] → `method` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_query]]
- [[assistant_app_providers_graph_networkx_fallback_rationale_14]] → `rationale_for` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_py_nodeinfo]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_explain]] → `references` → [[assistant_app_providers_graph_networkx_fallback_py_nodeinfo]]
- [[assistant_app_providers_graph_networkx_fallback_networkxfallback_path]] → `references` → [[assistant_app_providers_graph_networkx_fallback_py_pathinfo]]