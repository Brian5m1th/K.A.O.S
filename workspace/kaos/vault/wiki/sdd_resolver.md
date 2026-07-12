# assistant\app\audit\sdd_resolver.py

## Símbolos

- [[assistant_app_audit_sdd_resolver]] — code: sdd_resolver.py
- [[assistant_app_audit_sdd_resolver_sddentry]] — code: SDDEntry
- [[assistant_app_audit_sdd_resolver_sddentry_post_init]] — code: .__post_init__()
- [[assistant_app_audit_sdd_resolver_sddresolver]] — code: SDDResolver
- [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_dirs]] — code: .get_sdd_dirs()
- [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]] — code: .scan_all_sdds()
- [[assistant_app_audit_sdd_resolver_sddresolver_parse_sdd]] — code: ._parse_sdd()
- [[assistant_app_audit_sdd_resolver_sddresolver_extract_linked_features]] — code: ._extract_linked_features()
- [[assistant_app_audit_sdd_resolver_sddresolver_find_sdd_for_feature]] — code: .find_sdd_for_feature()
- [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_status]] — code: .get_sdd_status()
- [[assistant_app_audit_sdd_resolver_sddresolver_get_all_sdds]] — code: .get_all_sdds()
- [[assistant_app_audit_sdd_resolver_sddresolver_get_missing_features]] — code: .get_missing_features()
- [[assistant_app_audit_sdd_resolver_sddresolver_get_orphaned_sdds]] — code: .get_orphaned_sdds()
- [[assistant_app_audit_sdd_resolver_sddresolver_clear_cache]] — code: .clear_cache()

## Dependências

- [[assistant_app_audit_sdd_resolver_sddentry]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_audit_sdd_resolver]] → `contains` → [[assistant_app_audit_sdd_resolver_sddentry]]
- [[assistant_app_audit_sdd_resolver]] → `contains` → [[assistant_app_audit_sdd_resolver_sddresolver]]
- [[assistant_app_audit_sdd_resolver_sddentry]] → `method` → [[assistant_app_audit_sdd_resolver_sddentry_post_init]]
- [[assistant_app_audit_sdd_resolver_sddresolver_find_sdd_for_feature]] → `references` → [[assistant_app_audit_sdd_resolver_sddentry]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_all_sdds]] → `references` → [[assistant_app_audit_sdd_resolver_sddentry]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_orphaned_sdds]] → `references` → [[assistant_app_audit_sdd_resolver_sddentry]]
- [[assistant_app_audit_sdd_resolver_sddresolver_parse_sdd]] → `references` → [[assistant_app_audit_sdd_resolver_sddentry]]
- [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]] → `references` → [[assistant_app_audit_sdd_resolver_sddentry]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_clear_cache]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_extract_linked_features]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_find_sdd_for_feature]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_get_all_sdds]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_get_missing_features]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_get_orphaned_sdds]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_dirs]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_status]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_parse_sdd]]
- [[assistant_app_audit_sdd_resolver_sddresolver]] → `method` → [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_dirs]] → `references` → [[assistant_app_audit_sdd_resolver_py_path]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_dirs]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_get_vault_path]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_dirs]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_project_root]]
- [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_dirs]]
- [[assistant_app_audit_sdd_resolver_sddresolver_parse_sdd]] → `references` → [[assistant_app_audit_sdd_resolver_py_path]]
- [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]] → `calls` → [[assistant_app_audit_sdd_resolver_py_path]]
- [[assistant_app_audit_sdd_resolver_sddresolver_find_sdd_for_feature]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_all_sdds]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_missing_features]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_orphaned_sdds]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]]
- [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_parse_sdd]]
- [[assistant_app_audit_sdd_resolver_sddresolver_parse_sdd]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_extract_linked_features]]
- [[assistant_app_audit_sdd_resolver_sddresolver_parse_sdd]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_project_root]]
- [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_status]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_find_sdd_for_feature]]