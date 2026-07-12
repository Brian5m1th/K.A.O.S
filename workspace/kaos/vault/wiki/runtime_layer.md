# assistant\app\runtime\runtime_layer.py

## Símbolos

- [[assistant_app_runtime_runtime_layer]] — code: runtime_layer.py
- [[assistant_app_runtime_runtime_layer_airuntime]] — code: AIRuntime
- [[assistant_app_runtime_runtime_layer_airuntime_ainvoke]] — code: .ainvoke()
- [[assistant_app_runtime_runtime_layer_airuntime_astream]] — code: .astream()
- [[assistant_app_runtime_runtime_layer_airuntime_name]] — code: .name()
- [[assistant_app_runtime_runtime_layer_airuntime_type]] — code: .type()
- [[assistant_app_runtime_runtime_layer_airuntime_capabilities]] — code: .capabilities()
- [[assistant_app_runtime_runtime_layer_airuntime_supported_models]] — code: .supported_models()
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] — code: ProviderRuntimeAdapter
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_init]] — code: .__init__()
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_ainvoke]] — code: .ainvoke()
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_astream]] — code: .astream()
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_name]] — code: .name()
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_type]] — code: .type()
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_capabilities]] — code: .capabilities()
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_supported_models]] — code: .supported_models()

## Dependências

- [[assistant_app_runtime_runtime_layer]] → `contains` → [[assistant_app_runtime_runtime_layer_airuntime]]
- [[assistant_app_runtime_runtime_layer]] → `contains` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter]]
- [[assistant_app_runtime_runtime_layer]] → `imports_from` → [[assistant_app_runtime_runtime_layer_py_abc]]
- [[assistant_app_runtime_runtime_layer_airuntime]] → `method` → [[assistant_app_runtime_runtime_layer_airuntime_ainvoke]]
- [[assistant_app_runtime_runtime_layer_airuntime]] → `method` → [[assistant_app_runtime_runtime_layer_airuntime_astream]]
- [[assistant_app_runtime_runtime_layer_airuntime]] → `method` → [[assistant_app_runtime_runtime_layer_airuntime_capabilities]]
- [[assistant_app_runtime_runtime_layer_airuntime]] → `method` → [[assistant_app_runtime_runtime_layer_airuntime_name]]
- [[assistant_app_runtime_runtime_layer_airuntime]] → `method` → [[assistant_app_runtime_runtime_layer_airuntime_supported_models]]
- [[assistant_app_runtime_runtime_layer_airuntime]] → `method` → [[assistant_app_runtime_runtime_layer_airuntime_type]]
- [[assistant_app_runtime_runtime_layer_airuntime]] → `inherits` → [[assistant_app_runtime_runtime_layer_py_abc]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] → `inherits` → [[assistant_app_runtime_runtime_layer_airuntime]]
- [[assistant_app_runtime_runtime_layer_airuntime_ainvoke]] → `references` → [[assistant_app_runtime_runtime_layer_py_any]]
- [[assistant_app_runtime_runtime_layer_airuntime_ainvoke]] → `references` → [[assistant_app_runtime_runtime_layer_py_basemessage]]
- [[assistant_app_runtime_runtime_layer_airuntime_astream]] → `references` → [[assistant_app_runtime_runtime_layer_py_basemessage]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_ainvoke]] → `references` → [[assistant_app_runtime_runtime_layer_py_basemessage]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_astream]] → `references` → [[assistant_app_runtime_runtime_layer_py_basemessage]]
- [[assistant_app_runtime_runtime_layer_airuntime_astream]] → `references` → [[assistant_app_runtime_runtime_layer_py_any]]
- [[assistant_app_runtime_runtime_layer_airuntime_capabilities]] → `references` → [[assistant_app_runtime_runtime_layer_py_any]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_ainvoke]] → `references` → [[assistant_app_runtime_runtime_layer_py_any]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_astream]] → `references` → [[assistant_app_runtime_runtime_layer_py_any]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_capabilities]] → `references` → [[assistant_app_runtime_runtime_layer_py_any]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter_init]] → `references` → [[assistant_app_runtime_runtime_layer_py_any]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] → `method` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter_ainvoke]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] → `method` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter_astream]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] → `method` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter_capabilities]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] → `method` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter_init]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] → `method` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter_name]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] → `method` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter_supported_models]]
- [[assistant_app_runtime_runtime_layer_providerruntimeadapter]] → `method` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter_type]]