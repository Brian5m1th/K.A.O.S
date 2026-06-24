"""
Base interface for MCP (Model Context Protocol) servers.

Defines the abstract contract that all MCP server drivers must implement
for lifecycle management, tool discovery, and health reporting.
"""

from abc import ABC, abstractmethod


class MCPServer(ABC):
    """Abstract base class for MCP server implementations.

    Each concrete subclass wraps an external MCP server process
    (STDIO-based subprocess) and exposes its tools through this interface.
    """

    @abstractmethod
    def initialize(self) -> bool:
        """Start the MCP server subprocess and establish communication.

        Returns True if initialization succeeded, False otherwise.
        """
        ...

    @abstractmethod
    def shutdown(self) -> bool:
        """Gracefully terminate the MCP server subprocess.

        Returns True if shutdown succeeded, False otherwise.
        """
        ...

    @abstractmethod
    def get_tools(self) -> list[dict]:
        """Return the list of available tools exposed by this MCP server.

        Each tool is a dict with at least:
            {"name": str, "description": str, "inputSchema": dict}
        """
        ...

    @abstractmethod
    def call_tool(self, tool_name: str, params: dict) -> dict:
        """Invoke a tool on this MCP server with the given parameters.

        Returns the tool execution result as a dict.
        """
        ...

    @abstractmethod
    def get_health(self) -> dict:
        """Return health status information for this server.

        Expected keys: {"status": str, "latency_ms": int, "error": str | None}
        """
        ...
