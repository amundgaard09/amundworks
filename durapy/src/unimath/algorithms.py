"""UniMath Algorithms Module"""

def lovelace(a: float, b: float, c: float, d: float, e: float, f: float) -> tuple:
    """Lovelace's algorithm for solving systems of linear equations."""
    if a*e == b*d:
        raise ValueError("The system has no unique solution.")

    x = c*e - b*f / (a*e - b*d)
    y = a*f - c*d / (a*e - b*d)
    return (x, y)
