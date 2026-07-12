# assistant\app\core\opencode_watcher.py

## Símbolos

- [[assistant_app_core_opencode_watcher]] — code: opencode_watcher.py
- [[assistant_app_core_opencode_watcher_opencodehandler]] — code: _OpenCodeHandler
- [[assistant_app_core_opencode_watcher_opencodehandler_init]] — code: .__init__()
- [[assistant_app_core_opencode_watcher_opencodehandler_debounce_invalidate]] — code: ._debounce_invalidate()
- [[assistant_app_core_opencode_watcher_opencodehandler_on_modified]] — code: .on_modified()
- [[assistant_app_core_opencode_watcher_opencodehandler_on_created]] — code: .on_created()
- [[assistant_app_core_opencode_watcher_opencodehandler_on_deleted]] — code: .on_deleted()
- [[assistant_app_core_opencode_watcher_opencodewatcher]] — code: OpenCodeWatcher
- [[assistant_app_core_opencode_watcher_opencodewatcher_init]] — code: .__init__()
- [[assistant_app_core_opencode_watcher_opencodewatcher_start]] — code: .start()
- [[assistant_app_core_opencode_watcher_opencodewatcher_stop]] — code: .stop()
- [[assistant_app_core_opencode_watcher_opencodewatcher_is_dirty]] — code: .is_dirty()
- [[assistant_app_core_opencode_watcher_opencodewatcher_mark_clean]] — code: .mark_clean()
- [[assistant_app_core_opencode_watcher_opencodewatcher_is_fallback_mode]] — code: .is_fallback_mode()
- [[assistant_app_core_opencode_watcher_opencodewatcher_invalidate_cache]] — code: ._invalidate_cache()
- [[assistant_app_core_opencode_watcher_rationale_1]] — code: OpenCode Watcher — monitors the ``.opencode/`` directory for file changes and i
- [[assistant_app_core_opencode_watcher_rationale_32]] — code: Watchdog event handler with debounce.
- [[assistant_app_core_opencode_watcher_rationale_66]] — code: Background watcher for the ``.opencode/`` directory.      Usage::          w
- [[assistant_app_core_opencode_watcher_rationale_90]] — code: Start the filesystem watcher.          Falls back gracefully to on-demand scan
- [[assistant_app_core_opencode_watcher_rationale_126]] — code: Stop the filesystem watcher.
- [[assistant_app_core_opencode_watcher_rationale_134]] — code: Return True if the cache needs refresh.
- [[assistant_app_core_opencode_watcher_rationale_138]] — code: Mark the cache as clean after a refresh.
- [[assistant_app_core_opencode_watcher_rationale_142]] — code: Return True if running in on-demand (no watchdog) mode.

## Dependências

