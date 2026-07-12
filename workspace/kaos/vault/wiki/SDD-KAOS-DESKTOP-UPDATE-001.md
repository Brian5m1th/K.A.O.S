# docs\sdd\SDD-KAOS-DESKTOP-UPDATE-001.md

## Símbolos

- [[docs_sdd_sdd_kaos_desktop_update_001]] — code: SDD-KAOS-DESKTOP-UPDATE-001.md
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] — code: SDD-KAOS-DESKTOP-UPDATE-001
- [[docs_sdd_sdd_kaos_desktop_update_001_sistema_de_atualização_automática_k_a_o_s_desktop]] — code: Sistema de Atualização Automática — K.A.O.S Desktop
- [[docs_sdd_sdd_kaos_desktop_update_001_1_problema]] — code: 1. Problema
- [[docs_sdd_sdd_kaos_desktop_update_001_2_decisões_de_arquitetura]] — code: 2. Decisões de Arquitetura
- [[docs_sdd_sdd_kaos_desktop_update_001_dec_001_desacoplamento_do_sistema_de_providers]] — code: DEC-001 — Desacoplamento do Sistema de Providers
- [[docs_sdd_sdd_kaos_desktop_update_001_dec_002_separação_de_responsabilidades_service_store_ui]] — code: DEC-002 — Separação de Responsabilidades (Service/Store/UI)
- [[docs_sdd_sdd_kaos_desktop_update_001_dec_003_updatescheduler_como_intermediário]] — code: DEC-003 — UpdateScheduler como Intermediário
- [[docs_sdd_sdd_kaos_desktop_update_001_dec_004_single_source_of_truth_para_versão]] — code: DEC-004 — Single Source of Truth para Versão
- [[docs_sdd_sdd_kaos_desktop_update_001_3_contexto_técnico_atual]] — code: 3. Contexto Técnico Atual
- [[docs_sdd_sdd_kaos_desktop_update_001_estado_da_base_de_código]] — code: Estado da Base de Código
- [[docs_sdd_sdd_kaos_desktop_update_001_4_objetivos]] — code: 4. Objetivos
- [[docs_sdd_sdd_kaos_desktop_update_001_funcionais]] — code: Funcionais
- [[docs_sdd_sdd_kaos_desktop_update_001_não_funcionais]] — code: Não Funcionais
- [[docs_sdd_sdd_kaos_desktop_update_001_5_arquitetura]] — code: 5. Arquitetura
- [[docs_sdd_sdd_kaos_desktop_update_001_5_1_estrutura_de_camadas]] — code: 5.1 Estrutura de Camadas
- [[docs_sdd_sdd_kaos_desktop_update_001_5_2_fluxo_de_verificação_no_startup]] — code: 5.2 Fluxo de Verificação no Startup
- [[docs_sdd_sdd_kaos_desktop_update_001_5_3_fluxo_de_download_e_instalação]] — code: 5.3 Fluxo de Download e Instalação
- [[docs_sdd_sdd_kaos_desktop_update_001_6_contratos_de_interface]] — code: 6. Contratos de Interface
- [[docs_sdd_sdd_kaos_desktop_update_001_6_1_updatestore_estado_puro]] — code: 6.1 UpdateStore — Estado Puro
- [[docs_sdd_sdd_kaos_desktop_update_001_6_2_updaterservice_regras_de_negócio]] — code: 6.2 UpdaterService — Regras de Negócio
- [[docs_sdd_sdd_kaos_desktop_update_001_6_3_updatescheduler]] — code: 6.3 UpdateScheduler
- [[docs_sdd_sdd_kaos_desktop_update_001_6_4_comandos_rust_updater_rs]] — code: 6.4 Comandos Rust (updater.rs)
- [[docs_sdd_sdd_kaos_desktop_update_001_7_update_proxy_json_schema_formal_nf_06]] — code: 7. update-proxy.json — Schema Formal (NF-06)
- [[docs_sdd_sdd_kaos_desktop_update_001_8_estrutura_de_arquivos]] — code: 8. Estrutura de Arquivos
- [[docs_sdd_sdd_kaos_desktop_update_001_9_ui_updatecard_por_fase]] — code: 9. UI — UpdateCard por Fase
- [[docs_sdd_sdd_kaos_desktop_update_001_exemplo_fase_available]] — code: Exemplo — fase `available`
- [[docs_sdd_sdd_kaos_desktop_update_001_10_observabilidade]] — code: 10. Observabilidade
- [[docs_sdd_sdd_kaos_desktop_update_001_11_segurança]] — code: 11. Segurança
- [[docs_sdd_sdd_kaos_desktop_update_001_12_critérios_de_aceitação]] — code: 12. Critérios de Aceitação
- [[docs_sdd_sdd_kaos_desktop_update_001_13_fora_de_escopo_fase_1]] — code: 13. Fora de Escopo (Fase 1)
- [[docs_sdd_sdd_kaos_desktop_update_001_14_roadmap]] — code: 14. Roadmap

