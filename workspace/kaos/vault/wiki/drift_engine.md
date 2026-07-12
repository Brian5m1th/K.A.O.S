# assistant\app\ai\vault_analyzer\drift_engine.py

## Símbolos

- [[assistant_app_ai_vault_analyzer_drift_engine]] — code: drift_engine.py
- [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]] — code: DriftScore
- [[assistant_app_ai_vault_analyzer_drift_engine_driftscore_to_dict]] — code: .to_dict()
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] — code: DriftEngine
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_calculate]] — code: .calculate()
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_load_latest]] — code: .load_latest()
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_get_level_label]] — code: .get_level_label()
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_persist]] — code: ._persist()

## Dependências

- [[assistant_app_ai_vault_analyzer_drift_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]]
- [[assistant_app_ai_vault_analyzer_drift_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_calculate]] → `references` → [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_load_latest]] → `references` → [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_persist]] → `references` → [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]] → `method` → [[assistant_app_ai_vault_analyzer_drift_engine_driftscore_to_dict]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]] → `uses` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]] → `uses` → [[assistant_app_audit_code_scanner_codescanner]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftscore]] → `uses` → [[assistant_app_audit_sdd_resolver_sddresolver]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_persist]] → `calls` → [[assistant_app_ai_vault_analyzer_drift_engine_driftscore_to_dict]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] → `method` → [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_calculate]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] → `method` → [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_get_level_label]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] → `method` → [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_load_latest]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] → `method` → [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_persist]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] → `uses` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] → `uses` → [[assistant_app_audit_code_scanner_codescanner]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]] → `uses` → [[assistant_app_audit_sdd_resolver_sddresolver]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_calculate]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_calculate]] → `calls` → [[assistant_app_audit_code_scanner_codescanner_scan_all]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_calculate]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_load_from_json]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_calculate]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_load_latest]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_analysis_path]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_persist]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_analysis_path]]
- [[assistant_app_ai_vault_analyzer_drift_engine_driftengine_persist]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_architecture_history_dir]]