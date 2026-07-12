# assistant\app\audit\commit_classifier.py

## Símbolos

- [[assistant_app_audit_commit_classifier]] — code: commit_classifier.py
- [[assistant_app_audit_commit_classifier_committype]] — code: CommitType
- [[assistant_app_audit_commit_classifier_impactlevel]] — code: ImpactLevel
- [[assistant_app_audit_commit_classifier_classifiedcommit]] — code: ClassifiedCommit
- [[assistant_app_audit_commit_classifier_classify_type]] — code: classify_type()
- [[assistant_app_audit_commit_classifier_extract_scope]] — code: extract_scope()
- [[assistant_app_audit_commit_classifier_is_breaking]] — code: is_breaking()
- [[assistant_app_audit_commit_classifier_assess_impact]] — code: assess_impact()
- [[assistant_app_audit_commit_classifier_extract_features]] — code: extract_features()
- [[assistant_app_audit_commit_classifier_classify_commit]] — code: classify_commit()
- [[assistant_app_audit_commit_classifier_classify_commits]] — code: classify_commits()

## Dependências

- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_assess_impact]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_classifiedcommit]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_classify_commit]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_classify_commits]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_classify_type]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_committype]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_extract_features]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_extract_scope]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_impactlevel]]
- [[assistant_app_audit_commit_classifier]] → `contains` → [[assistant_app_audit_commit_classifier_is_breaking]]
- [[assistant_app_audit_commit_classifier]] → `imports_from` → [[assistant_app_audit_commit_classifier_py_enum]]
- [[assistant_app_audit_commit_classifier_classify_type]] → `references` → [[assistant_app_audit_commit_classifier_committype]]
- [[assistant_app_audit_commit_classifier_committype]] → `inherits` → [[assistant_app_audit_commit_classifier_py_enum]]
- [[assistant_app_audit_commit_classifier_impactlevel]] → `inherits` → [[assistant_app_audit_commit_classifier_py_enum]]
- [[assistant_app_audit_commit_classifier_assess_impact]] → `references` → [[assistant_app_audit_commit_classifier_impactlevel]]
- [[assistant_app_audit_commit_classifier_classify_commit]] → `references` → [[assistant_app_audit_commit_classifier_classifiedcommit]]
- [[assistant_app_audit_commit_classifier_classify_commits]] → `references` → [[assistant_app_audit_commit_classifier_classifiedcommit]]
- [[assistant_app_audit_commit_classifier_classify_commit]] → `calls` → [[assistant_app_audit_commit_classifier_classify_type]]
- [[assistant_app_audit_commit_classifier_classify_commit]] → `calls` → [[assistant_app_audit_commit_classifier_extract_scope]]
- [[assistant_app_audit_commit_classifier_classify_commit]] → `calls` → [[assistant_app_audit_commit_classifier_is_breaking]]
- [[assistant_app_audit_commit_classifier_classify_commit]] → `calls` → [[assistant_app_audit_commit_classifier_assess_impact]]
- [[assistant_app_audit_commit_classifier_classify_commit]] → `calls` → [[assistant_app_audit_commit_classifier_extract_features]]
- [[assistant_app_audit_commit_classifier_classify_commits]] → `calls` → [[assistant_app_audit_commit_classifier_classify_commit]]