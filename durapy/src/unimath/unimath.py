"""
The UniMath function library for the `DuraPy` library.
"""

import math
import sympy

from ..shared.constants import PI

def d2r(deg: float) -> float:
    """Return radians from degrees."""
    return float(deg / 180 * PI)
def r2d(rad: float) -> float:
    """Return degrees from radians."""
    return float(rad / PI * 180)

def avg(*args: int | float) -> float:
    """Return the average of the given arguments."""
    return sum(args) / len(args)

def fibonacci_integer(fib_idx: float) -> int:
    """Fibonacci integer generator that returns the Fibonacci integer at the given index."""

    try:
        fib_idx = int(fib_idx)
    except ValueError:
        raise ValueError("fibonacci_integer does not take floats or strings!")

    if fib_idx < 2:
        raise ValueError("fibonacci_integer does not take integers less than 2!")

    if fib_idx == 2:
        return 1

    fib0, fib1, fib2 = 0, 1, 1

    for _ in range(0, (fib_idx - 2)):
        fib2 = fib0 + fib1
        fib0, fib1 = fib1, fib2

    return fib2
def fibonacci_list(n: int) -> list[int]:
    """Fibonacci sequence generator that returns a list of the sequence up to the given length."""

    try:
        n = int(n)
    except ValueError:
        raise ValueError("fibonacci_integer does not take floats or strings!")

    if n < 2:
        raise ValueError("fibonacci_integer does not take integers less than 2!")

    if n == 2:
        return [0, 1]

    fib0, fib1, fiblist = 0, 1, [0, 1]

    for _ in range(0, (n - 2)):
        fib2 = fib0 + fib1
        fib0, fib1 = fib1, fib2
        fiblist.append(fib2)

    return fiblist

def lovelace(a: float, b: float, c: float, d: float, e: float, f: float) -> tuple:
    """Lovelace's algorithm for solving systems of linear equations."""
    if a*e == b*d:
        raise ValueError("The system has no unique solution.")

    x = c*e - b*f / (a*e - b*d)
    y = a*f - c*d / (a*e - b*d)
    return (x, y)

