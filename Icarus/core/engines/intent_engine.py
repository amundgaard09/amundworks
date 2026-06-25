"""
The `ICARUS` Complex Intent Engine

This file contains dependencies for ICARUS linked to figuring out what and how to do tasks.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

import re as regex

from durapy import uniCLI
from core.mcp.types import MCPTool
from difflib import SequenceMatcher
from core.types import Query, ToolCall
from core.mcp.mcp_server import build_registry
from core.utilities.decorators import logger

class IntentEngine:
    """IntentEngine class for the ICARUS Complex. 
    
    This class unifies all resources that the Intent Engine provides, such as MCP services, query processing, and more."""
    @logger
    def __init__(self, debug: bool) -> None:
        """Initialization logic for the Intent Engine."""
        if debug: uniCLI.console_print("ICARUS", "blue", "Initializing Icarus Intent Engine...", "white")
 
        self.tools = build_registry()
    
        if debug: uniCLI.console_print("ICARUS", "blue", "Success!", "green")
    
    @staticmethod
    def normalize(query: Query) -> Query:
        return Query(
            text=query.text.strip().lower(),
            emotions=query.emotions
        )

    @staticmethod
    def is_chat_like(text: str) -> bool: 
        CHAT_SEEDS = ["hello", "hi", "hey", "what's up", "how are you"]
        return any(seed in text.lower() for seed in CHAT_SEEDS)

    @logger
    def select_tool(self, query: Query) -> tuple[MCPTool, float]:
        """Select a tool from the `TOOL_REGISTRY` that matches the query best."""
    
        # Initialization
        best_tool: MCPTool = None
        best_score: float = 0.0

        # Iterate over all tools in the registry
        for tool in self.tools.values():
            score = 0

            # Iterate over tool aliases
            for alias in tool.aliases:
                if alias in query.text:
                    score += 1
                
                else:
                    score += SequenceMatcher(None, alias, query.text).ratio() * 0.3

            score = score / max(len(tool.aliases), 1)

            # Replace the best tool with the current if it outperforms the previous best one
            if score > best_score:
                best_score = score
                best_tool = tool
    
        # Fallbacks to either local fallback skill or ChatGPT API
        if best_tool is None:
            return self.tools["fallback"], 0.0
    
        if best_score < 0.25:
            if self.is_chat_like(query.text):
                return self.tools["chat"], 1.0
            return self.tools["fallback"], 0.0
        return best_tool, best_score

    def extract_args(self, query: Query, tool: MCPTool) -> dict:
        args = {}
    
        if tool.input_schema is None:
            return None

        for prop in tool.input_schema.properties:
            name = prop.name

            # Simple number extraction
            if prop.dtype == list[int] or prop.dtype == list:
                nums = regex.findall(r"\d+", query.text)
                if nums:
                    args[name] = list(map(int, nums))

            # Fallback: raw text
            elif prop.dtype == str:
                args[name] = query.text

        return args

    @logger
    def process(self, query: Query) -> ToolCall:
        """Processes a Query and returns a `ToolCall`"""
    
        query = self.normalize(query)
        best_tool, best_score = self.select_tool(query)
        args = self.extract_args(query, best_tool)

        return ToolCall(
            tool_name=best_tool.name,
            arguments=args,
            confidence=best_score,
            source_text=query.text
        )