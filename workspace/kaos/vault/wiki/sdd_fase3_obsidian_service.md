# docs\sdd\sdd_fase3_obsidian_service.md

## Símbolos

- [[docs_sdd_sdd_fase3_obsidian_service]] — code: sdd_fase3_obsidian_service.md
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] — code: SDD — Fase 3: ObsidianService e Ferramentas de Nota
- [[docs_sdd_sdd_fase3_obsidian_service_objetivo]] — code: Objetivo
- [[docs_sdd_sdd_fase3_obsidian_service_critério_de_sucesso]] — code: Critério de Sucesso
- [[docs_sdd_sdd_fase3_obsidian_service_tarefas]] — code: Tarefas
- [[docs_sdd_sdd_fase3_obsidian_service_configuração]] — code: ⚙️ Configuração
- [[docs_sdd_sdd_fase3_obsidian_service_leitura]] — code: 📖 Leitura
- [[docs_sdd_sdd_fase3_obsidian_service_escrita]] — code: ✏️ Escrita
- [[docs_sdd_sdd_fase3_obsidian_service_busca]] — code: 🔍 Busca
- [[docs_sdd_sdd_fase3_obsidian_service_1_estrutura_de_módulos]] — code: 1. Estrutura de Módulos
- [[docs_sdd_sdd_fase3_obsidian_service_2_dtos_de_domínio_domain_document_py]] — code: 2. DTOs de Domínio (`domain/document.py`)
- [[docs_sdd_sdd_fase3_obsidian_service_3_obsidianservice_obsidian_services_obsidian_service_py]] — code: 3. ObsidianService (`obsidian/services/obsidian_service.py`)
- [[docs_sdd_sdd_fase3_obsidian_service_4_ferramentas_langgraph_compatíveis]] — code: 4. Ferramentas LangGraph-Compatíveis
- [[docs_sdd_sdd_fase3_obsidian_service_create_note_tool_py]] — code: `create_note_tool.py`
- [[docs_sdd_sdd_fase3_obsidian_service_read_note_tool_py]] — code: `read_note_tool.py`
- [[docs_sdd_sdd_fase3_obsidian_service_update_note_tool_py]] — code: `update_note_tool.py`
- [[docs_sdd_sdd_fase3_obsidian_service_delete_note_tool_py]] — code: `delete_note_tool.py`
- [[docs_sdd_sdd_fase3_obsidian_service_search_notes_tool_py]] — code: `search_notes_tool.py`
- [[docs_sdd_sdd_fase3_obsidian_service_5_testes_unitários]] — code: 5. Testes Unitários
- [[docs_sdd_sdd_fase3_obsidian_service_dependências_desta_fase]] — code: Dependências Desta Fase
- [[docs_sdd_sdd_fase3_obsidian_service_desbloqueia]] — code: Desbloqueia
- [[docs_sdd_sdd_fase3_obsidian_service_resumo]] — code: Resumo
- [[docs_sdd_sdd_fase3_obsidian_service_responsabilidades]] — code: Responsabilidades
- [[docs_sdd_sdd_fase3_obsidian_service_dependencias]] — code: Dependencias
- [[docs_sdd_sdd_fase3_obsidian_service_fluxos]] — code: Fluxos
- [[docs_sdd_sdd_fase3_obsidian_service_integracoes]] — code: Integracoes
- [[docs_sdd_sdd_fase3_obsidian_service_arquivos_relacionados]] — code: Arquivos Relacionados
- [[docs_sdd_sdd_fase3_obsidian_service_referencias_kirl]] — code: Referencias KIRL
- [[docs_sdd_sdd_fase3_obsidian_service_status]] — code: Status
- [[docs_sdd_sdd_fase3_obsidian_service_ultima_atualizacao]] — code: Ultima Atualizacao

## Dependências

- [[docs_sdd_sdd_fase3_obsidian_service]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]]
- [[docs_sdd_sdd_fase3_obsidian_service]] → `references` → [[docs_sdd_sdd_fase4_rag_pipeline]]
- [[docs_sdd_sdd_fase3_obsidian_service]] → `references` → [[docs_sdd_sdd_fase5_watcher_langgraph]]
- [[docs_sdd_sdd_fase3_obsidian_service]] → `references` → [[docs_sdd_sdd_obsidian_memoria]]
- [[docs_sdd_sdd_fase3_obsidian_service]] → `references` → [[docs_sdd_sdd_obsidian_tools]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_1_estrutura_de_módulos]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_2_dtos_de_domínio_domain_document_py]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_3_obsidianservice_obsidian_services_obsidian_service_py]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_4_ferramentas_langgraph_compatíveis]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_5_testes_unitários]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_arquivos_relacionados]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_critério_de_sucesso]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_dependencias]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_dependências_desta_fase]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_desbloqueia]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_fluxos]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_integracoes]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_objetivo]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_referencias_kirl]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_responsabilidades]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_resumo]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_status]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_tarefas]]
- [[docs_sdd_sdd_fase3_obsidian_service_sdd_fase_3_obsidianservice_e_ferramentas_de_nota]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_ultima_atualizacao]]
- [[docs_sdd_sdd_fase3_obsidian_service_tarefas]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_busca]]
- [[docs_sdd_sdd_fase3_obsidian_service_tarefas]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_configuração]]
- [[docs_sdd_sdd_fase3_obsidian_service_tarefas]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_escrita]]
- [[docs_sdd_sdd_fase3_obsidian_service_tarefas]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_leitura]]
- [[docs_sdd_sdd_fase3_obsidian_service_4_ferramentas_langgraph_compatíveis]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_create_note_tool_py]]
- [[docs_sdd_sdd_fase3_obsidian_service_4_ferramentas_langgraph_compatíveis]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_delete_note_tool_py]]
- [[docs_sdd_sdd_fase3_obsidian_service_4_ferramentas_langgraph_compatíveis]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_read_note_tool_py]]
- [[docs_sdd_sdd_fase3_obsidian_service_4_ferramentas_langgraph_compatíveis]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_search_notes_tool_py]]
- [[docs_sdd_sdd_fase3_obsidian_service_4_ferramentas_langgraph_compatíveis]] → `contains` → [[docs_sdd_sdd_fase3_obsidian_service_update_note_tool_py]]