# assistant\app\audit\commit_mapper.py

## Símbolos

- [[assistant_app_audit_commit_mapper]] — code: commit_mapper.py
- [[assistant_app_audit_commit_mapper_commitmapentry]] — code: CommitMapEntry
- [[assistant_app_audit_commit_mapper_commitmapper]] — code: CommitMapper
- [[assistant_app_audit_commit_mapper_commitmapper_set_max_commits]] — code: .set_max_commits()
- [[assistant_app_audit_commit_mapper_commitmapper_run_git_log]] — code: ._run_git_log()
- [[assistant_app_audit_commit_mapper_commitmapper_generate_map]] — code: .generate_map()
- [[assistant_app_audit_commit_mapper_commitmapper_persist]] — code: ._persist()
- [[assistant_app_audit_commit_mapper_commitmapper_load]] — code: .load()
- [[assistant_app_audit_commit_mapper_commitmapper_get_features_for_commit]] — code: .get_features_for_commit()
- [[assistant_app_audit_commit_mapper_commitmapper_get_commits_for_feature]] — code: .get_commits_for_feature()
- [[assistant_app_audit_commit_mapper_commitmapper_get_high_impact_commits]] — code: .get_high_impact_commits()
- [[assistant_app_audit_commit_mapper_commitmapper_get_commits_by_type]] — code: .get_commits_by_type()
- [[assistant_app_audit_commit_mapper_commitmapper_get_latest_commit]] — code: .get_latest_commit()

## Dependências

- [[assistant_app_audit_commit_mapper_commitmapper_generate_map]] → `calls` → [[assistant_app_audit_commit_classifier_classify_commits]]
- [[assistant_app_audit_commit_mapper]] → `contains` → [[assistant_app_audit_commit_mapper_commitmapentry]]
- [[assistant_app_audit_commit_mapper]] → `contains` → [[assistant_app_audit_commit_mapper_commitmapper]]
- [[assistant_app_audit_commit_mapper_commitmapper_generate_map]] → `references` → [[assistant_app_audit_commit_mapper_commitmapentry]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_commits_by_type]] → `references` → [[assistant_app_audit_commit_mapper_commitmapentry]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_commits_for_feature]] → `references` → [[assistant_app_audit_commit_mapper_commitmapentry]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_high_impact_commits]] → `references` → [[assistant_app_audit_commit_mapper_commitmapentry]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_latest_commit]] → `references` → [[assistant_app_audit_commit_mapper_commitmapentry]]
- [[assistant_app_audit_commit_mapper_commitmapper_load]] → `references` → [[assistant_app_audit_commit_mapper_commitmapentry]]
- [[assistant_app_audit_commit_mapper_commitmapper_persist]] → `references` → [[assistant_app_audit_commit_mapper_commitmapentry]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_generate_map]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_get_commits_by_type]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_get_commits_for_feature]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_get_features_for_commit]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_get_high_impact_commits]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_get_latest_commit]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_load]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_persist]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_run_git_log]]
- [[assistant_app_audit_commit_mapper_commitmapper]] → `method` → [[assistant_app_audit_commit_mapper_commitmapper_set_max_commits]]
- [[assistant_app_audit_commit_mapper_commitmapper_generate_map]] → `calls` → [[assistant_app_audit_commit_mapper_commitmapper_run_git_log]]
- [[assistant_app_audit_commit_mapper_commitmapper_run_git_log]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_project_root]]
- [[assistant_app_audit_commit_mapper_commitmapper_generate_map]] → `calls` → [[assistant_app_audit_commit_mapper_commitmapper_persist]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_commits_by_type]] → `calls` → [[assistant_app_audit_commit_mapper_commitmapper_load]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_commits_for_feature]] → `calls` → [[assistant_app_audit_commit_mapper_commitmapper_load]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_features_for_commit]] → `calls` → [[assistant_app_audit_commit_mapper_commitmapper_load]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_high_impact_commits]] → `calls` → [[assistant_app_audit_commit_mapper_commitmapper_load]]
- [[assistant_app_audit_commit_mapper_commitmapper_get_latest_commit]] → `calls` → [[assistant_app_audit_commit_mapper_commitmapper_load]]