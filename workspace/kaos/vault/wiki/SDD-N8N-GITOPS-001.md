# docs\sdd\SDD-N8N-GITOPS-001.md

## Símbolos

- [[docs_sdd_sdd_n8n_gitops_001]] — code: SDD-N8N-GITOPS-001.md
- [[docs_sdd_sdd_n8n_gitops_001_sdd_n8n_gitops_001_sincronização_automática_de_workflows_do_n8n_gitops]] — code: SDD-N8N-GITOPS-001 — Sincronização Automática de Workflows do n8n (GitOps)
- [[docs_sdd_sdd_n8n_gitops_001_1_objetivo]] — code: 1. Objetivo
- [[docs_sdd_sdd_n8n_gitops_001_2_estrutura_do_repositório]] — code: 2. Estrutura do Repositório
- [[docs_sdd_sdd_n8n_gitops_001_3_manifesto_multi_ambiente_manifest_yaml]] — code: 3. Manifesto Multi-Ambiente (`manifest.yaml`)
- [[docs_sdd_sdd_n8n_gitops_001_4_arquitetura_do_processo_de_sincronização_sync_py]] — code: 4. Arquitetura do Processo de Sincronização (`sync.py`)
- [[docs_sdd_sdd_n8n_gitops_001_5_recursos_e_recursos_de_engenharia]] — code: 5. Recursos e Recursos de Engenharia
- [[docs_sdd_sdd_n8n_gitops_001_5_1_identificador_estável_por_workflow]] — code: 5.1. Identificador Estável por Workflow
- [[docs_sdd_sdd_n8n_gitops_001_5_2_comparação_inteligente_normalização_de_json]] — code: 5.2. Comparação Inteligente (Normalização de JSON)
- [[docs_sdd_sdd_n8n_gitops_001_5_3_validação_de_pré_deploy_linting]] — code: 5.3. Validação de Pré-Deploy (Linting)
- [[docs_sdd_sdd_n8n_gitops_001_5_4_ordenação_por_dependência_depends_on]] — code: 5.4. Ordenação por Dependência (`depends_on`)
- [[docs_sdd_sdd_n8n_gitops_001_5_5_backup_e_rollback_automático_resiliência]] — code: 5.5. Backup e Rollback Automático (Resiliência)
- [[docs_sdd_sdd_n8n_gitops_001_6_exportação_automática_fluxo_reverso_gitops_sync]] — code: 6. Exportação Automática (Fluxo Reverso / GitOps Sync)

## Dependências

- [[docs_sdd_sdd_n8n_gitops_001]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_sdd_n8n_gitops_001_sincronização_automática_de_workflows_do_n8n_gitops]]
- [[docs_sdd_sdd_n8n_gitops_001_sdd_n8n_gitops_001_sincronização_automática_de_workflows_do_n8n_gitops]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_1_objetivo]]
- [[docs_sdd_sdd_n8n_gitops_001_sdd_n8n_gitops_001_sincronização_automática_de_workflows_do_n8n_gitops]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_2_estrutura_do_repositório]]
- [[docs_sdd_sdd_n8n_gitops_001_sdd_n8n_gitops_001_sincronização_automática_de_workflows_do_n8n_gitops]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_3_manifesto_multi_ambiente_manifest_yaml]]
- [[docs_sdd_sdd_n8n_gitops_001_sdd_n8n_gitops_001_sincronização_automática_de_workflows_do_n8n_gitops]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_4_arquitetura_do_processo_de_sincronização_sync_py]]
- [[docs_sdd_sdd_n8n_gitops_001_sdd_n8n_gitops_001_sincronização_automática_de_workflows_do_n8n_gitops]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_5_recursos_e_recursos_de_engenharia]]
- [[docs_sdd_sdd_n8n_gitops_001_sdd_n8n_gitops_001_sincronização_automática_de_workflows_do_n8n_gitops]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_6_exportação_automática_fluxo_reverso_gitops_sync]]
- [[docs_sdd_sdd_n8n_gitops_001_5_recursos_e_recursos_de_engenharia]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_5_1_identificador_estável_por_workflow]]
- [[docs_sdd_sdd_n8n_gitops_001_5_recursos_e_recursos_de_engenharia]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_5_2_comparação_inteligente_normalização_de_json]]
- [[docs_sdd_sdd_n8n_gitops_001_5_recursos_e_recursos_de_engenharia]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_5_3_validação_de_pré_deploy_linting]]
- [[docs_sdd_sdd_n8n_gitops_001_5_recursos_e_recursos_de_engenharia]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_5_4_ordenação_por_dependência_depends_on]]
- [[docs_sdd_sdd_n8n_gitops_001_5_recursos_e_recursos_de_engenharia]] → `contains` → [[docs_sdd_sdd_n8n_gitops_001_5_5_backup_e_rollback_automático_resiliência]]