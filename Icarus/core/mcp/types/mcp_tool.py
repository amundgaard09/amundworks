
from pathlib import Path
from typing import Callable
from core.mcp.types.input_schema import InputSchema
from dataclasses import dataclass

@dataclass
class MCPTool:
    name: str
    desc: str
    aliases: list[str]
    path: Path
    execute: Callable
    input_schema: InputSchema
    
    