- [[assistant_app_core_opencode_watcher]] → `contains` → [[assistant_app_core_opencode_watcher_opencodehandler]]
- [[assistant_app_core_opencode_watcher]] → `contains` → [[assistant_app_core_opencode_watcher_opencodewatcher]]
- [[assistant_app_core_opencode_watcher_rationale_1]] → `rationale_for` → [[assistant_app_core_opencode_watcher]]
- [[assistant_app_core_opencode_watcher_opencodehandler]] → `method` → [[assistant_app_core_opencode_watcher_opencodehandler_debounce_invalidate]]
- [[assistant_app_core_opencode_watcher_opencodehandler]] → `method` → [[assistant_app_core_opencode_watcher_opencodehandler_init]]
- [[assistant_app_core_opencode_watcher_opencodehandler]] → `method` → [[assistant_app_core_opencode_watcher_opencodehandler_on_created]]
- [[assistant_app_core_opencode_watcher_opencodehandler]] → `method` → [[assistant_app_core_opencode_watcher_opencodehandler_on_deleted]]
- [[assistant_app_core_opencode_watcher_opencodehandler]] → `method` → [[assistant_app_core_opencode_watcher_opencodehandler_on_modified]]
- [[assistant_app_core_opencode_watcher_opencodehandler]] → `inherits` → [[assistant_app_core_opencode_watcher_py_filesystemeventhandler]]
- [[assistant_app_core_opencode_watcher_opencodehandler]] → `uses` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver]]
- [[assistant_app_core_opencode_watcher_opencodewatcher_start]] → `calls` → [[assistant_app_core_opencode_watcher_opencodehandler]]
- [[assistant_app_core_opencode_watcher_rationale_32]] → `rationale_for` → [[assistant_app_core_opencode_watcher_opencodehandler]]
- [[assistant_app_core_opencode_watcher_opencodehandler_init]] → `calls` → [[assistant_app_core_opencode_watcher_opencodewatcher_init]]
- [[assistant_app_core_opencode_watcher_opencodehandler_debounce_invalidate]] → `calls` → [[assistant_app_core_opencode_watcher_opencodewatcher_start]]
- [[assistant_app_core_opencode_watcher_opencodehandler_on_created]] → `calls` → [[assistant_app_core_opencode_watcher_opencodehandler_debounce_invalidate]]
- [[assistant_app_core_opencode_watcher_opencodehandler_on_deleted]] → `calls` → [[assistant_app_core_opencode_watcher_opencodehandler_debounce_invalidate]]
- [[assistant_app_core_opencode_watcher_opencodehandler_on_modified]] → `calls` → [[assistant_app_core_opencode_watcher_opencodehandler_debounce_invalidate]]
- [[assistant_app_core_opencode_watcher_opencodewatcher]] → `method` → [[assistant_app_core_opencode_watcher_opencodewatcher_init]]
- [[assistant_app_core_opencode_watcher_opencodewatcher]] → `method` → [[assistant_app_core_opencode_watcher_opencodewatcher_invalidate_cache]]
- [[assistant_app_core_opencode_watcher_opencodewatcher]] → `method` → [[assistant_app_core_opencode_watcher_opencodewatcher_is_dirty]]
- [[assistant_app_core_opencode_watcher_opencodewatcher]] → `method` → [[assistant_app_core_opencode_watcher_opencodewatcher_is_fallback_mode]]
- [[assistant_app_core_opencode_watcher_opencodewatcher]] → `method` → [[assistant_app_core_opencode_watcher_opencodewatcher_mark_clean]]
- [[assistant_app_core_opencode_watcher_opencodewatcher]] → `method` → [[assistant_app_core_opencode_watcher_opencodewatcher_start]]
- [[assistant_app_core_opencode_watcher_opencodewatcher]] → `method` → [[assistant_app_core_opencode_watcher_opencodewatcher_stop]]
- [[assistant_app_core_opencode_watcher_opencodewatcher]] → `uses` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver]]
- [[assistant_app_core_opencode_watcher_rationale_66]] → `rationale_for` → [[assistant_app_core_opencode_watcher_opencodewatcher]]
- [[assistant_app_core_opencode_watcher_opencodewatcher_init]] → `references` → [[assistant_app_core_opencode_watcher_py_path]]
- [[assistant_app_core_opencode_watcher_opencodewatcher_init]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_get_opencode_path]]
- [[assistant_app_core_opencode_watcher_rationale_90]] → `rationale_for` → [[assistant_app_core_opencode_watcher_opencodewatcher_start]]
- [[assistant_app_core_opencode_watcher_rationale_126]] → `rationale_for` → [[assistant_app_core_opencode_watcher_opencodewatcher_stop]]
- [[assistant_app_core_opencode_watcher_rationale_134]] → `rationale_for` → [[assistant_app_core_opencode_watcher_opencodewatcher_is_dirty]]
- [[assistant_app_core_opencode_watcher_rationale_138]] → `rationale_for` → [[assistant_app_core_opencode_watcher_opencodewatcher_mark_clean]]
- [[assistant_app_core_opencode_watcher_rationale_142]] → `rationale_for` → [[assistant_app_core_opencode_watcher_opencodewatcher_is_fallback_mode]]