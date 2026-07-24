"""DuraPy package entrypoint."""

# Always import the module, not singular functions, classes, etc
# Never use import functionality provided by this init file within the DuraPy library!
# This will create circular import bugs!

# IMPORT RULES:
#
# For single module modules:
# from durapy import "MODULE" -> Module exposes all functionality through its init file.
#
# from durapy import uniCLI; x = uniCLI.TaskConsole()
#
# EXCEPT!
#
# The shared library upimports directly, skipping the module:
#
# from durapy import constants, exceptions, etc

from src import (
    uniCLI,
    unicogni,
    unicrypt,
    uniflight,
    unimath,
    uniops,
    uniphys,
    unipower,
)
from src.shared import color_system, constants, exceptions, numval_types, units

__all__ = [
    "color_system",
    "constants",
    "exceptions",
    "numval_types",
    "uniCLI",
    "unicogni",
    "unicrypt",
    "uniflight",
    "unimath",
    "uniops",
    "uniphys",
    "unipower",
    "units",
]

__version__ = "1.0.0.3"
