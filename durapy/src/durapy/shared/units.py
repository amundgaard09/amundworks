"""DuraPy Unit Definitions"""

from fractions import Fraction

from .numval_types import Dimension, Unit

F_4, F_3, F_2, F_1, F0, F1, F2, F3, F4 = (
    Fraction(-4),
    Fraction(-3),
    Fraction(-2),
    Fraction(-1),
    Fraction(0),
    Fraction(1),
    Fraction(2),
    Fraction(3),
    Fraction(4),
)

# ISO Base Units - Scale: 1 # The scale is a measurement of how many times to multiply the value to get to one base units worth.
NUMERICAL = Unit(
    symbol="NUM", dimension=Dimension((F0, F0, F0, F0, F0, F0, F0)), scale=1
)  # N/A

METER = Unit(
    symbol="M", dimension=Dimension((F1, F0, F0, F0, F0, F0, F0)), scale=1
)  # L
KILOGRAM = Unit(
    symbol="KG", dimension=Dimension((F0, F1, F0, F0, F0, F0, F0)), scale=1
)  # M
SECOND = Unit(
    symbol="S", dimension=Dimension((F0, F0, F1, F0, F0, F0, F0)), scale=1
)  # T
AMPERE = Unit(
    symbol="B", dimension=Dimension((F0, F0, F0, F1, F0, F0, F0)), scale=1
)  # I
KELVIN = Unit(
    symbol="K", dimension=Dimension((F0, F0, F0, F0, F1, F0, F0)), scale=1
)  # Θ
MOLE = Unit(
    symbol="MOL", dimension=Dimension((F0, F0, F0, F0, F0, F1, F0)), scale=1
)  # N
CANDELA = Unit(
    symbol="CD", dimension=Dimension((F0, F0, F0, F0, F0, F0, F1)), scale=1
)  # J

PASCAL = Unit(
    symbol="Pa", dimension=Dimension((F1, F1, F_2, F0, F0, F0, F0))
)  # L * M / T^2
PSI = Unit(
    symbol="psi", dimension=Dimension((F1, F1, F_2, F0, F0, F0, F0))
)  # L * M / T^2
BAR = Unit(
    symbol="bar", dimension=Dimension((F1, F1, F_2, F0, F0, F0, F0))
)  # L * M / T^2

UNIGUNIT = Unit(
    symbol="UNI_G", dimension=Dimension((F3, F_1, F_2, F0, F0, F0, F0))
)  # L^3 / M * T^2
G = Unit(symbol="G", dimension=Dimension((F1, F0, F_2, F0, F0, F0, F0)))  # L / T^2

NEWTON = Unit(
    symbol="N", dimension=Dimension((F1, F1, F_2, F0, F0, F0, F0))
)  # L * M / T^2
JOULE = Unit(
    symbol="J", dimension=Dimension((F2, F1, F_2, F0, F0, F0, F0))
)  # L^2 * M / T^2
ELECTRONVOLT = Unit(
    symbol="eV", dimension=Dimension((F2, F1, F_2, F0, F0, F0, F0)), scale=6.242e18
)  # L^2 * M / T^2
NEWTONMETER = Unit(
    symbol="Nm", dimension=Dimension((F2, F1, F_2, F0, F0, F0, F0))
)  # L^2 * M / T^2

COULOMB = Unit(symbol="C", dimension=Dimension((F0, F0, F1, F1, F0, F0, F0)))  # I * T
FARAD = Unit(
    symbol="F", dimension=Dimension((F_2, F_1, F4, F2, F0, F0, F0))
)  # T^4 * I^2 / L^2 * M
WATT = Unit(
    symbol="W", dimension=Dimension((F2, F1, F_3, F0, F0, F0, F0))
)  # L^2 * M / T^3
VOLT = Unit(
    symbol="V", dimension=Dimension((F2, F1, F_2, F_1, F0, F0, F0))
)  # L^2 * M / T^2 * I
OHM = Unit(
    symbol="Ω", dimension=Dimension((F2, F1, F_3, F_2, F0, F0, F0))
)  # L^2 * M / T^3 * I^2

HERTZ = Unit(symbol="Hz", dimension=Dimension((F0, F0, F_1, F0, F0, F0, F0)))  # 1 / T

RADIAN = Unit(
    symbol="rad", dimension=Dimension((F0, F0, F0, F0, F0, F0, F0)), scale=1
)
DEGREE = Unit(
    symbol="deg", dimension=Dimension((F0, F0, F0, F0, F0, F0, F0)), scale=0.01745329251
)

# Derived units
MPS = METER / SECOND  # L / T
