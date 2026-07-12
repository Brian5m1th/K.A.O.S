# docs\sdd\sdd_fase5_watcher_langgraph.md

## Símbolos

- [[docs_sdd_sdd_fase5_watcher_langgraph]] — code: sdd_fase5_watcher_langgraph.md
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] — code: SDD — Fases 6 e 7: LangGraph Agent + Memória de Longo Prazo
- [[docs_sdd_sdd_fase5_watcher_langgraph_objetivo]] — code: Objetivo
- [[docs_sdd_sdd_fase5_watcher_langgraph_status_concluído]] — code: Status: ✅ CONCLUÍDO
- [[docs_sdd_sdd_fase5_watcher_langgraph_1_estrutura_de_módulos]] — code: 1. Estrutura de Módulos
- [[docs_sdd_sdd_fase5_watcher_langgraph_2_estado_do_agente_agent_state_py]] — code: 2. Estado do Agente (`agent/state.py`)
- [[docs_sdd_sdd_fase5_watcher_langgraph_3_nó_de_recuperação_rag_agent_nodes_retrieve_py]] — code: 3. Nó de Recuperação RAG (`agent/nodes/retrieve.py`)
- [[docs_sdd_sdd_fase5_watcher_langgraph_4_nó_planner_agent_nodes_planner_py]] — code: 4. Nó Planner (`agent/nodes/planner.py`)
- [[docs_sdd_sdd_fase5_watcher_langgraph_5_grafo_langgraph_agent_graph_py]] — code: 5. Grafo LangGraph (`agent/graph.py`)
- [[docs_sdd_sdd_fase5_watcher_langgraph_6_agent_service_service_agent_service_py]] — code: 6. Agent Service (`service/agent_service.py`)
- [[docs_sdd_sdd_fase5_watcher_langgraph_dependências]] — code: Dependências
- [[docs_sdd_sdd_fase5_watcher_langgraph_resumo]] — code: Resumo
- [[docs_sdd_sdd_fase5_watcher_langgraph_responsabilidades]] — code: Responsabilidades
- [[docs_sdd_sdd_fase5_watcher_langgraph_dependencias]] — code: Dependencias
- [[docs_sdd_sdd_fase5_watcher_langgraph_fluxos]] — code: Fluxos
- [[docs_sdd_sdd_fase5_watcher_langgraph_integracoes]] — code: Integracoes
- [[docs_sdd_sdd_fase5_watcher_langgraph_arquivos_relacionados]] — code: Arquivos Relacionados
- [[docs_sdd_sdd_fase5_watcher_langgraph_referencias_kirl]] — code: Referencias KIRL
- [[docs_sdd_sdd_fase5_watcher_langgraph_ultima_atualizacao]] — code: Ultima Atualizacao

## Dependências

- [[docs_sdd_sdd_fase5_watcher_langgraph]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]]
- [[docs_sdd_sdd_fase5_watcher_langgraph]] → `references` → [[docs_sdd_sdd_obsidian_tools]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_1_estrutura_de_módulos]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_2_estado_do_agente_agent_state_py]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_3_nó_de_recuperação_rag_agent_nodes_retrieve_py]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_4_nó_planner_agent_nodes_planner_py]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_5_grafo_langgraph_agent_graph_py]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_6_agent_service_service_agent_service_py]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_arquivos_relacionados]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_dependencias]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_dependências]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_fluxos]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_integracoes]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_objetivo]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_referencias_kirl]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_responsabilidades]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_resumo]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_status_concluído]]
- [[docs_sdd_sdd_fase5_watcher_langgraph_sdd_fases_6_e_7_langgraph_agent_memória_de_longo_prazo]] → `contains` → [[docs_sdd_sdd_fase5_watcher_langgraph_ultima_atualizacao]]