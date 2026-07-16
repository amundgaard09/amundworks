"""
This module contains the base classes for the custom data types used in the `DuraPy` library, such as the unit system, including `Unit`, `Quantity`, and `PhysicalConstant`.
"""

# Alpha - A α, Beta - B β, Gamma - Γ γ, Delta - Δ δ,  Epsilon - E ε, Zeta - Z ζ, Eta - H η,
# Theta - Θ θ, Iota - I ι, Kappa - K κ, Lambda - Λ λ, Mu - M μ,      Nu - N ν,   Xi - Ξ ξ,  Omicron - O ο,
# Pi - Π π,    Rho - P ρ,  Sigma - Σ σ ς, Tau - T τ,  Ypsilon - Y υ, Phi - Φ φ,  Chi - X χ, Psi - Ψ ψ, Omega - Ω ω

from math import pi

from ..commons.exceptions import DimensionMismatch

class Unit:
    """Base class for the unit system - unifying units of measurement along with the dimension of measurement (e.g. length, weight, etc.)."""

    def __init__(self, unitname: str, measurement: str, *, factor: float = 1.0, offset: float = 0.0):
        self.unitname = unitname
        self.measurement = measurement
        self.factor = factor
        self.offset = offset

    def convert_to_base(self, value: float | int | complex) -> float | int | complex:
        """Convert a value expressed in this unit to the canonical base value for the dimension."""
        return value * self.factor + self.offset

    def convert_from_base(self, value: float | int | complex) -> float | int | complex:
        """Convert a canonical base value back into this unit."""
        if self.factor == 0:
            raise ZeroDivisionError("Unit conversion factor cannot be zero.")
        return (value - self.offset) / self.factor

    def __str__(self):
        return self.unitname

    def __repr__(self) -> str:
        return f"Unit({self.unitname!r}, {self.measurement!r}, factor={self.factor!r}, offset={self.offset!r})"

    def __eq__(self, other):
        return (
            isinstance(other, Unit)
            and self.unitname == other.unitname
            and self.measurement == other.measurement
            and self.factor == other.factor
            and self.offset == other.offset
        )

    def __hash__(self):
        return hash((self.unitname, self.measurement, self.factor, self.offset))

    def __bool__(self):
        return True


class Quantity:
    """Base Class for storing values and their units."""

    def __init__(self, value: float | int | complex, unit: Unit):
        self._value = value
        self._unit = unit

    @property
    def value(self) -> float | int | complex:
        """Return the numeric value of the quantity."""
        return self._value

    @value.setter
    def value(self, value: float | int | complex) -> None:
        self._value = value

    @property
    def unit(self) -> Unit:
        """Return the unit attached to the quantity."""
        return self._unit

    @unit.setter
    def unit(self, unit: Unit) -> None:
        self._unit = unit

    def to(self, target_unit: Unit) -> "Quantity":
        """Convert the quantity to another unit of the same dimension."""
        if not isinstance(target_unit, Unit):
            raise TypeError("target_unit must be an instance of Unit")
        if self._unit.measurement != target_unit.measurement:
            raise DimensionMismatch(
                f"Cannot convert {self._unit.measurement!r} to {target_unit.measurement!r}."
            )

        base_value = self._unit.convert_to_base(self._value)
        converted_value = target_unit.convert_from_base(base_value)
        return Quantity(converted_value, target_unit)

    def convert_to(self, target_unit: Unit) -> "Quantity":
        """Alias for :meth:`to` for more explicit conversion semantics."""
        return self.to(target_unit)

    def __str__(self) -> str:
        return f"{self._value} - {self._unit}"

    def __repr__(self) -> str:
        return f"Quantity({self._value!r}, {self._unit!r})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Quantity) and self._unit == other._unit and self._value == other._value

    def __hash__(self) -> int:
        return hash((self._value, self._unit))

    def __bool__(self) -> bool:
        return self._value != 0

    def __neg__(self) -> float | int | complex:
        return -self._value

    def __abs__(self) -> float | int | complex:
        return abs(self._value)

    def __add__(self, other: float | int | complex) -> float | int | complex:
        if isinstance(other, self.__class__):
            return self._value + other._value
        return self._value + other

    def __radd__(self, other: float | int | complex) -> float | int | complex:
        if isinstance(other, self.__class__):
            return other._value + self._value
        return other + self._value

    def __sub__(self, other: float | int | complex) -> float | int | complex:
        if isinstance(other, self.__class__):
            return self._value - other._value
        return self._value - other

    def __rsub__(self, other: float | int | complex) -> float | int | complex:
        if isinstance(other, self.__class__):
            return other._value - self._value
        return other - self._value

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self._value * other._value
        return self._value * other

    def __rmul__(self, other: float | int | complex) -> float | int | complex:
        if isinstance(other, self.__class__):
            return other._value * self._value
        return other * self._value

    def __truediv__(self, other: float | int | complex) -> float | int | complex:
        if isinstance(other, self.__class__):
            return self._value / other._value
        return self._value / other

    def __rtruediv__(self, other):
        if isinstance(other, self.__class__):
            return other._value / self._value
        return other / self._value

    def __floordiv__(self, other: float | int | complex) -> float | int | complex:
        if isinstance(other, self.__class__):
            return self._value // other._value
        return self._value // other

    def __rfloordiv__(self, other):
        if isinstance(other, self.__class__):
            return other._value // self._value
        return other // self._value

    def __mod__(self, other):
        if isinstance(other, self.__class__):
            return self._value % other._value
        return self._value % other

    def __rmod__(self, other):
        if isinstance(other, self.__class__):
            return other._value % self._value
        return other % self._value

    def __pow__(self, other):
        if isinstance(other, self.__class__):
            return self._value ** other._value
        return self._value ** other

    def __rpow__(self, other):
        if isinstance(other, self.__class__):
            return other._value ** self._value
        return other ** self._value

