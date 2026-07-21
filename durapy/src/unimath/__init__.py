"""The UniMath module for DuraPy."""

from .coordinate_systems import (
    Cartesian1D,
    Cartesian2D,
    Cartesian3D,
    Cylindrical,
    Spherical,
    Polar,
)

from . import (
    algebra,
    algorithms,
    decorators,
    exceptions,
    geometry,
    linalg,
    num_theory,
    trigonometry
)

__all__ = [
    "Cartesian1D",
    "Cartesian2D",
    "Cartesian3D",
    "Cylindrical",
    "Spherical",
    "Polar",

    "algebra",
    "algorithms",
    "decorators",
    "exceptions",
    "geometry",
    "linalg",
    "num_theory",
    "trigonometry"
]
