# graphify\graphify\affected.py

## Símbolos

- [[graphify_graphify_affected]] — code: affected.py
- [[graphify_graphify_affected_affectedhit]] — code: AffectedHit
- [[graphify_graphify_affected_node_label]] — code: _node_label()
- [[graphify_graphify_affected_format_location]] — code: _format_location()
- [[graphify_graphify_affected_bare_name]] — code: _bare_name()
- [[graphify_graphify_affected_normalize_label]] — code: _normalize_label()
- [[graphify_graphify_affected_prefer_file_node]] — code: _prefer_file_node()
- [[graphify_graphify_affected_resolve_seed]] — code: resolve_seed()
- [[graphify_graphify_affected_affected_nodes]] — code: affected_nodes()
- [[graphify_graphify_affected_format_affected]] — code: format_affected()
- [[graphify_graphify_affected_load_graph]] — code: load_graph()
- [[graphify_graphify_affected_rationale_49]] — code: Lowercased label with the callable decoration (trailing "()") removed.
- [[graphify_graphify_affected_rationale_63]] — code: Return the file-level node when a source_file query matches many nodes.

## Dependências

- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_affected_nodes]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_affectedhit]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_bare_name]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_format_affected]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_format_location]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_load_graph]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_node_label]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_normalize_label]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_prefer_file_node]]
- [[graphify_graphify_affected]] → `contains` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_graphify_affected_affected_nodes]] → `references` → [[graphify_graphify_affected_affectedhit]]
- [[graphify_graphify_affected_format_affected]] → `calls` → [[graphify_graphify_affected_node_label]]
- [[graphify_graphify_affected_format_affected]] → `calls` → [[graphify_graphify_affected_format_location]]
- [[graphify_graphify_affected_bare_name]] → `calls` → [[graphify_graphify_affected_normalize_label]]
- [[graphify_graphify_affected_rationale_49]] → `rationale_for` → [[graphify_graphify_affected_bare_name]]
- [[graphify_graphify_affected_resolve_seed]] → `calls` → [[graphify_graphify_affected_bare_name]]
- [[graphify_graphify_affected_prefer_file_node]] → `calls` → [[graphify_graphify_affected_normalize_label]]
- [[graphify_graphify_affected_resolve_seed]] → `calls` → [[graphify_graphify_affected_normalize_label]]
- [[graphify_graphify_affected_prefer_file_node]] → `calls` → [[graphify_graphify_affected_py_path]]
- [[graphify_graphify_affected_rationale_63]] → `rationale_for` → [[graphify_graphify_affected_prefer_file_node]]
- [[graphify_graphify_affected_resolve_seed]] → `calls` → [[graphify_graphify_affected_prefer_file_node]]
- [[graphify_graphify_affected_format_affected]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_graphify_affected_format_affected]] → `calls` → [[graphify_graphify_affected_affected_nodes]]
- [[graphify_graphify_affected_load_graph]] → `references` → [[graphify_graphify_affected_py_path]]