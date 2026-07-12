# assistant\app\ai\vault_analyzer\analyzer_engine.py

## Símbolos

- [[assistant_app_ai_vault_analyzer_analyzer_engine]] — code: analyzer_engine.py
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] — code: ArchitectureAnalysis
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis_to_dict]] — code: .to_dict()
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] — code: AnalyzerEngine
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]] — code: .analyze()
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_generate_suggestions]] — code: ._generate_suggestions()
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_generate_warnings]] — code: ._generate_warnings()
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_persist]] — code: ._persist()
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze_async]] — code: .analyze_async()
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_load_latest]] — code: .load_latest()
- [[assistant_app_ai_vault_analyzer_analyzer_engine_rationale_144]] — code: Async wrapper that runs analysis and emits EventBus event (RF-B05).

## Dependências

- [[assistant_app_ai_vault_analyzer_analyzer_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]] → `references` → [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze_async]] → `references` → [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_load_latest]] → `references` → [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_persist]] → `references` → [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] → `method` → [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis_to_dict]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] → `uses` → [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] → `uses` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] → `uses` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] → `uses` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_persist]] → `calls` → [[assistant_app_ai_vault_analyzer_analyzer_engine_architectureanalysis_to_dict]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `method` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `method` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze_async]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `method` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_generate_suggestions]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `method` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_generate_warnings]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `method` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_load_latest]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `method` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_persist]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `uses` → [[assistant_app_ai_vault_analyzer_drift_engine_driftengine]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `uses` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `uses` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `uses` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]] → `calls` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_generate_suggestions]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]] → `calls` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_generate_warnings]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]] → `calls` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_persist]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_load_from_json]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze_async]] → `calls` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_generate_suggestions]] → `references` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_persist]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_analysis_path]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze_async]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_rationale_144]] → `rationale_for` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze_async]]
- [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_load_latest]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_analysis_path]]