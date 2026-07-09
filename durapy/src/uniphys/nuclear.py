"""
The Nuclear Physics module for `DuraPy` `UniPhys`

This module contains resources for calculations and simulations for Nuclear Physics. 
"""

from durapy.src.commons.constants import E

def radioactive_decay(initial_quantity: float, decay_const: float, time: float) -> float:
    """Returns the remaining quantity of a radioactive substance after a given time, based on its initial quantity and decay constant."""
    return initial_quantity * (E ** (-decay_const * time))
def half_life(decay_const: float) -> float:
    """Returns the half-life of a radioactive substance based on its decay constant."""
    return 0.693 / decay_const
def decay_constant(half_life: float) -> float:
    """Returns the decay constant of a radioactive substance based on its half-life."""
    return 0.693 / half_life
def activity(quantity: float, decay_const: float) -> float:
    """Returns the activity of a radioactive substance based on its quantity and decay constant."""
    return decay_const * quantity
def mean_lifetime(decay_const: float) -> float:
    """Returns the mean lifetime of a radioactive substance based on its decay constant."""
    return 1 / decay_const
def decay_energy(mass_defect: float) -> float:
    """Returns the energy released in a nuclear decay based on the mass defect."""
    return mass_defect * E
def binding_energy(mass_defect: float) -> float:
    """Returns the binding energy of a nucleus based on the mass defect."""
    return mass_defect * E
def mass_defect(proton_mass: float, neutron_mass: float, nucleus_mass: float) -> float:
    """Returns the mass defect of a nucleus based on the mass of its protons, neutrons, and the nucleus itself."""
    return (proton_mass + neutron_mass) - nucleus_mass
def decay_rate(initial_quantity: float, decay_const: float) -> float:
    """Returns the decay rate of a radioactive substance based on its initial quantity and decay constant."""
    return decay_const * initial_quantity

