"""
The Classical Mechanics module for `AWPC` `UniPhys`

This module contains resources for calculations and simulations for Classical Mechanics. 
"""

from ..frameworks.color_sys import color_text
from .phys_dtypes import Quantity, UNITS
from ..commons.constants import EARTH_G, PI, C 

import math

def torque(moment_arm_distance: float, force: float) -> Quantity:
    """Returns a `torque` quantity in newtonmeters from moment arm distance in meters and force in newtons."""
    return Quantity((moment_arm_distance * force), UNITS["Nm"])
def gear_ratio(driving_teeth: int, driven_teeth: int) -> str:
    """Returns the gear ratio from the driving gear's teeth count and the driven gear's teeth count."""
    ratio = driven_teeth / driving_teeth
    if ratio > 1:
        return f"{ratio} - {color_text('Speed-', 'red')} - {color_text('Torque+', 'green')}"
    elif ratio < 1:
        return f"{ratio} - {color_text('Speed+', 'green')} - {color_text('Torque-', 'red')}"
    else:
        return f"{ratio} - Same Speed - Same Torque"

def angular_velocity_r(RPM: float) -> Quantity:
    """Returns angular velocity from RPM in radians/s"""
    return Quantity((RPM * PI / 30), UNITS["rad"])
def angular_velocity_d(RPM: float) -> Quantity:
    """Returns angular velocity from RPM in degrees/s"""
    return Quantity(math.radians((RPM * PI / 30)), UNITS["deg"])

def kinetic_energy(mass: float, vel: float) -> Quantity:
    """Returns the kinetic energy from mass in kgs and velocity in m/s"""
    return Quantity((0.5 * mass * vel**2), UNITS["J"])
def potential_energy(mass: float, height: float, g: float | None = EARTH_G._value) -> Quantity:
    """Returns the potential energy of a mass. Gravity is defaulted to 9.8m /s^2"""
    return Quantity(mass * g * height, UNITS["J"])

def einstein_mass_energy_equivalence(mass: float) -> Quantity:
    return Quantity((mass * C * C), UNITS["J"])

