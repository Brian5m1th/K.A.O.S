# assistant\app\core\knowledge_graph_watcher.py

## Símbolos

- [[assistant_app_core_knowledge_graph_watcher]] — code: knowledge_graph_watcher.py
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] — code: KnowledgeGraphEventHandler
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_init]] — code: .__init__()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_is_relevant]] — code: ._is_relevant()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_trigger_debounce]] — code: ._trigger_debounce()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_process_dirty_files]] — code: ._process_dirty_files()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_modified]] — code: .on_modified()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_created]] — code: .on_created()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_deleted]] — code: .on_deleted()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_moved]] — code: .on_moved()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher]] — code: KnowledgeGraphWatcher
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_init]] — code: .__init__()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_start]] — code: .start()
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_stop]] — code: .stop()
- [[assistant_app_core_knowledge_graph_watcher_rationale_1]] — code: Knowledge Graph Watcher — monitors workspace files (docs, backend app, desktop s

## Dependências

- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `uses` → [[assistant_app_ai_vault_analyzer_knowledge_graph_knowledgegraphbuilder]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher]] → `uses` → [[assistant_app_ai_vault_analyzer_knowledge_graph_knowledgegraphbuilder]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_process_dirty_files]] → `calls` → [[assistant_app_ai_vault_analyzer_knowledge_graph_knowledgegraphbuilder_update_file]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_process_dirty_files]] → `calls` → [[assistant_app_ai_vault_analyzer_knowledge_graph_knowledgegraphbuilder_delete_file]]
- [[assistant_app_core_knowledge_graph_watcher]] → `contains` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]]
- [[assistant_app_core_knowledge_graph_watcher]] → `contains` → [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher]]
- [[assistant_app_core_knowledge_graph_watcher_rationale_1]] → `rationale_for` → [[assistant_app_core_knowledge_graph_watcher]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_init]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_is_relevant]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_created]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_deleted]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_modified]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_moved]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_process_dirty_files]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_trigger_debounce]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `inherits` → [[assistant_app_core_knowledge_graph_watcher_py_filesystemeventhandler]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]] → `uses` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_start]] → `calls` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_init]] → `calls` → [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_init]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_trigger_debounce]] → `calls` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_is_relevant]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_created]] → `calls` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_trigger_debounce]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_deleted]] → `calls` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_trigger_debounce]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_modified]] → `calls` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_trigger_debounce]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_on_moved]] → `calls` → [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_trigger_debounce]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegrapheventhandler_trigger_debounce]] → `calls` → [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_start]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_init]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_start]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher]] → `method` → [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_stop]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher]] → `uses` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver]]
- [[assistant_app_core_knowledge_graph_watcher_knowledgegraphwatcher_start]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_project_root]]