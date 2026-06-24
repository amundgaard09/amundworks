
import os, json, importlib.util

from pathlib import Path
from types import ModuleType
from core.mcp.types import MCPTool, InputSchema, MCPProperty
from core.utilities.decorators import logger
from core.utilities.exceptions import MissingFileError, SkillLoadError

TOOL_DIR = Path(__file__).parents[2].resolve() / "skills"

def is_dunder(string: str) -> bool:
    return string.strip().startswith("__") and string.strip().endswith("__")

@logger
def load_executable(skill_path: Path) -> ModuleType:
    """
    Loads a Python file from the tool path and returns its module (python source file).
    
    Args
    ----
        skill_path (Path): The path to the skill folder
        
    Returns
    -------
        module (ModuleType): The python file represented as an object.
    """
    py_path = skill_path / "execute.py"
    
    if not py_path.exists():
        raise MissingFileError(py_path)

    modspec = importlib.util.spec_from_file_location(
        "skill_module",
        py_path
    )

    module = importlib.util.module_from_spec(modspec)
    modspec.loader.exec_module(module)
    
    # Check module executability
    if not hasattr(module, "execute"):
        raise SkillLoadError(f"Module {module} is missing attribute 'execute'")
       
    return module

def build_input_schema(schema_dict: dict[str, dict]) -> InputSchema:
    if schema_dict is None:
        return None
    
    props = []

    for name, meta in schema_dict.items():
        props.append(
            MCPProperty(
                name=name,
                type=meta["type"],
                required=meta.get("required", True)
            )
        )

    return InputSchema(properties=props)

def load_tool(tool_path: Path) -> MCPTool:
    with open(tool_path / "config.json") as f:
        config = dict(json.load(f))

    module = load_executable(tool_path)
    input_schema = config["input_schema"]

    return MCPTool(
        name=config["name"],
        desc=config["description"],
        aliases=config["aliases"],
        input_schema=build_input_schema(input_schema),
        execute=module.execute,
        path=tool_path
    )

@logger
def build_registry(tool_directory: Path = TOOL_DIR) -> dict[str, MCPTool]:
    """
    Build the MCP tool registry for Intent + Execution engines

    Args
    ----
        **tool_directory**: `Path`
        The path to the tool directory. Defaults to `TOOL_DIR`

    Raises
    ------
        `MissingFileError`: Raises of the skill directory path is missing

    Returns
    -------
        dict[str, MCPTool]: The tool registry
    """
    if not tool_directory.exists():
        raise MissingFileError(tool_directory)
    
    # Initialize registry
    tool_registry: dict[str, MCPTool] = {}
    
    # Iterate over all entities in the skill directory
    for tool_path in tool_directory.iterdir():
        
        # Check if the given skill path actually points to a skill
        if not tool_path.is_dir() or is_dunder(tool_path.name):
            continue
        
        # Load tool
        tool = load_tool(tool_path)
        
        # Add to registry
        tool_registry[tool.name] = tool
        
    return tool_registry



            