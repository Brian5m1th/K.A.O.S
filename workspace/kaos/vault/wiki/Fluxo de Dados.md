# docs\Arquitetura\Fluxo de Dados.md

## Símbolos

- [[docs_arquitetura_fluxo_de_dados]] — code: Fluxo de Dados.md
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados]] — code: Fluxo de Dados
- [[docs_arquitetura_fluxo_de_dados_parent]] — code: Parent
- [[docs_arquitetura_fluxo_de_dados_children]] — code: Children
- [[docs_arquitetura_fluxo_de_dados_related]] — code: Related
- [[docs_arquitetura_fluxo_de_dados_tags]] — code: Tags
- [[docs_arquitetura_fluxo_de_dados_conteudo]] — code: Conteudo
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados_e_ciclo_de_vida_do_agente]] — code: Fluxo de Dados e Ciclo de Vida do Agente
- [[docs_arquitetura_fluxo_de_dados_visão_geral_do_roteamento]] — code: Visão Geral do Roteamento
- [[docs_arquitetura_fluxo_de_dados_fluxo_fast_execução_direta_de_tools]] — code: Fluxo FAST — Execução Direta de Tools
- [[docs_arquitetura_fluxo_de_dados_fluxo_memory_rag_llm_sem_langgraph]] — code: Fluxo MEMORY — RAG + LLM sem LangGraph
- [[docs_arquitetura_fluxo_de_dados_fluxo_smart_langgraph_completo]] — code: Fluxo SMART — LangGraph Completo
- [[docs_arquitetura_fluxo_de_dados_fluxo_proxy_openai_v1_chat_completions]] — code: Fluxo Proxy OpenAI (/v1/chat/completions)
- [[docs_arquitetura_fluxo_de_dados_relacao_com_outras_notas]] — code: Relacao com outras Notas

## Dependências

- [[docs_arquitetura_fluxo_de_dados]] → `contains` → [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados]]
- [[docs_arquitetura_fluxo_de_dados]] → `contains` → [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados_e_ciclo_de_vida_do_agente]]
- [[docs_arquitetura_fluxo_de_dados]] → `references` → [[docs_arquitetura_infraestrutura_docker]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados]] → `contains` → [[docs_arquitetura_fluxo_de_dados_children]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados]] → `contains` → [[docs_arquitetura_fluxo_de_dados_conteudo]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados]] → `contains` → [[docs_arquitetura_fluxo_de_dados_parent]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados]] → `contains` → [[docs_arquitetura_fluxo_de_dados_related]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados]] → `contains` → [[docs_arquitetura_fluxo_de_dados_tags]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados_e_ciclo_de_vida_do_agente]] → `contains` → [[docs_arquitetura_fluxo_de_dados_fluxo_fast_execução_direta_de_tools]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados_e_ciclo_de_vida_do_agente]] → `contains` → [[docs_arquitetura_fluxo_de_dados_fluxo_memory_rag_llm_sem_langgraph]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados_e_ciclo_de_vida_do_agente]] → `contains` → [[docs_arquitetura_fluxo_de_dados_fluxo_proxy_openai_v1_chat_completions]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados_e_ciclo_de_vida_do_agente]] → `contains` → [[docs_arquitetura_fluxo_de_dados_fluxo_smart_langgraph_completo]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados_e_ciclo_de_vida_do_agente]] → `contains` → [[docs_arquitetura_fluxo_de_dados_relacao_com_outras_notas]]
- [[docs_arquitetura_fluxo_de_dados_fluxo_de_dados_e_ciclo_de_vida_do_agente]] → `contains` → [[docs_arquitetura_fluxo_de_dados_visão_geral_do_roteamento]]