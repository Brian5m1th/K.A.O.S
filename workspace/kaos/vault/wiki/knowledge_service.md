# assistant\app\core\services\knowledge_service.py

## Símbolos

- [[assistant_app_core_services_knowledge_service]] — code: knowledge_service.py
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] — code: KnowledgeService
- [[assistant_app_core_services_knowledge_service_knowledgeservice_init]] — code: .__init__()
- [[assistant_app_core_services_knowledge_service_knowledgeservice_query]] — code: .query()
- [[assistant_app_core_services_knowledge_service_knowledgeservice_health]] — code: .health()
- [[assistant_app_core_services_knowledge_service_rationale_1]] — code: KnowledgeService — Unified knowledge coalescing orchestrator.  Combines Graph, M
- [[assistant_app_core_services_knowledge_service_rationale_24]] — code: High-level service that coalesces multiple knowledge sources.
- [[assistant_app_core_services_knowledge_service_rationale_37]] — code: Coalescing query across all knowledge sources.

## Dependências

- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `uses` → [[assistant_app_core_provider_registry_providerregistry]]
- [[assistant_app_core_services_knowledge_service]] → `contains` → [[assistant_app_core_services_knowledge_service_knowledgeservice]]
- [[assistant_app_core_services_knowledge_service_rationale_1]] → `rationale_for` → [[assistant_app_core_services_knowledge_service]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `method` → [[assistant_app_core_services_knowledge_service_knowledgeservice_health]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `method` → [[assistant_app_core_services_knowledge_service_knowledgeservice_init]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `method` → [[assistant_app_core_services_knowledge_service_knowledgeservice_query]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `uses` → [[assistant_app_domain_ports_graph_port_graphport]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `uses` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `uses` → [[assistant_app_domain_ports_graph_port_graphresult]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `uses` → [[assistant_app_domain_ports_graph_port_nodeinfo]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `uses` → [[assistant_app_domain_ports_graph_port_pathinfo]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice]] → `uses` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_core_services_knowledge_service_rationale_24]] → `rationale_for` → [[assistant_app_core_services_knowledge_service_knowledgeservice]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice_query]] → `calls` → [[assistant_app_domain_ports_graph_port_graphquery]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice_query]] → `calls` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_core_services_knowledge_service_knowledgeservice_query]] → `calls` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_core_services_knowledge_service_rationale_37]] → `rationale_for` → [[assistant_app_core_services_knowledge_service_knowledgeservice_query]]