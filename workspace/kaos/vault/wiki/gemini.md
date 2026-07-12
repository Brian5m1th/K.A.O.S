# assistant\app\providers\chat\gemini.py

## Símbolos

- [[assistant_app_providers_chat_gemini]] — code: gemini.py
- [[assistant_app_providers_chat_gemini_geminichatprovider]] — code: GeminiChatProvider
- [[assistant_app_providers_chat_gemini_geminichatprovider_init]] — code: .__init__()
- [[assistant_app_providers_chat_gemini_geminichatprovider_convert_messages]] — code: ._convert_messages()
- [[assistant_app_providers_chat_gemini_geminichatprovider_chat]] — code: .chat()
- [[assistant_app_providers_chat_gemini_geminichatprovider_stream]] — code: .stream()
- [[assistant_app_providers_chat_gemini_geminichatprovider_models]] — code: .models()
- [[assistant_app_providers_chat_gemini_geminichatprovider_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_chat_gemini_geminichatprovider]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_providers_chat_gemini_geminichatprovider]] → `inherits` → [[assistant_app_providers_base_chat_basechatprovider]]
- [[assistant_app_providers_chat_gemini]] → `contains` → [[assistant_app_providers_chat_gemini_geminichatprovider]]
- [[assistant_app_providers_chat_gemini_geminichatprovider]] → `method` → [[assistant_app_providers_chat_gemini_geminichatprovider_chat]]
- [[assistant_app_providers_chat_gemini_geminichatprovider]] → `method` → [[assistant_app_providers_chat_gemini_geminichatprovider_convert_messages]]
- [[assistant_app_providers_chat_gemini_geminichatprovider]] → `method` → [[assistant_app_providers_chat_gemini_geminichatprovider_healthcheck]]
- [[assistant_app_providers_chat_gemini_geminichatprovider]] → `method` → [[assistant_app_providers_chat_gemini_geminichatprovider_init]]
- [[assistant_app_providers_chat_gemini_geminichatprovider]] → `method` → [[assistant_app_providers_chat_gemini_geminichatprovider_models]]
- [[assistant_app_providers_chat_gemini_geminichatprovider]] → `method` → [[assistant_app_providers_chat_gemini_geminichatprovider_stream]]
- [[assistant_app_providers_chat_gemini_geminichatprovider_chat]] → `calls` → [[assistant_app_providers_chat_gemini_geminichatprovider_convert_messages]]
- [[assistant_app_providers_chat_gemini_geminichatprovider_convert_messages]] → `references` → [[assistant_app_providers_chat_gemini_py_message]]
- [[assistant_app_providers_chat_gemini_geminichatprovider_stream]] → `calls` → [[assistant_app_providers_chat_gemini_geminichatprovider_convert_messages]]
- [[assistant_app_providers_chat_gemini_geminichatprovider_chat]] → `references` → [[assistant_app_providers_chat_gemini_py_message]]
- [[assistant_app_providers_chat_gemini_geminichatprovider_stream]] → `references` → [[assistant_app_providers_chat_gemini_py_message]]