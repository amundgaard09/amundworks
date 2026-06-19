
import os, json
from pathlib import Path
from core.mcp.types.mcptool import MCPTool
from core.mcp.types.input_schema import InputSchema
from core.utilities.decorators import logger

_SKILLS_DIR = Path(__file__).parents[2].resolve() / "skills"

# Depecrate?

@logger
def create_input_schema() -> InputSchema:
    """Create a new MCPTool instance from a skill."""

@logger
def get_tools() -> list[MCPTool]:
    """Iterates through the skills directory and creates a list of MCPTools"""
    
    tools: list[MCPTool] = []
    
    for folder in os.listdir(_SKILLS_DIR):
        config_path = os.path.join(_SKILLS_DIR, folder, "config.json")
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                config = dict(json.load(f))
            
            new_tool = MCPTool(
                name="",
                desc="",
                path=Path(os.path.join(_SKILLS_DIR, folder)),
                config=config,
                input_schema={}
            )
            tools.append(new_tool)
    
    return tools
            