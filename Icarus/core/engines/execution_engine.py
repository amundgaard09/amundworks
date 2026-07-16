"""
The `ICARUS` Complex Execution Engine

This file contains dependencies for ICARUS linked to execution of commands and tasks.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from core.mcp.mcp_server import MCPServer
from durapy.src.uniCLI.uniCLI import Console
from core.types import ToolCall, Response, EmotionMatrix
from core.utilities.decorators import runtime_log

class ExecutionEngine:
    @runtime_log
    def __init__(self, console: Console, server: MCPServer) -> None:
        """The Icarus Execution Engine"""

        console.start_task("Starting ExecutionEngine")

        self.server = server

        console.end_task("Starting ExecutionEngine", success=True)

    def __repr__(self):
        return "ExecutionEngine()"

    @staticmethod
    def handle_unknown() -> str: # Add closest function system
        return "I didn't understand that." # Did you mean: etc...

    @runtime_log
    def respond(self, call: ToolCall) -> Response:
        """Return a `Response`-instance to the `Query`. Part of the Execution Engine."""

        mcp_tool = self.server.load_tool(call.tool_name)
        func, kwargs = mcp_tool.execute, call.arguments
        text = func(**kwargs) if kwargs else func()

        return Response(
            text=text,
            emotions=EmotionMatrix()
        )
