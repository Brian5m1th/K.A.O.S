# assistant\app\api\webhooks.py

## Símbolos

- [[assistant_app_api_webhooks]] — code: webhooks.py
- [[assistant_app_api_webhooks_n8n_callback]] — code: n8n_callback()
- [[assistant_app_api_webhooks_n8n_webhook]] — code: n8n_webhook()
- [[assistant_app_api_webhooks_n8n_chat_webhook]] — code: n8n_chat_webhook()
- [[assistant_app_api_webhooks_n8n_memory_webhook]] — code: n8n_memory_webhook()
- [[assistant_app_api_webhooks_n8n_agent_webhook]] — code: n8n_agent_webhook()
- [[assistant_app_api_webhooks_n8n_register_webhook]] — code: n8n_register_webhook()
- [[assistant_app_api_webhooks_n8n_webhook_info]] — code: n8n_webhook_info()
- [[assistant_app_api_webhooks_rationale_14]] — code: Callback triggered by n8n to report execution results (success/failure/durations

## Dependências

- [[assistant_app_api_webhooks]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_webhooks]] → `contains` → [[assistant_app_api_webhooks_n8n_agent_webhook]]
- [[assistant_app_api_webhooks]] → `contains` → [[assistant_app_api_webhooks_n8n_callback]]
- [[assistant_app_api_webhooks]] → `contains` → [[assistant_app_api_webhooks_n8n_chat_webhook]]
- [[assistant_app_api_webhooks]] → `contains` → [[assistant_app_api_webhooks_n8n_memory_webhook]]
- [[assistant_app_api_webhooks]] → `contains` → [[assistant_app_api_webhooks_n8n_register_webhook]]
- [[assistant_app_api_webhooks]] → `contains` → [[assistant_app_api_webhooks_n8n_webhook]]
- [[assistant_app_api_webhooks]] → `contains` → [[assistant_app_api_webhooks_n8n_webhook_info]]
- [[assistant_app_api_webhooks]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_webhooks_n8n_callback]] → `indirect_call` → [[assistant_app_models_automation_registry_automationexecution]]
- [[assistant_app_api_webhooks_n8n_callback]] → `indirect_call` → [[assistant_app_models_automation_registry_automationworkflow]]
- [[assistant_app_api_webhooks_n8n_callback]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_webhooks_rationale_14]] → `rationale_for` → [[assistant_app_api_webhooks_n8n_callback]]
- [[assistant_app_api_webhooks_n8n_webhook]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_webhooks_n8n_chat_webhook]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_webhooks_n8n_memory_webhook]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_webhooks_n8n_agent_webhook]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_webhooks_n8n_register_webhook]] → `references` → [[graphify_worked_httpx_raw_models_request]]