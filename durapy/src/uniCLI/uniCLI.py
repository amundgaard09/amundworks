"""
The `DuraPy` `UniCLI` module. 
This module contains the standard command-line interface framework from the `DuraPy` library. 
It provides the necessary functions and classes to create a command-line interface for the `DuraPy` library, 
including command parsing, argument validation, and command dispatching.
"""

from typing import Callable
from prompt_toolkit.completion import NestedCompleter
from ..frameworks.color_sys import color_text
from ..commons import exceptions
 
import os, shlex, inspect, subprocess

class ExitEnvironmentSignal(Exception):
    """Raise when the user wants to return to MAINEnv."""
    def __init__(self):
        super().__init__()
        
class CommandMap:
    def __init__(self):
        pass

class ArgumentMap:
    def __init__(self):
        pass
        
def exit_env() -> None:
    """Exit the current environment and return to MAINEnv."""
    raise ExitEnvironmentSignal

def generate_completer(Map: dict[str, dict]) -> NestedCompleter:
    """Generate a `NestedCompleter` dict with parameter names for each function."""
    
    completer_dict = {}
    
    for module, subcmd in Map.items():
        completer_dict[module] = {}
        for subcmd_name, cmd_func in subcmd.items():
            sig = inspect.signature(cmd_func)
            completer_dict[module][subcmd_name] = {param: None for param in sig.parameters}
    
    return NestedCompleter.from_nested_dict(completer_dict)
def tokenize(raw_cmd_str: str) -> list[str]:
    """Tokenize a raw command string and return token list."""
    tokens = shlex.split(raw_cmd_str)
    proc_tokens = [] # Processed tokens
    for token in tokens:
        if token.startswith("[") and token.endswith("]"):
            proc_val = [float(x.strip()) for x in token.strip("[]").split(",") if x.strip()]
            proc_tokens.append(proc_val)
        else:
            proc_tokens.append(token)
    return proc_tokens

def dispatcher(raw_cmd_str: str, cmd_map: dict[str, dict[str, Callable]], arg_map: dict[str, dict[str, set]]) -> Callable:
    """The main dispatcher function that takes in a raw command string, tokenizes it, verifies the tokens, validates the arguments and dispatches the command to the correct function."""
    tokens = tokenize(raw_cmd_str) 
    validate_command(tokens, cmd_map, arg_map)
    module, cmd, raw_args = tokens[0], tokens[1], tokens[2:]
    args = []
    for arg in raw_args:
        if arg == "_":
            args.append(None)
        else:
            try:
                args.append(float(arg))
            except ValueError:
                args.append(arg)
            
    return cmd_map[module][cmd](*args)

def validate_command(tokens: list, cmd_map: dict, arg_map: dict) -> None:
    if not tokens:
        raise exceptions.EmptyTokenList

    module = tokens[0]
    if module not in cmd_map:
        raise exceptions.UnknownModule(module)

    if len(tokens) < 2:
        raise exceptions.MissingSubCommand(module)

    command = tokens[1]
    if command not in cmd_map[module]:
        raise exceptions.UnknownSubCommand(module, command)

    args = tokens[2:]
    if len(args) not in arg_map[module][command]:
        raise exceptions.IncorrectArgumentCount(cmd_map[module][command], len(args), arg_map[module][command])

def clear_terminal() -> None:
    try: subprocess.check_output('cls' if os.name == 'nt' else 'clear')
    except subprocess.CalledProcessError: pass

def console_msg(sender: str, sender_color: str, info: str, info_color: str = "white") -> str:
    return f"[{color_text(sender, sender_color)}] >>> {color_text(info, info_color)}"

def console_print(sender: str, sender_color: str, info: str, info_color: str = "white") -> None:
    print(console_msg(sender, sender_color, info, info_color))

def console_input(sender: str, sender_color: str, prompt: str = "", prompt_color: str = "white") -> str | float:
    user_input = input(console_msg(sender, sender_color, prompt, prompt_color) + " ")
    try:               return float(user_input)
    except ValueError: return user_input

def console_confirm(sender: str, sender_color: str, prompt_info: str, prompt_color: str = "white") -> bool:
    while True:
        user_input = input(console_msg(sender, sender_color, prompt_info + ":", prompt_color) + " ").lower().strip()
        if user_input in ["y", "ye", "yes"]:
            return True
        elif user_input in ["n", "no"]:
            return False
        else:
            print(f"Please enter {color_text('y', 'green')} or {color_text('n', 'red')}")
