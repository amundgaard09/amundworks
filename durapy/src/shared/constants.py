"""
The `DuraPy` Constants Library

This module contains all the physical constants used in the `DuraPy` library, such as the gravitational constant, speed of light, and various planetary parameters.
The constants are stored as instances of the `Constant` class, which includes the value, unit, and name of the constant.
"""

# Alpha - A α, Beta - B β,    Gamma - Γ γ,   Delta - Δ δ,   Epsilon - E ε, Zeta - Z ζ, Eta - H η,     Theta - Θ θ,
# Iota - I ι,  Kappa - K κ,   Lambda - Λ λ,  Mu - M μ,      Nu - N ν,      Xi - Ξ ξ,   Omicron - O ο, Pi - Π π,
# Rho - P ρ,   Sigma - Σ σ ς, Tau - T τ,     Ypsilon - Y υ, Phi - Φ φ,     Chi - X χ,  Psi - Ψ ψ,     Omega - Ω ω

# Order: Length, Mass, Time, Electric Charge, Thermodynamic Temperature, Amount of Substance, Luminous Intensity

from fractions import Fraction
from ..shared.numval_types import Quantity, Constant, Unit, Dimension

F0, F1, F2, F3, F4 = Fraction(0), Fraction(1), Fraction(2), Fraction(3), Fraction(4)
F_1, F_2, F_3, F_4 = Fraction(-1), Fraction(-2), Fraction(-3), Fraction(-4)

# ISO Base Units - Scale: 1
NUMERICAL = Unit(symbol="NUM", dimension=Dimension((F0, F0, F0, F0, F0, F0, F0)), scale=1) # N/A

METER     = Unit(symbol="M",   dimension=Dimension((F1, F0, F0, F0, F0, F0, F0)), scale=1) # L
KILOGRAM  = Unit(symbol="KG",  dimension=Dimension((F0, F1, F0, F0, F0, F0, F0)), scale=1) # M
SECOND    = Unit(symbol="S",   dimension=Dimension((F0, F0, F1, F0, F0, F0, F0)), scale=1) # T
AMPERE    = Unit(symbol="B",   dimension=Dimension((F0, F0, F0, F1, F0, F0, F0)), scale=1) # I
KELVIN    = Unit(symbol="K",   dimension=Dimension((F0, F0, F0, F0, F1, F0, F0)), scale=1) # Θ
MOLE      = Unit(symbol="MOL", dimension=Dimension((F0, F0, F0, F0, F0, F1, F0)), scale=1) # N
CANDELA   = Unit(symbol="CD",  dimension=Dimension((F0, F0, F0, F0, F0, F0, F1)), scale=1) # J

PASCAL = Unit(symbol="Pa",  dimension=Dimension((F1, F1, F_2, F0, F0, F0, F0))) # L * M / T^2
PSI    = Unit(symbol="psi", dimension=Dimension((F1, F1, F_2, F0, F0, F0, F0))) # L * M / T^2
BAR    = Unit(symbol="bar", dimension=Dimension((F1, F1, F_2, F0, F0, F0, F0))) # L * M / T^2

G       = Unit(symbol="UNI_G", dimension=Dimension((F3, F_1, F_2, F0, F0, F0, F0))) # L^3 / M * T^2
GRAVITY = Unit(symbol="G",   dimension=Dimension((F1, F0, F_2, F0, F0, F0, F0))) # L / T^2

NEWTON    = Unit(symbol="N", dimension=Dimension((F1, F1, F_2, F0, F0, F0, F0))) # L * M / T^2
JOULE      = Unit(symbol="J", dimension=Dimension((F2, F1, F_2, F0, F0, F0, F0))) # L^2 * M / T^2
NEWTONMETER = Unit(symbol="Nm", dimension=Dimension((F2, F1, F_2, F0, F0, F0, F0))) # L^2 * M / T^2

