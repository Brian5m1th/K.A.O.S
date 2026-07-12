# assistant\app\models\conversation.py

## Símbolos

- [[assistant_app_models_conversation]] — code: conversation.py
- [[assistant_app_models_conversation_conversation]] — code: Conversation
- [[assistant_app_models_conversation_rationale_1]] — code: Conversation SQLAlchemy model.  Persists individual chat turns (user + assista

## Dependências

- [[assistant_app_models_conversation]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_models_conversation_conversation]] → `uses` → [[assistant_app_database_base]]
- [[assistant_app_models_conversation]] → `contains` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_models_conversation_rationale_1]] → `rationale_for` → [[assistant_app_models_conversation]]
- [[assistant_app_models_conversation_conversation]] → `inherits` → [[assistant_app_models_conversation_py_base]]