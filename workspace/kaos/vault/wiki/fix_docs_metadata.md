# scripts\fix_docs_metadata.py

## Símbolos

- [[scripts_fix_docs_metadata]] — code: fix_docs_metadata.py
- [[scripts_fix_docs_metadata_normalize_id]] — code: normalize_id()
- [[scripts_fix_docs_metadata_parse_frontmatters]] — code: parse_frontmatters()
- [[scripts_fix_docs_metadata_fix_metadata]] — code: fix_metadata()

## Dependências

- [[scripts_fix_docs_metadata]] → `contains` → [[scripts_fix_docs_metadata_fix_metadata]]
- [[scripts_fix_docs_metadata]] → `contains` → [[scripts_fix_docs_metadata_normalize_id]]
- [[scripts_fix_docs_metadata]] → `contains` → [[scripts_fix_docs_metadata_parse_frontmatters]]
- [[scripts_fix_docs_metadata_fix_metadata]] → `calls` → [[scripts_fix_docs_metadata_normalize_id]]
- [[scripts_fix_docs_metadata_fix_metadata]] → `calls` → [[scripts_fix_docs_metadata_parse_frontmatters]]