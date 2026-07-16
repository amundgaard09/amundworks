"""
The UniPower function package for the `DuraPy` library.
This library contains functions for electrical calculations and simulations. The functions are designed to be easy to use and understand, with clear input and output formats.
The library is still in development and may contain some unstable functions that are not yet fully tested.
"""

import math
import types
import typing

from durapy.src.unimath.unimath import avg
from durapy.src.frameworks.color_sys import ANSI_COLORS
from durapy.src.frameworks.phys_dtypes import (
    Quantity,
    UNITS
)

from durapy.src.commons.exceptions import (
    InconsistencyError,
    InvalidColors,
    MissingParameters
)

BANDS: types.MappingProxyType[str, int] = types.MappingProxyType({
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
MULTIPLIERS: types.MappingProxyType[str, float] = types.MappingProxyType({
    "black":  1.0,
    "brown":  10.0,
    "red":    100.0,
    "orange": 1000.0,
    "yellow": 10000.0,
    "green":  100000.0,
    "blue":   1000000.0,
    "violet": 10000000.0,
    "gray":   100000000.0,
    "white":  1000000000.0,
    "gold":   0.1,
    "silver": 0.01,
})
TOLERANCES: types.MappingProxyType[str, float] = types.MappingProxyType({
    "brown":  1.0,
    "red":    2.0,
    "green":  0.5,
    "blue":   0.25,
    "violet": 0.1,
    "gray":   0.05,
    "gold":   5.0,
    "silver": 10.0,
})

def ohms_law(v: float | None = None, i: float | None = None, r: float | None = None) -> tuple[float, float, float]:
    """Ohms Law calculation for voltage, current, and resistivity. Returns: (V, I, R)"""

    missing = [param for param, value in zip(("v", "i", "r"), (v, i, r)) if value is None]

    if v is None:
        if i is None or r is None:
            raise MissingParameters(ohms_law, missing)
        v = i * r

    elif i is None:
        if r is None:
            raise MissingParameters(ohms_law, missing)
        i = v / r

    elif r is None:
        r = v / i

    return v, i, r

def volt_divider(VIn: float, R1: float, R2: float) -> Quantity:
    """Calculates the output voltage of a voltage divider from input voltage and the two resistances."""
    return Quantity((VIn * (R2 / (R1 + R2))), UNITS["V"])

def rc_time_constant(capacitance: float, resistance: float) -> Quantity:
    """Calculates the time constant of an RC circuit from capacitance in farads and resistance in ohms."""
    return Quantity((capacitance * resistance), UNITS["S"])

def inductor_impedance(hertz: float, inductance: float) -> Quantity:
    """Calculates the impedance of an inductor at a given frequency in hertz and inductance in henrys."""
    return Quantity((2 * math.pi * hertz * inductance), UNITS["Ω"])

def power_dissipation(v: float | None = None, i: float | None = None, r: float | None = None) -> Quantity:
    """Calculates power dissipation from voltage, current and resistance. If all three parameters are given, it checks for consistency between the three formulas P = I^2 * R, P = V^2 / R and P = V * I."""

    missing = [param for param, value in zip(("v", "i", "r"), (v, i, r)) if value is None]

    if v is None:
        if i is None or r is None:
            raise MissingParameters(power_dissipation, missing)
        return Quantity(i ** 2 * r, UNITS["W"])

    elif i is None:
        if r is None:
            raise MissingParameters(power_dissipation, missing)
        return Quantity(v ** 2 / r, UNITS["W"])

    elif r is None:
        return Quantity(v * i, UNITS["W"])

    else:
        P1 = i ** 2 * r
        P2 = v ** 2 / r
        P3 = v * i

        if not math.isclose(P1, P2):
            if not math.isclose(P1, P3):
                raise InconsistencyError(ohms_law, "Inconsistency with P1 = I ** 2 * R")
            else:
                raise InconsistencyError(ohms_law, "Inconsistency with P2 = V ** 2 / R")
        else:
            if not math.isclose(P2, P3):
                raise InconsistencyError(ohms_law, "Inconsistency with P3 = V * I")
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
    """Returns the resistance value of a resistor given its color bands."""

    try:
        b1 = BANDS[C1]
        b2 = BANDS[C2]
    except KeyError as e:
        raise InvalidColors(resistor_value, str(e)) from e

    if C5 is None:
        try:
            multiplier = MULTIPLIERS[C3]
            tolerance = TOLERANCES[C4]
        except KeyError as e:
            raise InvalidColors(resistor_value, str(e)) from e

        ohms = (b1 * 10 + b2) * multiplier

    else:
        try:
            b3 = BANDS[C3]
            multiplier = MULTIPLIERS[C4]
            tolerance = TOLERANCES[C5]
        except KeyError as e:
            raise InvalidColors(resistor_value, str(e)) from e

        ohms = (b1 * 100 + b2 * 10 + b3) * multiplier

    tolerance_decimal = tolerance / 100

    lower = ohms * (1 - tolerance_decimal)
    upper = ohms * (1 + tolerance_decimal)

    return (ohms, tolerance, lower, upper)

### TODO finish wrapping these functions
def total_esr(caps: list[tuple], connection: typing.Literal["parallel", "series"]) -> float:
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
def total_capacitance(caps: list[tuple], connection: typing.Literal["parallel", "series"]) -> str: ### caps (capacitance, voltage, esr) (for now)
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
