# graphify\graphify\extractors\rust.py

## Símbolos

- [[graphify_graphify_extractors_rust]] — code: rust.py
- [[graphify_graphify_extractors_rust_rust_collect_type_refs]] — code: _rust_collect_type_refs()
- [[graphify_graphify_extractors_rust_extract_rust]] — code: extract_rust()
- [[graphify_graphify_extractors_rust_rationale_1]] — code: Rust extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_rust_rationale_10]] — code: Walk a Rust type expression; append (name, role) tuples.
- [[graphify_graphify_extractors_rust_rationale_62]] — code: Extract functions, structs, enums, traits, impl methods, and use declarations fr

## Dependências

- [[graphify_graphify_extractors_rust_extract_rust]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_rust_extract_rust]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_rust_extract_rust]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_rust_rust_collect_type_refs]] → `calls` → [[graphify_graphify_extractors_base_read_text]]
- [[graphify_graphify_extractors_rust]] → `contains` → [[graphify_graphify_extractors_rust_extract_rust]]
- [[graphify_graphify_extractors_rust]] → `contains` → [[graphify_graphify_extractors_rust_rust_collect_type_refs]]
- [[graphify_graphify_extractors_rust_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_rust]]
- [[graphify_graphify_extractors_rust_rationale_10]] → `rationale_for` → [[graphify_graphify_extractors_rust_rust_collect_type_refs]]
- [[graphify_graphify_extractors_rust_extract_rust]] → `references` → [[graphify_graphify_extractors_rust_py_path]]
- [[graphify_graphify_extractors_rust_extract_rust]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_rust_rationale_62]] → `rationale_for` → [[graphify_graphify_extractors_rust_extract_rust]]