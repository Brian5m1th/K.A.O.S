# assistant\scripts\sync_github_registry.py

## Símbolos

- [[assistant_scripts_sync_github_registry]] — code: sync_github_registry.py
- [[assistant_scripts_sync_github_registry_fetch_remote_registry]] — code: fetch_remote_registry()
- [[assistant_scripts_sync_github_registry_validate_schema]] — code: validate_schema()
- [[assistant_scripts_sync_github_registry_merge_registries]] — code: merge_registries()
- [[assistant_scripts_sync_github_registry_main]] — code: main()
- [[assistant_scripts_sync_github_registry_rationale_39]] — code: Busca o registry remoto e retorna o JSON e o commit SHA correspondente.
- [[assistant_scripts_sync_github_registry_rationale_75]] — code: Valida o schema do registry json.
- [[assistant_scripts_sync_github_registry_rationale_87]] — code: Realiza o merge inteligente entre local e remote.

## Dependências

- [[assistant_scripts_sync_github_registry_main]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_features_index_path]]
- [[assistant_scripts_sync_github_registry]] → `contains` → [[assistant_scripts_sync_github_registry_fetch_remote_registry]]
- [[assistant_scripts_sync_github_registry]] → `contains` → [[assistant_scripts_sync_github_registry_main]]
- [[assistant_scripts_sync_github_registry]] → `contains` → [[assistant_scripts_sync_github_registry_merge_registries]]
- [[assistant_scripts_sync_github_registry]] → `contains` → [[assistant_scripts_sync_github_registry_validate_schema]]
- [[assistant_scripts_sync_github_registry_main]] → `calls` → [[assistant_scripts_sync_github_registry_fetch_remote_registry]]
- [[assistant_scripts_sync_github_registry_rationale_39]] → `rationale_for` → [[assistant_scripts_sync_github_registry_fetch_remote_registry]]
- [[assistant_scripts_sync_github_registry_main]] → `calls` → [[assistant_scripts_sync_github_registry_validate_schema]]
- [[assistant_scripts_sync_github_registry_rationale_75]] → `rationale_for` → [[assistant_scripts_sync_github_registry_validate_schema]]
- [[assistant_scripts_sync_github_registry_main]] → `calls` → [[assistant_scripts_sync_github_registry_merge_registries]]
- [[assistant_scripts_sync_github_registry_rationale_87]] → `rationale_for` → [[assistant_scripts_sync_github_registry_merge_registries]]