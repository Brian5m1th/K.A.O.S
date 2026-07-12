# assistant\app\providers\embedding\openai.py

## Símbolos

- [[assistant_app_providers_embedding_openai]] — code: openai.py
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider]] — code: OpenAIEmbeddingProvider
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider_init]] — code: .__init__()
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider_embed]] — code: .embed()
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider_embed_batch]] — code: .embed_batch()
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_embedding_openai_openaiembeddingprovider]] → `uses` → [[assistant_app_providers_base_embedding_baseembeddingprovider]]
- [[assistant_app_providers_embedding_openai]] → `contains` → [[assistant_app_providers_embedding_openai_openaiembeddingprovider]]
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider]] → `method` → [[assistant_app_providers_embedding_openai_openaiembeddingprovider_embed]]
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider]] → `method` → [[assistant_app_providers_embedding_openai_openaiembeddingprovider_embed_batch]]
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider]] → `method` → [[assistant_app_providers_embedding_openai_openaiembeddingprovider_healthcheck]]
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider]] → `method` → [[assistant_app_providers_embedding_openai_openaiembeddingprovider_init]]
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider_embed]] → `calls` → [[assistant_app_providers_embedding_openai_openaiembeddingprovider_embed_batch]]
- [[assistant_app_providers_embedding_openai_openaiembeddingprovider_healthcheck]] → `calls` → [[assistant_app_providers_embedding_openai_openaiembeddingprovider_embed]]