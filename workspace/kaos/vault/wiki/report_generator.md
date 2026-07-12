# assistant\app\core\documentation\report_generator.py

## Símbolos

- [[assistant_app_core_documentation_report_generator]] — code: report_generator.py
- [[assistant_app_core_documentation_report_generator_reportgenerator]] — code: ReportGenerator
- [[assistant_app_core_documentation_report_generator_reportgenerator_get_generated_dir]] — code: .get_generated_dir()
- [[assistant_app_core_documentation_report_generator_reportgenerator_write_dry_run_reports]] — code: .write_dry_run_reports()
- [[assistant_app_core_documentation_report_generator_reportgenerator_write_audit_context]] — code: .write_audit_context()
- [[assistant_app_core_documentation_report_generator_reportgenerator_generate_markdown_report]] — code: .generate_markdown_report()
- [[assistant_app_core_documentation_report_generator_datetime_now_str]] — code: datetime_now_str()
- [[assistant_app_core_documentation_report_generator_rationale_16]] — code: Salva os 5 arquivos de relatório no formato dry-run.
- [[assistant_app_core_documentation_report_generator_rationale_61]] — code: Gera docs/generated/audit_context.json para consumo do AI Vault Analyzer.
- [[assistant_app_core_documentation_report_generator_rationale_94]] — code: Gera o audit-report.md final com comparativo de métricas.

## Dependências

- [[assistant_app_core_documentation_report_generator]] → `contains` → [[assistant_app_core_documentation_report_generator_datetime_now_str]]
- [[assistant_app_core_documentation_report_generator]] → `contains` → [[assistant_app_core_documentation_report_generator_reportgenerator]]
- [[assistant_app_core_documentation_report_generator_reportgenerator]] → `method` → [[assistant_app_core_documentation_report_generator_reportgenerator_generate_markdown_report]]
- [[assistant_app_core_documentation_report_generator_reportgenerator]] → `method` → [[assistant_app_core_documentation_report_generator_reportgenerator_get_generated_dir]]
- [[assistant_app_core_documentation_report_generator_reportgenerator]] → `method` → [[assistant_app_core_documentation_report_generator_reportgenerator_write_audit_context]]
- [[assistant_app_core_documentation_report_generator_reportgenerator]] → `method` → [[assistant_app_core_documentation_report_generator_reportgenerator_write_dry_run_reports]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_get_generated_dir]] → `references` → [[assistant_app_core_documentation_report_generator_py_path]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_get_generated_dir]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_docs_root]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_write_audit_context]] → `calls` → [[assistant_app_core_documentation_report_generator_reportgenerator_get_generated_dir]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_write_dry_run_reports]] → `calls` → [[assistant_app_core_documentation_report_generator_reportgenerator_get_generated_dir]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_generate_markdown_report]] → `references` → [[assistant_app_core_documentation_report_generator_py_path]]
- [[assistant_app_core_documentation_report_generator_rationale_16]] → `rationale_for` → [[assistant_app_core_documentation_report_generator_reportgenerator_write_dry_run_reports]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_write_dry_run_reports]] → `references` → [[assistant_app_core_documentation_report_generator_py_any]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_write_dry_run_reports]] → `calls` → [[assistant_app_core_documentation_report_generator_reportgenerator_write_audit_context]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_generate_markdown_report]] → `references` → [[assistant_app_core_documentation_report_generator_py_any]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_write_audit_context]] → `references` → [[assistant_app_core_documentation_report_generator_py_any]]
- [[assistant_app_core_documentation_report_generator_rationale_61]] → `rationale_for` → [[assistant_app_core_documentation_report_generator_reportgenerator_write_audit_context]]
- [[assistant_app_core_documentation_report_generator_rationale_94]] → `rationale_for` → [[assistant_app_core_documentation_report_generator_reportgenerator_generate_markdown_report]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_generate_markdown_report]] → `calls` → [[assistant_app_core_documentation_report_generator_datetime_now_str]]
- [[assistant_app_core_documentation_report_generator_reportgenerator_generate_markdown_report]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_docs_root]]