# assistant\app\api\feature_flags.py

## Símbolos

- [[assistant_app_api_feature_flags]] — code: feature_flags.py
- [[assistant_app_api_feature_flags_list_flags]] — code: list_flags()
- [[assistant_app_api_feature_flags_get_flag]] — code: get_flag()
- [[assistant_app_api_feature_flags_set_flag]] — code: set_flag()

## Dependências

- [[assistant_app_api_feature_flags]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_feature_flags]] → `contains` → [[assistant_app_api_feature_flags_get_flag]]
- [[assistant_app_api_feature_flags]] → `contains` → [[assistant_app_api_feature_flags_list_flags]]
- [[assistant_app_api_feature_flags]] → `contains` → [[assistant_app_api_feature_flags_set_flag]]
- [[assistant_app_api_feature_flags]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_feature_flags_list_flags]] → `references` → [[assistant_app_api_feature_flags_py_asyncsession]]
- [[assistant_app_api_feature_flags_list_flags]] → `calls` → [[assistant_app_repositories_feature_flag_repository_featureflagrepository]]
- [[assistant_app_api_feature_flags_get_flag]] → `references` → [[assistant_app_api_feature_flags_py_asyncsession]]
- [[assistant_app_api_feature_flags_set_flag]] → `references` → [[assistant_app_api_feature_flags_py_asyncsession]]
- [[assistant_app_api_feature_flags_get_flag]] → `calls` → [[assistant_app_repositories_feature_flag_repository_featureflagrepository]]
- [[assistant_app_api_feature_flags_set_flag]] → `calls` → [[assistant_app_repositories_feature_flag_repository_featureflagrepository]]