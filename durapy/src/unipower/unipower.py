"""
The UniPower function package for the `DuraPy` library. 
This library contains functions for electrical calculations and simulations. The functions are designed to be easy to use and understand, with clear input and output formats. 
The library is still in development and may contain some unstable functions that are not yet fully tested.
"""

import math

from typing import Literal
from types import MappingProxyType
from durapy.src.unimath.unimath import avg
from durapy.src.frameworks.color_sys import ANSI_COLORS
from durapy.src.uniphys.phys_dtypes import (
    Quantity,
    UNITS
)

from durapy.src.commons.exceptions import (
    MissingParameters, 
    InconsistencyError, 
    InvalidColors
)

BANDS = MappingProxyType({
    "black":  0,
    "brown":  1,
    "red":    2,
    "orange": 3,
    "yellow": 4,
    "green":  5,
    "blue":   6,
    "violet": 7,
    "gray":   8,
    "white":  9,
})
MULTIPLIERS = MappingProxyType({
    "black":  1,
    "brown":  10,
    "red":    1e2,
    "orange": 1e3,
    "yellow": 1e4,
    "green":  1e5,
    "blue":   1e6,
    "violet": 1e7,
    "gray":   1e8,
    "white":  1e9,
    "gold":   0.1,
    "silver": 0.01,
})
TOLERANCES = MappingProxyType({
    "brown":  1,
    "red":    2,
    "green":  0.5,
    "blue":   0.25,
    "violet": 0.1,
    "gray":   0.05,
    "gold":   5,
    "silver": 10,
})

def ohms_law(V: float | None = None, I: float | None = None, R: float | None = None) -> str:
    """
    Ohms Law calculation for Voltage, Current, and Resistivity. \n
    Formulas:
    >>> V = I * R \n
    >>> I = V / R \n 
    >>> R = V / I \n 
    """
    
    if V is not None: V = float(V)
    if I is not None: I = float(I)
    if R is not None: R = float(R)
            
    if (V, I, R).count(None) > 1:
        missing_params = []
        for idx, value in enumerate((V, I, R)):
            if value is None:
                missing_params.append(("V", "I", "R")[idx])
        
        raise MissingParameters(ohms_law, missing_params)
    
    if V is None:
        V = I * R
    elif I is None:
        I = V / R
    elif R is None:
        R = V / I
        
    return f"V: {V}, I: {I}, R: {R}"
def volt_divider(VIn: float, R1: float, R2: float) -> Quantity:
    """Calculates the output voltage of a voltage divider from input voltage and the two resistances."""
    return Quantity((VIn * (R2 / (R1 + R2))), UNITS["V"])
def rc_time_constant(capacitance: float, resistance: float) -> Quantity:
    """Calculates the time constant of an RC circuit from capacitance in farads and resistance in ohms."""
    return Quantity((capacitance * resistance), UNITS["S"])
def inductor_impedance(hertz: float, inductance: float) -> Quantity:
    """Calculates the impedance of an inductor at a given frequency in hertz and inductance in henrys."""
    return Quantity((2 * math.pi * hertz * inductance), UNITS["Ω"])
def power_dissipation(V: float | None = None, I: float | None = None, R: float | None = None) -> Quantity:
    """Calculates power dissipation from voltage, current and resistance. If all three parameters are given, it checks for consistency between the three formulas P = I^2 * R, P = V^2 / R and P = V * I."""
    if (V, I, R).count(None) > 1:
        missing_params = []
        for idx, val in enumerate((V, I, R)):
            if val is None:
                missing_params.append(("V", "I", "R")[idx])
        
        raise MissingParameters(power_dissipation, missing_params)

    if (V, I, R).count(None) == 1:
        if V is None:
            P = I ** 2 * R
        elif I is None:
            P = V ** 2 / R
        elif R is None:
            P = V * I
        return Quantity(P, UNITS["W"])
    
    else:
        P1 = I ** 2 * R
        P2 = V ** 2 / R
        P3 = V * I
        
        if not math.isclose(P1, P2):
            if not math.isclose(P1, P3):
                raise InconsistencyError(power_dissipation, "Inconsistency with P1 = I ** 2 * R")      
            else:
                raise InconsistencyError(power_dissipation, "Inconsistency with P2 = V ** 2 / R")
        else:
            if not math.isclose(P2, P3):
                raise InconsistencyError(power_dissipation, "Inconsistency with P3 = V * I")    
            else:
                return Quantity(avg(P1, P2, P3), UNITS["W"])
 
