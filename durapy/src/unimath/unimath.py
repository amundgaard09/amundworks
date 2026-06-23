"""
The UniMath function library for the `DuraPy` library.
"""

import math, sympy

from ..frameworks.color_sys import color_text as _ct
from ..commons import exceptions, constants
from typing import Literal

PI = constants.PI

def D2R(deg: float) -> float:
    """Return radians from degrees."""
    return deg / 180 * PI
def R2D(rad: float) -> float:
    """Return degrees from radians."""
    return rad / PI * 180

def avg(*args) -> float:
    return sum(args) / len(args)

def fibonacci_list(list_len: float) -> list[int]:
    """Fibonacci sequence generator that returns a list of the sequence up to the given length."""
    
    try:
        list_len = int(list_len)  
    except ValueError:
        raise ValueError("FibonacciInteger does not take floats or strings!")      
    
    fib0, fib1 = 0, 1
    fib_list = [fib0, fib1]
    
    if list_len < 2:
        raise ValueError("FibonacciList does not take integers less than 2!")
    
    for _ in range(0, (list_len - 2)):
        fib2 = fib0 + fib1
        fib0, fib1 = fib1, fib2
        fib_list.append(fib2)
        
    return fib_list  
 
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

def lovelace(a: float, b: float, c: float, d: float, e: float, f: float) -> tuple:
    """Lovelace's algorithm for solving systems of linear equations."""
    if a*e == b*d: 
        raise ValueError("The system has no unique solution.")
    
    Dx = c*e - b*f
    Dy = a*f - c*d
    x = Dx / (a*e - b*d)
    y = Dy / (a*e - b*d)
    return (x, y)

