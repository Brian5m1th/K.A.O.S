# graphify\graphify\ids.py

## Símbolos

- [[graphify_graphify_ids]] — code: ids.py
- [[graphify_graphify_ids_normalize_id]] — code: normalize_id()
- [[graphify_graphify_ids_make_id]] — code: make_id()
- [[graphify_graphify_ids_rationale_1]] — code: Single source of truth for node-ID normalization.  Three independent producers
- [[graphify_graphify_ids_rationale_33]] — code: r"""Normalize a single ID string to its canonical form.      Idempotent: ``nor
- [[graphify_graphify_ids_rationale_44]] — code: Build a canonical node ID from one or more name parts.      Parts are joined w

## Dependências

- [[graphify_graphify_ids]] → `contains` → [[graphify_graphify_ids_make_id]]
- [[graphify_graphify_ids]] → `contains` → [[graphify_graphify_ids_normalize_id]]
- [[graphify_graphify_ids_rationale_1]] → `rationale_for` → [[graphify_graphify_ids]]
- [[graphify_graphify_ids_make_id]] → `calls` → [[graphify_graphify_ids_normalize_id]]
- [[graphify_graphify_ids_rationale_33]] → `rationale_for` → [[graphify_graphify_ids_normalize_id]]
- [[graphify_graphify_ids_rationale_44]] → `rationale_for` → [[graphify_graphify_ids_make_id]]