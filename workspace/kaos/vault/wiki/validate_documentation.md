# assistant\scripts\validate_documentation.py

## Símbolos

- [[assistant_scripts_validate_documentation]] — code: validate_documentation.py
- [[assistant_scripts_validate_documentation_load_report]] — code: load_report()
- [[assistant_scripts_validate_documentation_validate]] — code: validate()
- [[assistant_scripts_validate_documentation_main]] — code: main()

## Dependências

- [[assistant_scripts_validate_documentation]] → `contains` → [[assistant_scripts_validate_documentation_load_report]]
- [[assistant_scripts_validate_documentation]] → `contains` → [[assistant_scripts_validate_documentation_main]]
- [[assistant_scripts_validate_documentation]] → `contains` → [[assistant_scripts_validate_documentation_validate]]
- [[assistant_scripts_validate_documentation_load_report]] → `references` → [[assistant_scripts_validate_documentation_py_path]]
- [[assistant_scripts_validate_documentation_main]] → `calls` → [[assistant_scripts_validate_documentation_load_report]]
- [[assistant_scripts_validate_documentation_main]] → `calls` → [[assistant_scripts_validate_documentation_py_path]]
- [[assistant_scripts_validate_documentation_main]] → `calls` → [[assistant_scripts_validate_documentation_validate]]