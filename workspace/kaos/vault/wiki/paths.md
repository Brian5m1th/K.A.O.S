# graphify\graphify\paths.py

## Símbolos

- [[graphify_graphify_paths]] — code: paths.py
- [[graphify_graphify_paths_is_test_path]] — code: _is_test_path()
- [[graphify_graphify_paths_path_proximity_winner]] — code: _path_proximity_winner()
- [[graphify_graphify_paths_disambiguate_ambiguous_candidates]] — code: disambiguate_ambiguous_candidates()
- [[graphify_graphify_paths_out_path]] — code: out_path()
- [[graphify_graphify_paths_default_graph_json]] — code: default_graph_json()
- [[graphify_graphify_paths_rationale_1]] — code: Single source of truth for the graphify output-directory name.  The output dir
- [[graphify_graphify_paths_rationale_56]] — code: Classify a source path as a test path (case-insensitive, segment-aware).
- [[graphify_graphify_paths_rationale_92]] — code: Pick the candidate whose source file is closest to the call site.      ``candi
- [[graphify_graphify_paths_rationale_158]] — code: Resolve an ambiguous bare-name call to one candidate, or ``None``.      Shared
- [[graphify_graphify_paths_rationale_219]] — code: A path inside the configured output dir, e.g. ``out_path("cache")``.      ``Pa
- [[graphify_graphify_paths_rationale_228]] — code: Default ``graph.json`` path under the configured output dir.      The package-

## Dependências

- [[graphify_graphify_paths]] → `contains` → [[graphify_graphify_paths_default_graph_json]]
- [[graphify_graphify_paths]] → `contains` → [[graphify_graphify_paths_disambiguate_ambiguous_candidates]]
- [[graphify_graphify_paths]] → `contains` → [[graphify_graphify_paths_is_test_path]]
- [[graphify_graphify_paths]] → `contains` → [[graphify_graphify_paths_out_path]]
- [[graphify_graphify_paths]] → `contains` → [[graphify_graphify_paths_path_proximity_winner]]
- [[graphify_graphify_paths_rationale_1]] → `rationale_for` → [[graphify_graphify_paths]]
- [[graphify_graphify_paths_disambiguate_ambiguous_candidates]] → `calls` → [[graphify_graphify_paths_is_test_path]]
- [[graphify_graphify_paths_rationale_56]] → `rationale_for` → [[graphify_graphify_paths_is_test_path]]
- [[graphify_graphify_paths_disambiguate_ambiguous_candidates]] → `calls` → [[graphify_graphify_paths_path_proximity_winner]]
- [[graphify_graphify_paths_rationale_92]] → `rationale_for` → [[graphify_graphify_paths_path_proximity_winner]]
- [[graphify_graphify_paths_rationale_158]] → `rationale_for` → [[graphify_graphify_paths_disambiguate_ambiguous_candidates]]
- [[graphify_graphify_paths_default_graph_json]] → `calls` → [[graphify_graphify_paths_out_path]]
- [[graphify_graphify_paths_out_path]] → `references` → [[graphify_graphify_paths_py_path]]
- [[graphify_graphify_paths_rationale_219]] → `rationale_for` → [[graphify_graphify_paths_out_path]]
- [[graphify_graphify_paths_rationale_228]] → `rationale_for` → [[graphify_graphify_paths_default_graph_json]]