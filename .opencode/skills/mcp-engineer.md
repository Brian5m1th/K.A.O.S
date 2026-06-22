---
description: Skill para MCP no K.A.O.S
---
# MCP Engineer

## Descricao
Implementacao de servidores MCP (Model Context Protocol) para integracao com LLMs.

## Responsabilidades
- Criar servidores MCP com tools e resources
- Expor ferramentas do K.A.O.S como MCP tools
- Configurar autenticacao via API Key
- Health check e monitoramento de servidores MCP
- Integracao com LangGraph tools

## Criterios de Qualidade
- Schema padrao (name, description, inputSchema)
- Async handlers
- Error handling com mensagens descritivas
- Logs com request_id
- Tools registradas no ServiceRegistry
