# assistant\app\api\user_model_profiles.py

## Símbolos

- [[assistant_app_api_user_model_profiles]] — code: user_model_profiles.py
- [[assistant_app_api_user_model_profiles_list_user_profiles]] — code: list_user_profiles()
- [[assistant_app_api_user_model_profiles_get_user_profile]] — code: get_user_profile()
- [[assistant_app_api_user_model_profiles_upsert_user_profile]] — code: upsert_user_profile()
- [[assistant_app_api_user_model_profiles_delete_user_profile]] — code: delete_user_profile()

## Dependências

- [[assistant_app_api_user_model_profiles]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_user_model_profiles]] → `contains` → [[assistant_app_api_user_model_profiles_delete_user_profile]]
- [[assistant_app_api_user_model_profiles]] → `contains` → [[assistant_app_api_user_model_profiles_get_user_profile]]
- [[assistant_app_api_user_model_profiles]] → `contains` → [[assistant_app_api_user_model_profiles_list_user_profiles]]
- [[assistant_app_api_user_model_profiles]] → `contains` → [[assistant_app_api_user_model_profiles_upsert_user_profile]]
- [[assistant_app_api_user_model_profiles]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_user_model_profiles_list_user_profiles]] → `references` → [[assistant_app_api_user_model_profiles_py_asyncsession]]
- [[assistant_app_api_user_model_profiles_list_user_profiles]] → `calls` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]]
- [[assistant_app_api_user_model_profiles_delete_user_profile]] → `references` → [[assistant_app_api_user_model_profiles_py_asyncsession]]
- [[assistant_app_api_user_model_profiles_get_user_profile]] → `references` → [[assistant_app_api_user_model_profiles_py_asyncsession]]
- [[assistant_app_api_user_model_profiles_upsert_user_profile]] → `references` → [[assistant_app_api_user_model_profiles_py_asyncsession]]
- [[assistant_app_api_user_model_profiles_get_user_profile]] → `calls` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]]
- [[assistant_app_api_user_model_profiles_upsert_user_profile]] → `calls` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]]
- [[assistant_app_api_user_model_profiles_delete_user_profile]] → `calls` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]]