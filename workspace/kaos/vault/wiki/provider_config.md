# assistant\app\setup\provider_config.py

## Símbolos

- [[assistant_app_setup_provider_config]] — code: provider_config.py
- [[assistant_app_setup_provider_config_get_config_version]] — code: get_config_version()
- [[assistant_app_setup_provider_config_get_default_config]] — code: get_default_config()
- [[assistant_app_setup_provider_config_patch_settings]] — code: _patch_settings()
- [[assistant_app_setup_provider_config_bump_version]] — code: _bump_version()
- [[assistant_app_setup_provider_config_load_from_disk]] — code: _load_from_disk()
- [[assistant_app_setup_provider_config_save_to_disk]] — code: _save_to_disk()
- [[assistant_app_setup_provider_config_get_config]] — code: get_config()
- [[assistant_app_setup_provider_config_save_config]] — code: save_config()
- [[assistant_app_setup_provider_config_get_active_provider_config]] — code: get_active_provider_config()
- [[assistant_app_setup_provider_config_rationale_63]] — code: Resolve provider default configurations dynamically from environment settings.
- [[assistant_app_setup_provider_config_rationale_117]] — code: Load configuration from ConfigService (central settings file).
- [[assistant_app_setup_provider_config_rationale_143]] — code: Save configuration to ConfigService (separating public config and secrets).

## Dependências

- [[assistant_app_setup_provider_config_load_from_disk]] → `calls` → [[assistant_app_core_config_service_configservice_load_config]]
- [[assistant_app_setup_provider_config_save_to_disk]] → `calls` → [[assistant_app_core_config_service_configservice_load_config]]
- [[assistant_app_setup_provider_config_save_to_disk]] → `calls` → [[assistant_app_core_config_service_configservice_save_config]]
- [[assistant_app_setup_provider_config_load_from_disk]] → `calls` → [[assistant_app_core_config_service_configservice_load_secrets]]
- [[assistant_app_setup_provider_config_save_to_disk]] → `calls` → [[assistant_app_core_config_service_configservice_load_secrets]]
- [[assistant_app_setup_provider_config_save_to_disk]] → `calls` → [[assistant_app_core_config_service_configservice_save_secrets]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_bump_version]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_get_active_provider_config]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_get_config]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_get_config_version]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_get_default_config]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_load_from_disk]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_patch_settings]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_save_config]]
- [[assistant_app_setup_provider_config]] → `contains` → [[assistant_app_setup_provider_config_save_to_disk]]
- [[assistant_app_setup_provider_config_get_active_provider_config]] → `calls` → [[assistant_app_setup_provider_config_get_default_config]]
- [[assistant_app_setup_provider_config_get_config]] → `calls` → [[assistant_app_setup_provider_config_get_default_config]]
- [[assistant_app_setup_provider_config_rationale_63]] → `rationale_for` → [[assistant_app_setup_provider_config_get_default_config]]
- [[assistant_app_setup_provider_config_save_config]] → `calls` → [[assistant_app_setup_provider_config_get_default_config]]
- [[assistant_app_setup_provider_config_save_config]] → `calls` → [[assistant_app_setup_provider_config_patch_settings]]
- [[assistant_app_setup_provider_config_save_config]] → `calls` → [[assistant_app_setup_provider_config_bump_version]]
- [[assistant_app_setup_provider_config_get_active_provider_config]] → `calls` → [[assistant_app_setup_provider_config_load_from_disk]]
- [[assistant_app_setup_provider_config_get_config]] → `calls` → [[assistant_app_setup_provider_config_load_from_disk]]
- [[assistant_app_setup_provider_config_load_from_disk]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_setup_provider_config_rationale_117]] → `rationale_for` → [[assistant_app_setup_provider_config_load_from_disk]]
- [[assistant_app_setup_provider_config_rationale_143]] → `rationale_for` → [[assistant_app_setup_provider_config_save_to_disk]]
- [[assistant_app_setup_provider_config_save_config]] → `calls` → [[assistant_app_setup_provider_config_save_to_disk]]
- [[assistant_app_setup_provider_config_save_to_disk]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]