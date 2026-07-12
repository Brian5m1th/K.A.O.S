# assistant\app\core\services\evidence_service.py

## Símbolos

- [[assistant_app_core_services_evidence_service]] — code: evidence_service.py
- [[assistant_app_core_services_evidence_service_evidenceservice]] — code: EvidenceService
- [[assistant_app_core_services_evidence_service_evidenceservice_init]] — code: .__init__()
- [[assistant_app_core_services_evidence_service_evidenceservice_collect]] — code: .collect()
- [[assistant_app_core_services_evidence_service_evidenceservice_get_metric]] — code: .get_metric()
- [[assistant_app_core_services_evidence_service_evidenceservice_get_history]] — code: .get_history()
- [[assistant_app_core_services_evidence_service_evidenceservice_health]] — code: .health()
- [[assistant_app_core_services_evidence_service_rationale_1]] — code: EvidenceService — Architecture evidence and health orchestrator.  Aggregates mul
- [[assistant_app_core_services_evidence_service_rationale_13]] — code: Service for evidence collection and architectural health assessment.

## Dependências

- [[assistant_app_core_services_evidence_service_evidenceservice]] → `uses` → [[assistant_app_core_provider_registry_providerregistry]]
- [[assistant_app_core_services_evidence_service]] → `contains` → [[assistant_app_core_services_evidence_service_evidenceservice]]
- [[assistant_app_core_services_evidence_service_rationale_1]] → `rationale_for` → [[assistant_app_core_services_evidence_service]]
- [[assistant_app_core_services_evidence_service_evidenceservice]] → `method` → [[assistant_app_core_services_evidence_service_evidenceservice_collect]]
- [[assistant_app_core_services_evidence_service_evidenceservice]] → `method` → [[assistant_app_core_services_evidence_service_evidenceservice_get_history]]
- [[assistant_app_core_services_evidence_service_evidenceservice]] → `method` → [[assistant_app_core_services_evidence_service_evidenceservice_get_metric]]
- [[assistant_app_core_services_evidence_service_evidenceservice]] → `method` → [[assistant_app_core_services_evidence_service_evidenceservice_health]]
- [[assistant_app_core_services_evidence_service_evidenceservice]] → `method` → [[assistant_app_core_services_evidence_service_evidenceservice_init]]
- [[assistant_app_core_services_evidence_service_evidenceservice]] → `uses` → [[assistant_app_domain_ports_evidence_port_evidencemetric]]
- [[assistant_app_core_services_evidence_service_evidenceservice]] → `uses` → [[assistant_app_domain_ports_evidence_port_evidenceport]]
- [[assistant_app_core_services_evidence_service_evidenceservice]] → `uses` → [[assistant_app_domain_ports_evidence_port_evidencereport]]
- [[assistant_app_core_services_evidence_service_rationale_13]] → `rationale_for` → [[assistant_app_core_services_evidence_service_evidenceservice]]
- [[assistant_app_core_services_evidence_service_evidenceservice_collect]] → `references` → [[assistant_app_core_services_evidence_service_py_evidencereport]]
- [[assistant_app_core_services_evidence_service_evidenceservice_get_metric]] → `references` → [[assistant_app_core_services_evidence_service_py_evidencemetric]]
- [[assistant_app_core_services_evidence_service_evidenceservice_get_history]] → `references` → [[assistant_app_core_services_evidence_service_py_evidencemetric]]