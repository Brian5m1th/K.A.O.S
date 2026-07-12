# graphify\graphify\_minhash.py

## Símbolos

- [[graphify_graphify_minhash]] — code: _minhash.py
- [[graphify_graphify_minhash_mh_coeffs]] — code: _mh_coeffs()
- [[graphify_graphify_minhash_minhash]] — code: MinHash
- [[graphify_graphify_minhash_minhash_init]] — code: .__init__()
- [[graphify_graphify_minhash_minhash_update]] — code: .update()
- [[graphify_graphify_minhash_lsh_integrate]] — code: _lsh_integrate()
- [[graphify_graphify_minhash_optimal_lsh_params]] — code: _optimal_lsh_params()
- [[graphify_graphify_minhash_minhashlsh]] — code: MinHashLSH
- [[graphify_graphify_minhash_minhashlsh_init]] — code: .__init__()
- [[graphify_graphify_minhash_minhashlsh_insert]] — code: .insert()
- [[graphify_graphify_minhash_minhashlsh_query]] — code: .query()
- [[graphify_graphify_minhash_rationale_1]] — code: MinHash + band-LSH — datasketch-compatible drop-in (no scipy).  datasketch.lsh
- [[graphify_graphify_minhash_rationale_37]] — code: MinHash sketch — same API as datasketch.MinHash for the subset used here.
- [[graphify_graphify_minhash_rationale_53]] — code: Numerical integration — replaces scipy.integrate.quad for LSH param search.
- [[graphify_graphify_minhash_rationale_62]] — code: Find (bands, rows) that minimise weighted FP+FN error, without scipy.
- [[graphify_graphify_minhash_rationale_85]] — code: Band-hashing LSH — same API as datasketch.MinHashLSH for the subset used here.

## Dependências

- [[graphify_graphify_minhash]] → `contains` → [[graphify_graphify_minhash_lsh_integrate]]
- [[graphify_graphify_minhash]] → `contains` → [[graphify_graphify_minhash_mh_coeffs]]
- [[graphify_graphify_minhash]] → `contains` → [[graphify_graphify_minhash_minhash]]
- [[graphify_graphify_minhash]] → `contains` → [[graphify_graphify_minhash_minhashlsh]]
- [[graphify_graphify_minhash]] → `contains` → [[graphify_graphify_minhash_optimal_lsh_params]]
- [[graphify_graphify_minhash_rationale_1]] → `rationale_for` → [[graphify_graphify_minhash]]
- [[graphify_graphify_minhash_mh_coeffs]] → `references` → [[ndarray]]
- [[graphify_graphify_minhash_minhash_init]] → `calls` → [[graphify_graphify_minhash_mh_coeffs]]
- [[graphify_graphify_minhash_minhash]] → `method` → [[graphify_graphify_minhash_minhash_init]]
- [[graphify_graphify_minhash_minhash]] → `method` → [[graphify_graphify_minhash_minhash_update]]
- [[graphify_graphify_minhash_minhashlsh_insert]] → `references` → [[graphify_graphify_minhash_minhash]]
- [[graphify_graphify_minhash_minhashlsh_query]] → `references` → [[graphify_graphify_minhash_minhash]]
- [[graphify_graphify_minhash_rationale_37]] → `rationale_for` → [[graphify_graphify_minhash_minhash]]
- [[graphify_graphify_minhash_minhashlsh_query]] → `calls` → [[graphify_graphify_minhash_minhash_update]]
- [[graphify_graphify_minhash_optimal_lsh_params]] → `calls` → [[graphify_graphify_minhash_lsh_integrate]]
- [[graphify_graphify_minhash_rationale_53]] → `rationale_for` → [[graphify_graphify_minhash_lsh_integrate]]
- [[graphify_graphify_minhash_minhashlsh_init]] → `calls` → [[graphify_graphify_minhash_optimal_lsh_params]]
- [[graphify_graphify_minhash_rationale_62]] → `rationale_for` → [[graphify_graphify_minhash_optimal_lsh_params]]
- [[graphify_graphify_minhash_minhashlsh]] → `method` → [[graphify_graphify_minhash_minhashlsh_init]]
- [[graphify_graphify_minhash_minhashlsh]] → `method` → [[graphify_graphify_minhash_minhashlsh_insert]]
- [[graphify_graphify_minhash_minhashlsh]] → `method` → [[graphify_graphify_minhash_minhashlsh_query]]
- [[graphify_graphify_minhash_rationale_85]] → `rationale_for` → [[graphify_graphify_minhash_minhashlsh]]