COULOMB = Unit(symbol="C", dimension=Dimension((F0,  F0,  F1,  F1,  F0, F0, F0))) # I * T
FARAD   = Unit(symbol="F", dimension=Dimension((F_2, F_1, F4,  F2,  F0, F0, F0))) # T^4 * I^2 / L^2 * M
WATT    = Unit(symbol="W", dimension=Dimension((F2,  F1,  F_3, F0,  F0, F0, F0))) # L^2 * M / T^3
VOLT    = Unit(symbol="V", dimension=Dimension((F2,  F1,  F_2, F_1, F0, F0, F0))) # L^2 * M / T^2 * I
OHM     = Unit(symbol="Ω", dimension=Dimension((F2,  F1,  F_3, F_2, F0, F0, F0))) # L^2 * M / T^3 * I^2

HERTZ = Unit(symbol="Hz", dimension=Dimension((F0, F0, F_1, F0, F0, F0, F0))) # 1 / T

DEGREE    = Unit(symbol="deg", dimension=Dimension((F0, F0, F0, F0, F0, F0, F0)), scale=1) # N/A
RADIAN    = Unit(symbol="rad", dimension=Dimension((F0, F0, F0, F0, F0, F0, F0)), scale=1) # N/A

#Derived units
MPS = METER / SECOND # L / T

# Universal Gravitational Constant
UNI_G = Constant(Quantity(6.74e-11, G), name="Gravitational Constant") # L^3 / M * T^2

# Mathematical/Dimensionless Constants
E       = Constant(Quantity(2.718281828459045,  NUMERICAL), name="Eulers Number")
PI      = Constant(Quantity(3.141592653589793,  NUMERICAL), name="Pi - π")
TAU     = Constant(Quantity(6.283185307179586,  NUMERICAL), name="Archimedes' Constant - τ - (AKA 2 * PI)")
INF     = Constant(Quantity(float('inf'),       NUMERICAL), name="Positive Infinity")
NINF    = Constant(Quantity(float('-inf'),      NUMERICAL), name="Negative Infinity")
IMAG    = Constant(Quantity(1j,                 NUMERICAL), name="Imaginary Unit - sqrt(-1)")
GOLDEN  = Constant(Quantity(1.618033988749895,  NUMERICAL), name="The Golden Ratio - φ,")
EULMAS  = Constant(Quantity(0.5772156649015329, NUMERICAL), name="The Euler-Mascheroni Constant")
FSTRUCT = Constant(Quantity(7.2973525693e-03,   NUMERICAL), name="Fine-Structure Constant")

# Length Constants - L
PLANCKL = Constant(Quantity(1.616255e-35,   METER), name="Planck Length")
BOHR_R  = Constant(Quantity(5.291772109e-11, METER), name="The Bohr Radius")
EARTH_R = Constant(Quantity(6.371e+6,     METER), name="Radius of the Earth")
ASTUNIT = Constant(Quantity(1.496e+11,  METER), name="Astronomical Unit")
MOON_R  = Constant(Quantity(1.737e+6,  METER), name="Radius of the Moon")
SUN_R   = Constant(Quantity(6.957e+8,  METER), name="Radius of the Sun")
MARS_R  = Constant(Quantity(3.390e+6,  METER), name="Radius of Mars")
LIGHTYR = Constant(Quantity(9.461e+15, METER), name="Light year")
PARSEC  = Constant(Quantity(.086e+16,  METER), name="Parsec")

# Mass Constants - M
ELECTRON_M = Constant(Quantity(9.1093837015e-31, KILOGRAM), name="Electron Mass")
NEUTRON_M = Constant(Quantity(1.67492749804e-27, KILOGRAM), name="Neutron Mass")
PROTON_M = Constant(Quantity(1.67262192369e-27, KILOGRAM), name="Proton Mass")
EARTH_M = Constant(Quantity(5.972e+24, KILOGRAM), name="Mass of the Earth")
MOON_M = Constant(Quantity(7.342e+22, KILOGRAM), name="Mass of the Moon")
MARS_M = Constant(Quantity(6.390e+23, KILOGRAM), name="Mass of Mars")
SUN_M = Constant(Quantity(1.989e+30, KILOGRAM), name="Mass of the Sun")

