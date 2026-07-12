# assistant\app\api\integrations.py

## Símbolos

- [[assistant_app_api_integrations]] — code: integrations.py
- [[assistant_app_api_integrations_list_integrations]] — code: list_integrations()
- [[assistant_app_api_integrations_configure_integration]] — code: configure_integration()
- [[assistant_app_api_integrations_get_github_token]] — code: _get_github_token()
- [[assistant_app_api_integrations_get_github_runs]] — code: get_github_runs()
- [[assistant_app_api_integrations_trigger_github_workflow]] — code: trigger_github_workflow()
- [[assistant_app_api_integrations_rationale_1]] — code: Generic Integrations API.  Manages third-party service connections (GitHub, Di
- [[assistant_app_api_integrations_rationale_18]] — code: Return all configured integrations with their connection status.
- [[assistant_app_api_integrations_rationale_41]] — code: Configure or update an integration type with credentials.      Request body::
- [[assistant_app_api_integrations_rationale_100]] — code: Fetches real runs from GitHub Actions API or falls back gracefully.
- [[assistant_app_api_integrations_rationale_168]] — code: Trigger manual GitHub Actions pipeline run.

## Dependências

- [[assistant_app_api_integrations]] → `contains` → [[assistant_app_api_integrations_configure_integration]]
- [[assistant_app_api_integrations]] → `contains` → [[assistant_app_api_integrations_get_github_runs]]
- [[assistant_app_api_integrations]] → `contains` → [[assistant_app_api_integrations_get_github_token]]
- [[assistant_app_api_integrations]] → `contains` → [[assistant_app_api_integrations_list_integrations]]
- [[assistant_app_api_integrations]] → `contains` → [[assistant_app_api_integrations_trigger_github_workflow]]
- [[assistant_app_api_integrations]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_integrations_rationale_1]] → `rationale_for` → [[assistant_app_api_integrations]]
- [[assistant_app_api_integrations_list_integrations]] → `calls` → [[assistant_app_core_config_service_configservice_load_config]]
- [[assistant_app_api_integrations_rationale_18]] → `rationale_for` → [[assistant_app_api_integrations_list_integrations]]
- [[assistant_app_api_integrations_configure_integration]] → `calls` → [[assistant_app_core_config_service_configservice_load_config]]
- [[assistant_app_api_integrations_configure_integration]] → `calls` → [[assistant_app_core_config_service_configservice_load_secrets]]
- [[assistant_app_api_integrations_configure_integration]] → `calls` → [[assistant_app_core_config_service_configservice_save_config]]
- [[assistant_app_api_integrations_configure_integration]] → `calls` → [[assistant_app_core_config_service_configservice_save_secrets]]
- [[assistant_app_api_integrations_rationale_41]] → `rationale_for` → [[assistant_app_api_integrations_configure_integration]]
- [[assistant_app_api_integrations_get_github_runs]] → `calls` → [[assistant_app_api_integrations_get_github_token]]
- [[assistant_app_api_integrations_get_github_token]] → `calls` → [[assistant_app_core_config_service_configservice_load_secrets]]
- [[assistant_app_api_integrations_trigger_github_workflow]] → `calls` → [[assistant_app_api_integrations_get_github_token]]
- [[assistant_app_api_integrations_rationale_100]] → `rationale_for` → [[assistant_app_api_integrations_get_github_runs]]
- [[assistant_app_api_integrations_rationale_168]] → `rationale_for` → [[assistant_app_api_integrations_trigger_github_workflow]]