def resistor_visual(C1: str, C2: str, C3: str, C4: str, C5: str | None = None) -> str:
    """Prints a ASCII representation of a resistor with the color code""" 
    def color_block(color: str):
        ansi = ANSI_COLORS.get(color.lower(), "\033[0m")
        reset = "\033[0m"
        return f"{ansi}    {reset}"
    if C5 is not None:
        return f"    <----------------------------->\n    |                             |\n    |  ┌────┬────┬────┬────┬────┐ |\n   ----│{color_block(C1)}│{color_block(C2)}│{color_block(C3)}│{color_block(C4)}│{color_block(C5)}|----\n    |  └────┴────┴────┴────┴────┘ |\n    |                             |\n    <----------------------------->" 
    else:
        return f"    <------------------------->\n    |                         |\n    |  ┌────┬────┬────┬────┐  |\n   ----│{color_block(C1)}│{color_block(C2)}│{color_block(C3)}│{color_block(C4)}│----\n    |  └────┴────┴────┴────┘  |\n    |                         |\n    <------------------------->" 
def resistor_value(C1: str, C2: str, C3: str, C4: str, C5: str | None = None) -> tuple[float, float, float, float]:
    """Takes in the colors of a resistor and returns its resistivity and tolerance range.

    Args
    ----
        C1 (str): Color band 1
        C2 (str): Color band 2
        C3 (str): Color band 3
        C4 (str): Color band 4
        C5 (str | None, optional): Color band 5. Defaults to None.

    Raises
    ------
        InvalidColors: Raised if user gives a color that is invalid for that band.

    Returns
    -------
        tuple[float, float, float, float]: Ohm value, tolerance precent (+-), lower and upper bound of the tolerance range.
    """
    
    b1 = BANDS.get(C1, None)
    b2 = BANDS.get(C2, None)
    
    if C5 is None:
        multiplier = MULTIPLIERS.get(C3, None)
        tolerance = TOLERANCES.get(C4, None)
        bands = (b1, b2, multiplier, tolerance)
        
        if None in bands:
            raise InvalidColors(resistor_value, bands.index(None) + 1)
        
        ohms = (b1 * 10 + b2) * multiplier
        
    else:
        b3 = BANDS.get(C3)
        multiplier = MULTIPLIERS.get(C4, None)
        tolerance = TOLERANCES.get(C5, None)
        bands = (b1, b2, b3, multiplier, tolerance)
        
        if None in bands:
            raise InvalidColors(resistor_value, bands.index(None) + 1)
        
        ohms = (b1 * 100 + b2 * 10 + b3) * multiplier

    tolerance_decimal = tolerance / 100
    lower = ohms * (1 - tolerance_decimal)
    upper = ohms * (1 + tolerance_decimal)

    return (ohms, tolerance, lower, upper)

### TODO finish wrapping these functions
def total_esr(caps: list[tuple], connection: Literal["parallel", "series"]) -> float:
    """Calculates total ESR of a list of capacitors based on their connection type. Caps are in the format (capacitance, voltage, esr) for now."""
    if connection == "series":
        return sum(cap[2] for cap in caps)
    
    elif connection == "parallel":
        try:
            return 1 / sum(1 / cap[2] for cap in caps if cap[2] != 0)
        except ZeroDivisionError:
            return 0  
        
    else:
        raise ValueError("Connection type must be 'parallel' or 'series'")
def total_capacitance(caps: list[tuple], connection: Literal["parallel", "series"]) -> str: ### caps (capacitance, voltage, esr) (for now)
    """Calculates total capacitance, voltage limit and ESR of a list of capacitors based on their connection type."""
        
    if connection == "parallel":
        total_capacitance = sum(cap[0] for cap in caps)
        volt_limit = min([cap[1] for cap in caps])
        
    elif connection == "series":
        total_capacitance = 1 / sum(1/cap[0] for cap in caps)
        volt_limit = sum([cap[1] for cap in caps])   
        
    else:
        raise ValueError("Connection type must be 'parallel' or 'series'")

    return f"Total Capacitance: {total_capacitance}, Volt Limit: {volt_limit}, Total ESR: {total_esr(caps, connection)}"
