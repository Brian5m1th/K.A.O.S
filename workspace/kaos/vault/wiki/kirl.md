# assistant\app\api\kirl.py

## Símbolos

- [[assistant_app_api_kirl]] — code: kirl.py
- [[assistant_app_api_kirl_kirlissueresponse]] — code: KIRLIssueResponse
- [[assistant_app_api_kirl_kirlreviewresponse]] — code: KIRLReviewResponse
- [[assistant_app_api_kirl_generate_report_markdown]] — code: _generate_report_markdown()
- [[assistant_app_api_kirl_run_kirl_review]] — code: run_kirl_review()
- [[assistant_app_api_kirl_rationale_1]] — code: KIRL API — Self-Review pipeline.  RF-H01: POST /api/kirl/review — complete Aud
- [[assistant_app_api_kirl_rationale_42]] — code: Generate a self-review report in markdown format.
- [[assistant_app_api_kirl_rationale_79]] — code: RF-H01: Pipeline completo DocumentationAudit → VaultAnalyzer → Suggestions.

## Dependências

- [[assistant_app_api_kirl_kirlissueresponse]] → `uses` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]]
- [[assistant_app_api_kirl_kirlreviewresponse]] → `uses` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]]
- [[assistant_app_api_kirl_run_kirl_review]] → `calls` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze_async]]
- [[assistant_app_api_kirl_kirlissueresponse]] → `uses` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]]
- [[assistant_app_api_kirl_kirlreviewresponse]] → `uses` → [[assistant_app_ai_vault_analyzer_evidence_engine_evidenceengine]]
- [[assistant_app_api_kirl_generate_report_markdown]] → `references` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_api_kirl_kirlissueresponse]] → `uses` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_api_kirl_kirlreviewresponse]] → `uses` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestion]]
- [[assistant_app_api_kirl_kirlissueresponse]] → `uses` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]]
- [[assistant_app_api_kirl_kirlreviewresponse]] → `uses` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine]]
- [[assistant_app_api_kirl_run_kirl_review]] → `calls` → [[assistant_app_ai_vault_analyzer_suggestion_engine_suggestionengine_generate_from_evidences]]
- [[assistant_app_api_kirl]] → `contains` → [[assistant_app_api_kirl_generate_report_markdown]]
- [[assistant_app_api_kirl]] → `contains` → [[assistant_app_api_kirl_kirlissueresponse]]
- [[assistant_app_api_kirl]] → `contains` → [[assistant_app_api_kirl_kirlreviewresponse]]
- [[assistant_app_api_kirl]] → `contains` → [[assistant_app_api_kirl_run_kirl_review]]
- [[assistant_app_api_kirl]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_kirl_rationale_1]] → `rationale_for` → [[assistant_app_api_kirl]]
- [[assistant_app_api_kirl_kirlissueresponse]] → `inherits` → [[assistant_app_api_kirl_py_basemodel]]
- [[assistant_app_api_kirl_kirlissueresponse]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_app_api_kirl_kirlissueresponse]] → `uses` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_app_api_kirl_kirlreviewresponse]] → `inherits` → [[assistant_app_api_kirl_py_basemodel]]
- [[assistant_app_api_kirl_kirlreviewresponse]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_app_api_kirl_kirlreviewresponse]] → `uses` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_app_api_kirl_run_kirl_review]] → `calls` → [[assistant_app_api_kirl_kirlreviewresponse]]
- [[assistant_app_api_kirl_generate_report_markdown]] → `references` → [[assistant_app_api_kirl_py_driftreport]]
- [[assistant_app_api_kirl_rationale_42]] → `rationale_for` → [[assistant_app_api_kirl_generate_report_markdown]]
- [[assistant_app_api_kirl_run_kirl_review]] → `calls` → [[assistant_app_api_kirl_generate_report_markdown]]
- [[assistant_app_api_kirl_rationale_79]] → `rationale_for` → [[assistant_app_api_kirl_run_kirl_review]]
- [[assistant_app_api_kirl_run_kirl_review]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_run_audit]]
- [[assistant_app_api_kirl_run_kirl_review]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_analysis_path]]
- [[assistant_app_api_kirl_run_kirl_review]] → `references` → [[assistant_app_notifications_service_notificationservice]]