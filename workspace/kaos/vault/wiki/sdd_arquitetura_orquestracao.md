# docs\sdd\sdd_arquitetura_orquestracao.md

## Símbolos

- [[docs_sdd_sdd_arquitetura_orquestracao]] — code: sdd_arquitetura_orquestracao.md
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] — code: SDD — Proxy OpenAI & Gateway de Orquestração
- [[docs_sdd_sdd_arquitetura_orquestracao_objetivo]] — code: Objetivo
- [[docs_sdd_sdd_arquitetura_orquestracao_visão_geral]] — code: Visão Geral
- [[docs_sdd_sdd_arquitetura_orquestracao_endpoints_do_gateway]] — code: Endpoints do Gateway
- [[docs_sdd_sdd_arquitetura_orquestracao_modelos_disponíveis]] — code: Modelos Disponíveis
- [[docs_sdd_sdd_arquitetura_orquestracao_fluxo_do_proxy_openai_triple_router]] — code: Fluxo do Proxy OpenAI (Triple-Router)
- [[docs_sdd_sdd_arquitetura_orquestracao_configuração_do_open_webui]] — code: Configuração do Open WebUI
- [[docs_sdd_sdd_arquitetura_orquestracao_contexto_de_usuário]] — code: Contexto de Usuário
- [[docs_sdd_sdd_arquitetura_orquestracao_resumo]] — code: Resumo
- [[docs_sdd_sdd_arquitetura_orquestracao_responsabilidades]] — code: Responsabilidades
- [[docs_sdd_sdd_arquitetura_orquestracao_dependencias]] — code: Dependencias
- [[docs_sdd_sdd_arquitetura_orquestracao_fluxos]] — code: Fluxos
- [[docs_sdd_sdd_arquitetura_orquestracao_integracoes]] — code: Integracoes
- [[docs_sdd_sdd_arquitetura_orquestracao_arquivos_relacionados]] — code: Arquivos Relacionados
- [[docs_sdd_sdd_arquitetura_orquestracao_referencias_kirl]] — code: Referencias KIRL
- [[docs_sdd_sdd_arquitetura_orquestracao_status]] — code: Status
- [[docs_sdd_sdd_arquitetura_orquestracao_ultima_atualizacao]] — code: Ultima Atualizacao

## Dependências

- [[docs_sdd_sdd_arquitetura_orquestracao]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]]
- [[docs_sdd_sdd_arquitetura_orquestracao]] → `references` → [[docs_sdd_sdd_fase2_ia_local]]
- [[docs_sdd_sdd_arquitetura_orquestracao]] → `references` → [[docs_sdd_sdd_user_context_propagation]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_arquivos_relacionados]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_configuração_do_open_webui]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_contexto_de_usuário]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_dependencias]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_endpoints_do_gateway]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_fluxo_do_proxy_openai_triple_router]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_fluxos]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_integracoes]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_objetivo]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_referencias_kirl]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_responsabilidades]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_resumo]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_status]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_ultima_atualizacao]]
- [[docs_sdd_sdd_arquitetura_orquestracao_sdd_proxy_openai_gateway_de_orquestração]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_visão_geral]]
- [[docs_sdd_sdd_arquitetura_orquestracao_endpoints_do_gateway]] → `contains` → [[docs_sdd_sdd_arquitetura_orquestracao_modelos_disponíveis]]