class PhysicalConstant(Quantity):
    """Physical Constant class for fixed constants that can't be changed nor converted."""

    def __init__(self, value: float | int | complex, unit: Unit, name: str) -> None:
        super().__init__(value, unit)
        self._name = name

    @property
    def name(self) -> str:
        """Return the name of the constant."""
        return self._name

    @property
    def value(self) -> float:
        return self._value

    def __str__(self) -> str:
        return f"{self._name}: {self._value} - {self._unit}"

    def __repr__(self) -> str:
        return f"PhysicalConstant({self._value!r}, {self._unit!r}, {self._name!r})"


UNITS: dict[str, Unit] = {
    "am": Unit("Attometer", "Length", factor=1e-18),
    "fm": Unit("Femtometer", "Length", factor=1e-15),
    "pm": Unit("Picometer", "Length", factor=1e-12),
    "nm": Unit("Nanometer", "Length", factor=1e-9),
    "μm": Unit("Micrometer", "Length", factor=1e-6),
    "mm": Unit("Millimeter", "Length", factor=1e-3),
    "cm": Unit("Centimeter", "Length", factor=1e-2),
    "in": Unit("Inch", "Length", factor=0.0254),
    "dm": Unit("Decameter", "Length", factor=10.0),
    "ft": Unit("Foot", "Length", factor=0.3048),
    "Yd": Unit("Yard", "Length", factor=0.9144),
    "m": Unit("Meter", "Length", factor=1.0),
    "km": Unit("Kilometer", "Length", factor=1000.0),
    "mi": Unit("Mile", "Length", factor=1609.344),
    "ly": Unit("Light year", "Length", factor=9.4607e15),
    "psrc": Unit("Parsec", "Length", factor=3.0856775814913673e16),

    "m²": Unit("Square Meter", "Area", factor=1.0),
    "km²": Unit("Square Kilometer", "Area", factor=1e6),
    "ft²": Unit("Square Foot", "Area", factor=0.09290304),
    "acr": Unit("Acre", "Area", factor=4046.8564224),

    "mL": Unit("Milliliter", "Volume", factor=1e-6),
    "L": Unit("Liter", "Volume", factor=1e-3),
    "gal": Unit("Gallon", "Volume", factor=0.003785411784),
    "ft³": Unit("Cubic Foot", "Volume", factor=0.028316846592),
    "m³": Unit("Cubic Meter", "Volume", factor=1.0),

    "ag": Unit("Attogram", "Mass", factor=1e-18),
    "fg": Unit("Femtogram", "Mass", factor=1e-15),
    "pg": Unit("Picogram", "Mass", factor=1e-12),
    "ng": Unit("Nanogram", "Mass", factor=1e-9),
    "μg": Unit("Microgram", "Mass", factor=1e-6),
    "mg": Unit("Milligram", "Mass", factor=1e-3),
    "g": Unit("Gram", "Mass", factor=1e-3),
    "oz": Unit("Ounce", "Mass", factor=0.028349523125),
    "lb": Unit("Pound", "Mass", factor=0.45359237),
    "kg": Unit("Kilogram", "Mass", factor=1.0),
    "t": Unit("Ton", "Mass", factor=1000.0),
    "kt": Unit("Kiloton", "Mass", factor=1e6),
    "mt": Unit("Megaton", "Mass", factor=1e9),
    "gt": Unit("Gigaton", "Mass", factor=1e12),

    "ns": Unit("Nanosecond", "Time", factor=1e-9),
    "μs": Unit("Microsecond", "Time", factor=1e-6),
    "ms": Unit("Millisecond", "Time", factor=1e-3),
    "s": Unit("Second", "Time", factor=1.0),
    "min": Unit("Minute", "Time", factor=60.0),
    "h": Unit("Hour", "Time", factor=3600.0),
    "day": Unit("Day", "Time", factor=86400.0),
    "wk": Unit("Week", "Time", factor=604800.0),
    "yr": Unit("Year", "Time", factor=31536000.0),

    "J": Unit("Joule", "Energy", factor=1.0),
    "cal": Unit("Calorie", "Energy", factor=4.184),
    "kcl": Unit("Kilocalorie", "Energy", factor=4184.0),
    "kWh": Unit("Kilowatthour", "Energy", factor=3600000.0),
    "eV": Unit("Electronvolt", "Energy", factor=1.602176634e-19),

    "J*s": Unit("Joule Seconds", "Energy-Time", factor=1.0),

    "hp": Unit("Horsepower", "Power", factor=745.6998715822702),
    "W": Unit("Watt", "Power", factor=1.0),

    "N": Unit("Newton", "Force", factor=1.0),
    "kgf": Unit("Kg-force", "Force", factor=9.80665),
    "lbf": Unit("lb-force", "Force", factor=4.4482216152605),

    "deg": Unit("Degree", "Angles", factor=pi / 180.0),
    "rad": Unit("Radian", "Angles", factor=1.0),

    "Δv": Unit("Delta-V", "Change in Velocity"),
    "°K": Unit("Kelvin", "Temperature", factor=1.0),
    "°C": Unit("Celsius", "Temperature", factor=1.0, offset=273.15),
    "°F": Unit("Fahrenheit", "Temperature", factor=5.0 / 9.0, offset=255.37222222222223),

    "A": Unit("Ampere", "Current"),
    "V": Unit("Volt", "Voltage"),
    "Ω": Unit("Ohm", "Resistance"),
    "C": Unit("Coloumb", "Electric Charge"),
    "F": Unit("Farad", "Electric Capacitance"),
    "H": Unit("Henry", "Magnetic Capacitance"),
    "T": Unit("Tesla", "Magnetic Flux Density"),
    "G": Unit("Gauss", "Magnetic Flux Density"),

    "Hz": Unit("Hertz", "Frequency", factor=1.0),
    "kHz": Unit("Kilohertz", "Frequency", factor=1e3),
    "MHz": Unit("Megahertz", "Frequency", factor=1e6),
    "GHz": Unit("Gigahertz", "Frequency", factor=1e9),

    "pa": Unit("Pascal", "Pressure", factor=1.0),
    "psi": Unit("Psi", "Pressure", factor=6894.757293168361),
    "bar": Unit("Bar", "Pressure", factor=100000.0),
    "atm": Unit("Atmosphere", "Pressure", factor=101325.0),
    "torr": Unit("Torr", "Pressure", factor=133.32236842105263),
    "mmHg": Unit("mm Mercury", "Pressure", factor=133.32236842105263),

    "m/s": Unit("Meter/Second", "Velocity", factor=1.0),
    "mph": Unit("Miles/Hour", "Velocity", factor=0.44704),
    "km/h": Unit("Kilometer/Hour", "Velocity", factor=1000.0 / 3600.0),
    "knot": Unit("Knot", "Velocity", factor=0.5144444444444445),

    "m/s²": Unit("m/s²", "Acceleration", factor=1.0),
    "ft/s²": Unit("ft/s²", "Acceleration", factor=0.3048),

    "Nm": Unit("Newtonmeter", "Torque", factor=1.0),
    "ft-lb": Unit("Foot-pound", "Torque", factor=1.3558179483314004),

    "km/s/prsc": Unit("Kilometer/Second/Parsec", "Hubble's Constant"),

    "GCONST": Unit("Nm²/kg²", "The Gravitational Constant"),
    "NCONST": Unit("N/A", "Unit for Numerical / Unitless Constants"),
}
