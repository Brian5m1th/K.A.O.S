# assistant\app\providers\memory\postgres.py

## Símbolos

- [[assistant_app_providers_memory_postgres]] — code: postgres.py
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] — code: PostgresMemoryProvider
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_init]] — code: .__init__()
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_ensure_repo]] — code: ._ensure_repo()
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_save]] — code: .save()
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_load]] — code: .load()
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_clear]] — code: .clear()
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `uses` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_ensure_repo]] → `references` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_ensure_repo]] → `calls` → [[assistant_app_memory_postgres_repository_get_postgres_repository]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `inherits` → [[assistant_app_providers_base_memory_basememoryprovider]]
- [[assistant_app_providers_memory_postgres]] → `contains` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `method` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_clear]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `method` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_ensure_repo]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `method` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_healthcheck]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `method` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_init]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `method` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_load]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider]] → `method` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_save]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_healthcheck]] → `calls` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_ensure_repo]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_load]] → `calls` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_ensure_repo]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_save]] → `calls` → [[assistant_app_providers_memory_postgres_postgresmemoryprovider_ensure_repo]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_save]] → `references` → [[assistant_app_providers_memory_postgres_py_message]]
- [[assistant_app_providers_memory_postgres_postgresmemoryprovider_load]] → `references` → [[assistant_app_providers_memory_postgres_py_message]]