## Dependências

- [[docs_sdd_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_10_observabilidade]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_11_segurança]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_12_critérios_de_aceitação]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_13_fora_de_escopo_fase_1]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_14_roadmap]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_1_problema]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_2_decisões_de_arquitetura]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_3_contexto_técnico_atual]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_4_objetivos]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_5_arquitetura]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_6_contratos_de_interface]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_7_update_proxy_json_schema_formal_nf_06]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_8_estrutura_de_arquivos]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_9_ui_updatecard_por_fase]]
- [[docs_sdd_sdd_kaos_desktop_update_001_sdd_kaos_desktop_update_001]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_sistema_de_atualização_automática_k_a_o_s_desktop]]
- [[docs_sdd_sdd_kaos_desktop_update_001_2_decisões_de_arquitetura]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_dec_001_desacoplamento_do_sistema_de_providers]]
- [[docs_sdd_sdd_kaos_desktop_update_001_2_decisões_de_arquitetura]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_dec_002_separação_de_responsabilidades_service_store_ui]]
- [[docs_sdd_sdd_kaos_desktop_update_001_2_decisões_de_arquitetura]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_dec_003_updatescheduler_como_intermediário]]
- [[docs_sdd_sdd_kaos_desktop_update_001_2_decisões_de_arquitetura]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_dec_004_single_source_of_truth_para_versão]]
- [[docs_sdd_sdd_kaos_desktop_update_001_3_contexto_técnico_atual]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_estado_da_base_de_código]]
- [[docs_sdd_sdd_kaos_desktop_update_001_4_objetivos]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_funcionais]]
- [[docs_sdd_sdd_kaos_desktop_update_001_4_objetivos]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_não_funcionais]]
- [[docs_sdd_sdd_kaos_desktop_update_001_5_arquitetura]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_5_1_estrutura_de_camadas]]
- [[docs_sdd_sdd_kaos_desktop_update_001_5_arquitetura]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_5_2_fluxo_de_verificação_no_startup]]
- [[docs_sdd_sdd_kaos_desktop_update_001_5_arquitetura]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_5_3_fluxo_de_download_e_instalação]]
- [[docs_sdd_sdd_kaos_desktop_update_001_6_contratos_de_interface]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_6_1_updatestore_estado_puro]]
- [[docs_sdd_sdd_kaos_desktop_update_001_6_contratos_de_interface]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_6_2_updaterservice_regras_de_negócio]]
- [[docs_sdd_sdd_kaos_desktop_update_001_6_contratos_de_interface]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_6_3_updatescheduler]]
- [[docs_sdd_sdd_kaos_desktop_update_001_6_contratos_de_interface]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_6_4_comandos_rust_updater_rs]]
- [[docs_sdd_sdd_kaos_desktop_update_001_9_ui_updatecard_por_fase]] → `contains` → [[docs_sdd_sdd_kaos_desktop_update_001_exemplo_fase_available]]