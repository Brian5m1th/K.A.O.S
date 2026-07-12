# assistant\tests\unit\test_audit_commit_classifier.py

## Símbolos

- [[assistant_tests_unit_test_audit_commit_classifier]] — code: test_audit_commit_classifier.py
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] — code: TestCommitClassifier
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_feat]] — code: .test_classify_type_feat()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_fix]] — code: .test_classify_type_fix()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_merge]] — code: .test_classify_type_merge()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_test]] — code: .test_classify_type_test()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_style]] — code: .test_classify_type_style()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_unknown]] — code: .test_classify_type_unknown()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_scope]] — code: .test_extract_scope()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_is_breaking]] — code: .test_is_breaking()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_high]] — code: .test_assess_impact_high()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_medium]] — code: .test_assess_impact_medium()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_low]] — code: .test_assess_impact_low()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_observability]] — code: .test_extract_features_observability()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_event_bus]] — code: .test_extract_features_event_bus()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_workflow]] — code: .test_extract_features_workflow()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_multiple]] — code: .test_extract_features_multiple()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_commit]] — code: .test_classify_commit()
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_commits]] — code: .test_classify_commits()

## Dependências

- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `uses` → [[assistant_app_audit_commit_classifier_committype]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `uses` → [[assistant_app_audit_commit_classifier_impactlevel]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_feat]] → `calls` → [[assistant_app_audit_commit_classifier_classify_type]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_fix]] → `calls` → [[assistant_app_audit_commit_classifier_classify_type]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_merge]] → `calls` → [[assistant_app_audit_commit_classifier_classify_type]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_style]] → `calls` → [[assistant_app_audit_commit_classifier_classify_type]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_test]] → `calls` → [[assistant_app_audit_commit_classifier_classify_type]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_unknown]] → `calls` → [[assistant_app_audit_commit_classifier_classify_type]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_scope]] → `calls` → [[assistant_app_audit_commit_classifier_extract_scope]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_is_breaking]] → `calls` → [[assistant_app_audit_commit_classifier_is_breaking]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_high]] → `calls` → [[assistant_app_audit_commit_classifier_assess_impact]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_low]] → `calls` → [[assistant_app_audit_commit_classifier_assess_impact]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_medium]] → `calls` → [[assistant_app_audit_commit_classifier_assess_impact]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_event_bus]] → `calls` → [[assistant_app_audit_commit_classifier_extract_features]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_multiple]] → `calls` → [[assistant_app_audit_commit_classifier_extract_features]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_observability]] → `calls` → [[assistant_app_audit_commit_classifier_extract_features]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_workflow]] → `calls` → [[assistant_app_audit_commit_classifier_extract_features]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_commit]] → `calls` → [[assistant_app_audit_commit_classifier_classify_commit]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_commits]] → `calls` → [[assistant_app_audit_commit_classifier_classify_commits]]
- [[assistant_tests_unit_test_audit_commit_classifier]] → `contains` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_high]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_low]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_assess_impact_medium]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_commit]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_commits]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_feat]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_fix]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_merge]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_style]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_test]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_classify_type_unknown]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_event_bus]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_multiple]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_observability]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_features_workflow]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_extract_scope]]
- [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier]] → `method` → [[assistant_tests_unit_test_audit_commit_classifier_testcommitclassifier_test_is_breaking]]