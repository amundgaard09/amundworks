"""
The `ICARUS` Complex Intent Engine

This file contains dependencies for ICARUS linked to figuring out what and how to do tasks.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

import re as regex, os, dotenv

from openai import OpenAI
from durapy import uniCLI
from core.mcp.types import MCPTool
from difflib import SequenceMatcher
from core.types import Query, ToolCall
from core.mcp.mcp_server import build_registry
from core.utilities.decorators import logger

@logger
def initialize_intent(debug: bool) -> None:
    """Placeholder for future init logic for the Intent Engine."""
    global TOOL_REGISTRY
    
    if debug: uniCLI.console_print("ICARUS", "blue", "Initializing Icarus Intent Engine...", "white")
    
    TOOL_REGISTRY = build_registry()
    
    if debug: uniCLI.console_print("ICARUS", "blue", "Success!", "green")

def normalize(query: Query) -> Query:
    return Query(
        text=query.text.strip().lower(),
        emotions=query.emotions
    )

CHAT_SEEDS = ["hello", "hi", "hey", "what's up", "how are you"]

def is_chat_like(text: str) -> bool:
    return any(seed in text.lower() for seed in CHAT_SEEDS)

def select_tool(query: Query) -> tuple[MCPTool, float]:
    best_tool: MCPTool = None
    best_score: float = 0.0
    
    tools = TOOL_REGISTRY

    for tool in tools.values():
        score = 0

        for alias in tool.aliases:
            if alias in query.text:
                score += 1
            else:
                score += SequenceMatcher(None, alias, query.text).ratio() * 0.3

        score = score / max(len(tool.aliases), 1)

        if score > best_score:
            best_score = score
            best_tool = tool
            
    if best_tool is None:
        return TOOL_REGISTRY["fallback"], 0.0
    
    if best_score < 0.25:
        if is_chat_like(query.text):
            return TOOL_REGISTRY["chat"], 1.0
        return TOOL_REGISTRY["fallback"], 0.0
    return best_tool, best_score

def extract_args(query: Query, tool: MCPTool) -> dict:
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
def process(query: Query) -> ToolCall:
    """Processes a Query and returns a `ToolCall`"""
    
    query = normalize(query)
    best_tool, best_score = select_tool(query)
    args = extract_args(query, best_tool)

    return ToolCall(
        tool_name=best_tool.name,
        arguments=args,
        confidence=best_score,
        source_text=query.text
    )