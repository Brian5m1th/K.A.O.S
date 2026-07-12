# assistant\app\runtime\runtime_selector.py

## Símbolos

- [[assistant_app_runtime_runtime_selector]] — code: runtime_selector.py
- [[assistant_app_runtime_runtime_selector_runtimeselector]] — code: RuntimeSelector
- [[assistant_app_runtime_runtime_selector_runtimeselector_init]] — code: .__init__()
- [[assistant_app_runtime_runtime_selector_runtimeselector_init_runtimes]] — code: ._init_runtimes()
- [[assistant_app_runtime_runtime_selector_runtimeselector_select]] — code: .select()
- [[assistant_app_runtime_runtime_selector_rationale_85]] — code: Seleciona o melhor runtime com base em objetivos do usuário.

## Dependências

- [[assistant_app_runtime_runtime_selector_runtimeselector]] → `uses` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_runtime_runtime_selector_runtimeselector_init]] → `calls` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_runtime_runtime_selector_runtimeselector]] → `uses` → [[assistant_app_runtime_runtime_layer_airuntime]]
- [[assistant_app_runtime_runtime_selector_runtimeselector_select]] → `references` → [[assistant_app_runtime_runtime_layer_airuntime]]
- [[assistant_app_runtime_runtime_selector_runtimeselector]] → `uses` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter]]
- [[assistant_app_runtime_runtime_selector_runtimeselector_init_runtimes]] → `calls` → [[assistant_app_runtime_runtime_layer_providerruntimeadapter]]
- [[assistant_app_runtime_runtime_selector]] → `contains` → [[assistant_app_runtime_runtime_selector_runtimeselector]]
- [[assistant_app_runtime_runtime_selector_runtimeselector]] → `method` → [[assistant_app_runtime_runtime_selector_runtimeselector_init]]
- [[assistant_app_runtime_runtime_selector_runtimeselector]] → `method` → [[assistant_app_runtime_runtime_selector_runtimeselector_init_runtimes]]
- [[assistant_app_runtime_runtime_selector_runtimeselector]] → `method` → [[assistant_app_runtime_runtime_selector_runtimeselector_select]]
- [[assistant_app_runtime_runtime_selector_runtimeselector_init]] → `calls` → [[assistant_app_runtime_runtime_selector_runtimeselector_init_runtimes]]
- [[assistant_app_runtime_runtime_selector_rationale_85]] → `rationale_for` → [[assistant_app_runtime_runtime_selector_runtimeselector_select]]