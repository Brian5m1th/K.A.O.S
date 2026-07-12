# assistant\scripts\generate_feature_catalog.py

## Símbolos

- [[assistant_scripts_generate_feature_catalog]] — code: generate_feature_catalog.py
- [[assistant_scripts_generate_feature_catalog_load_registry]] — code: load_registry()
- [[assistant_scripts_generate_feature_catalog_generate_catalog]] — code: generate_catalog()
- [[assistant_scripts_generate_feature_catalog_main]] — code: main()

## Dependências

- [[assistant_scripts_generate_feature_catalog]] → `contains` → [[assistant_scripts_generate_feature_catalog_generate_catalog]]
- [[assistant_scripts_generate_feature_catalog]] → `contains` → [[assistant_scripts_generate_feature_catalog_load_registry]]
- [[assistant_scripts_generate_feature_catalog]] → `contains` → [[assistant_scripts_generate_feature_catalog_main]]
- [[assistant_scripts_generate_feature_catalog_load_registry]] → `references` → [[assistant_scripts_generate_feature_catalog_py_path]]
- [[assistant_scripts_generate_feature_catalog_main]] → `calls` → [[assistant_scripts_generate_feature_catalog_load_registry]]
- [[assistant_scripts_generate_feature_catalog_main]] → `calls` → [[assistant_scripts_generate_feature_catalog_generate_catalog]]