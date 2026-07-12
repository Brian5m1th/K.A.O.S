# graphify\graphify\extractors\go.py

## Símbolos

- [[graphify_graphify_extractors_go]] — code: go.py
- [[graphify_graphify_extractors_go_go_collect_type_refs]] — code: _go_collect_type_refs()
- [[graphify_graphify_extractors_go_extract_go]] — code: extract_go()
- [[graphify_graphify_extractors_go_rationale_1]] — code: Go extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_go_rationale_16]] — code: Walk a Go type expression; append (name, role) tuples.
- [[graphify_graphify_extractors_go_rationale_54]] — code: Extract functions, methods, type declarations, and imports from a .go file.

## Dependências

- [[graphify_graphify_extractors_go_extract_go]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_go_extract_go]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_go_extract_go]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_go_go_collect_type_refs]] → `calls` → [[graphify_graphify_extractors_base_read_text]]
- [[graphify_graphify_extractors_go]] → `contains` → [[graphify_graphify_extractors_go_extract_go]]
- [[graphify_graphify_extractors_go]] → `contains` → [[graphify_graphify_extractors_go_go_collect_type_refs]]
- [[graphify_graphify_extractors_go_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_go]]
- [[graphify_graphify_extractors_go_rationale_16]] → `rationale_for` → [[graphify_graphify_extractors_go_go_collect_type_refs]]
- [[graphify_graphify_extractors_go_extract_go]] → `references` → [[graphify_graphify_extractors_go_py_path]]
- [[graphify_graphify_extractors_go_extract_go]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_go_rationale_54]] → `rationale_for` → [[graphify_graphify_extractors_go_extract_go]]