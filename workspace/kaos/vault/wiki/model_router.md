# assistant\app\models\model_router.py

## Símbolos

- [[assistant_app_models_model_router]] — code: model_router.py
- [[assistant_app_models_model_router_modelselection]] — code: ModelSelection
- [[assistant_app_models_model_router_modelrouter]] — code: ModelRouter
- [[assistant_app_models_model_router_modelrouter_init]] — code: .__init__()
- [[assistant_app_models_model_router_modelrouter_select_model]] — code: .select_model()

## Dependências

- [[assistant_app_models_model_router]] → `contains` → [[assistant_app_models_model_router_modelrouter]]
- [[assistant_app_models_model_router]] → `contains` → [[assistant_app_models_model_router_modelselection]]
- [[assistant_app_models_model_router_modelrouter_select_model]] → `references` → [[assistant_app_models_model_router_modelselection]]
- [[assistant_app_models_model_router_modelselection]] → `uses` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_models_model_router_modelselection]] → `uses` → [[assistant_app_repositories_capability_policy_repository_capabilitypolicyrepository]]
- [[assistant_app_models_model_router_modelselection]] → `uses` → [[assistant_app_repositories_model_repository_modelrepository]]
- [[assistant_app_models_model_router_modelselection]] → `uses` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]]
- [[assistant_app_models_model_router_modelrouter]] → `method` → [[assistant_app_models_model_router_modelrouter_init]]
- [[assistant_app_models_model_router_modelrouter]] → `method` → [[assistant_app_models_model_router_modelrouter_select_model]]
- [[assistant_app_models_model_router_modelrouter]] → `uses` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_models_model_router_modelrouter]] → `uses` → [[assistant_app_repositories_capability_policy_repository_capabilitypolicyrepository]]
- [[assistant_app_models_model_router_modelrouter]] → `uses` → [[assistant_app_repositories_model_repository_modelrepository]]
- [[assistant_app_models_model_router_modelrouter]] → `uses` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]]
- [[assistant_app_models_model_router_modelrouter_init]] → `references` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_models_model_router_modelrouter_init]] → `references` → [[assistant_app_repositories_capability_policy_repository_capabilitypolicyrepository]]
- [[assistant_app_models_model_router_modelrouter_init]] → `references` → [[assistant_app_repositories_model_repository_modelrepository]]
- [[assistant_app_models_model_router_modelrouter_init]] → `references` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerepository]]