# assistant\app\api\plugins.py

## Símbolos

- [[assistant_app_api_plugins]] — code: plugins.py
- [[assistant_app_api_plugins_get_sandbox]] — code: _get_sandbox()
- [[assistant_app_api_plugins_get_registry]] — code: _get_registry()
- [[assistant_app_api_plugins_list_plugins]] — code: list_plugins()
- [[assistant_app_api_plugins_install_plugin]] — code: install_plugin()
- [[assistant_app_api_plugins_execute_plugin]] — code: execute_plugin()
- [[assistant_app_api_plugins_uninstall_plugin]] — code: uninstall_plugin()
- [[assistant_app_api_plugins_get_plugin]] — code: get_plugin()
- [[assistant_app_api_plugins_rationale_1]] — code: API Router — Gerenciamento de Plugins Wasm.  Permite instalar, listar, executa
- [[assistant_app_api_plugins_rationale_51]] — code: Lista todos os plugins instalados (do registro + sandbox).
- [[assistant_app_api_plugins_rationale_71]] — code: Instala um plugin a partir de arquivo .wasm + manifesto JSON.      O manifesto
- [[assistant_app_api_plugins_rationale_137]] — code: Executa uma funcao em um plugin carregado.
- [[assistant_app_api_plugins_rationale_153]] — code: Remove um plugin do sandbox e do registro.
- [[assistant_app_api_plugins_rationale_175]] — code: Obtem detalhes de um plugin.

## Dependências

- [[assistant_app_api_plugins]] → `contains` → [[assistant_app_api_plugins_execute_plugin]]
- [[assistant_app_api_plugins]] → `contains` → [[assistant_app_api_plugins_get_plugin]]
- [[assistant_app_api_plugins]] → `contains` → [[assistant_app_api_plugins_get_registry]]
- [[assistant_app_api_plugins]] → `contains` → [[assistant_app_api_plugins_get_sandbox]]
- [[assistant_app_api_plugins]] → `contains` → [[assistant_app_api_plugins_install_plugin]]
- [[assistant_app_api_plugins]] → `contains` → [[assistant_app_api_plugins_list_plugins]]
- [[assistant_app_api_plugins]] → `contains` → [[assistant_app_api_plugins_uninstall_plugin]]
- [[assistant_app_api_plugins]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_plugins_rationale_1]] → `rationale_for` → [[assistant_app_api_plugins]]
- [[assistant_app_api_plugins_execute_plugin]] → `calls` → [[assistant_app_api_plugins_get_sandbox]]
- [[assistant_app_api_plugins_get_plugin]] → `calls` → [[assistant_app_api_plugins_get_sandbox]]
- [[assistant_app_api_plugins_get_sandbox]] → `references` → [[assistant_app_core_plugin_sandbox_pluginsandbox]]
- [[assistant_app_api_plugins_install_plugin]] → `calls` → [[assistant_app_api_plugins_get_sandbox]]
- [[assistant_app_api_plugins_list_plugins]] → `calls` → [[assistant_app_api_plugins_get_sandbox]]
- [[assistant_app_api_plugins_uninstall_plugin]] → `calls` → [[assistant_app_api_plugins_get_sandbox]]
- [[assistant_app_api_plugins_get_plugin]] → `calls` → [[assistant_app_api_plugins_get_registry]]
- [[assistant_app_api_plugins_get_registry]] → `references` → [[assistant_app_core_plugin_registry_pluginregistry]]
- [[assistant_app_api_plugins_install_plugin]] → `calls` → [[assistant_app_api_plugins_get_registry]]
- [[assistant_app_api_plugins_list_plugins]] → `calls` → [[assistant_app_api_plugins_get_registry]]
- [[assistant_app_api_plugins_uninstall_plugin]] → `calls` → [[assistant_app_api_plugins_get_registry]]
- [[assistant_app_api_plugins_list_plugins]] → `references` → [[assistant_app_api_plugins_py_any]]
- [[assistant_app_api_plugins_rationale_51]] → `rationale_for` → [[assistant_app_api_plugins_list_plugins]]
- [[assistant_app_api_plugins_execute_plugin]] → `references` → [[assistant_app_api_plugins_py_any]]
- [[assistant_app_api_plugins_get_plugin]] → `references` → [[assistant_app_api_plugins_py_any]]
- [[assistant_app_api_plugins_install_plugin]] → `references` → [[assistant_app_api_plugins_py_any]]
- [[assistant_app_api_plugins_install_plugin]] → `calls` → [[assistant_app_core_plugin_sandbox_pluginmanifest_from_dict]]
- [[assistant_app_api_plugins_install_plugin]] → `calls` → [[assistant_app_core_plugin_sandbox_validate_wasm_bytes]]
- [[assistant_app_api_plugins_install_plugin]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_api_plugins_install_plugin]] → `references` → [[uploadfile]]
- [[assistant_app_api_plugins_rationale_71]] → `rationale_for` → [[assistant_app_api_plugins_install_plugin]]
- [[assistant_app_api_plugins_rationale_137]] → `rationale_for` → [[assistant_app_api_plugins_execute_plugin]]
- [[assistant_app_api_plugins_rationale_153]] → `rationale_for` → [[assistant_app_api_plugins_uninstall_plugin]]
- [[assistant_app_api_plugins_rationale_175]] → `rationale_for` → [[assistant_app_api_plugins_get_plugin]]