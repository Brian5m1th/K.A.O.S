# graphify\graphify\pg_introspect.py

## Símbolos

- [[graphify_graphify_pg_introspect]] — code: pg_introspect.py
- [[graphify_graphify_pg_introspect_quote_ident]] — code: _quote_ident()
- [[graphify_graphify_pg_introspect_introspect_postgres]] — code: introspect_postgres()
- [[graphify_graphify_pg_introspect_rationale_7]] — code: Double-quote a PostgreSQL identifier, escaping embedded double-quotes.
- [[graphify_graphify_pg_introspect_rationale_12]] — code: Connect to PostgreSQL, reconstruct DDL, and extract via extract_sql().

## Dependências

- [[graphify_graphify_pg_introspect]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_graphify_pg_introspect_introspect_postgres]] → `calls` → [[graphify_graphify_extractors_sql_extract_sql]]
- [[graphify_graphify_pg_introspect]] → `contains` → [[graphify_graphify_pg_introspect_introspect_postgres]]
- [[graphify_graphify_pg_introspect]] → `contains` → [[graphify_graphify_pg_introspect_quote_ident]]
- [[graphify_graphify_pg_introspect_introspect_postgres]] → `calls` → [[graphify_graphify_pg_introspect_quote_ident]]
- [[graphify_graphify_pg_introspect_rationale_7]] → `rationale_for` → [[graphify_graphify_pg_introspect_quote_ident]]
- [[graphify_graphify_pg_introspect_rationale_12]] → `rationale_for` → [[graphify_graphify_pg_introspect_introspect_postgres]]