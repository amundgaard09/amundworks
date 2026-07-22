"""
The UniPower function library for the `DuraPy` library.
This library contains functions for electrical calculations and simulations. The functions are designed to be easy to use and understand, with clear input and output formats.
The library is still in development and may contain some unstable functions that are not yet fully tested.
"""

from .unipower import (
    ohms_law,
    volt_divider,
    rc_time_constant,
    inductor_impedance,
    power_dissipation,
    total_esr,
    total_capacitance,
)

from .types import (
    capacitor,
    diode,
    fuse,
    ic,
    inductor,
    oscillator,
    potentiometer,
    resistor,
    transistor
)

__all__ = [
    "ohms_law",
    "volt_divider",
    "rc_time_constant",
    "inductor_impedance",
    "power_dissipation",
    "total_esr",
    "total_capacitance",

    "capacitor",
    "diode",
    "fuse",
    "ic",
    "inductor",
    "oscillator",
    "potentiometer",
    "resistor",
    "transistor",
]
