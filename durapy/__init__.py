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

from .src.shared import constants, exceptions, color_system, numval_types, units

from .src import (
    uniCLI,
    unicogni,
    unicrypt,
    uniflight,
    unimath,
    uniops,
    uniphys,
    unipower,
)

__all__ = [
    "color_system",
    "constants",
    "exceptions",
    "numval_types",
    "units",

    "uniCLI",
    "unicogni",
    "unicrypt",
    "uniflight",
    "unimath",
    "uniops",
    "uniphys",
    "unipower",
]

__version__ = "1.0.0.3"
