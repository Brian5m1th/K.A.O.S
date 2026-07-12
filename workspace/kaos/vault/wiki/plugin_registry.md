# assistant\app\core\plugin_registry.py

## Símbolos

- [[assistant_app_core_plugin_registry]] — code: plugin_registry.py
- [[assistant_app_core_plugin_registry_pluginrecord]] — code: PluginRecord
- [[assistant_app_core_plugin_registry_pluginrecord_init]] — code: .__init__()
- [[assistant_app_core_plugin_registry_pluginrecord_from_manifest]] — code: .from_manifest()
- [[assistant_app_core_plugin_registry_pluginrecord_to_dict]] — code: .to_dict()
- [[assistant_app_core_plugin_registry_pluginregistry]] — code: PluginRegistry
- [[assistant_app_core_plugin_registry_pluginregistry_init]] — code: .__init__()
- [[assistant_app_core_plugin_registry_pluginregistry_init_db]] — code: ._init_db()
- [[assistant_app_core_plugin_registry_pluginregistry_install]] — code: .install()
- [[assistant_app_core_plugin_registry_pluginregistry_uninstall]] — code: .uninstall()
- [[assistant_app_core_plugin_registry_pluginregistry_list_plugins]] — code: .list_plugins()
- [[assistant_app_core_plugin_registry_pluginregistry_get_plugin]] — code: .get_plugin()
- [[assistant_app_core_plugin_registry_pluginregistry_set_enabled]] — code: .set_enabled()
- [[assistant_app_core_plugin_registry_rationale_1]] — code: Plugin Registry — Gerenciamento persistente de plugins.  Mantem registro dos p
- [[assistant_app_core_plugin_registry_rationale_27]] — code: Representacao de um plugin registrado no banco.
- [[assistant_app_core_plugin_registry_rationale_89]] — code: Gerencia o registro persistente de plugins no SQLite.      Mantem uma tabela '
- [[assistant_app_core_plugin_registry_rationale_128]] — code: Registra um plugin no banco de dados.
- [[assistant_app_core_plugin_registry_rationale_161]] — code: Remove o registro de um plugin.
- [[assistant_app_core_plugin_registry_rationale_173]] — code: Lista todos os plugins registrados.
- [[assistant_app_core_plugin_registry_rationale_183]] — code: Busca um plugin pelo ID.
- [[assistant_app_core_plugin_registry_rationale_194]] — code: Ativa/desativa um plugin.

## Dependências

- [[assistant_app_core_plugin_registry]] → `contains` → [[assistant_app_core_plugin_registry_pluginrecord]]
- [[assistant_app_core_plugin_registry]] → `contains` → [[assistant_app_core_plugin_registry_pluginregistry]]
- [[assistant_app_core_plugin_registry_rationale_1]] → `rationale_for` → [[assistant_app_core_plugin_registry]]
- [[assistant_app_core_plugin_registry_pluginrecord]] → `method` → [[assistant_app_core_plugin_registry_pluginrecord_from_manifest]]
- [[assistant_app_core_plugin_registry_pluginrecord]] → `method` → [[assistant_app_core_plugin_registry_pluginrecord_init]]
- [[assistant_app_core_plugin_registry_pluginrecord]] → `method` → [[assistant_app_core_plugin_registry_pluginrecord_to_dict]]
- [[assistant_app_core_plugin_registry_pluginrecord]] → `uses` → [[assistant_app_core_plugin_sandbox_pluginmanifest]]
- [[assistant_app_core_plugin_registry_pluginrecord]] → `uses` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver]]
- [[assistant_app_core_plugin_registry_pluginregistry_get_plugin]] → `references` → [[assistant_app_core_plugin_registry_pluginrecord]]
- [[assistant_app_core_plugin_registry_pluginregistry_install]] → `references` → [[assistant_app_core_plugin_registry_pluginrecord]]
- [[assistant_app_core_plugin_registry_pluginregistry_list_plugins]] → `references` → [[assistant_app_core_plugin_registry_pluginrecord]]
- [[assistant_app_core_plugin_registry_rationale_27]] → `rationale_for` → [[assistant_app_core_plugin_registry_pluginrecord]]
- [[assistant_app_core_plugin_registry_pluginrecord_from_manifest]] → `references` → [[assistant_app_core_plugin_sandbox_pluginmanifest]]
- [[assistant_app_core_plugin_registry_pluginrecord_to_dict]] → `references` → [[assistant_app_core_plugin_registry_py_any]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `method` → [[assistant_app_core_plugin_registry_pluginregistry_get_plugin]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `method` → [[assistant_app_core_plugin_registry_pluginregistry_init]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `method` → [[assistant_app_core_plugin_registry_pluginregistry_init_db]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `method` → [[assistant_app_core_plugin_registry_pluginregistry_install]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `method` → [[assistant_app_core_plugin_registry_pluginregistry_list_plugins]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `method` → [[assistant_app_core_plugin_registry_pluginregistry_set_enabled]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `method` → [[assistant_app_core_plugin_registry_pluginregistry_uninstall]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `uses` → [[assistant_app_core_plugin_sandbox_pluginmanifest]]
- [[assistant_app_core_plugin_registry_pluginregistry]] → `uses` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver]]
- [[assistant_app_core_plugin_registry_rationale_89]] → `rationale_for` → [[assistant_app_core_plugin_registry_pluginregistry]]
- [[assistant_app_core_plugin_registry_pluginregistry_init]] → `calls` → [[assistant_app_core_plugin_registry_pluginregistry_init_db]]
- [[assistant_app_core_plugin_registry_pluginregistry_init]] → `references` → [[assistant_app_core_plugin_registry_py_path]]
- [[assistant_app_core_plugin_registry_pluginregistry_init]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_get_data_path]]
- [[assistant_app_core_plugin_registry_rationale_128]] → `rationale_for` → [[assistant_app_core_plugin_registry_pluginregistry_install]]
- [[assistant_app_core_plugin_registry_rationale_161]] → `rationale_for` → [[assistant_app_core_plugin_registry_pluginregistry_uninstall]]
- [[assistant_app_core_plugin_registry_rationale_173]] → `rationale_for` → [[assistant_app_core_plugin_registry_pluginregistry_list_plugins]]
- [[assistant_app_core_plugin_registry_rationale_183]] → `rationale_for` → [[assistant_app_core_plugin_registry_pluginregistry_get_plugin]]
- [[assistant_app_core_plugin_registry_rationale_194]] → `rationale_for` → [[assistant_app_core_plugin_registry_pluginregistry_set_enabled]]