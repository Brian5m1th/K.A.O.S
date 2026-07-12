# assistant\app\memory\summarizer.py

## Símbolos

- [[assistant_app_memory_summarizer]] — code: summarizer.py
- [[assistant_app_memory_summarizer_conversationsummarizer]] — code: ConversationSummarizer
- [[assistant_app_memory_summarizer_conversationsummarizer_generate]] — code: .generate()
- [[assistant_app_memory_summarizer_conversationsummarizer_generate_title]] — code: .generate_title()

## Dependências

- [[assistant_app_memory_summarizer_conversationsummarizer]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_memory_summarizer]] → `contains` → [[assistant_app_memory_summarizer_conversationsummarizer]]
- [[assistant_app_memory_summarizer_conversationsummarizer]] → `method` → [[assistant_app_memory_summarizer_conversationsummarizer_generate]]
- [[assistant_app_memory_summarizer_conversationsummarizer]] → `method` → [[assistant_app_memory_summarizer_conversationsummarizer_generate_title]]
- [[assistant_app_memory_summarizer_conversationsummarizer_generate]] → `references` → [[assistant_app_memory_summarizer_py_message]]
- [[assistant_app_memory_summarizer_conversationsummarizer_generate_title]] → `references` → [[assistant_app_memory_summarizer_py_message]]