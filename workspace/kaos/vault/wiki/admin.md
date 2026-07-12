# assistant\app\api\admin.py

## Símbolos

- [[assistant_app_api_admin]] — code: admin.py
- [[assistant_app_api_admin_createuserrequest]] — code: CreateUserRequest
- [[assistant_app_api_admin_updateuserrolerequest]] — code: UpdateUserRoleRequest
- [[assistant_app_api_admin_list_users]] — code: list_users()
- [[assistant_app_api_admin_create_user]] — code: create_user()
- [[assistant_app_api_admin_update_user_role]] — code: update_user_role()
- [[assistant_app_api_admin_delete_user]] — code: delete_user()

## Dependências

- [[assistant_app_api_admin]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_admin]] → `contains` → [[assistant_app_api_admin_create_user]]
- [[assistant_app_api_admin]] → `contains` → [[assistant_app_api_admin_createuserrequest]]
- [[assistant_app_api_admin]] → `contains` → [[assistant_app_api_admin_delete_user]]
- [[assistant_app_api_admin]] → `contains` → [[assistant_app_api_admin_list_users]]
- [[assistant_app_api_admin]] → `contains` → [[assistant_app_api_admin_update_user_role]]
- [[assistant_app_api_admin]] → `contains` → [[assistant_app_api_admin_updateuserrolerequest]]
- [[assistant_app_api_admin]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_admin_create_user]] → `references` → [[assistant_app_api_admin_createuserrequest]]
- [[assistant_app_api_admin_createuserrequest]] → `inherits` → [[assistant_app_api_admin_py_basemodel]]
- [[assistant_app_api_admin_updateuserrolerequest]] → `inherits` → [[assistant_app_api_admin_py_basemodel]]
- [[assistant_app_api_admin_update_user_role]] → `references` → [[assistant_app_api_admin_updateuserrolerequest]]
- [[assistant_app_api_admin_list_users]] → `references` → [[assistant_app_api_admin_py_asyncsession]]
- [[assistant_app_api_admin_list_users]] → `indirect_call` → [[assistant_app_models_user_user]]
- [[assistant_app_api_admin_list_users]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_admin_create_user]] → `references` → [[assistant_app_api_admin_py_asyncsession]]
- [[assistant_app_api_admin_delete_user]] → `references` → [[assistant_app_api_admin_py_asyncsession]]
- [[assistant_app_api_admin_update_user_role]] → `references` → [[assistant_app_api_admin_py_asyncsession]]
- [[assistant_app_api_admin_create_user]] → `calls` → [[assistant_app_auth_hash_hash_password]]
- [[assistant_app_api_admin_create_user]] → `indirect_call` → [[assistant_app_models_user_user]]
- [[assistant_app_api_admin_create_user]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_admin_update_user_role]] → `indirect_call` → [[assistant_app_models_user_user]]
- [[assistant_app_api_admin_update_user_role]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_admin_delete_user]] → `indirect_call` → [[assistant_app_models_user_user]]
- [[assistant_app_api_admin_delete_user]] → `references` → [[graphify_worked_httpx_raw_models_request]]