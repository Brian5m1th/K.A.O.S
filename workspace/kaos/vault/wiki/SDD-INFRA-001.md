# docs\sdd\SDD-INFRA-001.md

## Símbolos

- [[docs_sdd_sdd_infra_001]] — code: SDD-INFRA-001.md
- [[docs_sdd_sdd_infra_001_sdd_infra_001_docker_compose_produção_k_a_o_s]] — code: SDD-INFRA-001 — Docker Compose Produção (K.A.O.S)
- [[docs_sdd_sdd_infra_001_1_visão_geral]] — code: 1. Visão Geral
- [[docs_sdd_sdd_infra_001_2_rotação_de_logs_e_limites]] — code: 2. Rotação de Logs e Limites
- [[docs_sdd_sdd_infra_001_3_mapeamentos_de_volumes_críticos_e_logs_da_api]] — code: 3. Mapeamentos de Volumes Críticos e Logs da API
- [[docs_sdd_sdd_infra_001_4_estrutura_de_healthchecks]] — code: 4. Estrutura de Healthchecks
- [[docs_sdd_sdd_infra_001_4_1_postgresql_healthcheck]] — code: 4.1. PostgreSQL Healthcheck
- [[docs_sdd_sdd_infra_001_4_2_fastapi_kaos_api_healthcheck]] — code: 4.2. FastAPI kaos-api Healthcheck
- [[docs_sdd_sdd_infra_001_4_3_n8n_healthcheck]] — code: 4.3. n8n Healthcheck
- [[docs_sdd_sdd_infra_001_5_publicações_de_rotas_cloudflare_tunnel]] — code: 5. Publicações de Rotas (Cloudflare Tunnel)

## Dependências

- [[docs_sdd_sdd_infra_001]] → `contains` → [[docs_sdd_sdd_infra_001_sdd_infra_001_docker_compose_produção_k_a_o_s]]
- [[docs_sdd_sdd_infra_001_sdd_infra_001_docker_compose_produção_k_a_o_s]] → `contains` → [[docs_sdd_sdd_infra_001_1_visão_geral]]
- [[docs_sdd_sdd_infra_001_sdd_infra_001_docker_compose_produção_k_a_o_s]] → `contains` → [[docs_sdd_sdd_infra_001_2_rotação_de_logs_e_limites]]
- [[docs_sdd_sdd_infra_001_sdd_infra_001_docker_compose_produção_k_a_o_s]] → `contains` → [[docs_sdd_sdd_infra_001_3_mapeamentos_de_volumes_críticos_e_logs_da_api]]
- [[docs_sdd_sdd_infra_001_sdd_infra_001_docker_compose_produção_k_a_o_s]] → `contains` → [[docs_sdd_sdd_infra_001_4_estrutura_de_healthchecks]]
- [[docs_sdd_sdd_infra_001_sdd_infra_001_docker_compose_produção_k_a_o_s]] → `contains` → [[docs_sdd_sdd_infra_001_5_publicações_de_rotas_cloudflare_tunnel]]
- [[docs_sdd_sdd_infra_001_4_estrutura_de_healthchecks]] → `contains` → [[docs_sdd_sdd_infra_001_4_1_postgresql_healthcheck]]
- [[docs_sdd_sdd_infra_001_4_estrutura_de_healthchecks]] → `contains` → [[docs_sdd_sdd_infra_001_4_2_fastapi_kaos_api_healthcheck]]
- [[docs_sdd_sdd_infra_001_4_estrutura_de_healthchecks]] → `contains` → [[docs_sdd_sdd_infra_001_4_3_n8n_healthcheck]]