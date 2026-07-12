# assistant\app\core\services\retrieval_service.py

## Símbolos

- [[assistant_app_core_services_retrieval_service]] — code: retrieval_service.py
- [[assistant_app_core_services_retrieval_service_retrievalservice]] — code: RetrievalService
- [[assistant_app_core_services_retrieval_service_retrievalservice_init]] — code: .__init__()
- [[assistant_app_core_services_retrieval_service_retrievalservice_search]] — code: .search()
- [[assistant_app_core_services_retrieval_service_retrievalservice_count]] — code: .count()
- [[assistant_app_core_services_retrieval_service_retrievalservice_health]] — code: .health()
- [[assistant_app_core_services_retrieval_service_rationale_1]] — code: RetrievalService — Semantic search orchestrator.
- [[assistant_app_core_services_retrieval_service_rationale_10]] — code: Service for vector and semantic search.

## Dependências

- [[assistant_app_core_services_retrieval_service_retrievalservice]] → `uses` → [[assistant_app_core_provider_registry_providerregistry]]
- [[assistant_app_core_services_retrieval_service]] → `contains` → [[assistant_app_core_services_retrieval_service_retrievalservice]]
- [[assistant_app_core_services_retrieval_service_rationale_1]] → `rationale_for` → [[assistant_app_core_services_retrieval_service]]
- [[assistant_app_core_services_retrieval_service_rationale_10]] → `rationale_for` → [[assistant_app_core_services_retrieval_service_retrievalservice]]
- [[assistant_app_core_services_retrieval_service_retrievalservice]] → `method` → [[assistant_app_core_services_retrieval_service_retrievalservice_count]]
- [[assistant_app_core_services_retrieval_service_retrievalservice]] → `method` → [[assistant_app_core_services_retrieval_service_retrievalservice_health]]
- [[assistant_app_core_services_retrieval_service_retrievalservice]] → `method` → [[assistant_app_core_services_retrieval_service_retrievalservice_init]]
- [[assistant_app_core_services_retrieval_service_retrievalservice]] → `method` → [[assistant_app_core_services_retrieval_service_retrievalservice_search]]
- [[assistant_app_core_services_retrieval_service_retrievalservice]] → `uses` → [[assistant_app_domain_ports_retrieval_port_retrievalport]]
- [[assistant_app_core_services_retrieval_service_retrievalservice]] → `uses` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_core_services_retrieval_service_retrievalservice]] → `uses` → [[assistant_app_domain_ports_retrieval_port_retrievalresult]]
- [[assistant_app_core_services_retrieval_service_retrievalservice_search]] → `references` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_core_services_retrieval_service_retrievalservice_search]] → `references` → [[assistant_app_domain_ports_retrieval_port_retrievalresult]]