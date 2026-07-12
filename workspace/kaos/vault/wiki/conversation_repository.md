# assistant\app\repositories\conversation_repository.py

## Símbolos

- [[assistant_app_repositories_conversation_repository]] — code: conversation_repository.py
- [[assistant_app_repositories_conversation_repository_conversationturn]] — code: ConversationTurn
- [[assistant_app_repositories_conversation_repository_conversationturn_to_orm]] — code: .to_orm()
- [[assistant_app_repositories_conversation_repository_sessionsummary]] — code: SessionSummary
- [[assistant_app_repositories_conversation_repository_conversationrepository]] — code: ConversationRepository
- [[assistant_app_repositories_conversation_repository_conversationrepository_init]] — code: .__init__()
- [[assistant_app_repositories_conversation_repository_conversationrepository_save]] — code: .save()
- [[assistant_app_repositories_conversation_repository_conversationrepository_get_by_session]] — code: .get_by_session()
- [[assistant_app_repositories_conversation_repository_conversationrepository_get_session_count]] — code: .get_session_count()
- [[assistant_app_repositories_conversation_repository_conversationrepository_list_sessions]] — code: .list_sessions()
- [[assistant_app_repositories_conversation_repository_conversationrepository_delete_session]] — code: .delete_session()
- [[assistant_app_repositories_conversation_repository_rationale_1]] — code: ConversationRepository — CRUD for conversation history.  Uses SQLAlchemy async
- [[assistant_app_repositories_conversation_repository_rationale_19]] — code: Represents a single turn in a conversation (user or assistant).
- [[assistant_app_repositories_conversation_repository_rationale_45]] — code: Summarized view of a conversation session.
- [[assistant_app_repositories_conversation_repository_rationale_57]] — code: Repository for managing conversation history.
- [[assistant_app_repositories_conversation_repository_rationale_63]] — code: Persist a single turn (user or assistant) and return the ORM object.
- [[assistant_app_repositories_conversation_repository_rationale_72]] — code: Return all turns for a session, ordered by created_at ASC.
- [[assistant_app_repositories_conversation_repository_rationale_87]] — code: Return the number of turns in a session.
- [[assistant_app_repositories_conversation_repository_rationale_103]] — code: Return paginated list of sessions with summary per session.          Returns:
- [[assistant_app_repositories_conversation_repository_rationale_172]] — code: Remove all turns for a session. Returns count of deleted records.

## Dependências

- [[assistant_app_repositories_conversation_repository_conversationrepository]] → `uses` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_delete_session]] → `indirect_call` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_get_by_session]] → `references` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_get_session_count]] → `indirect_call` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_save]] → `references` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_repositories_conversation_repository_conversationturn]] → `uses` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_repositories_conversation_repository_conversationturn_to_orm]] → `references` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_repositories_conversation_repository_sessionsummary]] → `uses` → [[assistant_app_models_conversation_conversation]]
- [[assistant_app_repositories_conversation_repository]] → `contains` → [[assistant_app_repositories_conversation_repository_conversationrepository]]
- [[assistant_app_repositories_conversation_repository]] → `contains` → [[assistant_app_repositories_conversation_repository_conversationturn]]
- [[assistant_app_repositories_conversation_repository]] → `imports_from` → [[assistant_app_repositories_conversation_repository_py_uuid]]
- [[assistant_app_repositories_conversation_repository]] → `contains` → [[assistant_app_repositories_conversation_repository_sessionsummary]]
- [[assistant_app_repositories_conversation_repository_rationale_1]] → `rationale_for` → [[assistant_app_repositories_conversation_repository]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_save]] → `references` → [[assistant_app_repositories_conversation_repository_conversationturn]]
- [[assistant_app_repositories_conversation_repository_conversationturn]] → `method` → [[assistant_app_repositories_conversation_repository_conversationturn_to_orm]]
- [[assistant_app_repositories_conversation_repository_rationale_19]] → `rationale_for` → [[assistant_app_repositories_conversation_repository_conversationturn]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_save]] → `calls` → [[assistant_app_repositories_conversation_repository_conversationturn_to_orm]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_list_sessions]] → `references` → [[assistant_app_repositories_conversation_repository_sessionsummary]]
- [[assistant_app_repositories_conversation_repository_rationale_45]] → `rationale_for` → [[assistant_app_repositories_conversation_repository_sessionsummary]]
- [[assistant_app_repositories_conversation_repository_conversationrepository]] → `method` → [[assistant_app_repositories_conversation_repository_conversationrepository_delete_session]]
- [[assistant_app_repositories_conversation_repository_conversationrepository]] → `method` → [[assistant_app_repositories_conversation_repository_conversationrepository_get_by_session]]
- [[assistant_app_repositories_conversation_repository_conversationrepository]] → `method` → [[assistant_app_repositories_conversation_repository_conversationrepository_get_session_count]]
- [[assistant_app_repositories_conversation_repository_conversationrepository]] → `method` → [[assistant_app_repositories_conversation_repository_conversationrepository_init]]
- [[assistant_app_repositories_conversation_repository_conversationrepository]] → `method` → [[assistant_app_repositories_conversation_repository_conversationrepository_list_sessions]]
- [[assistant_app_repositories_conversation_repository_conversationrepository]] → `method` → [[assistant_app_repositories_conversation_repository_conversationrepository_save]]
- [[assistant_app_repositories_conversation_repository_rationale_57]] → `rationale_for` → [[assistant_app_repositories_conversation_repository_conversationrepository]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_init]] → `references` → [[assistant_app_repositories_conversation_repository_py_asyncsession]]
- [[assistant_app_repositories_conversation_repository_rationale_63]] → `rationale_for` → [[assistant_app_repositories_conversation_repository_conversationrepository_save]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_get_by_session]] → `references` → [[assistant_app_repositories_conversation_repository_py_uuid]]
- [[assistant_app_repositories_conversation_repository_rationale_72]] → `rationale_for` → [[assistant_app_repositories_conversation_repository_conversationrepository_get_by_session]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_delete_session]] → `references` → [[assistant_app_repositories_conversation_repository_py_uuid]]
- [[assistant_app_repositories_conversation_repository_conversationrepository_get_session_count]] → `references` → [[assistant_app_repositories_conversation_repository_py_uuid]]
- [[assistant_app_repositories_conversation_repository_rationale_87]] → `rationale_for` → [[assistant_app_repositories_conversation_repository_conversationrepository_get_session_count]]
- [[assistant_app_repositories_conversation_repository_rationale_103]] → `rationale_for` → [[assistant_app_repositories_conversation_repository_conversationrepository_list_sessions]]
- [[assistant_app_repositories_conversation_repository_rationale_172]] → `rationale_for` → [[assistant_app_repositories_conversation_repository_conversationrepository_delete_session]]