# assistant\app\providers\automation\base_workflow_provider.py

## Símbolos

- [[assistant_app_providers_automation_base_workflow_provider]] — code: base_workflow_provider.py
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]] — code: BaseWorkflowProvider
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_import_workflow]] — code: .import_workflow()
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_export_workflow]] — code: .export_workflow()
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_toggle_workflow]] — code: .toggle_workflow()
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_trigger_workflow]] — code: .trigger_workflow()
- [[assistant_app_providers_automation_base_workflow_provider_rationale_1]] — code: Base Workflow Provider Interface for K.A.O.S. Defines the standard contract for
- [[assistant_app_providers_automation_base_workflow_provider_rationale_15]] — code: Imports a workflow template into the external automation engine.         Return
- [[assistant_app_providers_automation_base_workflow_provider_rationale_23]] — code: Exports the JSON schema of a workflow from the external engine.
- [[assistant_app_providers_automation_base_workflow_provider_rationale_30]] — code: Enables or disables the execution of a workflow.         Returns True if succes
- [[assistant_app_providers_automation_base_workflow_provider_rationale_40]] — code: Invokes/triggers a workflow execution.         Returns execution details like {

## Dependências

- [[assistant_app_providers_automation_base_workflow_provider]] → `contains` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]]
- [[assistant_app_providers_automation_base_workflow_provider]] → `imports_from` → [[assistant_app_providers_automation_base_workflow_provider_py_abc]]
- [[assistant_app_providers_automation_base_workflow_provider_rationale_1]] → `rationale_for` → [[assistant_app_providers_automation_base_workflow_provider]]
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]] → `method` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_export_workflow]]
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]] → `method` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_import_workflow]]
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]] → `method` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_toggle_workflow]]
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]] → `method` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_trigger_workflow]]
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]] → `inherits` → [[assistant_app_providers_automation_base_workflow_provider_py_abc]]
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_import_workflow]] → `references` → [[assistant_app_providers_automation_base_workflow_provider_py_any]]
- [[assistant_app_providers_automation_base_workflow_provider_rationale_15]] → `rationale_for` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_import_workflow]]
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_export_workflow]] → `references` → [[assistant_app_providers_automation_base_workflow_provider_py_any]]
- [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_trigger_workflow]] → `references` → [[assistant_app_providers_automation_base_workflow_provider_py_any]]
- [[assistant_app_providers_automation_base_workflow_provider_rationale_23]] → `rationale_for` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_export_workflow]]
- [[assistant_app_providers_automation_base_workflow_provider_rationale_30]] → `rationale_for` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_toggle_workflow]]
- [[assistant_app_providers_automation_base_workflow_provider_rationale_40]] → `rationale_for` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider_trigger_workflow]]