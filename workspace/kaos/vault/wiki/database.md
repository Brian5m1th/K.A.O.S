# assistant\app\database.py

## Símbolos

- [[assistant_app_database]] — code: database.py
- [[assistant_app_database_base]] — code: Base
- [[assistant_app_database_get_session_factory]] — code: _get_session_factory()
- [[assistant_app_database_get_session]] — code: get_session()
- [[assistant_app_database_create_tables]] — code: create_tables()
- [[assistant_app_database_rationale_42]] — code: Create all tables registered on Base.metadata.

## Dependências

- [[assistant_app_database]] → `contains` → [[assistant_app_database_base]]
- [[assistant_app_database]] → `contains` → [[assistant_app_database_create_tables]]
- [[assistant_app_database]] → `contains` → [[assistant_app_database_get_session]]
- [[assistant_app_database]] → `indirect_call` → [[assistant_app_database_get_session_factory]]
- [[assistant_app_database_base]] → `inherits` → [[assistant_app_database_py_declarativebase]]
- [[assistant_app_database_create_tables]] → `calls` → [[assistant_app_database_get_session_factory]]
- [[assistant_app_database_get_session]] → `calls` → [[assistant_app_database_get_session_factory]]
- [[assistant_app_database_get_session_factory]] → `references` → [[assistant_app_database_py_asyncsession]]
- [[assistant_app_database_get_session_factory]] → `references` → [[async_sessionmaker]]
- [[assistant_app_database_get_session]] → `references` → [[assistant_app_database_py_asyncsession]]
- [[assistant_app_database_rationale_42]] → `rationale_for` → [[assistant_app_database_create_tables]]