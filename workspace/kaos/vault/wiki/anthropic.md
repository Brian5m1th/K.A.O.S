# assistant\app\providers\chat\anthropic.py

## Símbolos

- [[assistant_app_providers_chat_anthropic]] — code: anthropic.py
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider]] — code: AnthropicChatProvider
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider_init]] — code: .__init__()
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider_chat]] — code: .chat()
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider_stream]] — code: .stream()
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider_models]] — code: .models()
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_chat_anthropic_anthropicchatprovider]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider]] → `inherits` → [[assistant_app_providers_base_chat_basechatprovider]]
- [[assistant_app_providers_chat_anthropic]] → `contains` → [[assistant_app_providers_chat_anthropic_anthropicchatprovider]]
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider]] → `method` → [[assistant_app_providers_chat_anthropic_anthropicchatprovider_chat]]
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider]] → `method` → [[assistant_app_providers_chat_anthropic_anthropicchatprovider_healthcheck]]
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider]] → `method` → [[assistant_app_providers_chat_anthropic_anthropicchatprovider_init]]
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider]] → `method` → [[assistant_app_providers_chat_anthropic_anthropicchatprovider_models]]
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider]] → `method` → [[assistant_app_providers_chat_anthropic_anthropicchatprovider_stream]]
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider_chat]] → `references` → [[assistant_app_providers_chat_anthropic_py_message]]
- [[assistant_app_providers_chat_anthropic_anthropicchatprovider_stream]] → `references` → [[assistant_app_providers_chat_anthropic_py_message]]