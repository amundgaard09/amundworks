
class ImpossibleTriangleError(Exception): # Remove?
    """Raise when the sum of the angles of a triangle is not 180 degrees, a mathematical impossibility."""
    def __init__(self, *args):
        super().__init__("The sum of the angles of a triangle can't be anything else than 180 degrees!", args)

class NonSquareShapeError(Exception):
    def __init__(self, shape: tuple[int, int]):
        self.shape = shape
        super().__init__(f"ShapeError: expected square matrix, got shape {shape}.")
