"""
The `AWPC` Electromagnetics module for `UniPhys`

This module provides resources for calculations related to charged particles, electric and magnetic fields, optics and other related branches.
"""

from ..shared.numval_types import Quantity
from ..shared.color_sys import color_text as color_text
from ..shared.constants import PLANCK, JOULE, INF, C

__WAVLN_UV_SPEC: dict[tuple[float, float], str] = {
    (10, 13.5): f"{color_text('EUV', 'Violet')}",
    (13.5,100): f"{color_text('DUV', 'Violet')}",
    (100, 280): f"{color_text('UVC', 'Violet')}",
    (280, 315): f"{color_text('UVB', 'Violet')}",
    (315, 390): f"{color_text('UVA', 'Violet')}",
}
__WAVLN_VSBL_SPEC: dict[tuple[float, float], str] = {
    (390, 450): f"{color_text('Violet', 'violet')}",
    (450, 495): f"{color_text('Blue',   'blue')}",
    (495, 570): f"{color_text('Green',  'green')}",
    (570, 590): f"{color_text('Yellow', 'yellow')}",
    (590, 620): f"{color_text('Orange', 'orange')}",
    (620, 750): f"{color_text('Red',    'red')}",
}

_WAVLN_EM_SPEC: dict[tuple[float, float], str | dict] = {
    (0, 0.01): "Gamma-ray",
    (0.01, 10): "X-Ray",
    (10, 400): __WAVLN_UV_SPEC,
    (400, 700): __WAVLN_VSBL_SPEC,
    (700, 1e6): "Infrared Light",
    (1e7, 1e10): "Micro Wave",
    (1e10, INF.value): "Radio Wave",
}

def _spectrum_label(λ: float, spectrum_map: dict[tuple[float, float], str | dict]) -> str:
    """Return the spectrum label (e.g. `Radio Wave` or `X-Ray`) by checking recursively for wavelength `λ` in `spectrum_map`."""
    for (low, high), value in spectrum_map.items():
        if low <= λ < high:
            if isinstance(value, dict):
                return _spectrum_label(λ, value)
            return value
    raise ValueError(f"Wavelength {λ!r} is out of range for this spectrum map")

def λ(Hz: float) -> Quantity:
    """Return wavelength `λ` from `Hertz`."""
    return C / Hz
def hz(λ: float) -> Quantity:
    """Return `Hertz` from wavelength `λ`."""
    return C / λ*1e9

def ems(λ: float) -> tuple[str, float, str]:
    """
    Get the part of the electromagnetic spectrum the wavelength `λ` sits in, as well as the hertz.
    """
    label = _spectrum_label(λ, _WAVLN_EM_SPEC)
    Hz = float(hz(λ))

    return label, Hz, f'{label} - {Hz} Hz'

def photon_energy_λ(λ: float) -> Quantity:
    """Calculate the energy of a photon in joules with wavelength `λ`."""
    return Quantity(PLANCK * hz(λ), JOULE)
def photon_energy_hz(Hz: float) -> Quantity:
    """Calculate the energy of a photon in joules with frequency `Hz`."""
    return Quantity(PLANCK * Hz, JOULE)
def photon_energy_ev_λ(λ: float) -> Quantity:
    """Calculate the energy of a photon with wavelength `λ` in electron volts."""
    return photon_energy_λ(λ) / 1.60218e-19
def photon_energy_ev_hz(Hz: float) -> Quantity:
    """Calculate the energy of a photon with frequency `Hz` in electron volts."""
    return photon_energy_hz(Hz) / 1.60218e-19
