# graphify\graphify\extractors\objc.py

## Símbolos

- [[graphify_graphify_extractors_objc]] — code: objc.py
- [[graphify_graphify_extractors_objc_objc_local_var_types]] — code: _objc_local_var_types()
- [[graphify_graphify_extractors_objc_extract_objc]] — code: extract_objc()
- [[graphify_graphify_extractors_objc_rationale_1]] — code: objc — moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_objc_rationale_12]] — code: Collect ``var -> ClassName`` from ObjC local declarations (``Foo *f = ...;``)
- [[graphify_graphify_extractors_objc_rationale_44]] — code: Extract interfaces, implementations, protocols, methods, and imports from .m/.mm

## Dependências

- [[graphify_graphify_extractors_objc_extract_objc]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_objc_extract_objc]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_objc_extract_objc]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_objc_objc_local_var_types]] → `calls` → [[graphify_graphify_extractors_base_read_text]]
- [[graphify_graphify_extractors_objc_objc_local_var_types]] → `calls` → [[graphify_graphify_extractors_engine_cpp_declarator_name]]
- [[graphify_graphify_extractors_objc]] → `contains` → [[graphify_graphify_extractors_objc_extract_objc]]
- [[graphify_graphify_extractors_objc]] → `contains` → [[graphify_graphify_extractors_objc_objc_local_var_types]]
- [[graphify_graphify_extractors_objc_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_objc]]
- [[graphify_graphify_extractors_objc_extract_objc]] → `calls` → [[graphify_graphify_extractors_objc_objc_local_var_types]]
- [[graphify_graphify_extractors_objc_rationale_12]] → `rationale_for` → [[graphify_graphify_extractors_objc_objc_local_var_types]]
- [[graphify_graphify_extractors_objc_extract_objc]] → `references` → [[graphify_graphify_extractors_objc_py_path]]
- [[graphify_graphify_extractors_objc_extract_objc]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_objc_rationale_44]] → `rationale_for` → [[graphify_graphify_extractors_objc_extract_objc]]