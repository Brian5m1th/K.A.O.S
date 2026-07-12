# assistant\app\ai\vault_analyzer\evidence_engine.py

## Símbolos

- [[assistant_app_ai_vault_analyzer_evidence_engine]] — code: evidence_engine.py
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]] — code: Evidence
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidence_to_dict]] — code: .to_dict()
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] — code: EvidenceEngine
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_collect]] — code: .collect()
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_cycles]] — code: ._detect_cycles()
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_overcoupled]] — code: ._detect_overcoupled()
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_contradictions]] — code: ._detect_contradictions()
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_persist]] — code: ._persist()

## Dependências

- [[assistant_app_ai_vault_analyzer_evidence_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_evidence_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]] → `method` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence_to_dict]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]] → `uses` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]] → `uses` → [[assistant_app_audit_sdd_resolver_sddresolver]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_collect]] → `references` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_contradictions]] → `references` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_cycles]] → `references` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_overcoupled]] → `references` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_persist]] → `references` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_persist]] → `calls` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence_to_dict]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] → `method` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_collect]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] → `method` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_contradictions]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] → `method` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_cycles]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] → `method` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_detect_overcoupled]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] → `method` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_persist]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] → `uses` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]] → `uses` → [[assistant_app_audit_sdd_resolver_sddresolver]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_collect]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_collect]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_load_from_json]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_collect]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_get_all_sdds]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_collect]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]]
- [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine_persist]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_issues_path]]