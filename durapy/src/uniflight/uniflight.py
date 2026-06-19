"""
The `DuraPy` `UniFlight` module provides a collection of functions and classes for performing calculations and simulations related to flight dynamics, aerodynamics, and propulsion.
"""

from durapy.src.frameworks.color_sys import color_text
from durapy.src.uniphys.phys_dtypes import Quantity, UNITS
from durapy.src.commons.constants import MACH

def T2W_ratio(thrust: float, weight: float) -> str:
    """Thrust to Weight ratio calculator. Ensure consistent units!"""
    ratio = thrust / weight
    return f"Ratio: {color_text(f'{ratio}', 'green' if ratio > 1 else 'red' if ratio != 1 else 'yellow')}" 
def mach_number(vel: float, mach: float | None = MACH) -> str:
    """Mach Number Calulator. Speed of sound is defaulted to 343 m/s. Ensure consistent units!"""
    mach = vel / mach
    label = ('SUBSONIC' if mach < 1 else 'TRANSONIC' if abs(mach - 1) < 0.01 else 'SUPERSONIC' if mach < 5 else 'HYPERSONIC' if mach < 10 else 'HIGH-HYPERSONIC')
    color = ('red'      if mach < 1 else 'yellow'    if mach == 1            else 'green'      if mach < 5 else 'blue'       if mach < 10 else 'violet')
    return f"Ratio: {color_text(f'{mach} - {label}', color)}"
                                
def dynamic_pressure(velocity: float, air_density: float | None = 1.225) -> Quantity:
    return Quantity(0.5 * velocity ** 2 * air_density, UNITS["Pa"])

def lift_drag_equation(coeff: float, dynamic_pressure: float, ref_area: float) -> Quantity:
    return Quantity(coeff * dynamic_pressure * ref_area, UNITS["N"])

