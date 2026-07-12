# assistant\app\providers\automation\n8n_workflow_provider.py

## Símbolos

- [[assistant_app_providers_automation_n8n_workflow_provider]] — code: n8n_workflow_provider.py
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]] — code: N8NWorkflowProvider
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_init]] — code: .__init__()
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_get_headers]] — code: ._get_headers()
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_import_workflow]] — code: .import_workflow()
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_export_workflow]] — code: .export_workflow()
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_toggle_workflow]] — code: .toggle_workflow()
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_trigger_workflow]] — code: .trigger_workflow()
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_1]] — code: n8n Workflow Provider Implementation for K.A.O.S. Communicates with the n8n RES
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_30]] — code: Imports a workflow template.         Uses POST /api/v1/workflows to create it i
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_63]] — code: Retrieves a workflow schema by ID from n8n.         Uses GET /api/v1/workflows/
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_85]] — code: Activates or deactivates a workflow.         Uses POST /api/v1/workflows/{id}/a
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_108]] — code: Triggers a workflow by invoking its Webhook node.         webhook_path_or_id ca

## Dependências

- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]] → `uses` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]]
- [[assistant_app_providers_automation_n8n_workflow_provider]] → `contains` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]]
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_1]] → `rationale_for` → [[assistant_app_providers_automation_n8n_workflow_provider]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]] → `method` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_export_workflow]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]] → `method` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_get_headers]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]] → `method` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_import_workflow]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]] → `method` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_init]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]] → `method` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_toggle_workflow]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]] → `method` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_trigger_workflow]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_export_workflow]] → `calls` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_get_headers]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_import_workflow]] → `calls` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_get_headers]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_toggle_workflow]] → `calls` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_get_headers]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_import_workflow]] → `references` → [[assistant_app_providers_automation_n8n_workflow_provider_py_any]]
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_30]] → `rationale_for` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_import_workflow]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_export_workflow]] → `references` → [[assistant_app_providers_automation_n8n_workflow_provider_py_any]]
- [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_trigger_workflow]] → `references` → [[assistant_app_providers_automation_n8n_workflow_provider_py_any]]
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_63]] → `rationale_for` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_export_workflow]]
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_85]] → `rationale_for` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_toggle_workflow]]
- [[assistant_app_providers_automation_n8n_workflow_provider_rationale_108]] → `rationale_for` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider_trigger_workflow]]