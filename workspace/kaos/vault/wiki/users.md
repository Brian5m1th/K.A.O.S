# assistant\app\api\users.py

## Símbolos

- [[assistant_app_api_users]] — code: users.py
- [[assistant_app_api_users_get_user]] — code: get_user()
- [[assistant_app_api_users_upsert_user]] — code: upsert_user()

## Dependências

- [[assistant_app_api_users]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_users]] → `contains` → [[assistant_app_api_users_get_user]]
- [[assistant_app_api_users]] → `contains` → [[assistant_app_api_users_upsert_user]]
- [[assistant_app_api_users]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_users_get_user]] → `references` → [[assistant_app_api_users_py_asyncsession]]
- [[assistant_app_api_users_get_user]] → `calls` → [[assistant_app_repositories_user_profile_repository_userprofilerepository]]
- [[assistant_app_api_users_get_user]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[assistant_app_api_users_upsert_user]] → `references` → [[assistant_app_api_users_py_asyncsession]]
- [[assistant_app_api_users_upsert_user]] → `calls` → [[assistant_app_repositories_user_profile_repository_userprofilerecord]]
- [[assistant_app_api_users_upsert_user]] → `calls` → [[assistant_app_repositories_user_profile_repository_userprofilerepository]]
- [[assistant_app_api_users_upsert_user]] → `references` → [[graphify_worked_httpx_raw_models_request]]