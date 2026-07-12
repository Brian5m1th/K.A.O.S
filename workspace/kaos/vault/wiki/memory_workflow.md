# assistant\app\router\memory_workflow.py

## Símbolos

- [[assistant_app_router_memory_workflow]] — code: memory_workflow.py
- [[assistant_app_router_memory_workflow_memoryworkflow]] — code: MemoryWorkflow
- [[assistant_app_router_memory_workflow_memoryworkflow_init]] — code: .__init__()
- [[assistant_app_router_memory_workflow_memoryworkflow_execute]] — code: .execute()
- [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]] — code: ._save_conversation()

## Dependências

- [[assistant_app_router_memory_workflow_memoryworkflow]] → `uses` → [[assistant_app_domain_command_commandtype]]
- [[assistant_app_router_memory_workflow_memoryworkflow_execute]] → `references` → [[assistant_app_domain_command_commandtype]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `uses` → [[assistant_app_domain_context_requestcontext]]
- [[assistant_app_router_memory_workflow_memoryworkflow_execute]] → `references` → [[assistant_app_domain_context_requestcontext]]
- [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]] → `references` → [[assistant_app_domain_context_requestcontext]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `uses` → [[assistant_app_domain_memory_conversationsnapshot]]
- [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]] → `calls` → [[assistant_app_domain_memory_conversationsnapshot]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `uses` → [[assistant_app_memory_storage_postgres_storage_postgresstorage]]
- [[assistant_app_router_memory_workflow_memoryworkflow_init]] → `calls` → [[assistant_app_memory_storage_postgres_storage_postgresstorage]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `uses` → [[assistant_app_memory_storage_workspace_storage_workspacestorage]]
- [[assistant_app_router_memory_workflow_memoryworkflow_init]] → `calls` → [[assistant_app_memory_storage_workspace_storage_workspacestorage]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `uses` → [[assistant_app_memory_summarizer_conversationsummarizer]]
- [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]] → `calls` → [[assistant_app_memory_summarizer_conversationsummarizer_generate]]
- [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]] → `calls` → [[assistant_app_memory_summarizer_conversationsummarizer_generate_title]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_router_memory_workflow]] → `contains` → [[assistant_app_router_memory_workflow_memoryworkflow]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `method` → [[assistant_app_router_memory_workflow_memoryworkflow_execute]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `method` → [[assistant_app_router_memory_workflow_memoryworkflow_init]]
- [[assistant_app_router_memory_workflow_memoryworkflow]] → `method` → [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]]
- [[assistant_app_router_memory_workflow_memoryworkflow_execute]] → `calls` → [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]]
- [[assistant_app_router_memory_workflow_memoryworkflow_save_conversation]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]