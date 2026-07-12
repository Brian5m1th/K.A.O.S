# graphify\graphify\resolver_registry.py

## Símbolos

- [[graphify_graphify_resolver_registry]] — code: resolver_registry.py
- [[graphify_graphify_resolver_registry_languageresolver]] — code: LanguageResolver
- [[graphify_graphify_resolver_registry_register]] — code: register()
- [[graphify_graphify_resolver_registry_registered_resolvers]] — code: registered_resolvers()
- [[graphify_graphify_resolver_registry_run_language_resolvers]] — code: run_language_resolvers()
- [[graphify_graphify_resolver_registry_rationale_1]] — code: Registry for cross-file, language-specific resolution passes.  Some call/refer
- [[graphify_graphify_resolver_registry_rationale_30]] — code: One cross-file, language-specific resolution pass.      ``resolve`` has the si
- [[graphify_graphify_resolver_registry_rationale_49]] — code: Append a resolver to the global registry and return it (for inline use).
- [[graphify_graphify_resolver_registry_rationale_55]] — code: Return a copy of the registered resolvers, in registration order.
- [[graphify_graphify_resolver_registry_rationale_67]] — code: Run every resolver whose suffix appears in ``paths``.      Behaviorally identi

## Dependências

- [[graphify_graphify_resolver_registry]] → `contains` → [[graphify_graphify_resolver_registry_languageresolver]]
- [[graphify_graphify_resolver_registry]] → `contains` → [[graphify_graphify_resolver_registry_register]]
- [[graphify_graphify_resolver_registry]] → `contains` → [[graphify_graphify_resolver_registry_registered_resolvers]]
- [[graphify_graphify_resolver_registry]] → `contains` → [[graphify_graphify_resolver_registry_run_language_resolvers]]
- [[graphify_graphify_resolver_registry_rationale_1]] → `rationale_for` → [[graphify_graphify_resolver_registry]]
- [[graphify_graphify_resolver_registry_rationale_30]] → `rationale_for` → [[graphify_graphify_resolver_registry_languageresolver]]
- [[graphify_graphify_resolver_registry_register]] → `references` → [[graphify_graphify_resolver_registry_languageresolver]]
- [[graphify_graphify_resolver_registry_registered_resolvers]] → `references` → [[graphify_graphify_resolver_registry_languageresolver]]
- [[graphify_graphify_resolver_registry_run_language_resolvers]] → `references` → [[graphify_graphify_resolver_registry_languageresolver]]
- [[graphify_graphify_resolver_registry_rationale_49]] → `rationale_for` → [[graphify_graphify_resolver_registry_register]]
- [[graphify_graphify_resolver_registry_rationale_55]] → `rationale_for` → [[graphify_graphify_resolver_registry_registered_resolvers]]
- [[graphify_graphify_resolver_registry_rationale_67]] → `rationale_for` → [[graphify_graphify_resolver_registry_run_language_resolvers]]
- [[graphify_graphify_resolver_registry_run_language_resolvers]] → `references` → [[graphify_graphify_resolver_registry_py_path]]