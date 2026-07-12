# assistant\app\audit\sdd_generator.py

## Símbolos

- [[assistant_app_audit_sdd_generator]] — code: sdd_generator.py
- [[assistant_app_audit_sdd_generator_sddtemplate]] — code: SDDTemplate
- [[assistant_app_audit_sdd_generator_sddgenerator]] — code: SDDGenerator
- [[assistant_app_audit_sdd_generator_sddgenerator_generate_sdd]] — code: .generate_sdd()
- [[assistant_app_audit_sdd_generator_sddgenerator_build_content]] — code: ._build_content()
- [[assistant_app_audit_sdd_generator_sddgenerator_generate_feature_node]] — code: .generate_feature_node()
- [[assistant_app_audit_sdd_generator_sddgenerator_update_feature_node]] — code: .update_feature_node()

## Dependências

- [[assistant_app_audit_sdd_generator]] → `contains` → [[assistant_app_audit_sdd_generator_sddgenerator]]
- [[assistant_app_audit_sdd_generator]] → `contains` → [[assistant_app_audit_sdd_generator_sddtemplate]]
- [[assistant_app_audit_sdd_generator_sddgenerator_build_content]] → `references` → [[assistant_app_audit_sdd_generator_sddtemplate]]
- [[assistant_app_audit_sdd_generator_sddgenerator_generate_sdd]] → `references` → [[assistant_app_audit_sdd_generator_sddtemplate]]
- [[assistant_app_audit_sdd_generator_sddgenerator]] → `method` → [[assistant_app_audit_sdd_generator_sddgenerator_build_content]]
- [[assistant_app_audit_sdd_generator_sddgenerator]] → `method` → [[assistant_app_audit_sdd_generator_sddgenerator_generate_feature_node]]
- [[assistant_app_audit_sdd_generator_sddgenerator]] → `method` → [[assistant_app_audit_sdd_generator_sddgenerator_generate_sdd]]
- [[assistant_app_audit_sdd_generator_sddgenerator]] → `method` → [[assistant_app_audit_sdd_generator_sddgenerator_update_feature_node]]
- [[assistant_app_audit_sdd_generator_sddgenerator_generate_sdd]] → `references` → [[assistant_app_audit_sdd_generator_py_path]]
- [[assistant_app_audit_sdd_generator_sddgenerator_generate_sdd]] → `calls` → [[assistant_app_audit_sdd_generator_sddgenerator_build_content]]
- [[assistant_app_audit_sdd_generator_sddgenerator_generate_feature_node]] → `references` → [[assistant_app_audit_sdd_generator_py_path]]
- [[assistant_app_audit_sdd_generator_sddgenerator_update_feature_node]] → `references` → [[assistant_app_audit_sdd_generator_py_path]]