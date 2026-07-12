# assistant\app\api\settings_api.py

## Símbolos

- [[assistant_app_api_settings_api]] — code: settings_api.py
- [[assistant_app_api_settings_api_get_settings]] — code: get_settings()
- [[assistant_app_api_settings_api_save_settings]] — code: save_settings()

## Dependências

- [[assistant_app_api_settings_api]] → `contains` → [[assistant_app_api_settings_api_get_settings]]
- [[assistant_app_api_settings_api]] → `contains` → [[assistant_app_api_settings_api_save_settings]]
- [[assistant_app_api_settings_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_settings_api_get_settings]] → `calls` → [[assistant_app_core_config_service_configservice_load_config]]
- [[assistant_app_api_settings_api_save_settings]] → `calls` → [[assistant_app_core_config_service_configservice_load_config]]
- [[assistant_app_api_settings_api_save_settings]] → `calls` → [[assistant_app_core_config_service_configservice_save_config]]