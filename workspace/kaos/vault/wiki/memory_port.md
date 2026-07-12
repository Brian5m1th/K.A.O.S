# assistant\app\domain\ports\memory_port.py

## Símbolos

- [[assistant_app_domain_ports_memory_port]] — code: memory_port.py
- [[assistant_app_domain_ports_memory_port_memoryentry]] — code: MemoryEntry
- [[assistant_app_domain_ports_memory_port_memoryquery]] — code: MemoryQuery
- [[assistant_app_domain_ports_memory_port_memoryresult]] — code: MemoryResult
- [[assistant_app_domain_ports_memory_port_memoryport]] — code: MemoryPort
- [[assistant_app_domain_ports_memory_port_memoryport_provider_name]] — code: .provider_name()
- [[assistant_app_domain_ports_memory_port_memoryport_store]] — code: .store()
- [[assistant_app_domain_ports_memory_port_memoryport_search]] — code: .search()
- [[assistant_app_domain_ports_memory_port_memoryport_get]] — code: .get()
- [[assistant_app_domain_ports_memory_port_memoryport_delete]] — code: .delete()
- [[assistant_app_domain_ports_memory_port_memoryport_health]] — code: .health()
- [[assistant_app_domain_ports_memory_port_rationale_1]] — code: MemoryPort — Agent and user memory capability.  Stores and retrieves episodic, s
- [[assistant_app_domain_ports_memory_port_rationale_17]] — code: A single memory record.
- [[assistant_app_domain_ports_memory_port_rationale_29]] — code: Search parameters for memory retrieval.
- [[assistant_app_domain_ports_memory_port_rationale_39]] — code: Search result wrapper.
- [[assistant_app_domain_ports_memory_port_rationale_46]] — code: Interface for memory storage and retrieval.      Concrete implementations:
- [[assistant_app_domain_ports_memory_port_rationale_62]] — code: Store a memory entry. Returns the assigned ID.
- [[assistant_app_domain_ports_memory_port_rationale_67]] — code: Search memories by semantic similarity or metadata.
- [[assistant_app_domain_ports_memory_port_rationale_72]] — code: Retrieve a specific memory by ID.
- [[assistant_app_domain_ports_memory_port_rationale_77]] — code: Delete a memory entry. Returns True if deleted.

## Dependências

- [[assistant_app_domain_ports_memory_port]] → `contains` → [[assistant_app_domain_ports_memory_port_memoryentry]]
- [[assistant_app_domain_ports_memory_port]] → `contains` → [[assistant_app_domain_ports_memory_port_memoryport]]
- [[assistant_app_domain_ports_memory_port]] → `contains` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_domain_ports_memory_port]] → `contains` → [[assistant_app_domain_ports_memory_port_memoryresult]]
- [[assistant_app_domain_ports_memory_port]] → `imports_from` → [[assistant_app_domain_ports_memory_port_py_abc]]
- [[assistant_app_domain_ports_memory_port_rationale_1]] → `rationale_for` → [[assistant_app_domain_ports_memory_port]]
- [[assistant_app_domain_ports_memory_port_memoryport_get]] → `references` → [[assistant_app_domain_ports_memory_port_memoryentry]]
- [[assistant_app_domain_ports_memory_port_memoryport_store]] → `references` → [[assistant_app_domain_ports_memory_port_memoryentry]]
- [[assistant_app_domain_ports_memory_port_rationale_17]] → `rationale_for` → [[assistant_app_domain_ports_memory_port_memoryentry]]
- [[assistant_app_domain_ports_memory_port_memoryport_search]] → `references` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_domain_ports_memory_port_rationale_29]] → `rationale_for` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_domain_ports_memory_port_memoryport_search]] → `references` → [[assistant_app_domain_ports_memory_port_memoryresult]]
- [[assistant_app_domain_ports_memory_port_rationale_39]] → `rationale_for` → [[assistant_app_domain_ports_memory_port_memoryresult]]
- [[assistant_app_domain_ports_memory_port_memoryport]] → `method` → [[assistant_app_domain_ports_memory_port_memoryport_delete]]
- [[assistant_app_domain_ports_memory_port_memoryport]] → `method` → [[assistant_app_domain_ports_memory_port_memoryport_get]]
- [[assistant_app_domain_ports_memory_port_memoryport]] → `method` → [[assistant_app_domain_ports_memory_port_memoryport_health]]
- [[assistant_app_domain_ports_memory_port_memoryport]] → `method` → [[assistant_app_domain_ports_memory_port_memoryport_provider_name]]
- [[assistant_app_domain_ports_memory_port_memoryport]] → `method` → [[assistant_app_domain_ports_memory_port_memoryport_search]]
- [[assistant_app_domain_ports_memory_port_memoryport]] → `method` → [[assistant_app_domain_ports_memory_port_memoryport_store]]
- [[assistant_app_domain_ports_memory_port_memoryport]] → `inherits` → [[assistant_app_domain_ports_memory_port_py_abc]]
- [[assistant_app_domain_ports_memory_port_rationale_46]] → `rationale_for` → [[assistant_app_domain_ports_memory_port_memoryport]]
- [[assistant_app_domain_ports_memory_port_rationale_62]] → `rationale_for` → [[assistant_app_domain_ports_memory_port_memoryport_store]]
- [[assistant_app_domain_ports_memory_port_rationale_67]] → `rationale_for` → [[assistant_app_domain_ports_memory_port_memoryport_search]]
- [[assistant_app_domain_ports_memory_port_rationale_72]] → `rationale_for` → [[assistant_app_domain_ports_memory_port_memoryport_get]]
- [[assistant_app_domain_ports_memory_port_rationale_77]] → `rationale_for` → [[assistant_app_domain_ports_memory_port_memoryport_delete]]