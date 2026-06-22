---
description: Padroes MCP do K.A.O.S
globs: 
---
# MCP Patterns

## O que e MCP
MCP (Model Context Protocol) permite que LLMs se conectem a ferramentas e servicos externos.

## Estrutura de um Servidor MCP
```python
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions

server = Server("kaos-tools")

@server.list_tools()
async def handle_list_tools() -> list[dict]:
    return [{"name": "search_notes", "description": "Busca notas no vault", "inputSchema": {...}}]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[dict]:
    if name == "search_notes":
        result = await search_notes(arguments["query"])
        return [{"type": "text", "text": result}]
```

## Integracao com K.A.O.S
- MCP servers registrados no `ServiceRegistry`
- Tools expostas como LangGraph tools
- EventBus emite eventos para tools MCP
- Providers MCP seguem `BaseChatProvider` contract

## Configuracao no opencode.json
```json
{
  "mcpServers": {
    "kaos": {
      "command": "uv",
      "args": ["run", "python", "-m", "app.mcp.server"],
      "env": {
        "K.A.O.S_API_KEY": "${K.A.O.S_API_KEY}"
      }
    }
  }
}
```
