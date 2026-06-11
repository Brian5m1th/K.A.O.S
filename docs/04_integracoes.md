Source: K.A.O.S Project
Tags: #integracoes #n8n #webhooks #github #email
Related: [[index]] [[backlog]] [[00_visao_geral]]

# Integracoes

> Planejamento para Fase 9 do backlog. Ainda nao implementado.

## Proximas Integracoes

### N8N
- Subir N8N via Docker Compose
- Webhooks para acoes externas
- Automacao de workflows

### GitHub
- Consulta de repositorios
- Leitura de codigo
- Criacao de issues/PRs

### Email
- Leitura e triagem de mensagens
- Envio de resumos

### AWS
- Comandos CLI
- Monitoramento de recursos

## Arquitetura

Todas as integracoes serao canalizadas via N8N, que atuara como gateway de automacao. O K.A.O.S se comunica com o N8N via webhooks HTTP, mantendo o agente LangGraph como orquestrador central.
