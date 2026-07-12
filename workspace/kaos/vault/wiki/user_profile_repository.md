# assistant\app\repositories\user_profile_repository.py

## Símbolos

- [[assistant_app_repositories_user_profile_repository]] — code: user_profile_repository.py
- [[assistant_app_repositories_user_profile_repository_userprofilerecord]] — code: UserProfileRecord
- [[assistant_app_repositories_user_profile_repository_userprofilerepository]] — code: UserProfileRepository
- [[assistant_app_repositories_user_profile_repository_userprofilerepository_init]] — code: .__init__()
- [[assistant_app_repositories_user_profile_repository_userprofilerepository_get]] — code: .get()
- [[assistant_app_repositories_user_profile_repository_userprofilerepository_upsert]] — code: .upsert()

## Dependências

- [[assistant_app_repositories_user_profile_repository]] → `contains` → [[assistant_app_repositories_user_profile_repository_userprofilerecord]]
- [[assistant_app_repositories_user_profile_repository]] → `contains` → [[assistant_app_repositories_user_profile_repository_userprofilerepository]]
- [[assistant_app_repositories_user_profile_repository_userprofilerepository_get]] → `references` → [[assistant_app_repositories_user_profile_repository_userprofilerecord]]
- [[assistant_app_repositories_user_profile_repository_userprofilerepository_upsert]] → `references` → [[assistant_app_repositories_user_profile_repository_userprofilerecord]]
- [[assistant_app_repositories_user_profile_repository_userprofilerepository]] → `method` → [[assistant_app_repositories_user_profile_repository_userprofilerepository_get]]
- [[assistant_app_repositories_user_profile_repository_userprofilerepository]] → `method` → [[assistant_app_repositories_user_profile_repository_userprofilerepository_init]]
- [[assistant_app_repositories_user_profile_repository_userprofilerepository]] → `method` → [[assistant_app_repositories_user_profile_repository_userprofilerepository_upsert]]
- [[assistant_app_repositories_user_profile_repository_userprofilerepository_init]] → `references` → [[assistant_app_repositories_user_profile_repository_py_asyncsession]]
- [[assistant_app_repositories_user_profile_repository_userprofilerepository_get]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_user_profile_repository_userprofilerepository_upsert]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]