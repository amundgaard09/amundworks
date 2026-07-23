
import json
import importlib.util

from pathlib import Path
from durapy.src.uniCLI import Console
from types import ModuleType
from .types import MCPTool, InputSchema, MCPProperty
from ..shared.exceptions import MissingFileError, SkillLoadError
from ..shared.decorators import runtime_log

def is_dunder(string: str) -> bool:
    return string.strip().startswith("__") and string.strip().endswith("__")

class MCPServer:
    def __init__(self, console: Console) -> None:
        """Initialize the MCP Server"""
        console.start_task("Starting MCP Server")

        self.TOOL_DIR_PATH = Path(__file__).parents[2].resolve() / "skills"

        if not self.TOOL_DIR_PATH.exists():
            raise MissingFileError(self.TOOL_DIR_PATH)

        console.end_task("Starting MCP Server", success=True)

    def __repr__(self):
        return "MCPServer()"

    @staticmethod
    @runtime_log
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

        if modspec is None:
            raise SkillLoadError(f"Failed to load module spec for {py_path}")

        module = importlib.util.module_from_spec(modspec)
        modspec.loader.exec_module(module)

        # Check module executability
        if not hasattr(module, "execute"):
            raise SkillLoadError(f"Module {module} is missing attribute 'execute'")

        return module

    @runtime_log
    def build_input_schema(self, schema_dict: dict[str, dict] | None) -> InputSchema | None:
        """
        Build input schema, consisting of a list of `MCPProperty` objects.

        Args:
            schema_dict (dict[str, dict]): Dict representation of the InputSchema from JSON.

        Returns:
            InputSchema: InputSchema object.
        """
        if schema_dict is None:
            return None

        properties: list[MCPProperty] = []

        for name, meta in schema_dict.items():
            properties.append(
                MCPProperty(
                    name=name,
                    dtype=meta["type"],
                    required=meta.get("required", True)
                )
            )

        return InputSchema(properties=properties)

    @runtime_log
    def load_tool(self, tool_name: str) -> MCPTool:
        """
        Load a tool from the tool directory.

        Args:
            tool_path (Path): The `Path` to the tool folder

        Raises:
            MissingFileError: If files related to the tool are missing, raise MisingFileError

        Returns:
            MCPTool: MCPTool object describing the tool
        """

        tool_path = self.TOOL_DIR_PATH / tool_name

        if not tool_path.exists():
            raise MissingFileError(f"Unknown tool: {tool_name}")

        try:
            with open(tool_path / "config.json") as f:
                config = dict(json.load(f))
        except FileNotFoundError:
            uniCLI.console_print("MCP SERVER", "green", f"ERROR: {tool_path.name} config file not found.")
            raise MissingFileError(tool_path.name)

        schema_dict = config["input_schema"]
        input_schema = self.build_input_schema(schema_dict)
        module = self.load_executable(tool_path)

        return MCPTool(
            name=config["name"],
            desc=config["description"],
            aliases=config["aliases"],
            input_schema=input_schema,
            execute=module.execute,
            path=tool_path
        )

    @runtime_log
    def build_registry(self) -> dict[str, MCPTool]:
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

        # Initialize registry
        tool_registry: dict[str, MCPTool] = {}

        # Iterate over all entities in the tool directory
        for tool_path in self.TOOL_DIR_PATH.iterdir():

            # Check if the given skill path actually points to a skill
            if not tool_path.is_dir() or is_dunder(tool_path.name):
                continue

            # Load tool
            tool = self.load_tool(tool_path.name)

            # Add to registry
            tool_registry[tool.name] = tool

        return tool_registry
