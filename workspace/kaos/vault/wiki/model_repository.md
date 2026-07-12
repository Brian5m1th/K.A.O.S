# assistant\app\repositories\model_repository.py

## Símbolos

- [[assistant_app_repositories_model_repository]] — code: model_repository.py
- [[assistant_app_repositories_model_repository_modelrecord]] — code: ModelRecord
- [[assistant_app_repositories_model_repository_modelrepository]] — code: ModelRepository
- [[assistant_app_repositories_model_repository_modelrepository_init]] — code: .__init__()
- [[assistant_app_repositories_model_repository_modelrepository_get_by_name]] — code: .get_by_name()
- [[assistant_app_repositories_model_repository_modelrepository_list_by_capability]] — code: .list_by_capability()
- [[assistant_app_repositories_model_repository_modelrepository_list_all]] — code: .list_all()
- [[assistant_app_repositories_model_repository_modelrepository_upsert]] — code: .upsert()

## Dependências

- [[assistant_app_repositories_model_repository]] → `contains` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_app_repositories_model_repository]] → `contains` → [[assistant_app_repositories_model_repository_modelrepository]]
- [[assistant_app_repositories_model_repository_modelrepository_get_by_name]] → `references` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_app_repositories_model_repository_modelrepository_list_all]] → `references` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_app_repositories_model_repository_modelrepository_list_by_capability]] → `references` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_app_repositories_model_repository_modelrepository_upsert]] → `references` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_app_repositories_model_repository_modelrepository]] → `method` → [[assistant_app_repositories_model_repository_modelrepository_get_by_name]]
- [[assistant_app_repositories_model_repository_modelrepository]] → `method` → [[assistant_app_repositories_model_repository_modelrepository_init]]
- [[assistant_app_repositories_model_repository_modelrepository]] → `method` → [[assistant_app_repositories_model_repository_modelrepository_list_all]]
- [[assistant_app_repositories_model_repository_modelrepository]] → `method` → [[assistant_app_repositories_model_repository_modelrepository_list_by_capability]]
- [[assistant_app_repositories_model_repository_modelrepository]] → `method` → [[assistant_app_repositories_model_repository_modelrepository_upsert]]
- [[assistant_app_repositories_model_repository_modelrepository_init]] → `references` → [[assistant_app_repositories_model_repository_py_asyncsession]]
- [[assistant_app_repositories_model_repository_modelrepository_get_by_name]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_model_repository_modelrepository_list_by_capability]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_model_repository_modelrepository_list_all]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_model_repository_modelrepository_upsert]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]