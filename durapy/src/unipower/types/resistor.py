
#from ...shared.constants import OHM
from ..exceptions import InvalidColors
from types import MappingProxyType

BANDS: MappingProxyType[str, int] = MappingProxyType({
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
MULTIPLIERS: MappingProxyType[str, float] = MappingProxyType({
    "silver": 0.01,
    "gold":   0.1,
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
})
TOLERANCES: MappingProxyType[str, float] = MappingProxyType({
    "brown":  1.0,
    "red":    2.0,
    "green":  0.5,
    "blue":   0.25,
    "violet": 0.1,
    "gray":   0.05,
    "gold":   5.0,
    "silver": 10.0,
})

def resistor_value(C1: str, C2: str, C3: str, C4: str, C5: str | None = None) -> tuple[float, float, float, float]:
    """Returns the resistance value of a resistor given its color bands."""

    # Try given colors
    try:
        b1 = BANDS[C1]
        b2 = BANDS[C2]

    # Invalid colors given
    except KeyError as e:
        raise InvalidColors(str(e)) from e

    # 4-color mode
    if C5 is None:
        try:
            multiplier = MULTIPLIERS[C3]
            tolerance = TOLERANCES[C4]
        except KeyError as e:
            raise InvalidColors(str(e)) from e

        ohms = (b1 * 10 + b2) * multiplier

    # C5 given, 5-color mode
    else:
        try:
            b3 = BANDS[C3]
            multiplier = MULTIPLIERS[C4]
            tolerance = TOLERANCES[C5]
        except KeyError as e:
            raise InvalidColors(str(e)) from e

        ohms = (b1 * 100 + b2 * 10 + b3) * multiplier

    tolerance_decimal = tolerance / 100

    lower = ohms * (1 - tolerance_decimal)
    upper = ohms * (1 + tolerance_decimal)

    return (ohms, tolerance, lower, upper)

class Resistor:
    def __init__(self, args: tuple | float | None = None) -> None:
        if isinstance(args, tuple):
            pass
