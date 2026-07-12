# assistant\scripts\migrate_memory_to_postgres.py

## Símbolos

- [[assistant_scripts_migrate_memory_to_postgres]] — code: migrate_memory_to_postgres.py
- [[assistant_scripts_migrate_memory_to_postgres_parse_memoria_file]] — code: parse_memoria_file()
- [[assistant_scripts_migrate_memory_to_postgres_migrate]] — code: migrate()
- [[assistant_scripts_migrate_memory_to_postgres_rationale_20]] — code: Parse memoria.md e extrai conversas.

## Dependências

- [[assistant_scripts_migrate_memory_to_postgres_migrate]] → `calls` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository]]
- [[assistant_scripts_migrate_memory_to_postgres]] → `contains` → [[assistant_scripts_migrate_memory_to_postgres_migrate]]
- [[assistant_scripts_migrate_memory_to_postgres]] → `contains` → [[assistant_scripts_migrate_memory_to_postgres_parse_memoria_file]]
- [[assistant_scripts_migrate_memory_to_postgres_migrate]] → `calls` → [[assistant_scripts_migrate_memory_to_postgres_parse_memoria_file]]
- [[assistant_scripts_migrate_memory_to_postgres_parse_memoria_file]] → `references` → [[assistant_scripts_migrate_memory_to_postgres_py_path]]
- [[assistant_scripts_migrate_memory_to_postgres_rationale_20]] → `rationale_for` → [[assistant_scripts_migrate_memory_to_postgres_parse_memoria_file]]
- [[assistant_scripts_migrate_memory_to_postgres_migrate]] → `calls` → [[assistant_scripts_migrate_memory_to_postgres_py_path]]