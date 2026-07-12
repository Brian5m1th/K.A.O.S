# assistant\app\models\model_registry.py

## Símbolos

- [[assistant_app_models_model_registry]] — code: model_registry.py
- [[assistant_app_models_model_registry_modelregistry]] — code: ModelRegistry
- [[assistant_app_models_model_registry_modelregistry_init]] — code: .__init__()
- [[assistant_app_models_model_registry_modelregistry_get_model]] — code: .get_model()
- [[assistant_app_models_model_registry_modelregistry_list_by_capability]] — code: .list_by_capability()
- [[assistant_app_models_model_registry_modelregistry_list_all]] — code: .list_all()

## Dependências

- [[assistant_app_models_model_registry]] → `contains` → [[assistant_app_models_model_registry_modelregistry]]
- [[assistant_app_models_model_registry_modelregistry]] → `method` → [[assistant_app_models_model_registry_modelregistry_get_model]]
- [[assistant_app_models_model_registry_modelregistry]] → `method` → [[assistant_app_models_model_registry_modelregistry_init]]
- [[assistant_app_models_model_registry_modelregistry]] → `method` → [[assistant_app_models_model_registry_modelregistry_list_all]]
- [[assistant_app_models_model_registry_modelregistry]] → `method` → [[assistant_app_models_model_registry_modelregistry_list_by_capability]]
- [[assistant_app_models_model_registry_modelregistry]] → `uses` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_app_models_model_registry_modelregistry]] → `uses` → [[assistant_app_repositories_model_repository_modelrepository]]
- [[assistant_app_models_model_registry_modelregistry_init]] → `references` → [[assistant_app_models_model_registry_py_asyncsession]]
- [[assistant_app_models_model_registry_modelregistry_init]] → `calls` → [[assistant_app_repositories_model_repository_modelrepository]]
- [[assistant_app_models_model_registry_modelregistry_get_model]] → `references` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_app_models_model_registry_modelregistry_list_by_capability]] → `references` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_app_models_model_registry_modelregistry_list_all]] → `references` → [[assistant_app_repositories_model_repository_modelrecord]]