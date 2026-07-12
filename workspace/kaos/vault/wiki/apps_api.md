# assistant\app\api\apps_api.py

## Símbolos

- [[assistant_app_api_apps_api]] — code: apps_api.py
- [[assistant_app_api_apps_api_list_apps]] — code: list_apps()
- [[assistant_app_api_apps_api_get_app]] — code: get_app()

## Dependências

- [[assistant_app_api_apps_api]] → `contains` → [[assistant_app_api_apps_api_get_app]]
- [[assistant_app_api_apps_api]] → `contains` → [[assistant_app_api_apps_api_list_apps]]
- [[assistant_app_api_apps_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_apps_api_get_app]] → `calls` → [[assistant_app_apps_registry_appregistry_get]]