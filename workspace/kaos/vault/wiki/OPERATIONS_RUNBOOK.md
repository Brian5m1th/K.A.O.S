# docs\guides\OPERATIONS_RUNBOOK.md

## Símbolos

- [[docs_guides_operations_runbook]] — code: OPERATIONS_RUNBOOK.md
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] — code: K.A.O.S — Manual de Operações (Runbook)
- [[docs_guides_operations_runbook_1_gerenciamento_de_contêineres_e_serviços]] — code: 1. Gerenciamento de Contêineres e Serviços
- [[docs_guides_operations_runbook_iniciar_a_stack_completa]] — code: Iniciar a Stack Completa
- [[docs_guides_operations_runbook_parar_a_stack_completa]] — code: Parar a Stack Completa
- [[docs_guides_operations_runbook_reiniciar_serviço_específico_zero_downtime_para_outros]] — code: Reiniciar Serviço Específico (Zero Downtime para outros)
- [[docs_guides_operations_runbook_2_atualização_de_imagens_e_redeploy]] — code: 2. Atualização de Imagens e Redeploy
- [[docs_guides_operations_runbook_3_estratégia_e_comandos_de_backup]] — code: 3. Estratégia e Comandos de Backup
- [[docs_guides_operations_runbook_3_1_backup_automático_do_postgresql]] — code: 3.1. Backup Automático do PostgreSQL
- [[docs_guides_operations_runbook_3_2_backup_do_banco_vetorial_qdrant]] — code: 3.2. Backup do Banco Vetorial Qdrant
- [[docs_guides_operations_runbook_3_3_backup_de_volumes_físicos_docker_data]] — code: 3.3. Backup de Volumes Físicos (Docker Data)
- [[docs_guides_operations_runbook_4_procedimentos_de_restauração_restore]] — code: 4. Procedimentos de Restauração (Restore)
- [[docs_guides_operations_runbook_4_1_restaurar_banco_postgresql]] — code: 4.1. Restaurar Banco PostgreSQL
- [[docs_guides_operations_runbook_4_2_restaurar_snapshot_do_qdrant]] — code: 4.2. Restaurar Snapshot do Qdrant
- [[docs_guides_operations_runbook_5_gerenciamento_do_cloudflare_tunnel]] — code: 5. Gerenciamento do Cloudflare Tunnel
- [[docs_guides_operations_runbook_criar_ou_renovar_credenciais_do_túnel]] — code: Criar ou Renovar Credenciais do Túnel
- [[docs_guides_operations_runbook_6_alteração_de_domínio]] — code: 6. Alteração de Domínio
- [[docs_guides_operations_runbook_7_limpeza_e_coleta_de_lixo_garbage_collection]] — code: 7. Limpeza e Coleta de Lixo (Garbage Collection)
- [[docs_guides_operations_runbook_limpar_cache_do_builder_redes_órfãs_e_imagens_sem_tag]] — code: Limpar cache do Builder, redes órfãs e imagens sem tag
- [[docs_guides_operations_runbook_limpar_imagens_antigas_não_utilizadas_por_contêineres_ativos]] — code: Limpar imagens antigas não utilizadas por contêineres ativos
- [[docs_guides_operations_runbook_limpeza_física_dos_arquivos_de_log_da_api]] — code: Limpeza Física dos Arquivos de Log da API
- [[docs_guides_operations_runbook_8_monitoramento_de_logs]] — code: 8. Monitoramento de Logs
- [[docs_guides_operations_runbook_monitorar_logs_da_api_em_tempo_real_live_tail]] — code: Monitorar Logs da API em Tempo Real (Live Tail)
- [[docs_guides_operations_runbook_filtrar_logs_por_nível_de_severidade]] — code: Filtrar Logs por Nível de Severidade
- [[docs_guides_operations_runbook_loki_grafana_interface_gráfica]] — code: Loki & Grafana (Interface Gráfica)
- [[docs_guides_operations_runbook_9_troubleshooting_e_diagnósticos_rápidos]] — code: 9. Troubleshooting e Diagnósticos Rápidos
- [[docs_guides_operations_runbook_1_porta_do_backend_ocupada]] — code: 1. Porta do Backend Ocupada
- [[docs_guides_operations_runbook_2_banco_vetorial_bloqueado_travado]] — code: 2. Banco Vetorial Bloqueado/Travado
- [[docs_guides_operations_runbook_3_verificar_saúde_física_do_servidor]] — code: 3. Verificar Saúde Física do Servidor

