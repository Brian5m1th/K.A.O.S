# assistant\app\orchestrator\universal_orchestrator.py

## Símbolos

- [[assistant_app_orchestrator_universal_orchestrator]] — code: universal_orchestrator.py
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] — code: UniversalOrchestrator
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_init]] — code: .__init__()
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_select_model]] — code: ._select_model()
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_execute]] — code: .execute()
- [[assistant_app_orchestrator_universal_orchestrator_rationale_45]] — code: Select model via ModelRouter if available, fallback to settings.

## Dependências

- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_execute]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_execute]] → `calls` → [[assistant_app_domain_execution_plan_executionplan_create]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_models_model_router_modelselection]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_select_model]] → `references` → [[assistant_app_models_model_router_modelselection]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_models_model_router_modelrouter]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_init]] → `references` → [[assistant_app_models_model_router_modelrouter]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_execute]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_init]] → `references` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_init]] → `references` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `uses` → [[assistant_app_orchestrator_plan_executor_planexecutor]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_init]] → `calls` → [[assistant_app_orchestrator_plan_executor_planexecutor]]
- [[assistant_app_orchestrator_universal_orchestrator]] → `imports_from` → [[assistant_app_orchestrator_universal_orchestrator_py_uuid]]
- [[assistant_app_orchestrator_universal_orchestrator]] → `contains` → [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `method` → [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_execute]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `method` → [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_init]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]] → `method` → [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_select_model]]
- [[assistant_app_orchestrator_universal_orchestrator_rationale_45]] → `rationale_for` → [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_select_model]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_execute]] → `calls` → [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_select_model]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_select_model]] → `references` → [[assistant_app_orchestrator_universal_orchestrator_py_uuid]]
- [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator_execute]] → `references` → [[assistant_app_orchestrator_universal_orchestrator_py_uuid]]