# assistant\app\orchestrator\provider_selector.py

## Símbolos

- [[assistant_app_orchestrator_provider_selector]] — code: provider_selector.py
- [[assistant_app_orchestrator_provider_selector_providerselector]] — code: ProviderSelector
- [[assistant_app_orchestrator_provider_selector_providerselector_init]] — code: .__init__()
- [[assistant_app_orchestrator_provider_selector_providerselector_select]] — code: .select()
- [[assistant_app_orchestrator_provider_selector_providerselector_select_by_type]] — code: .select_by_type()
- [[assistant_app_orchestrator_provider_selector_providerselector_select_healthy]] — code: .select_healthy()

## Dependências

- [[assistant_app_orchestrator_provider_selector_providerselector]] → `uses` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]]
- [[assistant_app_orchestrator_provider_selector_providerselector_init]] → `references` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]]
- [[assistant_app_orchestrator_provider_selector_providerselector]] → `uses` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_orchestrator_provider_selector_providerselector_init]] → `references` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_orchestrator_provider_selector]] → `contains` → [[assistant_app_orchestrator_provider_selector_providerselector]]
- [[assistant_app_orchestrator_provider_selector_providerselector]] → `method` → [[assistant_app_orchestrator_provider_selector_providerselector_init]]
- [[assistant_app_orchestrator_provider_selector_providerselector]] → `method` → [[assistant_app_orchestrator_provider_selector_providerselector_select]]
- [[assistant_app_orchestrator_provider_selector_providerselector]] → `method` → [[assistant_app_orchestrator_provider_selector_providerselector_select_by_type]]
- [[assistant_app_orchestrator_provider_selector_providerselector]] → `method` → [[assistant_app_orchestrator_provider_selector_providerselector_select_healthy]]
- [[assistant_app_orchestrator_provider_selector_providerselector]] → `uses` → [[assistant_app_repositories_provider_config_repository_providerconfigrecord]]
- [[assistant_app_orchestrator_provider_selector_providerselector]] → `uses` → [[assistant_app_repositories_provider_config_repository_providerconfigrepository]]
- [[assistant_app_orchestrator_provider_selector_providerselector_init]] → `references` → [[assistant_app_repositories_provider_config_repository_providerconfigrepository]]
- [[assistant_app_orchestrator_provider_selector_providerselector_select]] → `references` → [[assistant_app_repositories_provider_config_repository_providerconfigrecord]]
- [[assistant_app_orchestrator_provider_selector_providerselector_select_by_type]] → `references` → [[assistant_app_repositories_provider_config_repository_providerconfigrecord]]
- [[assistant_app_orchestrator_provider_selector_providerselector_select_healthy]] → `references` → [[assistant_app_repositories_provider_config_repository_providerconfigrecord]]