# graphify\worked\mixed-corpus\raw\cluster.py

## Símbolos

- [[graphify_worked_mixed_corpus_raw_cluster]] — code: cluster.py
- [[graphify_worked_mixed_corpus_raw_cluster_build_graph]] — code: build_graph()
- [[graphify_worked_mixed_corpus_raw_cluster_cluster]] — code: cluster()
- [[graphify_worked_mixed_corpus_raw_cluster_split_community]] — code: _split_community()
- [[graphify_worked_mixed_corpus_raw_cluster_cohesion_score]] — code: cohesion_score()
- [[graphify_worked_mixed_corpus_raw_cluster_score_all]] — code: score_all()
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_1]] — code: Leiden community detection on NetworkX graphs. Splits oversized communities. Ret
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_7]] — code: Build a NetworkX graph from graphify node/edge dicts.      Preserves original
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_28]] — code: Run Leiden community detection. Returns {community_id: [node_ids]}.      Commu
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_73]] — code: Run a second Leiden pass on a community subgraph to split it further.
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_93]] — code: Ratio of actual intra-community edges to maximum possible.

## Dependências

- [[graphify_worked_mixed_corpus_raw_cluster_build_graph]] → `calls` → [[graphify_tests_fixtures_sample_graph]]
- [[graphify_worked_mixed_corpus_raw_cluster]] → `contains` → [[graphify_worked_mixed_corpus_raw_cluster_build_graph]]
- [[graphify_worked_mixed_corpus_raw_cluster]] → `contains` → [[graphify_worked_mixed_corpus_raw_cluster_cluster]]
- [[graphify_worked_mixed_corpus_raw_cluster]] → `contains` → [[graphify_worked_mixed_corpus_raw_cluster_cohesion_score]]
- [[graphify_worked_mixed_corpus_raw_cluster]] → `contains` → [[graphify_worked_mixed_corpus_raw_cluster_score_all]]
- [[graphify_worked_mixed_corpus_raw_cluster]] → `contains` → [[graphify_worked_mixed_corpus_raw_cluster_split_community]]
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_1]] → `rationale_for` → [[graphify_worked_mixed_corpus_raw_cluster]]
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_7]] → `rationale_for` → [[graphify_worked_mixed_corpus_raw_cluster_build_graph]]
- [[graphify_worked_mixed_corpus_raw_cluster_cluster]] → `calls` → [[graphify_worked_mixed_corpus_raw_cluster_split_community]]
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_28]] → `rationale_for` → [[graphify_worked_mixed_corpus_raw_cluster_cluster]]
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_73]] → `rationale_for` → [[graphify_worked_mixed_corpus_raw_cluster_split_community]]
- [[graphify_worked_mixed_corpus_raw_cluster_rationale_93]] → `rationale_for` → [[graphify_worked_mixed_corpus_raw_cluster_cohesion_score]]
- [[graphify_worked_mixed_corpus_raw_cluster_score_all]] → `calls` → [[graphify_worked_mixed_corpus_raw_cluster_cohesion_score]]