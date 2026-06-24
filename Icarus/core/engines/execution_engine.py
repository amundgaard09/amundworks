"""
The `ICARUS` Complex Execution Engine

This file contains dependencies for ICARUS linked to execution of commands and tasks.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from durapy import uniCLI
from core.types import Response, ToolCall, EmotionMatrix
from core.mcp.mcp_server import load_tool, TOOL_DIR

def handle_unknown() -> str: # Add closest function system
    return "I didn't understand that." # Did you mean: etc...

def respond(call: ToolCall) -> Response:
    """Return a `Response`-instance to the `Query`. Part of the Execution Engine."""
    
    mcp_tool = load_tool(TOOL_DIR / call.tool_name)
    func, kwargs = mcp_tool.execute, call.arguments
    text = func(**kwargs) if kwargs else func()
    
    return Response(
        text=text,
        emotions=EmotionMatrix()
    )
    
def initialize_execution(debug: bool) -> None:
    """Placeholder for future init logic for the Execution Engine."""
    if debug: 
        uniCLI.console_print("ICARUS", "blue", "Initializing Icarus Execution Engine...", "white")
        uniCLI.console_print("ICARUS", "blue", "Success!", "green")
