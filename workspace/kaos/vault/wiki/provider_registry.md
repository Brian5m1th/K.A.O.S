# assistant\app\core\provider_registry.py

## Símbolos

- [[assistant_app_core_provider_registry]] — code: provider_registry.py
- [[assistant_app_core_provider_registry_provider]] — code: Provider
- [[assistant_app_core_provider_registry_provider_name]] — code: .name()
- [[assistant_app_core_provider_registry_provider_version]] — code: .version()
- [[assistant_app_core_provider_registry_provider_health_check]] — code: .health_check()
- [[assistant_app_core_provider_registry_providerregistry]] — code: ProviderRegistry
- [[assistant_app_core_provider_registry_providerregistry_init]] — code: .__init__()
- [[assistant_app_core_provider_registry_providerregistry_register]] — code: .register()
- [[assistant_app_core_provider_registry_providerregistry_activate]] — code: .activate()
- [[assistant_app_core_provider_registry_providerregistry_remove]] — code: .remove()
- [[assistant_app_core_provider_registry_providerregistry_deactivate]] — code: .deactivate()
- [[assistant_app_core_provider_registry_providerregistry_active]] — code: .active()
- [[assistant_app_core_provider_registry_providerregistry_active_key]] — code: .active_key()
- [[assistant_app_core_provider_registry_providerregistry_providers]] — code: .providers()
- [[assistant_app_core_provider_registry_providerregistry_list_providers]] — code: .list_providers()
- [[assistant_app_core_provider_registry_providerregistry_contains]] — code: .__contains__()
- [[assistant_app_core_provider_registry_providerregistry_repr]] — code: .__repr__()
- [[assistant_app_core_provider_registry_rationale_1]] — code: Provider Registry — Generic dependency injection container for K.A.O.S.  Enables
- [[assistant_app_core_provider_registry_rationale_27]] — code: Base class for all K.A.O.S provider implementations.
- [[assistant_app_core_provider_registry_rationale_39]] — code: Optional async health check. Returns True if provider is ready.
- [[assistant_app_core_provider_registry_rationale_44]] — code: Generic registry for provider implementations of a K.A.O.S capability.      Feat
- [[assistant_app_core_provider_registry_rationale_59]] — code: Register a provider implementation under a unique key.
- [[assistant_app_core_provider_registry_rationale_70]] — code: Activate a specific provider by key.
- [[assistant_app_core_provider_registry_rationale_80]] — code: Remove a provider from the registry.
- [[assistant_app_core_provider_registry_rationale_88]] — code: Deactivate current provider (will use fallback or raise).
- [[assistant_app_core_provider_registry_rationale_93]] — code: Return the currently active provider.

## Dependências

- [[assistant_app_core_provider_registry]] → `contains` → [[assistant_app_core_provider_registry_provider]]
- [[assistant_app_core_provider_registry]] → `contains` → [[assistant_app_core_provider_registry_providerregistry]]
- [[assistant_app_core_provider_registry]] → `imports_from` → [[assistant_app_core_provider_registry_py_abc]]
- [[assistant_app_core_provider_registry_rationale_1]] → `rationale_for` → [[assistant_app_core_provider_registry]]
- [[assistant_app_core_provider_registry_provider]] → `method` → [[assistant_app_core_provider_registry_provider_health_check]]
- [[assistant_app_core_provider_registry_provider]] → `method` → [[assistant_app_core_provider_registry_provider_name]]
- [[assistant_app_core_provider_registry_provider]] → `method` → [[assistant_app_core_provider_registry_provider_version]]
- [[assistant_app_core_provider_registry_provider]] → `inherits` → [[assistant_app_core_provider_registry_py_abc]]
- [[assistant_app_core_provider_registry_rationale_27]] → `rationale_for` → [[assistant_app_core_provider_registry_provider]]
- [[assistant_app_core_provider_registry_rationale_39]] → `rationale_for` → [[assistant_app_core_provider_registry_provider_health_check]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_activate]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_active]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_active_key]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_contains]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_deactivate]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_init]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_list_providers]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_providers]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_register]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_remove]]
- [[assistant_app_core_provider_registry_providerregistry]] → `method` → [[assistant_app_core_provider_registry_providerregistry_repr]]
- [[assistant_app_core_provider_registry_rationale_44]] → `rationale_for` → [[assistant_app_core_provider_registry_providerregistry]]
- [[assistant_app_core_provider_registry_providerregistry_register]] → `references` → [[assistant_app_core_provider_registry_py_t]]
- [[assistant_app_core_provider_registry_rationale_59]] → `rationale_for` → [[assistant_app_core_provider_registry_providerregistry_register]]
- [[assistant_app_core_provider_registry_providerregistry_active]] → `references` → [[assistant_app_core_provider_registry_py_t]]
- [[assistant_app_core_provider_registry_providerregistry_providers]] → `references` → [[assistant_app_core_provider_registry_py_t]]
- [[assistant_app_core_provider_registry_rationale_70]] → `rationale_for` → [[assistant_app_core_provider_registry_providerregistry_activate]]
- [[assistant_app_core_provider_registry_rationale_80]] → `rationale_for` → [[assistant_app_core_provider_registry_providerregistry_remove]]
- [[assistant_app_core_provider_registry_rationale_88]] → `rationale_for` → [[assistant_app_core_provider_registry_providerregistry_deactivate]]
- [[assistant_app_core_provider_registry_rationale_93]] → `rationale_for` → [[assistant_app_core_provider_registry_providerregistry_active]]