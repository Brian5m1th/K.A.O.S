# assistant\app\ai\vault_analyzer\suggestion_engine.py

## Símbolos

- [[assistant_app_ai_vault_analyzer_suggestion_engine]] — code: suggestion_engine.py
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]] — code: Suggestion
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion_to_dict]] — code: .to_dict()
- [[assistant_app_ai_vault_analyzer_suggestion_engine_confidence_label]] — code: confidence_label()
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]] — code: SuggestionEngine
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_from_evidences]] — code: .generate_from_evidences()
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_evidence_to_suggestion]] — code: ._evidence_to_suggestion()
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_auto_sdd_suggestion]] — code: .generate_auto_sdd_suggestion()
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_sync_suggestion]] — code: .generate_sync_suggestion()
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_persist]] — code: .persist()

## Dependências

- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]] → `uses` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]] → `uses` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_evidence_to_suggestion]] → `references` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_from_evidences]] → `references` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidence]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_suggestion_engine_confidence_label]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine]] → `contains` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]] → `method` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion_to_dict]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_evidence_to_suggestion]] → `references` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_auto_sdd_suggestion]] → `references` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_from_evidences]] → `references` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_sync_suggestion]] → `references` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_persist]] → `references` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_persist]] → `calls` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion_to_dict]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]] → `method` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_evidence_to_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]] → `method` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_auto_sdd_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]] → `method` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_from_evidences]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]] → `method` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_sync_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]] → `method` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_persist]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_from_evidences]] → `calls` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_evidence_to_suggestion]]
- [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_persist]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_suggestions_path]]