## Dependências

- [[docs_guides_operations_runbook]] → `contains` → [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_1_gerenciamento_de_contêineres_e_serviços]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_2_atualização_de_imagens_e_redeploy]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_3_estratégia_e_comandos_de_backup]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_4_procedimentos_de_restauração_restore]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_5_gerenciamento_do_cloudflare_tunnel]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_6_alteração_de_domínio]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_7_limpeza_e_coleta_de_lixo_garbage_collection]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_8_monitoramento_de_logs]]
- [[docs_guides_operations_runbook_k_a_o_s_manual_de_operações_runbook]] → `contains` → [[docs_guides_operations_runbook_9_troubleshooting_e_diagnósticos_rápidos]]
- [[docs_guides_operations_runbook_1_gerenciamento_de_contêineres_e_serviços]] → `contains` → [[docs_guides_operations_runbook_iniciar_a_stack_completa]]
- [[docs_guides_operations_runbook_1_gerenciamento_de_contêineres_e_serviços]] → `contains` → [[docs_guides_operations_runbook_parar_a_stack_completa]]
- [[docs_guides_operations_runbook_1_gerenciamento_de_contêineres_e_serviços]] → `contains` → [[docs_guides_operations_runbook_reiniciar_serviço_específico_zero_downtime_para_outros]]
- [[docs_guides_operations_runbook_3_estratégia_e_comandos_de_backup]] → `contains` → [[docs_guides_operations_runbook_3_1_backup_automático_do_postgresql]]
- [[docs_guides_operations_runbook_3_estratégia_e_comandos_de_backup]] → `contains` → [[docs_guides_operations_runbook_3_2_backup_do_banco_vetorial_qdrant]]
- [[docs_guides_operations_runbook_3_estratégia_e_comandos_de_backup]] → `contains` → [[docs_guides_operations_runbook_3_3_backup_de_volumes_físicos_docker_data]]
- [[docs_guides_operations_runbook_4_procedimentos_de_restauração_restore]] → `contains` → [[docs_guides_operations_runbook_4_1_restaurar_banco_postgresql]]
- [[docs_guides_operations_runbook_4_procedimentos_de_restauração_restore]] → `contains` → [[docs_guides_operations_runbook_4_2_restaurar_snapshot_do_qdrant]]
- [[docs_guides_operations_runbook_5_gerenciamento_do_cloudflare_tunnel]] → `contains` → [[docs_guides_operations_runbook_criar_ou_renovar_credenciais_do_túnel]]
- [[docs_guides_operations_runbook_7_limpeza_e_coleta_de_lixo_garbage_collection]] → `contains` → [[docs_guides_operations_runbook_limpar_cache_do_builder_redes_órfãs_e_imagens_sem_tag]]
- [[docs_guides_operations_runbook_7_limpeza_e_coleta_de_lixo_garbage_collection]] → `contains` → [[docs_guides_operations_runbook_limpar_imagens_antigas_não_utilizadas_por_contêineres_ativos]]
- [[docs_guides_operations_runbook_7_limpeza_e_coleta_de_lixo_garbage_collection]] → `contains` → [[docs_guides_operations_runbook_limpeza_física_dos_arquivos_de_log_da_api]]
- [[docs_guides_operations_runbook_8_monitoramento_de_logs]] → `contains` → [[docs_guides_operations_runbook_filtrar_logs_por_nível_de_severidade]]
- [[docs_guides_operations_runbook_8_monitoramento_de_logs]] → `contains` → [[docs_guides_operations_runbook_loki_grafana_interface_gráfica]]
- [[docs_guides_operations_runbook_8_monitoramento_de_logs]] → `contains` → [[docs_guides_operations_runbook_monitorar_logs_da_api_em_tempo_real_live_tail]]
- [[docs_guides_operations_runbook_9_troubleshooting_e_diagnósticos_rápidos]] → `contains` → [[docs_guides_operations_runbook_1_porta_do_backend_ocupada]]
- [[docs_guides_operations_runbook_9_troubleshooting_e_diagnósticos_rápidos]] → `contains` → [[docs_guides_operations_runbook_2_banco_vetorial_bloqueado_travado]]
- [[docs_guides_operations_runbook_9_troubleshooting_e_diagnósticos_rápidos]] → `contains` → [[docs_guides_operations_runbook_3_verificar_saúde_física_do_servidor]]