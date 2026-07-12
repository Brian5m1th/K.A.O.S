# assistant\app\repositories\user_model_profile_repository.py

## Símbolos

- [[assistant_app_repositories_user_model_profile_repository]] — code: user_model_profile_repository.py
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerecord]] — code: UserModelProfileRecord
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]] — code: UserModelProfileRepository
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_init]] — code: .__init__()
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_get]] — code: .get()
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_upsert]] — code: .upsert()
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_list_by_user]] — code: .list_by_user()
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_delete]] — code: .delete()

## Dependências

- [[assistant_app_repositories_user_model_profile_repository]] → `imports_from` → [[assistant_app_repositories_user_model_profile_repository_py_uuid]]
- [[assistant_app_repositories_user_model_profile_repository]] → `contains` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerecord]]
- [[assistant_app_repositories_user_model_profile_repository]] → `contains` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_get]] → `references` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerecord]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_list_by_user]] → `references` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerecord]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]] → `method` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_delete]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]] → `method` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_get]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]] → `method` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_init]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]] → `method` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_list_by_user]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]] → `method` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_upsert]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_init]] → `references` → [[assistant_app_repositories_user_model_profile_repository_py_asyncsession]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_get]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_upsert]] → `references` → [[assistant_app_repositories_user_model_profile_repository_py_uuid]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_upsert]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_delete]] → `references` → [[assistant_app_repositories_user_model_profile_repository_py_uuid]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_list_by_user]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository_delete]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]