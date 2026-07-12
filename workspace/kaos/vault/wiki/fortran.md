# graphify\graphify\extractors\fortran.py

## Símbolos

- [[graphify_graphify_extractors_fortran]] — code: fortran.py
- [[graphify_graphify_extractors_fortran_cpp_preprocess]] — code: _cpp_preprocess()
- [[graphify_graphify_extractors_fortran_extract_fortran]] — code: extract_fortran()
- [[graphify_graphify_extractors_fortran_rationale_1]] — code: Fortran extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_fortran_rationale_12]] — code: Run cpp -w -P on a capital-F Fortran file and return preprocessed bytes.
- [[graphify_graphify_extractors_fortran_rationale_45]] — code: Extract programs, modules, subroutines, functions, use statements, and calls fro

## Dependências

- [[graphify_graphify_extractors_fortran_extract_fortran]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback_add_node]]
- [[graphify_graphify_extractors_fortran_extract_fortran]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_fortran_extract_fortran]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_fortran]] → `contains` → [[graphify_graphify_extractors_fortran_cpp_preprocess]]
- [[graphify_graphify_extractors_fortran]] → `contains` → [[graphify_graphify_extractors_fortran_extract_fortran]]
- [[graphify_graphify_extractors_fortran_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_fortran]]
- [[graphify_graphify_extractors_fortran_cpp_preprocess]] → `references` → [[graphify_graphify_extractors_fortran_py_path]]
- [[graphify_graphify_extractors_fortran_extract_fortran]] → `calls` → [[graphify_graphify_extractors_fortran_cpp_preprocess]]
- [[graphify_graphify_extractors_fortran_rationale_12]] → `rationale_for` → [[graphify_graphify_extractors_fortran_cpp_preprocess]]
- [[graphify_graphify_extractors_fortran_extract_fortran]] → `references` → [[graphify_graphify_extractors_fortran_py_path]]
- [[graphify_graphify_extractors_fortran_extract_fortran]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_fortran_rationale_45]] → `rationale_for` → [[graphify_graphify_extractors_fortran_extract_fortran]]