# assistant\app\agent\nodes\retrieve.py

## Símbolos

- [[assistant_app_agent_nodes_retrieve]] — code: retrieve.py
- [[assistant_app_agent_nodes_retrieve_get_retriever]] — code: _get_retriever()
- [[assistant_app_agent_nodes_retrieve_read_wiki_index]] — code: _read_wiki_index()
- [[assistant_app_agent_nodes_retrieve_read_wiki_page]] — code: _read_wiki_page()
- [[assistant_app_agent_nodes_retrieve_retrieve_context]] — code: retrieve_context()

## Dependências

- [[assistant_app_agent_nodes_retrieve]] → `contains` → [[assistant_app_agent_nodes_retrieve_get_retriever]]
- [[assistant_app_agent_nodes_retrieve]] → `contains` → [[assistant_app_agent_nodes_retrieve_read_wiki_index]]
- [[assistant_app_agent_nodes_retrieve]] → `contains` → [[assistant_app_agent_nodes_retrieve_read_wiki_page]]
- [[assistant_app_agent_nodes_retrieve]] → `contains` → [[assistant_app_agent_nodes_retrieve_retrieve_context]]
- [[assistant_app_agent_nodes_retrieve_get_retriever]] → `references` → [[assistant_app_rag_retriever_semantic_retriever_semanticretriever]]
- [[assistant_app_agent_nodes_retrieve_retrieve_context]] → `calls` → [[assistant_app_agent_nodes_retrieve_get_retriever]]
- [[assistant_app_agent_nodes_retrieve_retrieve_context]] → `calls` → [[assistant_app_agent_nodes_retrieve_read_wiki_index]]
- [[assistant_app_agent_nodes_retrieve_retrieve_context]] → `calls` → [[assistant_app_agent_nodes_retrieve_read_wiki_page]]
- [[assistant_app_agent_nodes_retrieve_retrieve_context]] → `references` → [[assistant_app_agent_nodes_retrieve_py_agentstate]]