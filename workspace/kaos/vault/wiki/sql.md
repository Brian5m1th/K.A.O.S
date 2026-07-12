# graphify\graphify\extractors\sql.py

## Símbolos

- [[graphify_graphify_extractors_sql]] — code: sql.py
- [[graphify_graphify_extractors_sql_extract_sql]] — code: extract_sql()
- [[graphify_graphify_extractors_sql_rationale_1]] — code: Sql extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_sql_rationale_11]] — code: Extract tables, views, functions, and relationships from .sql files via tree-sit

## Dependências

- [[graphify_graphify_extractors_sql_extract_sql]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_sql_extract_sql]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_extractors_sql]] → `contains` → [[graphify_graphify_extractors_sql_extract_sql]]
- [[graphify_graphify_extractors_sql_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_sql]]
- [[graphify_graphify_extractors_sql_extract_sql]] → `references` → [[graphify_graphify_extractors_sql_py_path]]
- [[graphify_graphify_extractors_sql_extract_sql]] → `calls` → [[graphify_graphify_mcp_ingest_add_edge]]
- [[graphify_graphify_extractors_sql_rationale_11]] → `rationale_for` → [[graphify_graphify_extractors_sql_extract_sql]]