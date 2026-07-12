# assistant\tests\unit\test_audit_sdd_generator.py

## Símbolos

- [[assistant_tests_unit_test_audit_sdd_generator]] — code: test_audit_sdd_generator.py
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator]] — code: TestSDDGenerator
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_sdd_creates_file]] — code: .test_generate_sdd_creates_file()
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_sdd_frontmatter]] — code: .test_generate_sdd_frontmatter()
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_feature_node]] — code: .test_generate_feature_node()

## Dependências

- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator]] → `uses` → [[assistant_app_audit_sdd_generator_sddtemplate]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_sdd_creates_file]] → `calls` → [[assistant_app_audit_sdd_generator_sddtemplate]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_sdd_frontmatter]] → `calls` → [[assistant_app_audit_sdd_generator_sddtemplate]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator]] → `uses` → [[assistant_app_audit_sdd_generator_sddgenerator]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_sdd_creates_file]] → `calls` → [[assistant_app_audit_sdd_generator_sddgenerator_generate_sdd]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_sdd_frontmatter]] → `calls` → [[assistant_app_audit_sdd_generator_sddgenerator_generate_sdd]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_feature_node]] → `calls` → [[assistant_app_audit_sdd_generator_sddgenerator_generate_feature_node]]
- [[assistant_tests_unit_test_audit_sdd_generator]] → `contains` → [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator]] → `method` → [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_feature_node]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator]] → `method` → [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_sdd_creates_file]]
- [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator]] → `method` → [[assistant_tests_unit_test_audit_sdd_generator_testsddgenerator_test_generate_sdd_frontmatter]]