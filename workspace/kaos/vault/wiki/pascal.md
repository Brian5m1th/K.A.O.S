# graphify\graphify\extractors\pascal.py

## Símbolos

- [[graphify_graphify_extractors_pascal]] — code: pascal.py
- [[graphify_graphify_extractors_pascal_pascal_strip_comments]] — code: _pascal_strip_comments()
- [[graphify_graphify_extractors_pascal_pascal_split_sections]] — code: _pascal_split_sections()
- [[graphify_graphify_extractors_pascal_pascal_split_uses]] — code: _pascal_split_uses()
- [[graphify_graphify_extractors_pascal_pascal_split_bases]] — code: _pascal_split_bases()
- [[graphify_graphify_extractors_pascal_pascal_find_body]] — code: _pascal_find_body()
- [[graphify_graphify_extractors_pascal_resolve_pascal_callee_factory]] — code: _resolve_pascal_callee_factory()
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] — code: _extract_pascal_regex()
- [[graphify_graphify_extractors_pascal_extract_pascal]] — code: extract_pascal()
- [[graphify_graphify_extractors_pascal_rationale_1]] — code: pascal — moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_pascal_rationale_78]] — code: Strip Pascal comments ({}, (* *), //) while preserving newlines.
- [[graphify_graphify_extractors_pascal_rationale_87]] — code: Split into (iface_text, iface_offset, impl_text, impl_offset).     Files withou
- [[graphify_graphify_extractors_pascal_rationale_104]] — code: Split a uses list string, handling 'Foo in ''bar.pas''' syntax.
- [[graphify_graphify_extractors_pascal_rationale_114]] — code: Split inheritance list, handling generics like TList<T, U>.
- [[graphify_graphify_extractors_pascal_rationale_136]] — code: Find balanced begin..end after start. Returns (body_start, body_end).     Retur
- [[graphify_graphify_extractors_pascal_rationale_159]] — code: Build a scoped call resolver for a single Pascal/Delphi file.      ``records``
- [[graphify_graphify_extractors_pascal_rationale_232]] — code: Regex fallback for Pascal/Delphi extraction when tree-sitter-pascal     is unav
- [[graphify_graphify_extractors_pascal_rationale_431]] — code: Extract units, classes, procedures, uses-imports, and calls from Pascal/Delphi f

## Dependências

- [[graphify_graphify_extractors_pascal_extract_pascal]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_pascal_extract_pascal]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_pascal_extract_pascal]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_pascal]] → `contains` → [[graphify_graphify_extractors_pascal_extract_pascal]]
- [[graphify_graphify_extractors_pascal]] → `contains` → [[graphify_graphify_extractors_pascal_extract_pascal_regex]]
- [[graphify_graphify_extractors_pascal]] → `contains` → [[graphify_graphify_extractors_pascal_pascal_find_body]]
- [[graphify_graphify_extractors_pascal]] → `contains` → [[graphify_graphify_extractors_pascal_pascal_split_bases]]
- [[graphify_graphify_extractors_pascal]] → `contains` → [[graphify_graphify_extractors_pascal_pascal_split_sections]]
- [[graphify_graphify_extractors_pascal]] → `contains` → [[graphify_graphify_extractors_pascal_pascal_split_uses]]
- [[graphify_graphify_extractors_pascal]] → `contains` → [[graphify_graphify_extractors_pascal_pascal_strip_comments]]
- [[graphify_graphify_extractors_pascal]] → `contains` → [[graphify_graphify_extractors_pascal_resolve_pascal_callee_factory]]
- [[graphify_graphify_extractors_pascal_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_pascal]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_pascal_pascal_strip_comments]]
- [[graphify_graphify_extractors_pascal_rationale_78]] → `rationale_for` → [[graphify_graphify_extractors_pascal_pascal_strip_comments]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_pascal_pascal_split_sections]]
- [[graphify_graphify_extractors_pascal_rationale_87]] → `rationale_for` → [[graphify_graphify_extractors_pascal_pascal_split_sections]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_pascal_pascal_split_uses]]
- [[graphify_graphify_extractors_pascal_rationale_104]] → `rationale_for` → [[graphify_graphify_extractors_pascal_pascal_split_uses]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_pascal_pascal_split_bases]]
- [[graphify_graphify_extractors_pascal_rationale_114]] → `rationale_for` → [[graphify_graphify_extractors_pascal_pascal_split_bases]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_pascal_pascal_find_body]]
- [[graphify_graphify_extractors_pascal_rationale_136]] → `rationale_for` → [[graphify_graphify_extractors_pascal_pascal_find_body]]
- [[graphify_graphify_extractors_pascal_extract_pascal]] → `calls` → [[graphify_graphify_extractors_pascal_resolve_pascal_callee_factory]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_pascal_resolve_pascal_callee_factory]]
- [[graphify_graphify_extractors_pascal_rationale_159]] → `rationale_for` → [[graphify_graphify_extractors_pascal_resolve_pascal_callee_factory]]
- [[graphify_graphify_extractors_pascal_extract_pascal]] → `calls` → [[graphify_graphify_extractors_pascal_extract_pascal_regex]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `references` → [[graphify_graphify_extractors_pascal_py_path]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_resolution_pascal_resolve_class]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_extractors_resolution_pascal_resolve_unit]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_mcp_ingest_add_edge]]
- [[graphify_graphify_extractors_pascal_extract_pascal_regex]] → `calls` → [[graphify_graphify_mcp_ingest_add_node]]
- [[graphify_graphify_extractors_pascal_rationale_232]] → `rationale_for` → [[graphify_graphify_extractors_pascal_extract_pascal_regex]]
- [[graphify_graphify_extractors_pascal_extract_pascal]] → `references` → [[graphify_graphify_extractors_pascal_py_path]]
- [[graphify_graphify_extractors_pascal_rationale_431]] → `rationale_for` → [[graphify_graphify_extractors_pascal_extract_pascal]]