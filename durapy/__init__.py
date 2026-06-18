"""
The DuraPy STEM Python Package from Durendal Engineering.

DuraPy is the complete collection of all open-source Python projects from Durendal. 
"""

from .src.unialgo import unialgo
from .src.uniCLI import uniCLI
from .src.unicogni import unicogni
from .src.unicrypt import unicrypt
from .src.uniflight import uniflight
from .src.unipower import unipower
from .src.unispace import unispace
from .src.univiz import univiz

from .src.unimath import (coordinate_sys, linalg_dtypes, unimath)
from .src.uniops import (conpidcon, forward_kinematics, inverse_kinematics)
from .src.uniphys.phys_dtypes import (Unit, UNITS, PhysicalConstant, Quantity)
from .src.uniphys import (
    acoustics, 
    astrophys, 
    electromags, 
    fluidyn, 
    mechanics, 
    nuclear, 
    quantum,
    thermodyn,
)

from .src.commons import exceptions, constants
from .src.frameworks.color_sys import (
    RGB, 
    CMYK, 
    HEX, 
    color_text
)

__all__ = ["src"]
__version__ = "0.0.1.7"
