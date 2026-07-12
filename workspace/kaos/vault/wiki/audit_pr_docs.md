# assistant\scripts\audit_pr_docs.py

## Símbolos

- [[assistant_scripts_audit_pr_docs]] — code: audit_pr_docs.py
- [[assistant_scripts_audit_pr_docs_get_commits_from_range]] — code: get_commits_from_range()
- [[assistant_scripts_audit_pr_docs_get_commits_from_list]] — code: get_commits_from_list()
- [[assistant_scripts_audit_pr_docs_classify_impact]] — code: classify_impact()
- [[assistant_scripts_audit_pr_docs_check_documentation_exists]] — code: check_documentation_exists()
- [[assistant_scripts_audit_pr_docs_generate_auto_sdd]] — code: generate_auto_sdd()
- [[assistant_scripts_audit_pr_docs_register_feature]] — code: register_feature()
- [[assistant_scripts_audit_pr_docs_audit_commits]] — code: audit_commits()
- [[assistant_scripts_audit_pr_docs_print_report]] — code: print_report()
- [[assistant_scripts_audit_pr_docs_main]] — code: main()
- [[assistant_scripts_audit_pr_docs_rationale_22]] — code: Obtém commits entre base e head.
- [[assistant_scripts_audit_pr_docs_rationale_56]] — code: Parse lista de commits.
- [[assistant_scripts_audit_pr_docs_rationale_68]] — code: Classifica impacto do commit.
- [[assistant_scripts_audit_pr_docs_rationale_109]] — code: Verifica se existe SDD para a feature.
- [[assistant_scripts_audit_pr_docs_rationale_140]] — code: Gera AUTO-SDD para a feature.
- [[assistant_scripts_audit_pr_docs_rationale_156]] — code: Registra feature no registry se existir.
- [[assistant_scripts_audit_pr_docs_rationale_179]] — code: Audita lista de commits.
- [[assistant_scripts_audit_pr_docs_rationale_236]] — code: Exibe relatório formatado.

## Dependências

- [[assistant_scripts_audit_pr_docs_register_feature]] → `calls` → [[assistant_app_audit_feature_registry_featureentry]]
- [[assistant_scripts_audit_pr_docs_register_feature]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_register]]
- [[assistant_scripts_audit_pr_docs_register_feature]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_get]]
- [[assistant_scripts_audit_pr_docs_register_feature]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_update_last_commit]]
- [[assistant_scripts_audit_pr_docs_register_feature]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_load_from_json]]
- [[assistant_scripts_audit_pr_docs_generate_auto_sdd]] → `calls` → [[assistant_app_audit_sdd_generator_sddtemplate]]
- [[assistant_scripts_audit_pr_docs_generate_auto_sdd]] → `calls` → [[assistant_app_audit_sdd_generator_sddgenerator_generate_sdd]]
- [[assistant_scripts_audit_pr_docs_get_commits_from_range]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_project_root]]
- [[assistant_scripts_audit_pr_docs_check_documentation_exists]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_auto_dir]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_audit_commits]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_check_documentation_exists]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_classify_impact]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_generate_auto_sdd]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_get_commits_from_list]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_get_commits_from_range]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_main]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_print_report]]
- [[assistant_scripts_audit_pr_docs]] → `contains` → [[assistant_scripts_audit_pr_docs_register_feature]]
- [[assistant_scripts_audit_pr_docs_main]] → `calls` → [[assistant_scripts_audit_pr_docs_get_commits_from_range]]
- [[assistant_scripts_audit_pr_docs_rationale_22]] → `rationale_for` → [[assistant_scripts_audit_pr_docs_get_commits_from_range]]
- [[assistant_scripts_audit_pr_docs_main]] → `calls` → [[assistant_scripts_audit_pr_docs_get_commits_from_list]]
- [[assistant_scripts_audit_pr_docs_rationale_56]] → `rationale_for` → [[assistant_scripts_audit_pr_docs_get_commits_from_list]]
- [[assistant_scripts_audit_pr_docs_audit_commits]] → `calls` → [[assistant_scripts_audit_pr_docs_classify_impact]]
- [[assistant_scripts_audit_pr_docs_rationale_68]] → `rationale_for` → [[assistant_scripts_audit_pr_docs_classify_impact]]
- [[assistant_scripts_audit_pr_docs_audit_commits]] → `calls` → [[assistant_scripts_audit_pr_docs_check_documentation_exists]]
- [[assistant_scripts_audit_pr_docs_check_documentation_exists]] → `calls` → [[assistant_scripts_audit_pr_docs_py_path]]
- [[assistant_scripts_audit_pr_docs_rationale_109]] → `rationale_for` → [[assistant_scripts_audit_pr_docs_check_documentation_exists]]
- [[assistant_scripts_audit_pr_docs_audit_commits]] → `calls` → [[assistant_scripts_audit_pr_docs_generate_auto_sdd]]
- [[assistant_scripts_audit_pr_docs_generate_auto_sdd]] → `references` → [[assistant_scripts_audit_pr_docs_py_path]]
- [[assistant_scripts_audit_pr_docs_rationale_140]] → `rationale_for` → [[assistant_scripts_audit_pr_docs_generate_auto_sdd]]
- [[assistant_scripts_audit_pr_docs_audit_commits]] → `calls` → [[assistant_scripts_audit_pr_docs_register_feature]]
- [[assistant_scripts_audit_pr_docs_rationale_156]] → `rationale_for` → [[assistant_scripts_audit_pr_docs_register_feature]]
- [[assistant_scripts_audit_pr_docs_main]] → `calls` → [[assistant_scripts_audit_pr_docs_audit_commits]]
- [[assistant_scripts_audit_pr_docs_rationale_179]] → `rationale_for` → [[assistant_scripts_audit_pr_docs_audit_commits]]
- [[assistant_scripts_audit_pr_docs_main]] → `calls` → [[assistant_scripts_audit_pr_docs_print_report]]
- [[assistant_scripts_audit_pr_docs_rationale_236]] → `rationale_for` → [[assistant_scripts_audit_pr_docs_print_report]]