# graphify\graphify\global_graph.py

## Símbolos

- [[graphify_graphify_global_graph]] — code: global_graph.py
- [[graphify_graphify_global_graph_load_manifest]] — code: _load_manifest()
- [[graphify_graphify_global_graph_save_manifest]] — code: _save_manifest()
- [[graphify_graphify_global_graph_load_global_graph]] — code: _load_global_graph()
- [[graphify_graphify_global_graph_save_global_graph]] — code: _save_global_graph()
- [[graphify_graphify_global_graph_file_hash]] — code: _file_hash()
- [[graphify_graphify_global_graph_global_add]] — code: global_add()
- [[graphify_graphify_global_graph_global_remove]] — code: global_remove()
- [[graphify_graphify_global_graph_global_list]] — code: global_list()
- [[graphify_graphify_global_graph_global_path]] — code: global_path()
- [[graphify_graphify_global_graph_rationale_78]] — code: Add or update a project graph in the global graph.      Returns a summary dict
- [[graphify_graphify_global_graph_rationale_160]] — code: Remove all nodes for repo_tag from the global graph. Returns count removed.
- [[graphify_graphify_global_graph_rationale_177]] — code: Return the manifest repos dict.

## Dependências

- [[graphify_graphify_global_graph_global_add]] → `calls` → [[graphify_graphify_build_prefix_graph_for_global]]
- [[graphify_graphify_global_graph_global_add]] → `calls` → [[graphify_graphify_build_prune_repo_from_graph]]
- [[graphify_graphify_global_graph_global_remove]] → `calls` → [[graphify_graphify_build_prune_repo_from_graph]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_file_hash]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_global_add]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_global_list]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_global_path]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_global_remove]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_load_global_graph]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_load_manifest]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_save_global_graph]]
- [[graphify_graphify_global_graph]] → `contains` → [[graphify_graphify_global_graph_save_manifest]]
- [[graphify_graphify_global_graph_global_add]] → `calls` → [[graphify_graphify_global_graph_load_manifest]]
- [[graphify_graphify_global_graph_global_list]] → `calls` → [[graphify_graphify_global_graph_load_manifest]]
- [[graphify_graphify_global_graph_global_remove]] → `calls` → [[graphify_graphify_global_graph_load_manifest]]
- [[graphify_graphify_global_graph_global_add]] → `calls` → [[graphify_graphify_global_graph_save_manifest]]
- [[graphify_graphify_global_graph_global_remove]] → `calls` → [[graphify_graphify_global_graph_save_manifest]]
- [[graphify_graphify_global_graph_global_add]] → `calls` → [[graphify_graphify_global_graph_load_global_graph]]
- [[graphify_graphify_global_graph_global_remove]] → `calls` → [[graphify_graphify_global_graph_load_global_graph]]
- [[graphify_graphify_global_graph_load_global_graph]] → `calls` → [[graphify_graphify_security_check_graph_file_size_cap]]
- [[graphify_graphify_global_graph_load_global_graph]] → `calls` → [[graphify_tests_fixtures_sample_graph]]
- [[graphify_graphify_global_graph_global_add]] → `calls` → [[graphify_graphify_global_graph_save_global_graph]]
- [[graphify_graphify_global_graph_global_remove]] → `calls` → [[graphify_graphify_global_graph_save_global_graph]]
- [[graphify_graphify_global_graph_file_hash]] → `references` → [[graphify_graphify_global_graph_py_path]]
- [[graphify_graphify_global_graph_global_add]] → `calls` → [[graphify_graphify_global_graph_file_hash]]
- [[graphify_graphify_global_graph_global_add]] → `references` → [[graphify_graphify_global_graph_py_path]]
- [[graphify_graphify_global_graph_global_path]] → `references` → [[graphify_graphify_global_graph_py_path]]
- [[graphify_graphify_global_graph_global_add]] → `calls` → [[graphify_graphify_security_check_graph_file_size_cap]]
- [[graphify_graphify_global_graph_rationale_78]] → `rationale_for` → [[graphify_graphify_global_graph_global_add]]
- [[graphify_graphify_global_graph_rationale_160]] → `rationale_for` → [[graphify_graphify_global_graph_global_remove]]
- [[graphify_graphify_global_graph_rationale_177]] → `rationale_for` → [[graphify_graphify_global_graph_global_list]]