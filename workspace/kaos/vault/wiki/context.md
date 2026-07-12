# assistant\app\domain\context.py

## Símbolos

- [[assistant_app_domain_context]] — code: context.py
- [[assistant_app_domain_context_requestcontext]] — code: RequestContext

## Dependências

- [[assistant_app_domain_context_requestcontext]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_domain_context]] → `contains` → [[assistant_app_domain_context_requestcontext]]
- [[assistant_app_domain_context_requestcontext]] → `uses` → [[assistant_app_domain_identity_useridentity]]
- [[assistant_app_domain_context_requestcontext]] → `uses` → [[assistant_app_domain_identity_workspaceidentity]]