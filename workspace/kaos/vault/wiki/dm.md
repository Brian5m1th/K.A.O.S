# graphify\graphify\extractors\dm.py

## Símbolos

- [[graphify_graphify_extractors_dm]] — code: dm.py
- [[graphify_graphify_extractors_dm_extract_dm]] — code: extract_dm()
- [[graphify_graphify_extractors_dm_read_dmi_description]] — code: _read_dmi_description()
- [[graphify_graphify_extractors_dm_extract_dmi]] — code: extract_dmi()
- [[graphify_graphify_extractors_dm_split_dmm_tile]] — code: _split_dmm_tile()
- [[graphify_graphify_extractors_dm_dmm_type_path]] — code: _dmm_type_path()
- [[graphify_graphify_extractors_dm_extract_dmm]] — code: extract_dmm()
- [[graphify_graphify_extractors_dm_extract_dmf]] — code: extract_dmf()
- [[graphify_graphify_extractors_dm_rationale_1]] — code: Dm extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_dm_rationale_12]] — code: Extract types, procs, includes, and calls from a .dm/.dme file.
- [[graphify_graphify_extractors_dm_rationale_252]] — code: Pull the BYOND metadata text out of a .dmi PNG, or empty string on failure.
- [[graphify_graphify_extractors_dm_rationale_276]] — code: Extract icon state names from a .dmi (BYOND PNG icon sheet).
- [[graphify_graphify_extractors_dm_rationale_365]] — code: Extract type-path references from a .dmm map file's tile dictionary.
- [[graphify_graphify_extractors_dm_rationale_437]] — code: Extract windows and controls from a .dmf interface file.

## Dependências

- [[graphify_graphify_extractors_dm_extract_dm]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_dm_extract_dm]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_dm_extract_dmf]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_dm_extract_dmi]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_dm_extract_dmm]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_dm_extract_dm]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_dm_extract_dmf]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_dm_extract_dmi]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_dm]] → `contains` → [[graphify_graphify_extractors_dm_dmm_type_path]]
- [[graphify_graphify_extractors_dm]] → `contains` → [[graphify_graphify_extractors_dm_extract_dm]]
- [[graphify_graphify_extractors_dm]] → `contains` → [[graphify_graphify_extractors_dm_extract_dmf]]
- [[graphify_graphify_extractors_dm]] → `contains` → [[graphify_graphify_extractors_dm_extract_dmi]]
- [[graphify_graphify_extractors_dm]] → `contains` → [[graphify_graphify_extractors_dm_extract_dmm]]
- [[graphify_graphify_extractors_dm]] → `contains` → [[graphify_graphify_extractors_dm_read_dmi_description]]
- [[graphify_graphify_extractors_dm]] → `contains` → [[graphify_graphify_extractors_dm_split_dmm_tile]]
- [[graphify_graphify_extractors_dm_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_dm]]
- [[graphify_graphify_extractors_dm_extract_dm]] → `references` → [[graphify_graphify_extractors_dm_py_path]]
- [[graphify_graphify_extractors_dm_extract_dm]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_dm_rationale_12]] → `rationale_for` → [[graphify_graphify_extractors_dm_extract_dm]]
- [[graphify_graphify_extractors_dm_extract_dmf]] → `references` → [[graphify_graphify_extractors_dm_py_path]]
- [[graphify_graphify_extractors_dm_extract_dmi]] → `references` → [[graphify_graphify_extractors_dm_py_path]]
- [[graphify_graphify_extractors_dm_extract_dmm]] → `references` → [[graphify_graphify_extractors_dm_py_path]]
- [[graphify_graphify_extractors_dm_extract_dmi]] → `calls` → [[graphify_graphify_extractors_dm_read_dmi_description]]
- [[graphify_graphify_extractors_dm_rationale_252]] → `rationale_for` → [[graphify_graphify_extractors_dm_read_dmi_description]]
- [[graphify_graphify_extractors_dm_extract_dmi]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_dm_rationale_276]] → `rationale_for` → [[graphify_graphify_extractors_dm_extract_dmi]]
- [[graphify_graphify_extractors_dm_extract_dmm]] → `calls` → [[graphify_graphify_extractors_dm_split_dmm_tile]]
- [[graphify_graphify_extractors_dm_extract_dmm]] → `calls` → [[graphify_graphify_extractors_dm_dmm_type_path]]
- [[graphify_graphify_extractors_dm_extract_dmm]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_dm_rationale_365]] → `rationale_for` → [[graphify_graphify_extractors_dm_extract_dmm]]
- [[graphify_graphify_extractors_dm_extract_dmf]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_dm_rationale_437]] → `rationale_for` → [[graphify_graphify_extractors_dm_extract_dmf]]