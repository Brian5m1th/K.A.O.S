---
description: Skill para n8n no K.A.O.S
---
# N8N Architect

## Descricao
Arquitetura de automacoes com n8n como camada principal de automacao do K.A.O.S.

## Responsabilidades
- Design de workflows de automacao
- Configuracao de webhooks (trigger e action)
- Error handling com retry patterns
- Workflows event-driven (conectados ao EventBus)
- Integracao com GitHub Actions
- Orquestracao de agentes via n8n

## Criterios de Qualidade
- Webhooks com payload padronizado (`event` + `data`)
- Retry com exponential backoff
- Logs estruturados para debugging
- Variaveis sensiveis via env
- Workflows versionados
