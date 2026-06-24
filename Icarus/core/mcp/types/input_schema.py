
from core.mcp.types.mcp_property import MCPProperty
from dataclasses import dataclass

@dataclass
class InputSchema:
    properties: list[MCPProperty]
