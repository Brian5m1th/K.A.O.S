---
description: Regras n8n para o K.A.O.S
globs: []
---
# N8N Rules

- Webhooks configurados via `N8N_WEBHOOK_URL` env var
- Workflows expostos como endpoints POST
- Payload com `event` + `data` padronizado
- Error handling com retry e fallback
- Logs estruturados para debugging
- Nao exponha credenciais no workflow JSON
- Workflows versionados no repositorio
