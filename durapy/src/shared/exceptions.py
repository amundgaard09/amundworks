"""
The `DuraPy` `Exceptions` module.

This module contains all the custom exceptions used in the `DuraPy` library.
"""

from ..shared.color_sys import color_text
from typing import Callable

### MISCELLANEOUS ###

class DimensionMismatch(Exception):
    """Raise when the dimensions of two units don't match when trying to convert or perform operations on them."""
    def __init__(self, *args):
        super().__init__(*args)

class ImpossibleTriangleError(Exception):
    """Raise when the sum of the angles of a triangle is not 180 degrees, a mathematical impossibility."""
    def __init__(self, *args):
        super().__init__("The sum of the angles of a triangle can't be anything else than 180 degrees!", args)

class ArgumentError(Exception):
    """Error raised when the count of arguments given to a function is incorrect."""
    def __init__(self, *args):
        super().__init__(*args)

class InvalidColors(Exception):
    """Raises when the colors passed into resistor_insight() are invalid for the given band."""
    def __init__(self, func: Callable, *args):
        super().__init__(f"Invalid colors for {color_text(func.__name__, 'blue')} at indices {args}")

### UNICLI ###

class UnknownModule(Exception):
    """UniCLI Unknown Command Module"""
    def __init__(self, given_module: str):
        super().__init__(f"Unknown Module: {color_text(given_module, 'red')}")

class UnknownSubCommand(Exception):
    """Raises when an unknown subcommand gets caught in validate_command()."""
    def __init__(self, module: str, given_command: str):
        super().__init__(f"Unknown command for {module}: {color_text(given_command, 'red')}")

class MissingSubCommand(Exception):
    """Raises when the subcommand is missing from a command string."""
    def __init__(self, module):
        super().__init__(f"Missing subcommand for {module}")

class EmptyTokenList(Exception):
    """Raises when the TokenList passed into validate_command() is empty."""
    def __init__(self):
        super().__init__("Empty TokenList! Make sure of correct tokens before verification attempt.")

### SPECIALIZED EXCEPTIONS ###

class InconsistencyError(Exception):
    """Raises when the VIR-values passed into power_dissipation() gives inconsistent values for the three formulas."""
    def __init__(self, func: Callable, fault: str):
        super().__init__(f"Inconsistency error at {color_text(func.__name__, 'blue')} with {color_text(fault, 'red')}")
