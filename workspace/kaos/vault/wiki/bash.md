# graphify\graphify\extractors\bash.py

## Símbolos

- [[graphify_graphify_extractors_bash]] — code: bash.py
- [[graphify_graphify_extractors_bash_extract_bash]] — code: extract_bash()
- [[graphify_graphify_extractors_bash_rationale_1]] — code: Bash extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_bash_rationale_11]] — code: Extract functions, source imports, and cross-function calls from a .sh file.

## Dependências

- [[graphify_graphify_extractors_bash_extract_bash]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_bash_extract_bash]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_bash_extract_bash]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_bash]] → `contains` → [[graphify_graphify_extractors_bash_extract_bash]]
- [[graphify_graphify_extractors_bash_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_bash]]
- [[graphify_graphify_extractors_bash_extract_bash]] → `references` → [[graphify_graphify_extractors_bash_py_path]]
- [[graphify_graphify_extractors_bash_extract_bash]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_bash_rationale_11]] → `rationale_for` → [[graphify_graphify_extractors_bash_extract_bash]]