# graphify\graphify\extractors\verilog.py

## Símbolos

- [[graphify_graphify_extractors_verilog]] — code: verilog.py
- [[graphify_graphify_extractors_verilog_sv_first_identifier]] — code: _sv_first_identifier()
- [[graphify_graphify_extractors_verilog_sv_child]] — code: _sv_child()
- [[graphify_graphify_extractors_verilog_sv_strip_comments]] — code: _sv_strip_comments()
- [[graphify_graphify_extractors_verilog_sv_split_type_list]] — code: _sv_split_type_list()
- [[graphify_graphify_extractors_verilog_sv_collect_type_refs]] — code: _sv_collect_type_refs()
- [[graphify_graphify_extractors_verilog_augment_systemverilog_semantics]] — code: _augment_systemverilog_semantics()
- [[graphify_graphify_extractors_verilog_extract_verilog]] — code: extract_verilog()
- [[graphify_graphify_extractors_verilog_rationale_1]] — code: Verilog extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_verilog_rationale_11]] — code: First `simple_identifier` under node in pre-order, or None.      tree-sitter-v
- [[graphify_graphify_extractors_verilog_rationale_206]] — code: Extract modules, functions, tasks, package imports, instantiations, and     Sys

## Dependências

- [[graphify_graphify_extractors_verilog_augment_systemverilog_semantics]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_verilog_extract_verilog]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_verilog_augment_systemverilog_semantics]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_verilog_extract_verilog]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_verilog_extract_verilog]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_verilog_sv_first_identifier]] → `calls` → [[graphify_graphify_extractors_base_read_text]]
- [[graphify_graphify_extractors_verilog]] → `contains` → [[graphify_graphify_extractors_verilog_augment_systemverilog_semantics]]
- [[graphify_graphify_extractors_verilog]] → `contains` → [[graphify_graphify_extractors_verilog_extract_verilog]]
- [[graphify_graphify_extractors_verilog]] → `contains` → [[graphify_graphify_extractors_verilog_sv_child]]
- [[graphify_graphify_extractors_verilog]] → `contains` → [[graphify_graphify_extractors_verilog_sv_collect_type_refs]]
- [[graphify_graphify_extractors_verilog]] → `contains` → [[graphify_graphify_extractors_verilog_sv_first_identifier]]
- [[graphify_graphify_extractors_verilog]] → `contains` → [[graphify_graphify_extractors_verilog_sv_split_type_list]]
- [[graphify_graphify_extractors_verilog]] → `contains` → [[graphify_graphify_extractors_verilog_sv_strip_comments]]
- [[graphify_graphify_extractors_verilog_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_verilog]]
- [[graphify_graphify_extractors_verilog_rationale_11]] → `rationale_for` → [[graphify_graphify_extractors_verilog_sv_first_identifier]]
- [[graphify_graphify_extractors_verilog_augment_systemverilog_semantics]] → `calls` → [[graphify_graphify_extractors_verilog_sv_strip_comments]]
- [[graphify_graphify_extractors_verilog_augment_systemverilog_semantics]] → `calls` → [[graphify_graphify_extractors_verilog_sv_split_type_list]]
- [[graphify_graphify_extractors_verilog_sv_collect_type_refs]] → `calls` → [[graphify_graphify_extractors_verilog_sv_split_type_list]]
- [[graphify_graphify_extractors_verilog_augment_systemverilog_semantics]] → `calls` → [[graphify_graphify_extractors_verilog_sv_collect_type_refs]]
- [[graphify_graphify_extractors_verilog_extract_verilog]] → `calls` → [[graphify_graphify_extractors_verilog_augment_systemverilog_semantics]]
- [[graphify_graphify_extractors_verilog_extract_verilog]] → `references` → [[graphify_graphify_extractors_verilog_py_path]]
- [[graphify_graphify_extractors_verilog_extract_verilog]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_verilog_rationale_206]] → `rationale_for` → [[graphify_graphify_extractors_verilog_extract_verilog]]