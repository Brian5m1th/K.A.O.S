# graphify\graphify\querylog.py

## Símbolos

- [[graphify_graphify_querylog]] — code: querylog.py
- [[graphify_graphify_querylog_log_path]] — code: _log_path()
- [[graphify_graphify_querylog_log_responses]] — code: _log_responses()
- [[graphify_graphify_querylog_nodes_from_result]] — code: nodes_from_result()
- [[graphify_graphify_querylog_log_query]] — code: log_query()
- [[graphify_graphify_querylog_rationale_1]] — code: Query logging for graphify — append-only JSONL, fail-silent.
- [[graphify_graphify_querylog_rationale_43]] — code: Append one JSONL record to the query log. Never raises.

## Dependências

- [[graphify_graphify_querylog]] → `contains` → [[graphify_graphify_querylog_log_path]]
- [[graphify_graphify_querylog]] → `contains` → [[graphify_graphify_querylog_log_query]]
- [[graphify_graphify_querylog]] → `contains` → [[graphify_graphify_querylog_log_responses]]
- [[graphify_graphify_querylog]] → `contains` → [[graphify_graphify_querylog_nodes_from_result]]
- [[graphify_graphify_querylog_rationale_1]] → `rationale_for` → [[graphify_graphify_querylog]]
- [[graphify_graphify_querylog_log_path]] → `references` → [[graphify_graphify_querylog_py_path]]
- [[graphify_graphify_querylog_log_query]] → `calls` → [[graphify_graphify_querylog_log_path]]
- [[graphify_graphify_querylog_log_query]] → `calls` → [[graphify_graphify_querylog_log_responses]]
- [[graphify_graphify_querylog_log_query]] → `calls` → [[graphify_graphify_querylog_nodes_from_result]]
- [[graphify_graphify_querylog_log_query]] → `references` → [[graphify_graphify_querylog_py_any]]
- [[graphify_graphify_querylog_rationale_43]] → `rationale_for` → [[graphify_graphify_querylog_log_query]]