# assistant\app\core\documentation\audit_engine.py

## Símbolos

- [[assistant_app_core_documentation_audit_engine]] — code: audit_engine.py
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] — code: DocumentationAuditEngine
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] — code: .run_audit()
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_is_code_documented]] — code: .is_code_documented()
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] — code: .execute_recovery_flow()
- [[assistant_app_core_documentation_audit_engine_re_search_sec]] — code: re_search_sec()
- [[assistant_app_core_documentation_audit_engine_re_escape]] — code: re_escape()
- [[assistant_app_core_documentation_audit_engine_extract_bullet_links]] — code: extract_bullet_links()
- [[assistant_app_core_documentation_audit_engine_rationale_22]] — code: Executa a auditoria completa da documentação e retorna as métricas coletadas.
- [[assistant_app_core_documentation_audit_engine_rationale_235]] — code: Executa a correção automática e normalização de documentos.

## Dependências

- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_ai_vault_analyzer_graph_builder_graphbuilder]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_audit_code_scanner_codescanner]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_audit_code_scanner_codescanner_scan_all]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_audit_commit_mapper_commitmapper]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_get]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_add_doc_ref]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_load_from_json]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_audit_sdd_resolver_sddresolver]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_scan_all_sdds]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_audit_sdd_resolver_sddresolver_get_sdd_status]]
- [[assistant_app_core_documentation_audit_engine]] → `contains` → [[assistant_app_core_documentation_audit_engine_documentationauditengine]]
- [[assistant_app_core_documentation_audit_engine]] → `contains` → [[assistant_app_core_documentation_audit_engine_extract_bullet_links]]
- [[assistant_app_core_documentation_audit_engine]] → `contains` → [[assistant_app_core_documentation_audit_engine_re_escape]]
- [[assistant_app_core_documentation_audit_engine]] → `contains` → [[assistant_app_core_documentation_audit_engine_re_search_sec]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `method` → [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `method` → [[assistant_app_core_documentation_audit_engine_documentationauditengine_is_code_documented]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `method` → [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_core_documentation_graph_validator_graphvalidator]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_core_documentation_health_engine_healthengine]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_core_documentation_recovery_engine_recoveryengine]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine]] → `uses` → [[assistant_app_core_documentation_report_generator_reportgenerator]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `calls` → [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_core_documentation_audit_engine_documentationauditengine_is_code_documented]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_core_documentation_audit_engine_extract_bullet_links]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `references` → [[assistant_app_core_documentation_audit_engine_py_any]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_core_documentation_audit_engine_re_search_sec]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_core_documentation_graph_validator_graphvalidator_validate_graph]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_core_documentation_health_engine_healthengine_calculate_health]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_encoding]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_docs_root]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_project_root]]
- [[assistant_app_core_documentation_audit_engine_rationale_22]] → `rationale_for` → [[assistant_app_core_documentation_audit_engine_documentationauditengine_run_audit]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `references` → [[assistant_app_core_documentation_audit_engine_py_any]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_generate_stub]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `calls` → [[assistant_app_core_documentation_report_generator_reportgenerator_generate_markdown_report]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `calls` → [[assistant_app_core_documentation_report_generator_reportgenerator_write_dry_run_reports]]
- [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_docs_root]]
- [[assistant_app_core_documentation_audit_engine_rationale_235]] → `rationale_for` → [[assistant_app_core_documentation_audit_engine_documentationauditengine_execute_recovery_flow]]
- [[assistant_app_core_documentation_audit_engine_re_search_sec]] → `calls` → [[assistant_app_core_documentation_audit_engine_re_escape]]