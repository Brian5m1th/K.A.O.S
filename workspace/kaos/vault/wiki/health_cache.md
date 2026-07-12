# assistant\app\orchestrator\health_cache.py

## Símbolos

- [[assistant_app_orchestrator_health_cache]] — code: health_cache.py
- [[assistant_app_orchestrator_health_cache_healthstatus]] — code: HealthStatus
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] — code: ProviderHealthCache
- [[assistant_app_orchestrator_health_cache_providerhealthcache_init]] — code: .__init__()
- [[assistant_app_orchestrator_health_cache_providerhealthcache_is_healthy]] — code: .is_healthy()
- [[assistant_app_orchestrator_health_cache_providerhealthcache_get_health]] — code: .get_health()
- [[assistant_app_orchestrator_health_cache_providerhealthcache_set_health]] — code: .set_health()
- [[assistant_app_orchestrator_health_cache_providerhealthcache_mark_healthy]] — code: .mark_healthy()
- [[assistant_app_orchestrator_health_cache_providerhealthcache_mark_unhealthy]] — code: .mark_unhealthy()
- [[assistant_app_orchestrator_health_cache_providerhealthcache_refresh]] — code: .refresh()
- [[assistant_app_orchestrator_health_cache_providerhealthcache_entries]] — code: .entries()
- [[assistant_app_orchestrator_health_cache_providerhealthcache_clear]] — code: .clear()

## Dependências

- [[assistant_app_orchestrator_health_cache]] → `contains` → [[assistant_app_orchestrator_health_cache_healthstatus]]
- [[assistant_app_orchestrator_health_cache]] → `contains` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_orchestrator_health_cache]] → `imports_from` → [[assistant_app_orchestrator_health_cache_py_enum]]
- [[assistant_app_orchestrator_health_cache_healthstatus]] → `inherits` → [[assistant_app_orchestrator_health_cache_py_enum]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache_get_health]] → `references` → [[assistant_app_orchestrator_health_cache_healthstatus]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache_refresh]] → `references` → [[assistant_app_orchestrator_health_cache_healthstatus]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache_set_health]] → `references` → [[assistant_app_orchestrator_health_cache_healthstatus]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_clear]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_entries]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_get_health]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_init]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_is_healthy]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_mark_healthy]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_mark_unhealthy]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_refresh]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache]] → `method` → [[assistant_app_orchestrator_health_cache_providerhealthcache_set_health]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache_is_healthy]] → `calls` → [[assistant_app_orchestrator_health_cache_providerhealthcache_get_health]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache_mark_healthy]] → `calls` → [[assistant_app_orchestrator_health_cache_providerhealthcache_set_health]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache_mark_unhealthy]] → `calls` → [[assistant_app_orchestrator_health_cache_providerhealthcache_set_health]]
- [[assistant_app_orchestrator_health_cache_providerhealthcache_refresh]] → `calls` → [[assistant_app_orchestrator_health_cache_providerhealthcache_set_health]]