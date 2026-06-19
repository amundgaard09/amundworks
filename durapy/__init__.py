"""
The DuraPy Package from Durendal Engineering.

DuraPy is the complete collection of all open-source Python projects from Durendal. 

Packages:
---------
-  `UniAlgo` (Algorithms)
-  `UniCLI` (CLI Frameworks and Tools)
-  `UniCogni` (AI, ML, etc)
-  `UniCrypt` (Encryption and Decryption tools)
-  `UniFlight` (Aerospace)
-  `UniPower` (Electrical and Electronics Engineering)
-  `UniSpace` (Spaceflight)
-  `UniViz` (Data visualization)
---
- Exceptions
- Constants
---
- `UniMath` (Mathematics)
    - Coordinate Systems
    - Linear Algebra Data Types
    - UniMath Core Package
--- 
- `UniOps` (Robotics/Mechatronics Operations and Control)
    - Continuous PID Controller (conpidcon)
    - Forward Kinematics
    - Inverse Kinematics
--- 
- `UniPhys` (Physics)
    - Acoustics
    - Astrophysics
    - Electromagnetics
    - Fluid Dynamics
    - Mechanics
    - Nuclear
    - Quantum
    - Thermodynamics
    - Physics Data Types
        - `Unit`, `PhysicalConstant`, `Quantity`\n
---
- Frameworks
    - Color Systems
        - `RGB`, `HEX`, `CMYK`
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
    astrophysics,
    electromagnetics,
    fluid_dynamics, 
    mechanics, 
    nuclear, 
    quantum,
    thermodynamics,
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
