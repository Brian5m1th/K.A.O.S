---
description: Skill para Docker no K.A.O.S
---
# Docker Expert

## Descricao
Gerenciamento de infraestrutura Docker para o ecossistema K.A.O.S (9 servicos).

## Responsabilidades
- Manter docker-compose.yml (postgres, qdrant, ollama, n8n, prometheus, loki, grafana, open-webui, kaos-api)
- Otimizar Dockerfiles (multi-stage, nao-root, healthcheck)
- Gerenciar volumes nomeados e redes
- Configurar variaveis de ambiente via .env
- Health checks para todos os servicos

## Criterios de Qualidade
- Multi-stage builds
- Usuario nao-root em producao
- HEALTHCHECK em todo servico
- Sem hardcoded secrets
- Cache de camadas otimizado
