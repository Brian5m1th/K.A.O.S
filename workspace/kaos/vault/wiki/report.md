# graphify\graphify\report.py

## Símbolos

- [[graphify_graphify_report]] — code: report.py
- [[graphify_graphify_report_safe_community_name]] — code: _safe_community_name()
- [[graphify_graphify_report_load_learning_for_report]] — code: load_learning_for_report()
- [[graphify_graphify_report_learning_section]] — code: _learning_section()
- [[graphify_graphify_report_generate]] — code: generate()
- [[graphify_graphify_report_rationale_9]] — code: Mirrors export.safe_name so community hub filenames and report wikilinks always
- [[graphify_graphify_report_rationale_16]] — code: Assemble the report's work-memory inputs from sibling artifacts.      Reads th
- [[graphify_graphify_report_rationale_41]] — code: Append the ``## Work-memory lessons`` section, or nothing when empty.

## Dependências

- [[graphify_graphify_report]] → `imports` → [[graphify_graphify_analyze_is_file_node]]
- [[graphify_graphify_report_generate]] → `calls` → [[graphify_graphify_analyze_is_file_node]]
- [[graphify_graphify_report]] → `imports` → [[graphify_graphify_analyze_is_concept_node]]
- [[graphify_graphify_report_generate]] → `calls` → [[graphify_graphify_analyze_is_concept_node]]
- [[graphify_graphify_report]] → `imports` → [[graphify_graphify_analyze_find_import_cycles]]
- [[graphify_graphify_report_generate]] → `calls` → [[graphify_graphify_analyze_find_import_cycles]]
- [[graphify_graphify_report_load_learning_for_report]] → `calls` → [[graphify_graphify_reflect_load_memory_docs]]
- [[graphify_graphify_report_load_learning_for_report]] → `calls` → [[graphify_graphify_reflect_aggregate_lessons]]
- [[graphify_graphify_report_load_learning_for_report]] → `calls` → [[graphify_graphify_reflect_load_learning_overlay]]
- [[graphify_graphify_report]] → `contains` → [[graphify_graphify_report_generate]]
- [[graphify_graphify_report]] → `contains` → [[graphify_graphify_report_learning_section]]
- [[graphify_graphify_report]] → `contains` → [[graphify_graphify_report_load_learning_for_report]]
- [[graphify_graphify_report]] → `contains` → [[graphify_graphify_report_safe_community_name]]
- [[graphify_graphify_report_generate]] → `calls` → [[graphify_graphify_report_safe_community_name]]
- [[graphify_graphify_report_rationale_9]] → `rationale_for` → [[graphify_graphify_report_safe_community_name]]
- [[graphify_graphify_report_rationale_16]] → `rationale_for` → [[graphify_graphify_report_load_learning_for_report]]
- [[graphify_graphify_report_generate]] → `calls` → [[graphify_graphify_report_learning_section]]
- [[graphify_graphify_report_rationale_41]] → `rationale_for` → [[graphify_graphify_report_learning_section]]