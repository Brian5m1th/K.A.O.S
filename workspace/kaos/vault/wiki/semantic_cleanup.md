# graphify\graphify\semantic_cleanup.py

## Símbolos

- [[graphify_graphify_semantic_cleanup]] — code: semantic_cleanup.py
- [[graphify_graphify_semantic_cleanup_validate_semantic_fragment]] — code: validate_semantic_fragment()
- [[graphify_graphify_semantic_cleanup_load_validated_semantic_fragment]] — code: load_validated_semantic_fragment()
- [[graphify_graphify_semantic_cleanup_validate_semantic_id]] — code: _validate_semantic_id()
- [[graphify_graphify_semantic_cleanup_sanitize_semantic_fragment]] — code: sanitize_semantic_fragment()
- [[graphify_graphify_semantic_cleanup_is_sentence_like_rationale_label]] — code: _is_sentence_like_rationale_label()
- [[graphify_graphify_semantic_cleanup_append_rationale_attr]] — code: _append_rationale_attr()
- [[graphify_graphify_semantic_cleanup_rationale_38]] — code: Return validation errors for an untrusted semantic extraction fragment.      E
- [[graphify_graphify_semantic_cleanup_rationale_127]] — code: Load and validate a semantic chunk, rejecting oversize files before parsing.
- [[graphify_graphify_semantic_cleanup_rationale_166]] — code: Clean up a semantic extraction fragment in-place.      Operations:     1. Rem
- [[graphify_graphify_semantic_cleanup_rationale_297]] — code: Return True if *label* looks like prose / rationale text rather than an     ent
- [[graphify_graphify_semantic_cleanup_rationale_318]] — code: Append one or more rationale strings to *node*'s ``rationale`` attribute.

## Dependências

- [[graphify_graphify_semantic_cleanup]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_graphify_semantic_cleanup]] → `imports` → [[graphify_graphify_build_normalize_hyperedge_members]]
- [[graphify_graphify_semantic_cleanup_sanitize_semantic_fragment]] → `calls` → [[graphify_graphify_build_normalize_hyperedge_members]]
- [[graphify_graphify_semantic_cleanup_validate_semantic_fragment]] → `calls` → [[graphify_graphify_build_normalize_hyperedge_members]]
- [[graphify_graphify_semantic_cleanup]] → `contains` → [[graphify_graphify_semantic_cleanup_append_rationale_attr]]
- [[graphify_graphify_semantic_cleanup]] → `contains` → [[graphify_graphify_semantic_cleanup_is_sentence_like_rationale_label]]
- [[graphify_graphify_semantic_cleanup]] → `contains` → [[graphify_graphify_semantic_cleanup_load_validated_semantic_fragment]]
- [[graphify_graphify_semantic_cleanup]] → `contains` → [[graphify_graphify_semantic_cleanup_sanitize_semantic_fragment]]
- [[graphify_graphify_semantic_cleanup]] → `contains` → [[graphify_graphify_semantic_cleanup_validate_semantic_fragment]]
- [[graphify_graphify_semantic_cleanup]] → `contains` → [[graphify_graphify_semantic_cleanup_validate_semantic_id]]
- [[graphify_graphify_semantic_cleanup_load_validated_semantic_fragment]] → `calls` → [[graphify_graphify_semantic_cleanup_validate_semantic_fragment]]
- [[graphify_graphify_semantic_cleanup_rationale_38]] → `rationale_for` → [[graphify_graphify_semantic_cleanup_validate_semantic_fragment]]
- [[graphify_graphify_semantic_cleanup_validate_semantic_fragment]] → `calls` → [[graphify_graphify_semantic_cleanup_validate_semantic_id]]
- [[graphify_graphify_semantic_cleanup_load_validated_semantic_fragment]] → `references` → [[graphify_graphify_semantic_cleanup_py_path]]
- [[graphify_graphify_semantic_cleanup_rationale_127]] → `rationale_for` → [[graphify_graphify_semantic_cleanup_load_validated_semantic_fragment]]
- [[graphify_graphify_semantic_cleanup_rationale_166]] → `rationale_for` → [[graphify_graphify_semantic_cleanup_sanitize_semantic_fragment]]
- [[graphify_graphify_semantic_cleanup_sanitize_semantic_fragment]] → `calls` → [[graphify_graphify_semantic_cleanup_append_rationale_attr]]
- [[graphify_graphify_semantic_cleanup_sanitize_semantic_fragment]] → `calls` → [[graphify_graphify_semantic_cleanup_is_sentence_like_rationale_label]]
- [[graphify_graphify_semantic_cleanup_rationale_297]] → `rationale_for` → [[graphify_graphify_semantic_cleanup_is_sentence_like_rationale_label]]
- [[graphify_graphify_semantic_cleanup_rationale_318]] → `rationale_for` → [[graphify_graphify_semantic_cleanup_append_rationale_attr]]