# Time Constants - T
PLANCK_T = Constant(Quantity(5.39e-43, SECOND), name="Planck Time")
MINUTE = Constant(Quantity(60, SECOND), name="Minute")
HOUR = Constant(Quantity(3600, SECOND), name="Hour")
DAY = Constant(Quantity(86400, SECOND), name="Day")
YEAR = Constant(Quantity(31536000, SECOND), name="Year")

# Electric Charge Constants - I

# Thermodynamic Temperature Constants - Θ

# Amount of Substance Constants - N

# Luminous Intensity Constants - J

# Gravity Constants - L / T^2
EARTH_G = Constant(Quantity(9.8, GRAVITY), name="Surface Gravity of the Earth")
MOON_G = Constant(Quantity(1.62, GRAVITY), name="Surface Gravity of the Moon")
MARS_G = Constant(Quantity(3.71, GRAVITY), name="Surface Gravity of Mars")
SUN_G = Constant(Quantity(274, GRAVITY), name="Surface Gravity of the Sun")

# Speed Constants - L / T
C    = Constant(Quantity(299792458, MPS), name="Speed of Light")
MACH = Constant(Quantity(343, MPS), name="Speed of Sound at sea level")

# Energy Constants
PLANCK  = Constant(Quantity(6.2607015e-34, JOULE), name="Planck's Constant")
PLANCKR = Constant(Quantity(1.054571817e-34, JOULE), name="Reduced Planck Constant")

# Vacuum-related Constants
VAC_PERMEABILITY = Constant(Quantity(1.25663706127e-06, NEWTON / AMPERE**2), name="Vacuum Permeability") # Measure of the resistance encountered when forming a magnetic field in a vacuum; also known as the magnetic constant.
VAC_PERMITTIVITY = Constant(Quantity(8.8541878128e-12,  FARAD / METER), name="Vacuum Permittivity") # Capability of a vacuum to permit electric field lines; also known as the electric constant.
VAC_IMPEDANCE    = Constant(Quantity(376.730313412, OHM),             name="Vacuum Impedance")   # Ratio of the magnitudes of the electric and magnetic fields in an electromagnetic wave traveling through a vacuum.

# Miscellaneous Constants
STEFAN_BOLTZMANN = Constant(Quantity(5.670374419e-08, WATT / (METER**2 * KELVIN**4)), name="Stefan-Boltzmann Constant")  # Constant of proportionality in the Stefan-Boltzmann law relating total energy radiated per unit surface area of a black body.
COULOMB_CONST = Constant(Quantity(8.9875517923e+09,  NEWTON * METER**2 / AMPERE**2), name="Coulomb Constant") # Proportionality constant used in electrostatics equations, equal to 1 / (4pi * epsilon_0).
GAS_CONSTANT = Constant(Quantity(8.314462618,       JOULE / (MOLE * KELVIN)),       name="Gas Constant") # Work performed by one mole of a gas during a temperature change of 1 Kelvin at constant pressure.
JOSEPHSON   = Constant(Quantity(483597.8484e+09,   HERTZ / VOLT),   name="Josephson Constant") # Constant relating the potential difference across a Josephson junction to the frequency of the alternating current.
BOLTZMANN  = Constant(Quantity(.380649e-23,       JOULE / KELVIN), name="Boltzmann Constant") # Relates the average relative kinetic energy of particles in a gas with the thermodynamic temperature of the gas.
AVOGADRO  = Constant(Quantity(6.02214076e+23,    MOLE**-1),       name="Avogadro Constant") # Number of constituent particles (usually atoms or molecules) contained in one mole of a substance.
FARADAY  = Constant(Quantity(96485.33212,       COULOMB / MOLE), name="Faraday Constant") # Total electric charge carried by one mole of electrons.
RYDBERG = Constant(Quantity(10973731.56816,    METER ** -1),    name="Rydberg Constant") # Limiting value of the highest wavenumber of any photon that can be emitted from an atom.
HUBBLE = Constant(Quantity(70000, MPS)      / PARSEC,          name="Hubble Constant") # The average speed of galaxies moving away from each other in the universe -- the expansion rate of the universe.
WIEN  = Constant(Quantity(2.897771955e-03,   METER * KELVIN), name="Wien Displacement Constant") # Relationship between the thermodynamic temperature of a blackbody and the wavelength of its peak radiation.
