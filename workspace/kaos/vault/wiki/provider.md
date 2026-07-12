# assistant\app\llm\provider.py

## Símbolos

- [[assistant_app_llm_provider]] — code: provider.py
- [[assistant_app_llm_provider_baseprovider]] — code: BaseProvider
- [[assistant_app_llm_provider_baseprovider_invoke]] — code: .invoke()
- [[assistant_app_llm_provider_baseprovider_ainvoke]] — code: .ainvoke()
- [[assistant_app_llm_provider_baseprovider_stream]] — code: .stream()
- [[assistant_app_llm_provider_baseprovider_astream]] — code: .astream()
- [[assistant_app_llm_provider_baseprovider_model_name]] — code: .model_name()
- [[assistant_app_llm_provider_baseprovider_provider_name]] — code: .provider_name()

## Dependências

- [[assistant_app_llm_provider]] → `contains` → [[assistant_app_llm_provider_baseprovider]]
- [[assistant_app_llm_provider]] → `imports_from` → [[assistant_app_llm_provider_py_abc]]
- [[assistant_app_llm_provider_baseprovider]] → `method` → [[assistant_app_llm_provider_baseprovider_ainvoke]]
- [[assistant_app_llm_provider_baseprovider]] → `method` → [[assistant_app_llm_provider_baseprovider_astream]]
- [[assistant_app_llm_provider_baseprovider]] → `method` → [[assistant_app_llm_provider_baseprovider_invoke]]
- [[assistant_app_llm_provider_baseprovider]] → `method` → [[assistant_app_llm_provider_baseprovider_model_name]]
- [[assistant_app_llm_provider_baseprovider]] → `method` → [[assistant_app_llm_provider_baseprovider_provider_name]]
- [[assistant_app_llm_provider_baseprovider]] → `method` → [[assistant_app_llm_provider_baseprovider_stream]]
- [[assistant_app_llm_provider_baseprovider]] → `inherits` → [[assistant_app_llm_provider_py_abc]]
- [[assistant_app_llm_provider_baseprovider_invoke]] → `references` → [[assistant_app_llm_provider_py_basemessage]]
- [[assistant_app_llm_provider_baseprovider_ainvoke]] → `references` → [[assistant_app_llm_provider_py_basemessage]]
- [[assistant_app_llm_provider_baseprovider_astream]] → `references` → [[assistant_app_llm_provider_py_basemessage]]
- [[assistant_app_llm_provider_baseprovider_stream]] → `references` → [[assistant_app_llm_provider_py_basemessage]]