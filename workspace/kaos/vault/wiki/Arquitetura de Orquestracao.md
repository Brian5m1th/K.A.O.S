# docs\sdd\Arquitetura de Orquestracao.md

## Símbolos

- [[docs_sdd_arquitetura_de_orquestracao]] — code: Arquitetura de Orquestracao.md
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] — code: Arquitetura de Orquestracao
- [[docs_sdd_arquitetura_de_orquestracao_parent]] — code: Parent
- [[docs_sdd_arquitetura_de_orquestracao_children]] — code: Children
- [[docs_sdd_arquitetura_de_orquestracao_related]] — code: Related
- [[docs_sdd_arquitetura_de_orquestracao_tags]] — code: Tags
- [[docs_sdd_arquitetura_de_orquestracao_conteudo]] — code: Conteudo
- [[docs_sdd_arquitetura_de_orquestracao_objetivo]] — code: Objetivo
- [[docs_sdd_arquitetura_de_orquestracao_visão_geral]] — code: Visão Geral
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura]] — code: Arquitetura
- [[docs_sdd_arquitetura_de_orquestracao_endpoints_do_gateway]] — code: Endpoints do Gateway
- [[docs_sdd_arquitetura_de_orquestracao_modelos_disponíveis]] — code: Modelos Disponíveis
- [[docs_sdd_arquitetura_de_orquestracao_fluxo_do_proxy_openai_triple_router]] — code: Fluxo do Proxy OpenAI (Triple-Router)
- [[docs_sdd_arquitetura_de_orquestracao_system_prompt_do_k_a_o_s]] — code: System Prompt do K.A.O.S.
- [[docs_sdd_arquitetura_de_orquestracao_configuração_do_open_webui]] — code: Configuração do Open WebUI
- [[docs_sdd_arquitetura_de_orquestracao_contexto_de_usuário]] — code: Contexto de Usuário
- [[docs_sdd_arquitetura_de_orquestracao_considerações_de_segurança]] — code: Considerações de Segurança
- [[docs_sdd_arquitetura_de_orquestracao_dependências]] — code: Dependências
- [[docs_sdd_arquitetura_de_orquestracao_desbloqueia]] — code: Desbloqueia
- [[docs_sdd_arquitetura_de_orquestracao_resumo]] — code: Resumo
- [[docs_sdd_arquitetura_de_orquestracao_responsabilidades]] — code: Responsabilidades
- [[docs_sdd_arquitetura_de_orquestracao_dependencias]] — code: Dependencias
- [[docs_sdd_arquitetura_de_orquestracao_fluxos]] — code: Fluxos
- [[docs_sdd_arquitetura_de_orquestracao_integracoes]] — code: Integracoes
- [[docs_sdd_arquitetura_de_orquestracao_arquivos_relacionados]] — code: Arquivos Relacionados
- [[docs_sdd_arquitetura_de_orquestracao_referencias_kirl]] — code: Referencias KIRL
- [[docs_sdd_arquitetura_de_orquestracao_status]] — code: Status
- [[docs_sdd_arquitetura_de_orquestracao_ultima_atualizacao]] — code: Ultima Atualizacao

## Dependências

- [[docs_sdd_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]]
- [[docs_sdd_arquitetura_de_orquestracao]] → `references` → [[docs_sdd_estado_do_agente]]
- [[docs_sdd_arquitetura_de_orquestracao]] → `references` → [[docs_sdd_fase_2_ia_local]]
- [[docs_sdd_arquitetura_de_orquestracao]] → `references` → [[docs_sdd_fases_6_7_watcher_langgraph_e_memoria]]
- [[docs_sdd_arquitetura_de_orquestracao]] → `references` → [[docs_sdd_ferramentas_do_langgraph]]
- [[docs_sdd_arquitetura_de_orquestracao]] → `references` → [[docs_sdd_orquestrador_langgraph]]
- [[docs_sdd_arquitetura_de_orquestracao]] → `references` → [[docs_sdd_propagacao_de_contexto_de_usuario]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_arquitetura]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_arquivos_relacionados]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_children]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_configuração_do_open_webui]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_considerações_de_segurança]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_conteudo]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_contexto_de_usuário]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_dependencias]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_dependências]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_desbloqueia]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_endpoints_do_gateway]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_fluxo_do_proxy_openai_triple_router]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_fluxos]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_integracoes]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_objetivo]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_parent]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_referencias_kirl]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_related]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_responsabilidades]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_resumo]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_status]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_system_prompt_do_k_a_o_s]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_tags]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_ultima_atualizacao]]
- [[docs_sdd_arquitetura_de_orquestracao_arquitetura_de_orquestracao]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_visão_geral]]
- [[docs_sdd_arquitetura_de_orquestracao_endpoints_do_gateway]] → `contains` → [[docs_sdd_arquitetura_de_orquestracao_modelos_disponíveis]]