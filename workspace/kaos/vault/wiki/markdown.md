# graphify\graphify\extractors\markdown.py

## Símbolos

- [[graphify_graphify_extractors_markdown]] — code: markdown.py
- [[graphify_graphify_extractors_markdown_resolve_markdown_link]] — code: _resolve_markdown_link()
- [[graphify_graphify_extractors_markdown_extract_markdown]] — code: extract_markdown()
- [[graphify_graphify_extractors_markdown_rationale_1]] — code: Markdown extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_markdown_rationale_20]] — code: Resolve a markdown link target to the absolute path of a sibling document.
- [[graphify_graphify_extractors_markdown_rationale_54]] — code: Extract structural nodes and edges from a Markdown file.      Produces nodes f

## Dependências

- [[graphify_graphify_extractors_markdown_extract_markdown]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_markdown_extract_markdown]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_markdown_extract_markdown]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_markdown]] → `contains` → [[graphify_graphify_extractors_markdown_extract_markdown]]
- [[graphify_graphify_extractors_markdown]] → `contains` → [[graphify_graphify_extractors_markdown_resolve_markdown_link]]
- [[graphify_graphify_extractors_markdown_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_markdown]]
- [[graphify_graphify_extractors_markdown_rationale_20]] → `rationale_for` → [[graphify_graphify_extractors_markdown_resolve_markdown_link]]
- [[graphify_graphify_extractors_markdown_resolve_markdown_link]] → `references` → [[graphify_graphify_extractors_markdown_py_path]]
- [[graphify_graphify_extractors_markdown_extract_markdown]] → `references` → [[graphify_graphify_extractors_markdown_py_path]]
- [[graphify_graphify_extractors_markdown_extract_markdown]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_markdown_rationale_54]] → `rationale_for` → [[graphify_graphify_extractors_markdown_extract_markdown]]