def interpolate_triangle(a: float, b: float, c: float, A: float | None = None, B: float | None = None, C: float | None = None) -> tuple[float, tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    """
    Extrapolate the sides of a triangle from the AAAS case (3x Angle + 1x Side)

    Returns
    -------
        Area, (A, B, C), (a, b, c), (sin(a), sin(b), sin(c))
    """

    if sum((a, b, c)) != 180:
        raise ValueError("A triangles angles can't sum to anything other than 180 degrees!")

    sin_A = math.sin(d2r(a))
    sin_B = math.sin(d2r(b))
    sin_C = math.sin(d2r(c))

    if A and not B and not C:
        B = (A * sin_B) / sin_A
        C = (A * sin_C) / sin_A

    elif B and not A and not C:
        A = (B * sin_A) / sin_B
        C = (B * sin_C) / sin_B

    elif C and not A and not B:
        A = (C * sin_A) / sin_C
        B = (C * sin_B) / sin_C

    else:
        raise ValueError("A, B, and C cannot all be None!")

    area = herons_formula(A, B, C)

    return area, (A, B, C), (a, b, c), (sin_A, sin_B, sin_C)

def pythagoras(a: float | None = None, b: float | None = None, c: float | None = None) -> float:
    """
    Calculates the missing side of a right-angled triangle using either normal or reverse pythagoras.
    Formula: `A² + B² = C²` for normal, and `A² = C² - B²` or  `B² = C² - A²` for reverse.

    The function can take in any two sides and will return the missing side. If more than one side is missing, the function will return `None`. Same thing when 3 values are given.
    """

    if not a and b and c:
        return math.sqrt(c**2 - b**2)
    elif a and not b and c:
        return math.sqrt(c**2 - a**2)
    elif a and b and not c:
        return math.sqrt(a**2 + b**2)
    else:
        raise ValueError("Pythagoras requires exactly two sides to be known.")


def cosine_rule(len_A: float, len_B: float, angle_A: float) -> float:
    return math.sqrt(len_A ** 2 + len_B ** 2 - ((2 * len_A * len_B) * math.cos(d2r(angle_A))))
def reverse_cosine_rule(len_A: float, len_B: float, len_C: float) -> tuple[float, float, float]:
    """
    Returns a tuple of the three angles in degrees, in the order of AngleA, AngleB, and AngleC.

    Formula:
        Angle A = arccos( ( B² + C² - A² ) / ( 2 * B * C ) )
    """

    return (
        r2d(math.acos((len_B ** 2 + len_C ** 2 - len_A ** 2) / (2 * len_B * len_C))),  # AngleA
        r2d(math.acos((len_C ** 2 + len_A ** 2 - len_B ** 2) / (2 * len_C * len_A))),  # AngleB
        r2d(math.acos((len_A ** 2 + len_B ** 2 - len_C ** 2) / (2 * len_A * len_B)))   # AngleC
    )

def tangent_formula(func1: str, func2: str) -> list[str]:
    """Returns the tangent(s) between two functions by finding the points where the derivatives are equal and then calculating the slope of the tangent line at those points."""

    x = sympy.symbols('x')
    f1 = sympy.sympify(func1)
    f2 = sympy.sympify(func2)
    df1 = sympy.diff(f1, x)
    df2 = sympy.diff(f2, x)

    slope_eq = sympy.Eq(df1, df2)
    tan_points = sympy.solve(slope_eq, x)
    tangents = []

    for idx, point in enumerate(tan_points, 1):
        string = f"Tangent {idx} - point: {point} - y: {f1.subs(x, point)} - slope: {df1.subs(x, point)}"
        tangents.append(string)

    return tangents

def sas_area(a: float, b: float, C: float) -> float:
    """Returns the area of a triangle from two sides and the included angle."""
    if not all([a, b, C]):
        raise ValueError("sas_area needs three arguments!")
    return (0.5 * a * b * math.sin(math.radians(C)))
def herons_formula(a: float, b: float, c: float) -> float:
    """Returns the area of a triangle from the side lengths."""
    if not all([a, b, c]):
        raise ValueError("herons_formula needs three arguments!")
    S = (a + b + c) / 2
    return math.sqrt(S * (S - a) * (S - b) * (S - c))


def factorial(n: int) -> int:
    """Returns the factorial of a non-negative integer `n`."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    elif n == 0 or n == 1:
        return 1

    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def subfactorial(n: int) -> int:
    """Returns the subfactorial of a non-negative integer `n`."""
    if n < 0:
        raise ValueError("Subfactorial and Factorial are not defined for negative numbers.")
    return int(factorial(n) * sum((-1)**k / factorial(k) for k in range(n)))

def gcd(*ints: int) -> int:
    """Returns the greatest common divisor of the given integers."""
    return math.gcd(*ints)
def lcm(*ints: int) -> int:
    """Returns the least common multiple of the given integers."""
    return abs(math.prod(ints)) // gcd(*ints)

def prime_factorize(n: int) -> list[int]:
    """Returns the prime factorization of a number as a list of its prime factors."""
    factors = []
    div = 2

    while n >= 2:
        if n % div == 0:
            factors.append(div)
            n //= div
        else:
            div += 1

    return factors

def is_prime(n: int) -> bool:
    """Returns True if the number is prime, else returns False."""
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def is_perfect_square(n: int) -> bool:
    """Returns True if the number is a perfect square, else returns False."""
    if n < 0:
        return False
    return int(math.sqrt(n)) ** 2 == n
def is_perfect_cube(n: int) -> bool:
    """Returns True if the number is a perfect cube, else returns False."""
    if n < 0:
        return False
    return int(round(n ** (1/3))) ** 3 == n
def is_perfect_power(n: int) -> bool:
    """Returns True if the number is a perfect power - a number that can be expressed as an integer raised to an integer power - else returns False."""
    if n < 1:
        return False
    for b in range(2, int(math.log2(n)) + 1):
        a = round(n ** (1 / b))
        if a ** b == n:
            return True
    return False
def is_perfect_number(n: int) -> bool:
    """Returns True if the number is a perfect number - a number equal to the sum of its proper divisors - else returns False."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n
def is_abundant_number(n: int) -> bool:
    """Returns True if the number is an abundant number - a number for which the sum of its proper divisors is greater than the number itself - else returns False."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) > n
def is_deficient_number(n: int) -> bool:
    """Returns True if the number is a deficient number - a number for which the sum of its proper divisors is less than the number itself - else returns False."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) < n
def is_amicable_pair(a: int, b: int) -> bool:
    """Returns True if the numbers are an amicable pair - two numbers for which the sum of the proper divisors of each is equal to the other number - else returns False."""
    if a < 1 or b < 1:
        return False
    return sum(i for i in range(1, a) if a % i == 0) == b and sum(i for i in range(1, b) if b % i == 0) == a
def is_sociable_chain(chain: list[int]) -> bool:
    """Returns True if the numbers form a sociable chain - a sequence of numbers for which the sum of the proper divisors of each number is equal to the next number in the sequence, and the last number in the sequence is equal to the first number - else returns False."""
    if any(n < 1 for n in chain):
        return False
    return all(sum(i for i in range(1, n) if n % i == 0) == chain[(idx + 1) % len(chain)] for idx, n in enumerate(chain))
