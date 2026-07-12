# assistant\app\api\automation.py

## Símbolos

- [[assistant_app_api_automation]] — code: automation.py
- [[assistant_app_api_automation_list_templates]] — code: list_templates()
- [[assistant_app_api_automation_infer_category]] — code: _infer_category()
- [[assistant_app_api_automation_list_workflows]] — code: list_workflows()
- [[assistant_app_api_automation_import_workflow]] — code: import_workflow()
- [[assistant_app_api_automation_toggle_workflow]] — code: toggle_workflow()
- [[assistant_app_api_automation_get_execution_history]] — code: get_execution_history()
- [[assistant_app_api_automation_rationale_1]] — code: FastAPI Router for K.A.O.S Automation Platform. Handles workflow query, templat
- [[assistant_app_api_automation_rationale_22]] — code: Lista templates disponiveis no Marketplace (da pasta data/workflows/).
- [[assistant_app_api_automation_rationale_48]] — code: Infere categoria do workflow baseado nos nodes.
- [[assistant_app_api_automation_rationale_68]] — code: Lists all registered workflows in the K.A.O.S system.
- [[assistant_app_api_automation_rationale_95]] — code: Imports a new workflow JSON template.     Saves to n8n first, then registers in
- [[assistant_app_api_automation_rationale_150]] — code: Enables or disables a workflow in both n8n and K.A.O.S Postgres database.
- [[assistant_app_api_automation_rationale_188]] — code: Returns execution logs of all automated runs.

## Dependências

- [[assistant_app_api_automation]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_automation]] → `contains` → [[assistant_app_api_automation_get_execution_history]]
- [[assistant_app_api_automation]] → `contains` → [[assistant_app_api_automation_import_workflow]]
- [[assistant_app_api_automation]] → `contains` → [[assistant_app_api_automation_infer_category]]
- [[assistant_app_api_automation]] → `contains` → [[assistant_app_api_automation_list_templates]]
- [[assistant_app_api_automation]] → `contains` → [[assistant_app_api_automation_list_workflows]]
- [[assistant_app_api_automation]] → `imports_from` → [[assistant_app_api_automation_py_uuid]]
- [[assistant_app_api_automation]] → `contains` → [[assistant_app_api_automation_toggle_workflow]]
- [[assistant_app_api_automation]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_automation_rationale_1]] → `rationale_for` → [[assistant_app_api_automation]]
- [[assistant_app_api_automation_list_templates]] → `calls` → [[assistant_app_api_automation_infer_category]]
- [[assistant_app_api_automation_list_templates]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_api_automation_rationale_22]] → `rationale_for` → [[assistant_app_api_automation_list_templates]]
- [[assistant_app_api_automation_rationale_48]] → `rationale_for` → [[assistant_app_api_automation_infer_category]]
- [[assistant_app_api_automation_list_workflows]] → `references` → [[assistant_app_api_automation_py_any]]
- [[assistant_app_api_automation_list_workflows]] → `references` → [[assistant_app_api_automation_py_asyncsession]]
- [[assistant_app_api_automation_list_workflows]] → `indirect_call` → [[assistant_app_models_automation_registry_automationworkflow]]
- [[assistant_app_api_automation_rationale_68]] → `rationale_for` → [[assistant_app_api_automation_list_workflows]]
- [[assistant_app_api_automation_get_execution_history]] → `references` → [[assistant_app_api_automation_py_asyncsession]]
- [[assistant_app_api_automation_import_workflow]] → `references` → [[assistant_app_api_automation_py_asyncsession]]
- [[assistant_app_api_automation_toggle_workflow]] → `references` → [[assistant_app_api_automation_py_asyncsession]]
- [[assistant_app_api_automation_get_execution_history]] → `references` → [[assistant_app_api_automation_py_any]]
- [[assistant_app_api_automation_import_workflow]] → `references` → [[assistant_app_api_automation_py_any]]
- [[assistant_app_api_automation_toggle_workflow]] → `references` → [[assistant_app_api_automation_py_any]]
- [[assistant_app_api_automation_import_workflow]] → `calls` → [[assistant_app_core_automation_bus_automationbus_get_provider]]
- [[assistant_app_api_automation_import_workflow]] → `calls` → [[assistant_app_models_automation_registry_automationworkflow]]
- [[assistant_app_api_automation_rationale_95]] → `rationale_for` → [[assistant_app_api_automation_import_workflow]]
- [[assistant_app_api_automation_rationale_150]] → `rationale_for` → [[assistant_app_api_automation_toggle_workflow]]
- [[assistant_app_api_automation_toggle_workflow]] → `references` → [[assistant_app_api_automation_py_uuid]]
- [[assistant_app_api_automation_toggle_workflow]] → `calls` → [[assistant_app_core_automation_bus_automationbus_get_provider]]
- [[assistant_app_api_automation_toggle_workflow]] → `indirect_call` → [[assistant_app_models_automation_registry_automationworkflow]]
- [[assistant_app_api_automation_get_execution_history]] → `indirect_call` → [[assistant_app_models_automation_registry_automationexecution]]
- [[assistant_app_api_automation_rationale_188]] → `rationale_for` → [[assistant_app_api_automation_get_execution_history]]