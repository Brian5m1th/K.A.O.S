---
description: Regras MCP para o K.A.O.S
globs: []
---
# MCP Rules

- Servidores MCP registrados no ServiceRegistry
- Tools expostas seguem schema padrao (name, description, inputSchema)
- Resources expostos como `kaos://` URIs
- Autenticacao via API Key do K.A.O.S
- Logs com request_id para tracing
- Error handling com mensagens descritivas
- Nao bloquear event loop — usar async sempre
- Health check obrigatorio em todo server MCP
