"""
The `ICARUS` Complex Execution Engine

This file contains dependencies for ICARUS linked to execution of commands and tasks.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from durapy import uniCLI
from core.mcp.types import MCPTool
from core.mcp.mcp_server import MCPServer
from core.types import ToolCall, Response, EmotionMatrix
from core.utilities.decorators import runtime_log

class ExecutionEngine:
    """The Icarus Execution Engine"""
    @runtime_log
    def __init__(self, debug: bool = False):
        if debug: uniCLI.console_print("ICARUS", "blue", "Initializing Icarus Execution Engine...", "white")
        
        
        
        if debug: uniCLI.console_print("ICARUS", "blue", "Success!", "green")

    @staticmethod
    def handle_unknown() -> str: # Add closest function system
        return "I didn't understand that." # Did you mean: etc...

    @runtime_log
    def respond(self, call: ToolCall) -> Response:
        """Return a `Response`-instance to the `Query`. Part of the Execution Engine."""
    
        mcp_tool = MCPServer().load_tool(call.tool_name)
        func, kwargs = mcp_tool.execute, call.arguments
        text = func(**kwargs) if kwargs else func()
    
        return Response(
            text=text,
            emotions=EmotionMatrix()
        )

    
