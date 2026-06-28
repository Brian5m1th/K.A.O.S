"""
MCP API — endpoints for managing MCP servers and tools.

RF-C01: GET /api/mcp/tools — list tools from all active MCP servers
RF-C02: POST /api/mcp/servers — register a new MCP server at runtime
"""

from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import BaseModel

from app.core.mcp_manager import MCPManager
from app.core.mcp_registry import MCPRegistry

router = APIRouter(prefix="/api/mcp", tags=["MCP"])


# ── Pydantic models ──────────────────────────────────────────────────


class MCPSchema(BaseModel):
    type: str
    properties: dict


class MCPToolResponse(BaseModel):
    name: str
    server: str
    description: str
    schema: MCPSchema | None = None
    status: str  # "active" | "disabled"


class MCPToolsResponse(BaseModel):
    total: int
    tools: list[MCPToolResponse]


class MCPServerRequest(BaseModel):
    name: str
    command: str
    args: list[str] = []
    env: dict[str, str] = {}


class MCPServerResponse(BaseModel):
    name: str
    status: str
    tools_count: int | None = None
    message: str


class MCPServerListEntry(BaseModel):
    name: str
    health: dict
    tools_count: int


class MCPServerListResponse(BaseModel):
    total: int
    servers: list[MCPServerListEntry]


# ── Endpoints ────────────────────────────────────────────────────────


@router.get("/tools", response_model=MCPToolsResponse)
async def list_mcp_tools():
    """RF-C01: Lista todas as ferramentas de todos os servidores MCP ativos."""
    manager = MCPManager()

    if not manager.is_initialized():
        return MCPToolsResponse(total=0, tools=[])

    tools = []
    for server_name, server in manager.servers.items():
        health = server.get_health()
        status = "active" if health.get("status") == "healthy" else "disabled"
        for tool_def in server.get_tools():
            tools.append(
                MCPToolResponse(
                    name=f"mcp_{server_name}_{tool_def.get('name', 'unknown')}",
                    server=server_name,
                    description=tool_def.get("description", ""),
                    schema=MCPSchema(
                        type=tool_def.get("inputSchema", {}).get("type", "object"),
                        properties=tool_def.get("inputSchema", {}).get(
                            "properties", {}
                        ),
                    )
                    if tool_def.get("inputSchema")
                    else None,
                    status=status,
                )
            )

    return MCPToolsResponse(total=len(tools), tools=tools)


@router.get("/servers", response_model=MCPServerListResponse)
async def list_mcp_servers():
    """Lista servidores MCP registrados com health status."""
    manager = MCPManager()
    servers = manager.list_servers()
    return MCPServerListResponse(
        total=len(servers),
        servers=[
            MCPServerListEntry(
                name=s["name"],
                health=s["health"],
                tools_count=s["tools_count"],
            )
            for s in servers
        ],
    )


@router.post("/servers", status_code=201, response_model=MCPServerResponse)
async def register_mcp_server(payload: MCPServerRequest):
    """RF-C02: Registra um novo servidor MCP em runtime.

    O servidor será inicializado assincronamente.
    """
    if not payload.name.strip():
        raise HTTPException(status_code=422, detail="name is required")
    if not payload.command.strip():
        raise HTTPException(status_code=422, detail="command is required")

    # Verificar se já existe
    manager = MCPManager()
    existing = manager.get_server(payload.name)
    if existing is not None:
        raise HTTPException(
            status_code=409,
            detail=f"Server '{payload.name}' already exists",
        )

    # Adicionar ao registry
    registry = MCPRegistry.load()
    registry.setdefault("servers", [])
    registry["servers"].append(
        {
            "name": payload.name,
            "command": payload.command,
            "args": payload.args,
            "env": payload.env,
            "enabled": True,
        }
    )
    MCPRegistry.save(registry)

    # Tentar inicializar
    try:
        started = manager.start_all()
        server = manager.get_server(payload.name)
        tools_count = len(server.get_tools()) if server else 0
        return MCPServerResponse(
            name=payload.name,
            status="initialized" if started > 0 else "start_failed",
            tools_count=tools_count,
            message=f"Server '{payload.name}' registered and initialized",
        )
    except Exception as exc:
        logger.warning("[mcp] failed to initialize server '{}': {}", payload.name, exc)
        return MCPServerResponse(
            name=payload.name,
            status="register_failed",
            message=f"Server registered but initialization failed: {exc}",
        )


@router.delete("/servers/{server_name}")
async def delete_mcp_server(server_name: str):
    """Deletes an MCP server from configuration and stops its subprocess."""
    name = server_name.strip()
    if not name:
        raise HTTPException(status_code=422, detail="server_name is required")

    manager = MCPManager()
    
    # 1. Stop the running process in the manager
    stopped = manager.delete_server(name)

    # 2. Remove from the registry config file
    registry = MCPRegistry.load()
    servers = registry.get("servers", [])
    filtered_servers = [s for s in servers if s.get("name") != name]
    
    if len(servers) == len(filtered_servers) and not stopped:
        raise HTTPException(status_code=404, detail=f"Server '{name}' not found")
         
    registry["servers"] = filtered_servers
    MCPRegistry.save(registry)

    return {
        "status": "deleted",
        "name": name,
        "message": f"Server '{name}' stopped and removed from configuration"
    }
