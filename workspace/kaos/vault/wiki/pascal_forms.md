# graphify\graphify\extractors\pascal_forms.py

## Símbolos

- [[graphify_graphify_extractors_pascal_forms]] — code: pascal_forms.py
- [[graphify_graphify_extractors_pascal_forms_extract_lazarus_form]] — code: extract_lazarus_form()
- [[graphify_graphify_extractors_pascal_forms_extract_delphi_form]] — code: extract_delphi_form()
- [[graphify_graphify_extractors_pascal_forms_rationale_1]] — code: Pascal_forms extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_pascal_forms_rationale_11]] — code: Extract component hierarchy from Lazarus .lfm form files.      .lfm is a text-
- [[graphify_graphify_extractors_pascal_forms_rationale_104]] — code: Extract component hierarchy from Delphi .dfm form files.      .dfm files come

## Dependências

- [[graphify_graphify_extractors_pascal_forms_extract_delphi_form]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_pascal_forms_extract_lazarus_form]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_pascal_forms_extract_delphi_form]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_pascal_forms_extract_lazarus_form]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_pascal_forms_extract_delphi_form]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_pascal_forms_extract_lazarus_form]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_pascal_forms]] → `contains` → [[graphify_graphify_extractors_pascal_forms_extract_delphi_form]]
- [[graphify_graphify_extractors_pascal_forms]] → `contains` → [[graphify_graphify_extractors_pascal_forms_extract_lazarus_form]]
- [[graphify_graphify_extractors_pascal_forms_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_pascal_forms]]
- [[graphify_graphify_extractors_pascal_forms_extract_lazarus_form]] → `references` → [[graphify_graphify_extractors_pascal_forms_py_path]]
- [[graphify_graphify_extractors_pascal_forms_extract_lazarus_form]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_pascal_forms_rationale_11]] → `rationale_for` → [[graphify_graphify_extractors_pascal_forms_extract_lazarus_form]]
- [[graphify_graphify_extractors_pascal_forms_extract_delphi_form]] → `references` → [[graphify_graphify_extractors_pascal_forms_py_path]]
- [[graphify_graphify_extractors_pascal_forms_extract_delphi_form]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_pascal_forms_rationale_104]] → `rationale_for` → [[graphify_graphify_extractors_pascal_forms_extract_delphi_form]]