"""DuraPy package entrypoint."""

from .src.shared import constants, exceptions
from .src.shared.color_sys import CMYK, HEX, RGB, color_text
from .src.shared.numval_types import Constant, Quantity, Unit, Dimension

from .src.uniCLI import uniCLI
from .src.unicogni import unicogni
from .src.unicrypt import unicrypt
from .src.uniflight import uniflight
from .src.unipower import unipower
from .src.unimath import coordinate_systems, linalg_dtypes, algebra, geometry, unimath
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

__all__ = [
    "uniCLI",
    "unicogni",
    "unicrypt",
    "uniflight",
    "unipower",
    "Constant",
    "Quantity",
    "Unit",
    "Dimension",

    "constants",
    "exceptions",

    "RGB",
    "CMYK",
    "HEX",
    "color_text",

    "coordinate_systems",
    "linalg_dtypes",
    "algebra",
    "geometry",
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
]

__version__ = "0.0.1.9"
