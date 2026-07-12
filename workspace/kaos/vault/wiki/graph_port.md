# assistant\app\domain\ports\graph_port.py

## Símbolos

- [[assistant_app_domain_ports_graph_port]] — code: graph_port.py
- [[assistant_app_domain_ports_graph_port_nodeinfo]] — code: NodeInfo
- [[assistant_app_domain_ports_graph_port_pathinfo]] — code: PathInfo
- [[assistant_app_domain_ports_graph_port_graphquery]] — code: GraphQuery
- [[assistant_app_domain_ports_graph_port_graphresult]] — code: GraphResult
- [[assistant_app_domain_ports_graph_port_graphport]] — code: GraphPort
- [[assistant_app_domain_ports_graph_port_graphport_provider_name]] — code: .provider_name()
- [[assistant_app_domain_ports_graph_port_graphport_explain]] — code: .explain()
- [[assistant_app_domain_ports_graph_port_graphport_path]] — code: .path()
- [[assistant_app_domain_ports_graph_port_graphport_query]] — code: .query()
- [[assistant_app_domain_ports_graph_port_graphport_health]] — code: .health()
- [[assistant_app_domain_ports_graph_port_rationale_1]] — code: GraphPort — Code intelligence capability.  Exposes structural queries over the c
- [[assistant_app_domain_ports_graph_port_rationale_17]] — code: Information about a code symbol or file.
- [[assistant_app_domain_ports_graph_port_rationale_29]] — code: Path between two code symbols.
- [[assistant_app_domain_ports_graph_port_rationale_39]] — code: A query against the code graph.
- [[assistant_app_domain_ports_graph_port_rationale_48]] — code: Result of a graph query.
- [[assistant_app_domain_ports_graph_port_rationale_55]] — code: Interface for code intelligence graph queries.      Concrete implementations:
- [[assistant_app_domain_ports_graph_port_rationale_67]] — code: Unique provider identifier, e.g. 'graphify'.
- [[assistant_app_domain_ports_graph_port_rationale_72]] — code: Explain a code symbol: its location, connections, and community.
- [[assistant_app_domain_ports_graph_port_rationale_77]] — code: Find the shortest dependency path between two symbols.
- [[assistant_app_domain_ports_graph_port_rationale_82]] — code: Execute a traversal/neighborhood search from matching nodes.
- [[assistant_app_domain_ports_graph_port_rationale_87]] — code: Check if the graph source is available and up-to-date.

## Dependências

- [[assistant_app_domain_ports_graph_port]] → `contains` → [[assistant_app_domain_ports_graph_port_graphport]]
- [[assistant_app_domain_ports_graph_port]] → `contains` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_domain_ports_graph_port]] → `contains` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_domain_ports_graph_port]] → `contains` → [[assistant_app_domain_ports_graph_port_nodeinfo]]
- [[assistant_app_domain_ports_graph_port]] → `contains` → [[assistant_app_domain_ports_graph_port_pathinfo]]
- [[assistant_app_domain_ports_graph_port]] → `imports_from` → [[assistant_app_domain_ports_graph_port_py_abc]]
- [[assistant_app_domain_ports_graph_port_rationale_1]] → `rationale_for` → [[assistant_app_domain_ports_graph_port]]
- [[assistant_app_domain_ports_graph_port_graphport_explain]] → `references` → [[assistant_app_domain_ports_graph_port_nodeinfo]]
- [[assistant_app_domain_ports_graph_port_rationale_17]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_nodeinfo]]
- [[assistant_app_domain_ports_graph_port_graphport_path]] → `references` → [[assistant_app_domain_ports_graph_port_pathinfo]]
- [[assistant_app_domain_ports_graph_port_rationale_29]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_pathinfo]]
- [[assistant_app_domain_ports_graph_port_graphport_query]] → `references` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_domain_ports_graph_port_rationale_39]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_domain_ports_graph_port_graphport_query]] → `references` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_domain_ports_graph_port_rationale_48]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_domain_ports_graph_port_graphport]] → `method` → [[assistant_app_domain_ports_graph_port_graphport_explain]]
- [[assistant_app_domain_ports_graph_port_graphport]] → `method` → [[assistant_app_domain_ports_graph_port_graphport_health]]
- [[assistant_app_domain_ports_graph_port_graphport]] → `method` → [[assistant_app_domain_ports_graph_port_graphport_path]]
- [[assistant_app_domain_ports_graph_port_graphport]] → `method` → [[assistant_app_domain_ports_graph_port_graphport_provider_name]]
- [[assistant_app_domain_ports_graph_port_graphport]] → `method` → [[assistant_app_domain_ports_graph_port_graphport_query]]
- [[assistant_app_domain_ports_graph_port_graphport]] → `inherits` → [[assistant_app_domain_ports_graph_port_py_abc]]
- [[assistant_app_domain_ports_graph_port_rationale_55]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_graphport]]
- [[assistant_app_domain_ports_graph_port_rationale_67]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_graphport_provider_name]]
- [[assistant_app_domain_ports_graph_port_rationale_72]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_graphport_explain]]
- [[assistant_app_domain_ports_graph_port_rationale_77]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_graphport_path]]
- [[assistant_app_domain_ports_graph_port_rationale_82]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_graphport_query]]
- [[assistant_app_domain_ports_graph_port_rationale_87]] → `rationale_for` → [[assistant_app_domain_ports_graph_port_graphport_health]]