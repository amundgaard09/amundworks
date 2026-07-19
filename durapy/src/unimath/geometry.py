"""UniMath geometry utilities."""

import math

def polygon_area(n: int, side_length: float) -> float:
    """Returns the area of a regular polygon with `n` sides and a side length of `side_length`."""
    return (n * side_length**2) / (4 * math.tan(math.pi / n))
def polygon_circumference(n: int, side_length: float) -> float:
    """Returns the circumference of a regular polygon with `n` sides and a side length of `side_length`."""
    return n * side_length
def polygon_interior_angle(n: int) -> float:
    """Returns the interior angle of a regular polygon with `n` sides."""
    return (n - 2) * 180 / n
def polygon_exterior_angle(n: int) -> float:
    """Returns the exterior angle of a regular polygon with `n` sides."""
    return 360 / n
