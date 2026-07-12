# assistant\app\core\services\graph_service.py

## Símbolos

- [[assistant_app_core_services_graph_service]] — code: graph_service.py
- [[assistant_app_core_services_graph_service_graphservice]] — code: GraphService
- [[assistant_app_core_services_graph_service_graphservice_init]] — code: .__init__()
- [[assistant_app_core_services_graph_service_graphservice_explain]] — code: .explain()
- [[assistant_app_core_services_graph_service_graphservice_path]] — code: .path()
- [[assistant_app_core_services_graph_service_graphservice_query]] — code: .query()
- [[assistant_app_core_services_graph_service_graphservice_health]] — code: .health()
- [[assistant_app_core_services_graph_service_rationale_1]] — code: GraphService — Code intelligence orchestrator.  Wraps GraphPort with ProviderReg
- [[assistant_app_core_services_graph_service_rationale_14]] — code: Service for code intelligence graph queries.

## Dependências

- [[assistant_app_core_services_graph_service_graphservice]] → `uses` → [[assistant_app_core_provider_registry_providerregistry]]
- [[assistant_app_core_services_graph_service]] → `contains` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_core_services_graph_service_rationale_1]] → `rationale_for` → [[assistant_app_core_services_graph_service]]
- [[assistant_app_core_services_graph_service_graphservice]] → `method` → [[assistant_app_core_services_graph_service_graphservice_explain]]
- [[assistant_app_core_services_graph_service_graphservice]] → `method` → [[assistant_app_core_services_graph_service_graphservice_health]]
- [[assistant_app_core_services_graph_service_graphservice]] → `method` → [[assistant_app_core_services_graph_service_graphservice_init]]
- [[assistant_app_core_services_graph_service_graphservice]] → `method` → [[assistant_app_core_services_graph_service_graphservice_path]]
- [[assistant_app_core_services_graph_service_graphservice]] → `method` → [[assistant_app_core_services_graph_service_graphservice_query]]
- [[assistant_app_core_services_graph_service_graphservice]] → `uses` → [[assistant_app_domain_ports_graph_port_graphport]]
- [[assistant_app_core_services_graph_service_graphservice]] → `uses` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_core_services_graph_service_graphservice]] → `uses` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_core_services_graph_service_graphservice]] → `uses` → [[assistant_app_domain_ports_graph_port_nodeinfo]]
- [[assistant_app_core_services_graph_service_graphservice]] → `uses` → [[assistant_app_domain_ports_graph_port_pathinfo]]
- [[assistant_app_core_services_graph_service_rationale_14]] → `rationale_for` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_core_services_graph_service_graphservice_explain]] → `references` → [[assistant_app_core_services_graph_service_py_nodeinfo]]
- [[assistant_app_core_services_graph_service_graphservice_path]] → `references` → [[assistant_app_core_services_graph_service_py_pathinfo]]
- [[assistant_app_core_services_graph_service_graphservice_query]] → `references` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_core_services_graph_service_graphservice_query]] → `references` → [[assistant_app_domain_ports_graph_port_graphresult]]