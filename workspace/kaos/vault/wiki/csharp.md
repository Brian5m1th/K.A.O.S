# graphify\graphify\extractors\csharp.py

## Símbolos

- [[graphify_graphify_extractors_csharp]] — code: csharp.py
- [[graphify_graphify_extractors_csharp_build_csharp_type_def_index]] — code: _build_csharp_type_def_index()
- [[graphify_graphify_extractors_csharp_strip_trailing_csharp_generic_args]] — code: _strip_trailing_csharp_generic_args()
- [[graphify_graphify_extractors_csharp_resolve_cross_file_csharp_imports]] — code: _resolve_cross_file_csharp_imports()
- [[graphify_graphify_extractors_csharp_resolve_csharp_type_references]] — code: _resolve_csharp_type_references()
- [[graphify_graphify_extractors_csharp_rationale_1]] — code: C# cross-file resolution.  The config-driven C# *extractor* (``extract_csharp`
- [[graphify_graphify_extractors_csharp_rationale_20]] — code: Return deterministic ``(namespace, name) -> node_id`` C# type definitions.
- [[graphify_graphify_extractors_csharp_rationale_83]] — code: Re-point resolvable C# ``using`` import edges to canonical internal nodes.
- [[graphify_graphify_extractors_csharp_rationale_158]] — code: Arbitrate all C# ``inherits``/``implements``/``references`` targets.      The

## Dependências

- [[graphify_graphify_extractors_csharp]] → `imports` → [[graphify_graphify_exporters_html]]
- [[graphify_graphify_extractors_csharp]] → `contains` → [[graphify_graphify_extractors_csharp_build_csharp_type_def_index]]
- [[graphify_graphify_extractors_csharp]] → `contains` → [[graphify_graphify_extractors_csharp_resolve_cross_file_csharp_imports]]
- [[graphify_graphify_extractors_csharp]] → `contains` → [[graphify_graphify_extractors_csharp_resolve_csharp_type_references]]
- [[graphify_graphify_extractors_csharp]] → `contains` → [[graphify_graphify_extractors_csharp_strip_trailing_csharp_generic_args]]
- [[graphify_graphify_extractors_csharp_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_csharp]]
- [[graphify_graphify_extractors_csharp_rationale_20]] → `rationale_for` → [[graphify_graphify_extractors_csharp_build_csharp_type_def_index]]
- [[graphify_graphify_extractors_csharp_resolve_cross_file_csharp_imports]] → `calls` → [[graphify_graphify_extractors_csharp_build_csharp_type_def_index]]
- [[graphify_graphify_extractors_csharp_resolve_csharp_type_references]] → `calls` → [[graphify_graphify_extractors_csharp_build_csharp_type_def_index]]
- [[graphify_graphify_extractors_csharp_resolve_cross_file_csharp_imports]] → `calls` → [[graphify_graphify_extractors_csharp_strip_trailing_csharp_generic_args]]
- [[graphify_graphify_extractors_csharp_rationale_83]] → `rationale_for` → [[graphify_graphify_extractors_csharp_resolve_cross_file_csharp_imports]]
- [[graphify_graphify_extractors_csharp_resolve_cross_file_csharp_imports]] → `references` → [[graphify_graphify_extractors_csharp_py_path]]
- [[graphify_graphify_extractors_csharp_resolve_csharp_type_references]] → `references` → [[graphify_graphify_extractors_csharp_py_path]]
- [[graphify_graphify_extractors_csharp_rationale_158]] → `rationale_for` → [[graphify_graphify_extractors_csharp_resolve_csharp_type_references]]