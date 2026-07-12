# graphify\graphify\extractors\json_config.py

## Símbolos

- [[graphify_graphify_extractors_json_config]] — code: json_config.py
- [[graphify_graphify_extractors_json_config_is_config_json]] — code: _is_config_json()
- [[graphify_graphify_extractors_json_config_extract_json]] — code: extract_json()
- [[graphify_graphify_extractors_json_config_rationale_1]] — code: Json_config extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_json_config_rationale_24]] — code: True if a .json file is a recognized config/manifest worth AST-extracting.
- [[graphify_graphify_extractors_json_config_rationale_51]] — code: Extract structure and dependency edges from a *config/manifest* .json file.

## Dependências

- [[graphify_graphify_extractors_json_config_extract_json]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_json_config_extract_json]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_json_config_extract_json]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_json_config_is_config_json]] → `calls` → [[graphify_graphify_extractors_base_read_text]]
- [[graphify_graphify_extractors_json_config]] → `contains` → [[graphify_graphify_extractors_json_config_extract_json]]
- [[graphify_graphify_extractors_json_config]] → `contains` → [[graphify_graphify_extractors_json_config_is_config_json]]
- [[graphify_graphify_extractors_json_config_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_json_config]]
- [[graphify_graphify_extractors_json_config_extract_json]] → `calls` → [[graphify_graphify_extractors_json_config_is_config_json]]
- [[graphify_graphify_extractors_json_config_is_config_json]] → `references` → [[graphify_graphify_extractors_json_config_py_path]]
- [[graphify_graphify_extractors_json_config_rationale_24]] → `rationale_for` → [[graphify_graphify_extractors_json_config_is_config_json]]
- [[graphify_graphify_extractors_json_config_extract_json]] → `references` → [[graphify_graphify_extractors_json_config_py_path]]
- [[graphify_graphify_extractors_json_config_extract_json]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_json_config_rationale_51]] → `rationale_for` → [[graphify_graphify_extractors_json_config_extract_json]]