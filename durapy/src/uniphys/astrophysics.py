"""
The Astrophysics module for `AWPC` `UniPhys`

This module contains resources for calculations and simulations for Astrophysics. 
"""

# Alpha - A α, Beta - B β, Gamma - Γ γ, Delta - Δ δ,  Epsilon - E ε, Zeta - Z ζ, Eta - H η, 
# Theta - Θ θ, Iota - I ι, Kappa - K κ, Lambda - Λ λ, Mu - M μ,      Nu - N ν,   Xi - Ξ ξ,  Omicron - O ο, 
# Pi - Π π,    Rho - P ρ,  Sigma - Σ σ ς, Tau - T τ,  Ypsilon - Y υ, Phi - Φ φ,  Chi - X χ, Psi - Ψ ψ, Omega - Ω ω

import math

from durapy.src.frameworks.phys_dtypes import Quantity, UNITS
from durapy.src.commons.constants import G, C, PI, EARTH_M, EARTH_R, HUBBLE 

def schwarzschild_radius(M: float) -> Quantity:
    return Quantity(((2 * G * M) / C * C), UNITS["m"])

def redshift(λobs: float, λrest: float) -> Quantity:
    return Quantity(((λobs - λrest) / λrest), UNITS["nm"])

def orbital_period(semi_major_axis: float, M: float, m: float) -> Quantity:
    return Quantity((2 * PI * math.hypot(0, semi_major_axis ** 3 / (G * (M + m)))), UNITS["S"])
def orbital_velocity(orbital_radius: float = EARTH_R, mass: float = EARTH_M) -> Quantity:
    return Quantity((math.hypot(0, (G * mass) / orbital_radius)), UNITS["m/s"])
def escape_velocity(radius: float = EARTH_R, mass: float = EARTH_M) -> Quantity:
    return Quantity((math.hypot(0, 2) * orbital_velocity(radius, mass)), UNITS["m/s"])

def newtonian_gravitation(mass1: float, mass2: float, distance: float) -> Quantity:
    return Quantity((G * mass1 * mass2 / distance ** 2), UNITS["N"])
def surface_gravity(mass: float, radius: float) -> Quantity:
    return Quantity((G * mass / radius ** 2), UNITS["m/s^2"])

def tsiolkovsky_rocket_equation(exhaust_vel: float, initial_mass: float, final_mass: float) -> Quantity:
    if final_mass > initial_mass:
        return Quantity(0, UNITS["Δv"])
    
    return Quantity((exhaust_vel * math.log(initial_mass / final_mass)), UNITS["Δv"])

def hubbles_law(Distance: float) -> Quantity:
    return Quantity((HUBBLE * Distance), UNITS["m/s"])