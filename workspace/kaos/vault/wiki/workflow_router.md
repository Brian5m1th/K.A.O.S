# assistant\app\router\workflow_router.py

## Símbolos

- [[assistant_app_router_workflow_router]] — code: workflow_router.py
- [[assistant_app_router_workflow_router_workflowrouter]] — code: WorkflowRouter
- [[assistant_app_router_workflow_router_workflowrouter_resolve]] — code: .resolve()

## Dependências

- [[assistant_app_router_workflow_router_workflowrouter]] → `uses` → [[assistant_app_domain_context_requestcontext]]
- [[assistant_app_router_workflow_router_workflowrouter_resolve]] → `references` → [[assistant_app_domain_context_requestcontext]]
- [[assistant_app_router_workflow_router_workflowrouter]] → `uses` → [[assistant_app_domain_intent_intentresult]]
- [[assistant_app_router_workflow_router_workflowrouter_resolve]] → `references` → [[assistant_app_domain_intent_intentresult]]
- [[assistant_app_router_workflow_router_workflowrouter]] → `uses` → [[assistant_app_domain_workflow_workflowtype]]
- [[assistant_app_router_workflow_router_workflowrouter_resolve]] → `references` → [[assistant_app_domain_workflow_workflowtype]]
- [[assistant_app_router_workflow_router]] → `contains` → [[assistant_app_router_workflow_router_workflowrouter]]
- [[assistant_app_router_workflow_router_workflowrouter]] → `method` → [[assistant_app_router_workflow_router_workflowrouter_resolve]]