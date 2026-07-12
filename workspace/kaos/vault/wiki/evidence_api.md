# assistant\app\api\evidence_api.py

## Símbolos

- [[assistant_app_api_evidence_api]] — code: evidence_api.py
- [[assistant_app_api_evidence_api_get_evidence_service]] — code: get_evidence_service()
- [[assistant_app_api_evidence_api_evidence_report]] — code: evidence_report()
- [[assistant_app_api_evidence_api_evidence_metric]] — code: evidence_metric()
- [[assistant_app_api_evidence_api_evidence_history]] — code: evidence_history()
- [[assistant_app_api_evidence_api_evidence_health]] — code: evidence_health()
- [[assistant_app_api_evidence_api_rationale_1]] — code: Evidence REST API — Architecture health and decision support.  Endpoints:   GET
- [[assistant_app_api_evidence_api_rationale_27]] — code: Full architectural evidence report from all sources.
- [[assistant_app_api_evidence_api_rationale_53]] — code: Get a specific evidence metric by name.
- [[assistant_app_api_evidence_api_rationale_72]] — code: Get historical trend for a metric.

## Dependências

- [[assistant_app_api_evidence_api]] → `contains` → [[assistant_app_api_evidence_api_evidence_health]]
- [[assistant_app_api_evidence_api]] → `contains` → [[assistant_app_api_evidence_api_evidence_history]]
- [[assistant_app_api_evidence_api]] → `contains` → [[assistant_app_api_evidence_api_evidence_metric]]
- [[assistant_app_api_evidence_api]] → `contains` → [[assistant_app_api_evidence_api_evidence_report]]
- [[assistant_app_api_evidence_api]] → `contains` → [[assistant_app_api_evidence_api_get_evidence_service]]
- [[assistant_app_api_evidence_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_evidence_api_rationale_1]] → `rationale_for` → [[assistant_app_api_evidence_api]]
- [[assistant_app_api_evidence_api_get_evidence_service]] → `references` → [[assistant_app_core_services_evidence_service_evidenceservice]]
- [[assistant_app_api_evidence_api_evidence_report]] → `references` → [[assistant_app_core_services_evidence_service_evidenceservice]]
- [[assistant_app_api_evidence_api_rationale_27]] → `rationale_for` → [[assistant_app_api_evidence_api_evidence_report]]
- [[assistant_app_api_evidence_api_evidence_metric]] → `references` → [[assistant_app_core_services_evidence_service_evidenceservice]]
- [[assistant_app_api_evidence_api_rationale_53]] → `rationale_for` → [[assistant_app_api_evidence_api_evidence_metric]]
- [[assistant_app_api_evidence_api_evidence_history]] → `references` → [[assistant_app_core_services_evidence_service_evidenceservice]]
- [[assistant_app_api_evidence_api_rationale_72]] → `rationale_for` → [[assistant_app_api_evidence_api_evidence_history]]
- [[assistant_app_api_evidence_api_evidence_health]] → `references` → [[assistant_app_core_services_evidence_service_evidenceservice]]