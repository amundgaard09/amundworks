"""
The `DuraPy` `Exceptions` module.

This module contains all the custom exceptions used in the `DuraPy` library.
"""

from ..frameworks.color_sys import color_text
from typing import Callable

class ImpossibleTriangleError(Exception):
    """Raise when the sum of the angles of a triangle is not 180 degrees, a mathematical impossibility."""
    def __init__(self):
        super().__init__("The sum of the angles of a triangle can't be anything else than 180 degrees!")
class IncorrectArgumentCount(Exception):
    """Raises when the count of arguments given to a function is incorrect."""
    def __init__(self, func: Callable, given_args: int, wanted_args: set):
        super().__init__(f"Incorrect count of arguments for {color_text(func.__name__, 'blue')}. {color_text(func.__name__, 'blue')} takes {color_text(wanted_args, 'green')} but was given {color_text(given_args, 'red')}")
class InconsistencyError(Exception):
    """Raises when the VIR-values passed into PowerDissipation() gives inconsistent values for the three formulas."""
    def __init__(self, func: Callable, fault: str):
        super().__init__(f"Inconsistency error at {color_text(func.__name__, 'blue')} with {color_text(fault, 'red')}")
class DimensionMismatch(Exception):
    """Raise when the dimensions of two units don't match when trying to convert or perform operations on them."""
    def __init__(self, *args):
        super().__init__(*args)
class InvalidColorCount(Exception):
    """Raised when the color count passed into a function of the resistor group is invalid."""
    def __init__(self, func: Callable):
        super().__init__(f"Invalid Color Count for {color_text(func.__name__, 'blue')}")
class UnknownSubCommand(Exception):
    """Raises when an unknown subcommand gets caught in ValidateCommand()."""
    def __init__(self, module: str, given_command: str):
        super().__init__(f"Unknown command for {module}: {color_text(given_command, 'red')}")
class MissingSubCommand(Exception):
    """Raises when the subcommand is missing from a command string."""
    def __init__(self, module):
        super().__init__(f"Missing subcommand for {module}")
class MissingParameters(Exception):
    """Raises when a function is not given enough / too many parameters."""
    def __init__(self, *args):
        super().__init__(*args)
class EmptyTokenList(Exception):
    """Raises when the TokenList passed into ValidateCommand() is empty."""
    def __init__(self):
        super().__init__("Empty TokenList! Make sure of correct tokens before verification attempt.")
class InvalidColors(Exception):
    """Raises when the colors passed into ResistorInsight() are invalid for the given band."""
    def __init__(self, func: Callable, invalid_colors_indices: int):
        super().__init__(f"Invalid colors for {color_text(func.__name__, 'blue')} at indices {invalid_colors_indices}")
class UnknownModule(Exception):
    """Raises when an unknown module gets caught in ValidateCommand()."""
    def __init__(self, given_module: str):
        super().__init__(f"Unknown Module: {color_text(given_module, 'red')}")
class InvalidInput(Exception):
    """Raises when an invalid input gets caught, e.g. a str for a wanted float."""
    def __init__(self, wanted_type: type, given_type: type):
        super().__init__(f"Invalid Input: Wanted Type: {color_text(wanted_type, 'green')} Given Type: {color_text(given_type, 'red')}")
