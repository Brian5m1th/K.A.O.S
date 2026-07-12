# docs\sdd\SDD-OPS-002.md

## Símbolos

- [[docs_sdd_sdd_ops_002]] — code: SDD-OPS-002.md
- [[docs_sdd_sdd_ops_002_sdd_ops_002_disaster_recovery_limpezas_físicas_k_a_o_s]] — code: SDD-OPS-002 — Disaster Recovery & Limpezas Físicas (K.A.O.S)
- [[docs_sdd_sdd_ops_002_1_visão_geral]] — code: 1. Visão Geral
- [[docs_sdd_sdd_ops_002_2_procedimento_seguro_de_limpeza_de_disco_sem_perda_de_dados]] — code: 2. Procedimento Seguro de Limpeza de Disco (Sem Perda de Dados)
- [[docs_sdd_sdd_ops_002_passo_1_avaliar_uso_de_disco_do_docker]] — code: Passo 1: Avaliar Uso de Disco do Docker
- [[docs_sdd_sdd_ops_002_passo_2_limpar_cache_do_builder_altamente_seguro]] — code: Passo 2: Limpar Cache do Builder (Altamente Seguro)
- [[docs_sdd_sdd_ops_002_passo_3_limpar_contêineres_parados_inativos]] — code: Passo 3: Limpar Contêineres Parados/Inativos
- [[docs_sdd_sdd_ops_002_passo_4_limpar_imagens_não_utilizadas]] — code: Passo 4: Limpar Imagens Não Utilizadas
- [[docs_sdd_sdd_ops_002_passo_5_truncar_arquivo_de_logs_físico]] — code: Passo 5: Truncar Arquivo de Logs Físico
- [[docs_sdd_sdd_ops_002_3_procedimento_de_restauração_de_dados]] — code: 3. Procedimento de Restauração de Dados
- [[docs_sdd_sdd_ops_002_3_1_postgresql_restauração_lógica]] — code: 3.1. PostgreSQL (Restauração Lógica)
- [[docs_sdd_sdd_ops_002_3_2_qdrant_restauração_de_snapshots]] — code: 3.2. Qdrant (Restauração de Snapshots)

## Dependências

- [[docs_sdd_sdd_ops_002]] → `contains` → [[docs_sdd_sdd_ops_002_sdd_ops_002_disaster_recovery_limpezas_físicas_k_a_o_s]]
- [[docs_sdd_sdd_ops_002_sdd_ops_002_disaster_recovery_limpezas_físicas_k_a_o_s]] → `contains` → [[docs_sdd_sdd_ops_002_1_visão_geral]]
- [[docs_sdd_sdd_ops_002_sdd_ops_002_disaster_recovery_limpezas_físicas_k_a_o_s]] → `contains` → [[docs_sdd_sdd_ops_002_2_procedimento_seguro_de_limpeza_de_disco_sem_perda_de_dados]]
- [[docs_sdd_sdd_ops_002_sdd_ops_002_disaster_recovery_limpezas_físicas_k_a_o_s]] → `contains` → [[docs_sdd_sdd_ops_002_3_procedimento_de_restauração_de_dados]]
- [[docs_sdd_sdd_ops_002_2_procedimento_seguro_de_limpeza_de_disco_sem_perda_de_dados]] → `contains` → [[docs_sdd_sdd_ops_002_passo_1_avaliar_uso_de_disco_do_docker]]
- [[docs_sdd_sdd_ops_002_2_procedimento_seguro_de_limpeza_de_disco_sem_perda_de_dados]] → `contains` → [[docs_sdd_sdd_ops_002_passo_2_limpar_cache_do_builder_altamente_seguro]]
- [[docs_sdd_sdd_ops_002_2_procedimento_seguro_de_limpeza_de_disco_sem_perda_de_dados]] → `contains` → [[docs_sdd_sdd_ops_002_passo_3_limpar_contêineres_parados_inativos]]
- [[docs_sdd_sdd_ops_002_2_procedimento_seguro_de_limpeza_de_disco_sem_perda_de_dados]] → `contains` → [[docs_sdd_sdd_ops_002_passo_4_limpar_imagens_não_utilizadas]]
- [[docs_sdd_sdd_ops_002_2_procedimento_seguro_de_limpeza_de_disco_sem_perda_de_dados]] → `contains` → [[docs_sdd_sdd_ops_002_passo_5_truncar_arquivo_de_logs_físico]]
- [[docs_sdd_sdd_ops_002_3_procedimento_de_restauração_de_dados]] → `contains` → [[docs_sdd_sdd_ops_002_3_1_postgresql_restauração_lógica]]
- [[docs_sdd_sdd_ops_002_3_procedimento_de_restauração_de_dados]] → `contains` → [[docs_sdd_sdd_ops_002_3_2_qdrant_restauração_de_snapshots]]