def extrapolate_triangle(a: float, b: float, c: float, A: float | None = None, B: float | None = None, C: float | None = None) -> tuple[float, tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    """
    Extrapolate the sides of a triangle from the AAAS case (3x Angle + 1x Side)
    
    Returns
    -------
        Area, (A, B, C), (a, b, c), (sin(a), sin(b), sin(c))
    """

    if sum((a, b, c)) != 180:
        raise exceptions.ImpossibleTriangleError

    sin_A = math.sin(D2R(a))
    sin_B = math.sin(D2R(b))
    sin_C = math.sin(D2R(c))

    if A is not None:
        B = (A * sin_B) / sin_A
        C = (A * sin_C) / sin_A
        
    elif B is not None:
        A = (B * sin_A) / sin_B
        C = (B * sin_C) / sin_B
        
    elif C is not None:
        A = (C * sin_A) / sin_C
        B = (C * sin_B) / sin_C
    
    area = herons_formula(A, B, C)
    
    return (area, (A, B, C), (a, b, c), (sin_A, sin_B, sin_C))
def pythagoras(A: float | None = None, B: float | None = None, C: float | None = None) -> float:
    """
    Calculates the missing side of a right-angled triangle using either normal or reverse pythagoras.
    Formula: `A² + B² = C²` for normal, and `A² = C² - B²` or  `B² = C² - A²` for reverse.
    
    The function can take in any two sides and will return the missing side. If more than one side is missing, the function will return `None`. Same thing when 3 values are given.
    """
    
    if (A, B, C).count(None) > 1:
        return None
    
    if A is None:
        return math.sqrt(C**2 - B**2)
    elif B is None:
        return math.sqrt(C**2 - A**2)
    elif C is None:
        return math.sqrt(A**2 + B**2)
    
def sine_rule(
    Sides: list[float | None],
    Angles: list[float | None],
    AngleMeasurementMode: Literal["Degrees", "Radians"]
    ) -> list[list[float], list[float]] | None:
    """
    The Sine Rule calculation function. Takes in 

    Formula:
    `A / sin(a)` = `B / sin(b)` = `C / sin(c)`

    Return Format: [Angles: [A, B, C], Sides: [A, B, C]]
    """
    
    ### VERY UNSTABLE!
    
    angles_rad = []
    ReferenceRatio = None
    
    # Convert angles to radians if they are in degrees, and keep them as is if they are already in radians. If an angle is None, keep it as None.
    for angle in Angles:
        if angle is not None and AngleMeasurementMode == "Degrees":
            angles_rad.append(D2R(angle))
        else:
            angles_rad.append(angle)

    known_angle_indices = [i for i in range(3) if angles_rad[i] is not None]
    
    # If two angles are known, calculate the third angle using the fact that the sum of angles in a triangle is 180 degrees (or π radians).
    if len(known_angle_indices) == 2:
        missing = next(i for i in range(3) if angles_rad[i] is None)
        angles_rad[missing] = PI - sum(angles_rad[i] for i in known_angle_indices)
    
    # Find the first known side and angle to establish the reference ratio for the Sine Rule
    for idx in range(3):
        if Sides[idx] is not None and angles_rad[idx] is not None:
            ReferenceRatio = Sides[idx] / math.sin(angles_rad[idx])
            break
    
    # If the reference couldn't be established, return None
    if ReferenceRatio is None:
        return None

    # Loop through the sides and angles to calculate the missing values using the Sine Rule
    for idx in range(3):
        if Sides[idx] is None and angles_rad[idx] is not None:
            Sides[idx] = ReferenceRatio * math.sin(angles_rad[idx])
        elif angles_rad[idx] is None and Sides[idx] is not None:
            value = Sides[idx] / ReferenceRatio
            if not -1 <= value <= 1:
                return None
            asin_val = math.asin(value)
            known_sum = sum(a for a in angles_rad if a is not None)
            
            # Check for the ambiguous case of the sine rule, where there may be two possible angles that satisfy the equation
            if PI - asin_val + known_sum <= PI:
                angles_rad[idx] = PI - asin_val
            else:
                angles_rad[idx] = asin_val

    # Return in specified unit
    if AngleMeasurementMode == "Degrees":
        Angles_out = [R2D(a) if a is not None else None for a in angles_rad]
    else:
        Angles_out = angles_rad

    return [Angles_out, Sides]
def cosine_rule(len_A: float, len_B: float, angle_A: float) -> float:
    return math.sqrt(len_A ** 2 + len_B ** 2 - ((2 * len_A * len_B) * math.cos(D2R(angle_A))))
def reverse_cosine_rule(len_A: float, len_B: float, len_C: float) -> tuple[float, float, float]:
    """ 
    Returns a tuple of the three angles in degrees, in the order of AngleA, AngleB, and AngleC.
    
    Formula:
        Angle A = arccos( ( B² + C² - A² ) / ( 2 * B * C ) )
    """

    return (
        R2D(math.acos((len_B ** 2 + len_C ** 2 - len_A ** 2) / (2 * len_B * len_C))),  # AngleA
        R2D(math.acos((len_C ** 2 + len_A ** 2 - len_B ** 2) / (2 * len_C * len_A))),  # AngleB
        R2D(math.acos((len_A ** 2 + len_B ** 2 - len_C ** 2) / (2 * len_A * len_B)))   # AngleC
    )

def SAS_area(len_A: float, len_B: float, angle_C: float) -> float:
    """
    Returns the area of a triangle from two sides and the included angle.
    Formula: `Area = 0.5 * LengthA * LengthB * sin(AngleC)` where AngleC is in degrees.
    """
    return (0.5 * len_A * len_B * math.sin(D2R(angle_C)))
def herons_formula(len_A: float, len_B: float, len_c: float) -> float:
    """
    Returns the area of a triangle from the side lengths.
    Formula::

        S: float = (LengthA + LengthB + LengthC) / 2
        Area: float = math.sqrt(S * (S - LengthA) * (S - LengthB) * (S - LengthC))

    """
    S = (len_A + len_B + len_c) / 2
    return math.sqrt(S * (S - len_A) * (S - len_B) * (S - len_c))

def slope(x1: float, y1: float, x2: float, y2: float) -> float:
    """Returns the slope of a line from two points `(x1, y1)` and `(x2, y2)`"""
    return (y2 - y1) / (x2 - x1)
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the distance between two points `(x1, y1)` and `(x2, y2)`"""
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
def derivative(func: str, x: float | None = None, h: float = 1e-5) -> float:
    """Returns `f'(x)` if `x` is not given, else returns the numerical derivative of the function at the given x-value using the definition of the derivative."""
    x_sym = sympy.symbols('x')
    f = sympy.sympify(func)
    if x is None:
        return sympy.diff(f, x_sym)
    else:
        return (f.subs(x_sym, x + h) - f.subs(x_sym, x - h)) / (2 * h)

def line_intersection(m1: float, b1: float, m2: float, b2: float) -> tuple[float, float]:
    """"Return the point of intersection of two lines in the form of `(x, y)`"""
    x = (b2 - b1) / (m1 - m2)
    y = m1*x + b1
    return (x, y)
def line_from_points(x1: float, y1: float, x2: float, y2: float) -> tuple[float, float]:
    """Returns `m`, `b` as parts of the equation `y = mx + b` from the two given points `(x1, y1)` and `(x2, y2)`."""
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return (m, b)
def linear_zero(m: float, b: float) -> float:
    """Find the x-value where the line `y = mx + b` crosses the x-axis"""
    return -b / m
def linear_evaluation(m: float, b: float, x: float) -> float:
    return m*x + b   

def quadratic_vertex(a: float, b: float, c: float) -> tuple[tuple[float, float], str]:
    """Returns the vertex (aka the minimum/maximum point) of a quadratic function in the form of `(x, y)`."""
    xv = -b / (2*a)
    yv = quadratic_evaluation(a, b, c, xv)

    return (xv, yv), f"{'Minimum' if a > 0 else 'Maximum' if a < 0 else 'Linear'}"
def quadratic_num_roots(a: float, b: float, c: float) -> int:
    """Returns the number of roots of a quadratic function based on the discriminant."""
    D = b**2 - 4*a*c
    return 2 if D > 0 else 1 if D == 0 else 0
def quadratic_solutions(A: float, B: float, C: float) -> tuple[float, float] | tuple[float] | None:
    """Solves quadratic equations and returns x-values in a tuple."""
    if A == 0:
        return ValueError("Invalid quadratic equation! A cannot be 0.")
    D = B**2 - 4*A*C
    if D > 0:
        x1 = (-B - math.hypot(0, D)) / (2 * A)
        x2 = (-B + math.hypot(0, D)) / (2 * A)
        return (x1, x2)
    
    elif D == 0:
        x1 = -B / (2 * A)
        return (x1)
    else: 
        return None
def quadratic_factorized(a: float, b: float, c: float) -> str:
    """Returns the factorized form of a quadratic function in the form of `a(x - x1)(x - x2)` where `x1` and `x2` are the roots of the function."""
    D = b**2 - 4*a*c
    
    def sign(val: float) -> str:
        return "-" if val < 0 else "+"
    
    if D > 0:
        x1 = (-b - math.hypot(0, D)) / (2 * a)
        x2 = (-b + math.hypot(0, D)) / (2 * a)
        return f"{a}(x {sign(x1)} {x1})(x {sign(x2)} {x2})"
    
    elif D == 0:
        x1 = -b / (2 * a)
        return f"{a}(x {sign(x1)} {x1})^2"
    else: 
        return _ct('No real solutions', 'red')
def quadratic_evaluation(a: float, b: float, c: float, x: float) -> float:
    return a*x**2 + b*x + c

def cubic_vertex(a: float, b: float, c: float, d: float) -> list:
    """Returns the vertex (aka the minimum/maximum point) of a cubic function in the form of `(x, y)`."""
    x = sympy.symbols('x')
    f = sympy.sympify(f"{a}*x**3 + {b}*x**2 + {c}*x + {d}")
    dif = sympy.diff(f, x)
    critical_points = sympy.solve(dif, x)
    
    vertices = []
    for point in critical_points:
        y = f.subs(x, point)
        vertices.append((point, y))
    
    return vertices
def cubic_num_roots(a: float, b: float, c: float, d: float) -> int:
    """Returns the number of roots of a cubic function based on the discriminant."""
    D = 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2
    return 3 if D > 0 else 2 if D == 0 else 1
def cubic_solutions(a: float, b: float, c: float, d: float) -> list:
    """Returns the roots of a cubic function in a tuple."""
    x = sympy.symbols('x')
    f = sympy.sympify(f"{a}*x**3 + {b}*x**2 + {c}*x + {d}")
    solutions = sympy.solve(f, x)
    return solutions
def cubic_zeros(a: float, b: float, c: float, d: float) -> list:
    """Returns the x-values where the cubic function crosses the x-axis."""
    x = sympy.symbols('x')
    f = sympy.sympify(f"{a}*x³ + {b}*x² + {c}*x + {d}")
    zeros = sympy.solve(f, x)
    return zeros
def cubic_evaluation(a: float, b: float, c: float, d: float, x: float) -> float:
    """Evaluate a cubic polynomial."""
    result = a*x**3 + b*x**2 + c*x + d
    return result
def cubic_evaluation_bruteforce(a: float, b: float, c: float, d: float, lower: int, upper: int, plot: bool = False) -> list[float]:
    """Brute Force evaluation of a third-degree polynomial. The function checks all evaluations from `LowerBound` to `UpperBound` and highlights roots as green, as well as plotting the given function if wanted."""
    x_vals, y_vals, roots = [], [], []
    
    for x in range(int(lower), int(upper+1)):
        result = cubic_evaluation(a, b, c, d, x)
        x_vals.append(x)
        y_vals.append(result)
        roots.append(x) if result == 0 else None
        
    return roots

### UNSTABLE - ALPHA - DO NOT USE
def tangent_formula(Function1: str, Function2: str) -> list[str]:
    """Returns the tangent(s) between two functions by finding the points where the derivatives are equal and then calculating the slope of the tangent line at those points."""
    x = sympy.symbols('x')
    f1 = sympy.sympify(Function1)
    f2 = sympy.sympify(Function2)

    df1 = sympy.diff(f1, x)
    df2 = sympy.diff(f2, x)

    slope_eq = sympy.Eq(df1, df2)
    tangent_points = sympy.solve(slope_eq, x)

    tangents = []
    for idx, point in enumerate(tangent_points, 1):
        string = f"Tangent {idx} - point: {point} - y: {f1.subs(x, point)} - slope: {df1.subs(x, point)}"
        tangents.append(string) 

    return tangents

def prime_factorize(num: int) -> list[int]:
    """Returns the prime factorization of a number as a list of its prime factors."""
    factors = []
    div = 2
    
    while num >= 2:
        if num % div == 0:
            factors.append(div)
            num //= div
        else:
            div += 1
            
    return factors

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
    return int(factorial(n) * sum((((-1)**k) / factorial(k)) for k in range(n)))

def gcd(x: int, y: int) -> int:
    pass
def lcm(x: int, y: int) -> int:
    pass

def polygon_area(n: int) -> float:
    pass
def polygon_circumference(n: int) -> float:
    pass