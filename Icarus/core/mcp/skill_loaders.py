
import importlib.util, json
from pathlib import Path
from core.utilities.decorators import logger

@logger
def get_py_skill_and_triggers(skill_folder_path: Path):
    """Loads a Python Skill and returns its module (python source file) and its text triggers."""
    py_path = skill_folder_path / "execute.py"
    json_path = skill_folder_path / "config.json"

    modspec = importlib.util.spec_from_file_location(
        "skill_module",
        py_path
    )

    module = importlib.util.module_from_spec(modspec)
    modspec.loader.exec_module(module)
    
    with open(json_path, mode="r", encoding="utf-8") as f:
        jsondict: dict = json.load(f)
   
    triggers = jsondict.get("triggers", None)

    return module, triggers

@logger
def get_py_skill_and_tokens(skill_folder_path: Path):
    """Loads a Python Skill and returns its module (python source file) and its text tokens, used for score-based intent routing."""
    py_path = skill_folder_path / "execute.py"
    json_path = skill_folder_path / "config.json"

    modspec = importlib.util.spec_from_file_location(
        "skill_module",
        py_path
    )

    module = importlib.util.module_from_spec(modspec)
    modspec.loader.exec_module(module)
    
    with open(json_path, mode="r", encoding="utf-8") as f:
        jsondict: dict = json.load(f)
   
    tokens = jsondict.get("tokens", None)

    return module, tokens
