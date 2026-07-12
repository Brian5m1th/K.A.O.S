# assistant\app\api\capabilities.py

## Símbolos

- [[assistant_app_api_capabilities]] — code: capabilities.py
- [[assistant_app_api_capabilities_list_policies]] — code: list_policies()
- [[assistant_app_api_capabilities_get_policies_by_capability]] — code: get_policies_by_capability()
- [[assistant_app_api_capabilities_create_policy]] — code: create_policy()
- [[assistant_app_api_capabilities_delete_policy]] — code: delete_policy()

## Dependências

- [[assistant_app_api_capabilities]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_capabilities]] → `contains` → [[assistant_app_api_capabilities_create_policy]]
- [[assistant_app_api_capabilities]] → `contains` → [[assistant_app_api_capabilities_delete_policy]]
- [[assistant_app_api_capabilities]] → `contains` → [[assistant_app_api_capabilities_get_policies_by_capability]]
- [[assistant_app_api_capabilities]] → `contains` → [[assistant_app_api_capabilities_list_policies]]
- [[assistant_app_api_capabilities]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_capabilities_list_policies]] → `references` → [[assistant_app_api_capabilities_py_asyncsession]]
- [[assistant_app_api_capabilities_list_policies]] → `calls` → [[assistant_app_repositories_capability_policy_repository_capabilitypolicyrepository]]
- [[assistant_app_api_capabilities_create_policy]] → `references` → [[assistant_app_api_capabilities_py_asyncsession]]
- [[assistant_app_api_capabilities_delete_policy]] → `references` → [[assistant_app_api_capabilities_py_asyncsession]]
- [[assistant_app_api_capabilities_get_policies_by_capability]] → `references` → [[assistant_app_api_capabilities_py_asyncsession]]
- [[assistant_app_api_capabilities_get_policies_by_capability]] → `calls` → [[assistant_app_repositories_capability_policy_repository_capabilitypolicyrepository]]
- [[assistant_app_api_capabilities_create_policy]] → `calls` → [[assistant_app_repositories_capability_policy_repository_capabilitypolicyrepository]]
- [[assistant_app_api_capabilities_delete_policy]] → `calls` → [[assistant_app_repositories_capability_policy_repository_capabilitypolicyrepository]]