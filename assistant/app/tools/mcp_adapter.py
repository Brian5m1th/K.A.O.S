"""
MCP Adapter — converts MCP tool definitions into LangChain BaseTool
instances and registers them in the global TOOL_REGISTRY.

RF-C03: Bridge between MCPManager and LangGraph agent tool system.
"""

from loguru import logger
from langchain_core.tools import StructuredTool

from app.core.mcp_manager import MCPManager


def _make_tool_fn(server_name: str, tool_def: dict):
    """Return an async function that invokes the MCP tool."""
    tool_name = tool_def.get("name", "unknown")

    async def _invoke(**kwargs) -> str:
        manager = MCPManager()
        server = manager.get_server(server_name)
        if server is None:
            return f'{{"error": "mcp_server_unavailable", "server": "{server_name}"}}'
        result = server.call_tool(tool_name, kwargs)
        return str(result)

    _invoke.__name__ = f"mcp_{server_name}_{tool_name}"
    return _invoke


def build_mcp_tool(server_name: str, tool_def: dict) -> StructuredTool | None:
    """Convert a single MCP tool definition into a LangChain StructuredTool.

    Returns None if the tool definition is invalid.
    """
    tool_name = tool_def.get("name", "unknown")
    description = tool_def.get("description", f"MCP tool '{tool_name}' on server '{server_name}'")

    fn = _make_tool_fn(server_name, tool_def)

    structured_name = f"mcp_{server_name}_{tool_name}"

    try:
        tool = StructuredTool(
            name=structured_name,
            description=description,
            func=fn,
            coroutine=fn,
        )
        logger.debug("[mcp_adapter] built tool: {}", structured_name)
        return tool
    except Exception as exc:
        logger.warning("[mcp_adapter] failed to build tool '{}': {}", structured_name, exc)
        return None


def register_all_mcp_tools() -> int:
    """Iterate all active MCP servers and register their tools in TOOL_REGISTRY.

    Returns the count of successfully registered tools.
    """
    from app.agent.nodes.executor import TOOL_REGISTRY

    manager = MCPManager()
    if not manager.is_initialized():
        logger.info("[mcp_adapter] MCPManager not initialized, skipping tool registration")
        return 0

    count = 0
    for server_name, server in manager.servers.items():
        health = server.get_health()
        if health.get("status") != "healthy":
            logger.debug("[mcp_adapter] server '{}' not healthy, skipping", server_name)
            continue

        for tool_def in server.get_tools():
            tool = build_mcp_tool(server_name, tool_def)
            if tool is None:
                continue

            key = tool.name
            TOOL_REGISTRY[key] = tool
            count += 1
            logger.debug("[mcp_adapter] registered '{}' in TOOL_REGISTRY", key)

    logger.info("[mcp_adapter] registered {}/{} MCP tools", count, count)
    return count
