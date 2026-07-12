# assistant\tests\test_automation.py

## Símbolos

- [[assistant_tests_test_automation]] — code: test_automation.py
- [[assistant_tests_test_automation_client]] — code: client()
- [[assistant_tests_test_automation_ensure_workflow_templates]] — code: _ensure_workflow_templates()
- [[assistant_tests_test_automation_test_list_workflows_empty_db]] — code: test_list_workflows_empty_db()
- [[assistant_tests_test_automation_test_n8n_callback_unregistered_workflow]] — code: test_n8n_callback_unregistered_workflow()
- [[assistant_tests_test_automation_test_list_templates_no_dir]] — code: test_list_templates_no_dir()
- [[assistant_tests_test_automation_test_list_templates_uses_real_files]] — code: test_list_templates_uses_real_files()
- [[assistant_tests_test_automation_test_list_templates_has_names]] — code: test_list_templates_has_names()
- [[assistant_tests_test_automation_test_list_templates_categories_present]] — code: test_list_templates_categories_present()
- [[assistant_tests_test_automation_test_import_workflow_validates_name]] — code: test_import_workflow_validates_name()
- [[assistant_tests_test_automation_test_import_workflow_validates_json]] — code: test_import_workflow_validates_json()
- [[assistant_tests_test_automation_rationale_24]] — code: Cria templates de workflow minimos para que os testes passem em CI.
- [[assistant_tests_test_automation_rationale_117]] — code: Quando data/workflows/ nao existe, retorna lista vazia.
- [[assistant_tests_test_automation_rationale_128]] — code: Usa os templates reais em data/workflows/ (criados na Fase 7).
- [[assistant_tests_test_automation_rationale_139]] — code: Templates retornados tem nome e descricao.
- [[assistant_tests_test_automation_rationale_151]] — code: Categorias incluem valores esperados.
- [[assistant_tests_test_automation_rationale_161]] — code: Import sem nome retorna 422.
- [[assistant_tests_test_automation_rationale_168]] — code: Import sem json_data retorna 422.

## Dependências

- [[assistant_tests_test_automation]] → `imports_from` → [[assistant_app_database]]
- [[assistant_tests_test_automation]] → `imports_from` → [[assistant_app_main]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_client]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_ensure_workflow_templates]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_test_import_workflow_validates_json]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_test_import_workflow_validates_name]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_test_list_templates_categories_present]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_test_list_templates_has_names]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_test_list_templates_no_dir]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_test_list_templates_uses_real_files]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_test_list_workflows_empty_db]]
- [[assistant_tests_test_automation]] → `contains` → [[assistant_tests_test_automation_test_n8n_callback_unregistered_workflow]]
- [[assistant_tests_test_automation_client]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_automation_ensure_workflow_templates]] → `references` → [[assistant_tests_test_automation_py_any]]
- [[assistant_tests_test_automation_ensure_workflow_templates]] → `references` → [[assistant_tests_test_automation_py_path]]
- [[assistant_tests_test_automation_rationale_24]] → `rationale_for` → [[assistant_tests_test_automation_ensure_workflow_templates]]
- [[assistant_tests_test_automation_test_list_workflows_empty_db]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_automation_test_n8n_callback_unregistered_workflow]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_automation_rationale_117]] → `rationale_for` → [[assistant_tests_test_automation_test_list_templates_no_dir]]
- [[assistant_tests_test_automation_test_list_templates_no_dir]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_automation_rationale_128]] → `rationale_for` → [[assistant_tests_test_automation_test_list_templates_uses_real_files]]
- [[assistant_tests_test_automation_test_list_templates_uses_real_files]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_automation_rationale_139]] → `rationale_for` → [[assistant_tests_test_automation_test_list_templates_has_names]]
- [[assistant_tests_test_automation_test_list_templates_has_names]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_automation_rationale_151]] → `rationale_for` → [[assistant_tests_test_automation_test_list_templates_categories_present]]
- [[assistant_tests_test_automation_test_list_templates_categories_present]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_automation_rationale_161]] → `rationale_for` → [[assistant_tests_test_automation_test_import_workflow_validates_name]]
- [[assistant_tests_test_automation_test_import_workflow_validates_name]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_automation_rationale_168]] → `rationale_for` → [[assistant_tests_test_automation_test_import_workflow_validates_json]]
- [[assistant_tests_test_automation_test_import_workflow_validates_json]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]