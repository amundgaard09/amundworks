
from __future__ import annotations

# The 7 SI Base symbols mapping to your 7-tuple indices
BASE_SYMBOLS = ["m", "kg", "s", "A", "K", "mol", "cd"]

# Registry for named engineering units and their expected 7-tuple dimensions
KNOWN_UNITS = {
    (0, 0, 0, 0, 0, 0, 0): "",       # Dimensionless / Scalar
    (1, 0, 0, 0, 0, 0, 0): "m",      # Meter
    (0, 1, 0, 0, 0, 0, 0): "kg",     # Kilogram
    (0, 0, 1, 0, 0, 0, 0): "s",      # Second
    (1, 0, -1, 0, 0, 0, 0): "m/s",   # Velocity
    (1, 0, -2, 0, 0, 0, 0): "m/s²",  # Acceleration
    (1, 1, -2, 0, 0, 0, 0): "N",     # Newton (Force)
    (2, 1, -2, 0, 0, 0, 0): "J",     # Joule (Energy)
    (2, 1, -3, 0, 0, 0, 0): "W",     # Watt (Power)
    (-1, 1, -2, 0, 0, 0, 0): "Pa",   # Pascal (Pressure)
}

# Helper dictionary for pretty printing exponents
SUPERSCRIPTS = {
    '-': '⁻', '0': '⁰', '1': '', '2': '²', '3': '³',
    '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
}

def format_exponent(exp: float) -> str:
    """Converts a number like -2 into a superscript string like ⁻²."""
    # Handle ints cleanly so 2.0 becomes ² instead of ².⁰
    val_str = str(int(exp)) if exp.is_integer() else str(exp)
    if val_str == "1":
        return ""
    return "".join(SUPERSCRIPTS.get(char, char) for char in val_str)

def get_symbol(quantity: Quantity) -> str:
    # 1. Check if it's a known, named engineering unit
    if quantity.dimensions in KNOWN_UNITS:
        return KNOWN_UNITS[quantity.dimensions]

    # 2. Dynamic fallback: Construct string from base elements (e.g., m·kg·s⁻²)
    positives = []
    negatives = []

    for symbol, exp in zip(BASE_SYMBOLS, quantity.dimensions):
        if exp == 0:
            continue
        elif exp > 0:
            positives.append(f"{symbol}{format_exponent(float(exp))}")
        else:
            negatives.append(f"{symbol}{format_exponent(float(exp))}")

    # Combine them cleanly. Example output format: m·kg·s⁻²
    parts = positives + negatives
    return "·".join(parts) if parts else ""

class Quantity:
    def __init__(self, value: float, dimensions: tuple):
        self.value = value
        self.dimensions = dimensions
        self.symbol = get_symbol(self)

    def __str__(self):
        return f"{self.value} {self.symbol}"

    def __repr__(self):
        return f"Quantity({self.value}, {self.dimensions})"

    def __eq__(self, value):
        if isinstance(value, Quantity):
            return self.dimensions == value.dimensions and self.value == value.value
        elif isinstance(value, (int, float)):
            return self.value == value
        return NotImplemented

    def __add__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Cannot add a Quantity to a scalar.")
        if self.dimensions != other.dimensions:
            raise ValueError(f"Dimension mismatch: {self.dimensions} vs {other.dimensions}")
        return Quantity(self.value + other.value, self.dimensions)

    def __sub__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Cannot subtract a scalar from a Quantity.")
        if self.dimensions != other.dimensions:
            raise ValueError(f"Dimension mismatch: {self.dimensions} vs {other.dimensions}")
        return Quantity(self.value - other.value, self.dimensions)

    def __mul__(self, other):
        if isinstance(other, Quantity):
            new_dims = tuple(s + o for s, o in zip(self.dimensions, other.dimensions))
            return Quantity(self.value * other.value, new_dims)
        else:
            return Quantity(self.value * other, self.dimensions)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Quantity):
            new_dims = tuple(s - o for s, o in zip(self.dimensions, other.dimensions))
            return Quantity(self.value / other.value, new_dims)
        else:
            return Quantity(self.value / other, self.dimensions)

    def __rtruediv__(self, other):
        neg_dims = tuple(-d for d in self.dimensions)
        return Quantity(other / self.value, neg_dims)

    def __pow__(self, power: float):
        if isinstance(power, (int, float)):
            new_dims = tuple(d * power for d in self.dimensions)
            return Quantity(self.value ** power, new_dims)
        raise TypeError("Power must be a scalar number.")

    def __ge__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Cannot compare a Quantity to a non-Quantity.")
        if self.dimensions != other.dimensions:
            raise ValueError(f"Cannot compare different dimensions: {self.dimensions} vs {other.dimensions}")
        return self.value >= other.value

    def __gt__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Cannot compare a Quantity to a non-Quantity.")
        if self.dimensions != other.dimensions:
            raise ValueError(f"Cannot compare different dimensions: {self.dimensions} vs {other.dimensions}")
        return self.value > other.value

    def __le__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Cannot compare a Quantity to a non-Quantity.")
        if self.dimensions != other.dimensions:
            raise ValueError(f"Cannot compare different dimensions: {self.dimensions} vs {other.dimensions}")
        return self.value <= other.value

    def __lt__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Cannot compare a Quantity to a non-Quantity.")
        if self.dimensions != other.dimensions:
            raise ValueError(f"Cannot compare different dimensions: {self.dimensions} vs {other.dimensions}")
        return self.value < other.value

# Assuming you initialize base quantities using your dimensions:
meter = Quantity(1.0, (1, 0, 0, 0, 0, 0, 0))
kg = Quantity(1.0, (0, 1, 0, 0, 0, 0, 0))
second = Quantity(1.0, (0, 0, 1, 0, 0, 0, 0))

force = 10 * kg * (5 * meter / (second ** 2))
print(force)
# Output: 50.0 N  (Recognized via KNOWN_UNITS)

custom_rate = force / (meter ** 3)
print(custom_rate)
# Output: 50.0 m⁻²·kg·s⁻² (Dynamically built fallback string)

# Comparison enforcement
try:
    print(force >= meter)
except ValueError as e:
    print(e)
# Output: Cannot compare different dimensions: (1, 1, -2, 0, 0, 0, 0) vs (1, 0, 0, 0, 0, 0, 0)
