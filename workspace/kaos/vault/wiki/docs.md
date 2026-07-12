# assistant\app\api\docs.py

## Símbolos

- [[assistant_app_api_docs]] — code: docs.py
- [[assistant_app_api_docs_generatedocrequest]] — code: GenerateDocRequest
- [[assistant_app_api_docs_generatedocresponse]] — code: GenerateDocResponse
- [[assistant_app_api_docs_slugify]] — code: _slugify()
- [[assistant_app_api_docs_build_history_text]] — code: _build_history_text()
- [[assistant_app_api_docs_resolve_doc_path]] — code: _resolve_doc_path()
- [[assistant_app_api_docs_generate_and_save]] — code: _generate_and_save()
- [[assistant_app_api_docs_generate_doc]] — code: generate_doc()
- [[assistant_app_api_docs_list_docs]] — code: list_docs()
- [[assistant_app_api_docs_rationale_1]] — code: Docs API — Auto-documentation generation from conversation history.  SDD-DOCS-
- [[assistant_app_api_docs_rationale_71]] — code: Convert a title to a filesystem-safe slug.
- [[assistant_app_api_docs_rationale_87]] — code: Return the absolute path where the doc will be written.
- [[assistant_app_api_docs_rationale_98]] — code: Run LLM generation and persist the Markdown file (background task).
- [[assistant_app_api_docs_rationale_154]] — code: SDD-DOCS-001: Generate a Markdown document from a conversation session.
- [[assistant_app_api_docs_rationale_211]] — code: List all generated documents under docs/.

## Dependências

- [[assistant_app_api_docs]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_docs]] → `contains` → [[assistant_app_api_docs_build_history_text]]
- [[assistant_app_api_docs]] → `contains` → [[assistant_app_api_docs_generate_and_save]]
- [[assistant_app_api_docs]] → `contains` → [[assistant_app_api_docs_generate_doc]]
- [[assistant_app_api_docs]] → `contains` → [[assistant_app_api_docs_generatedocrequest]]
- [[assistant_app_api_docs]] → `contains` → [[assistant_app_api_docs_generatedocresponse]]
- [[assistant_app_api_docs]] → `contains` → [[assistant_app_api_docs_list_docs]]
- [[assistant_app_api_docs]] → `contains` → [[assistant_app_api_docs_resolve_doc_path]]
- [[assistant_app_api_docs]] → `contains` → [[assistant_app_api_docs_slugify]]
- [[assistant_app_api_docs]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_docs_rationale_1]] → `rationale_for` → [[assistant_app_api_docs]]
- [[assistant_app_api_docs_generate_doc]] → `references` → [[assistant_app_api_docs_generatedocrequest]]
- [[assistant_app_api_docs_generatedocrequest]] → `inherits` → [[assistant_app_api_docs_py_basemodel]]
- [[assistant_app_api_docs_generatedocrequest]] → `uses` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_api_docs_generatedocrequest]] → `uses` → [[assistant_app_repositories_conversation_repository_conversationrepository]]
- [[assistant_app_api_docs_generatedocresponse]] → `inherits` → [[assistant_app_api_docs_py_basemodel]]
- [[assistant_app_api_docs_generate_doc]] → `calls` → [[assistant_app_api_docs_generatedocresponse]]
- [[assistant_app_api_docs_generatedocresponse]] → `uses` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_api_docs_generatedocresponse]] → `uses` → [[assistant_app_repositories_conversation_repository_conversationrepository]]
- [[assistant_app_api_docs_generate_doc]] → `calls` → [[assistant_app_api_docs_slugify]]
- [[assistant_app_api_docs_rationale_71]] → `rationale_for` → [[assistant_app_api_docs_slugify]]
- [[assistant_app_api_docs_generate_and_save]] → `calls` → [[assistant_app_api_docs_build_history_text]]
- [[assistant_app_api_docs_generate_doc]] → `calls` → [[assistant_app_api_docs_resolve_doc_path]]
- [[assistant_app_api_docs_rationale_87]] → `rationale_for` → [[assistant_app_api_docs_resolve_doc_path]]
- [[assistant_app_api_docs_resolve_doc_path]] → `references` → [[assistant_app_api_docs_py_path]]
- [[assistant_app_api_docs_generate_and_save]] → `references` → [[assistant_app_api_docs_py_path]]
- [[assistant_app_api_docs_generate_and_save]] → `calls` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_api_docs_generate_doc]] → `indirect_call` → [[assistant_app_api_docs_generate_and_save]]
- [[assistant_app_api_docs_rationale_98]] → `rationale_for` → [[assistant_app_api_docs_generate_and_save]]
- [[assistant_app_api_docs_generate_doc]] → `references` → [[assistant_app_api_docs_py_asyncsession]]
- [[assistant_app_api_docs_generate_doc]] → `references` → [[assistant_app_api_docs_py_backgroundtasks]]
- [[assistant_app_api_docs_generate_doc]] → `calls` → [[assistant_app_repositories_conversation_repository_conversationrepository]]
- [[assistant_app_api_docs_rationale_154]] → `rationale_for` → [[assistant_app_api_docs_generate_doc]]
- [[assistant_app_api_docs_rationale_211]] → `rationale_for` → [[assistant_app_api_docs_list_docs]]