"""DuraPy package entrypoint."""

from .src.uniCLI import uniCLI
from .src.unicogni import unicogni
from .src.unicrypt import unicrypt
from .src.uniflight import uniflight
from .src.unipower import unipower
from .src.commons import constants, exceptions
from .src.frameworks.color_sys import CMYK, HEX, RGB, color_text
from .src.unimath import coordinate_sys, linalg_dtypes, unimath
from .src.uniops import conpidcon, forward_kinematics, inverse_kinematics
from .src.uniphys import (
    acoustics,
    astrophysics,
    electromagnetics,
    fluid_dynamics,
    mechanics,
    nuclear,
    quantum,
    thermodynamics,
)
from .src.frameworks.phys_dtypes import Constant, Quantity, UNITS, Unit # Change when quantity, constant, complexconstant, etc. systems are refactored
__all__ = [
    "uniCLI",
    "unicogni",
    "unicrypt",
    "uniflight",
    "unipower",
    "constants",
    "exceptions",
    "RGB",
    "CMYK",
    "HEX",
    "color_text",
    "coordinate_sys",
    "linalg_dtypes",
    "unimath",
    "conpidcon",
    "forward_kinematics",
    "inverse_kinematics",
    "acoustics",
    "astrophysics",
    "electromagnetics",
    "fluid_dynamics",
    "mechanics",
    "nuclear",
    "quantum",
    "thermodynamics",
    "Constant",
    "Quantity",
    "UNITS",
    "Unit",
]

__version__ = "0.0.1.8"
