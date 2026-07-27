"""
The `ICARUS` Complex Intent Engine

This file contains dependencies for ICARUS linked to figuring out what and how to do tasks.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from difflib import SequenceMatcher
from re import findall

from durapy.durapy.uniCLI.uniCLI import Console

from src.mcp.mcp_server import MCPServer
from src.mcp.types import MCPTool
from src.types import Query, ToolCall

from ..shared.decorators import runtime_log


class IntentEngine:
    @runtime_log
    def __init__(self, console: Console, server: MCPServer) -> None:
        """
        IntentEngine class for the ICARUS Complex.

        This class unifies all resources that the Intent Engine provides, such as MCP services, query processing, and more.
        """

        console.start_task("Starting IntentEngine")

        self.server = server
        self.tools = self.server.build_registry()

        console.end_task("Starting IntentEngine", success=True)

    def __repr__(self) -> str:
        return "IntentEngine()"

    @staticmethod
    def normalize(query: Query) -> Query:
        return Query(text=query.text.strip().lower(), emotions=query.emotions)

    @staticmethod
    def is_chat_like(text: str) -> bool:
        CHAT_SEEDS = ["hello", "hi", "hey", "what's up", "how are you"]
        return any(seed in text.lower() for seed in CHAT_SEEDS)

    @runtime_log
    def select_tool(self, query: Query) -> tuple[MCPTool, float]:
        """Select a tool from the `TOOL_REGISTRY` that matches the query best."""

        # Initialization
        best_tool: MCPTool | None = None
        best_score: float = 0.0

        # Iterate over all tools in the registry
        for tool in self.tools.values():
            score = 0

            # Iterate over tool aliases
            for alias in tool.aliases:
                if alias in query.text:
                    score += 1

                # Fuzzy matching for aliases
                else:
                    score += SequenceMatcher(None, alias, query.text).ratio() * 0.3

            # Normalize score by the number of aliases to avoid bias towards tools with more aliases
            score = score / max(len(tool.aliases), 1)

            # Replace the best tool with the current if it outperforms the previous best one
            if score > best_score:
                best_score = score
                best_tool = tool

        # No tool fallback
        if best_tool is None:
            return self.tools["fallback"], 0.0

        # ChatGPT and poor confidence fallbacks
        if best_score < 0.25:
            if self.is_chat_like(query.text):
                return self.tools["chat"], 1.0
            return self.tools["fallback"], 0.0
        return best_tool, best_score

    def extract_args(self, query: Query, tool: MCPTool) -> dict:
        """Extract arguments for a tool based on its `InputSchema`"""
        args = {}

        if tool.input_schema is None:
            return None

        for prop in tool.input_schema.properties:
            name = prop.name

            # Simple number extraction
            if prop.dtype == list[int] or prop.dtype == list:
                nums = findall(r"\d+", query.text)
                if nums:
                    args[name] = list(map(int, nums))

            # Fallback: raw text
            elif prop.dtype == str:
                args[name] = query.text

        return args

    @runtime_log
    def process(self, query: Query) -> ToolCall:
        """Process a Query and return a `ToolCall`"""

        query = self.normalize(query)
        best_tool, best_score = self.select_tool(query)
        args = self.extract_args(query, best_tool)

        return ToolCall(
            tool_name=best_tool.name,
            arguments=args,
            confidence=best_score,
            source_text=query.text,
        )
