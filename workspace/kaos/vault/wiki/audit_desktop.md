# assistant\scripts\audit_desktop.py

## Símbolos

- [[assistant_scripts_audit_desktop]] — code: audit_desktop.py
- [[assistant_scripts_audit_desktop_scan_desktop_code]] — code: scan_desktop_code()
- [[assistant_scripts_audit_desktop_main]] — code: main()
- [[assistant_scripts_audit_desktop_write_report]] — code: write_report()

## Dependências

- [[assistant_scripts_audit_desktop_scan_desktop_code]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_project_root]]
- [[assistant_scripts_audit_desktop_main]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_docs_root]]
- [[assistant_scripts_audit_desktop]] → `contains` → [[assistant_scripts_audit_desktop_main]]
- [[assistant_scripts_audit_desktop]] → `contains` → [[assistant_scripts_audit_desktop_scan_desktop_code]]
- [[assistant_scripts_audit_desktop]] → `contains` → [[assistant_scripts_audit_desktop_write_report]]
- [[assistant_scripts_audit_desktop_main]] → `calls` → [[assistant_scripts_audit_desktop_scan_desktop_code]]
- [[assistant_scripts_audit_desktop_main]] → `calls` → [[assistant_scripts_audit_desktop_write_report]]
- [[assistant_scripts_audit_desktop_write_report]] → `references` → [[assistant_scripts_audit_desktop_py_path]]