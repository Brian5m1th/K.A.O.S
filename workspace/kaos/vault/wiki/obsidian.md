# assistant\app\providers\memory\obsidian.py

## Símbolos

- [[assistant_app_providers_memory_obsidian]] — code: obsidian.py
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] — code: ObsidianMemoryProvider
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_init]] — code: .__init__()
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_save]] — code: .save()
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_load]] — code: .load()
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_clear]] — code: .clear()
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] → `uses` → [[assistant_app_core_services_memory_service_memoryservice]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] → `inherits` → [[assistant_app_providers_base_memory_basememoryprovider]]
- [[assistant_app_providers_memory_obsidian]] → `contains` → [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] → `method` → [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_clear]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] → `method` → [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_healthcheck]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] → `method` → [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_init]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] → `method` → [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_load]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider]] → `method` → [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_save]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_save]] → `references` → [[assistant_app_providers_memory_obsidian_py_message]]
- [[assistant_app_providers_memory_obsidian_obsidianmemoryprovider_load]] → `references` → [[assistant_app_providers_memory_obsidian_py_message]]