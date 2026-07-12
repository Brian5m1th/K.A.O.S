# assistant\app\api\provider_configs.py

## Símbolos

- [[assistant_app_api_provider_configs]] — code: provider_configs.py
- [[assistant_app_api_provider_configs_list_provider_configs]] — code: list_provider_configs()
- [[assistant_app_api_provider_configs_get_provider_config]] — code: get_provider_config()
- [[assistant_app_api_provider_configs_upsert_provider_config]] — code: upsert_provider_config()
- [[assistant_app_api_provider_configs_delete_provider_config]] — code: delete_provider_config()

## Dependências

- [[assistant_app_api_provider_configs]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_provider_configs]] → `contains` → [[assistant_app_api_provider_configs_delete_provider_config]]
- [[assistant_app_api_provider_configs]] → `contains` → [[assistant_app_api_provider_configs_get_provider_config]]
- [[assistant_app_api_provider_configs]] → `contains` → [[assistant_app_api_provider_configs_list_provider_configs]]
- [[assistant_app_api_provider_configs]] → `contains` → [[assistant_app_api_provider_configs_upsert_provider_config]]
- [[assistant_app_api_provider_configs]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_provider_configs_list_provider_configs]] → `references` → [[assistant_app_api_provider_configs_py_asyncsession]]
- [[assistant_app_api_provider_configs_list_provider_configs]] → `calls` → [[assistant_app_repositories_provider_config_repository_providerconfigrepository]]
- [[assistant_app_api_provider_configs_delete_provider_config]] → `references` → [[assistant_app_api_provider_configs_py_asyncsession]]
- [[assistant_app_api_provider_configs_get_provider_config]] → `references` → [[assistant_app_api_provider_configs_py_asyncsession]]
- [[assistant_app_api_provider_configs_upsert_provider_config]] → `references` → [[assistant_app_api_provider_configs_py_asyncsession]]
- [[assistant_app_api_provider_configs_get_provider_config]] → `calls` → [[assistant_app_repositories_provider_config_repository_providerconfigrepository]]
- [[assistant_app_api_provider_configs_upsert_provider_config]] → `references` → [[assistant_app_api_provider_configs_py_any]]
- [[assistant_app_api_provider_configs_upsert_provider_config]] → `calls` → [[assistant_app_repositories_provider_config_repository_providerconfigrecord]]
- [[assistant_app_api_provider_configs_upsert_provider_config]] → `calls` → [[assistant_app_repositories_provider_config_repository_providerconfigrepository]]
- [[assistant_app_api_provider_configs_delete_provider_config]] → `calls` → [[assistant_app_repositories_provider_config_repository_providerconfigrepository]]