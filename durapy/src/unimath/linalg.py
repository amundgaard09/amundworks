"""
Linear Algebra Type Library for the `DuraPy` package.

This module contains data types for linear algebra.

Data Types
----------

`NDVector` - N-dimensional vector.

`Matrix` - N*M-matrix.

`D4Tensor` - 4-dimensional tensor (A matrix of matrices.)
"""
from __future__ import annotations

import math
import copy
import random
import numpy as np

from typing import overload, Sequence, Any

from .decorators import requires_square#, requires_real
from ..shared.exceptions import ArgumentError
from _maxcompute import mat_mat_mul, mat_vec_mul, vec_mat_mul, dot_product, outer_product

USE_GPU = False

if USE_GPU:
    import cupy as xp # type: ignore
else:
    import numpy as xp

EPSILON = 1e-9

Real = int | float
Scalar = int | float | complex
Numerical = int | float | complex | xp.ndarray | list[float] | list[list[float]]

def is_close(a: Numerical, b: Numerical) -> bool:
    """Checks if two floats / list-like objects of floats are close"""

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b)

    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False

        return all(is_close(x, y) for x, y in zip(a, b))

    elif isinstance(a, xp.ndarray) and isinstance(b, xp.ndarray):
        return xp.allclose(a, b)

    else:
        return False

class NDVector:
    """
    `DuraPy` Dataclass for N-dimensional vectors.

    This class is to be used for applications where more than 3 dimensions in a vector is needed.
    Use the `D3Vector` class for 3-dimensional vectors.

    Args
    ----
    `components`: list[float] - The components of the vector, in order.
    """
    def __init__(self, components: Sequence[Scalar]):
        self.components: Sequence[Scalar] = components
        self.real_components = [component.real for component in components]
        self.imag_components = [component.imag for component in components if component.imag != 0]

    @property
    def magnitude(self) -> float:
        """The magnitude (length) of the vector. Uses the real components only."""
        return math.hypot(*self.real_components)

    @property
    def shape(self) -> tuple[int, int]:
        """The shape (dimension) of the vector."""
        return (len(self.components), 1)

    def __getitem__(self, idx: int) -> Scalar:
        return self.components[idx]
    def __setitem__(self, key: int, value: Scalar) -> None:
        temp = list(self.components)
        temp[key] = value
        self.components = temp
    def __format__(self, format_spec: str, /) -> str:
        return str(self.components)
    def __iter__(self):
        return iter(self.components)
    def __repr__(self) -> str:
        return f"<{(component for component in self.components)}>"
    def __str__(self) -> str:
        return str(self.components)
    def __abs__(self) -> NDVector:
        return NDVector([abs(component) for component in self.components])
    def __len__(self) -> int:
        return len(self.components)
    def __neg__(self) -> NDVector:
        return NDVector([-(component) for component in self.components])
    def __eq__(self, value: object) -> bool:
        if isinstance(value, NDVector):
            return (self.components == value.components)
        elif isinstance(value, list):
            return (self.components == value)
        return NotImplemented

    def __add__(self, other: Real | NDVector) -> NDVector:
        if isinstance(other, Real): # scalar addition
            return NDVector([self.components[i] + other for i in range(len(self.components))])
        if isinstance(other, NDVector): # vector addition
            return NDVector([self.components[i] + other.components[i] for i in range(len(self.components))])
        return NotImplemented
    def __radd__(self, other: Real | NDVector) -> NDVector:
        return self.__add__(other)

    def __sub__(self, other: Real | NDVector) -> NDVector:
        if isinstance(other, Real): # scalar subtraction
            return NDVector([self.components[i] - other for i in range(len(self.components))])
        if isinstance(other, NDVector): # vector subtraction
            return NDVector([self.components[i] - other.components[i] for i in range(len(self.components))])
        return NotImplemented
    def __rsub__(self, other: Real | NDVector) -> NDVector:
        if isinstance(other, Real): # scalar subtraction
            return NDVector([other - self.components[i] for i in range(len(self.components))])
        if isinstance(other, NDVector): # vector subtraction
            return NDVector([other.components[i] - self.components[i] for i in range(len(self.components))])
        return NotImplemented

    @overload
    def __mul__(self, other: Real) -> NDVector: ...
    @overload
    def __mul__(self, other: NDVector) -> float: ...
    def __mul__(self, other: Real | NDVector) -> NDVector | float:
        if isinstance(other, Real): # scalar multiplication
            return NDVector([other * self.components[i] for i in range(len(self.components))])
        if isinstance(other, NDVector): # vector multiplication | Dot product
            return dot_product(np.array(self.components), np.array(other.components))
        return NotImplemented
    def __rmul__(self, other: Real) -> NDVector:
        return self.__mul__(other)

    def __truediv__(self, other: Real | NDVector) -> NDVector:
        if isinstance(other, Real): # scalar division
            return NDVector([component / other for component in self.components])
        elif isinstance(other, NDVector): # vector division
            return NDVector([x / y for x, y in zip(self.components, other.components)])
        else:
            return NotImplemented
    def __rtruediv__(self, other: Real | NDVector) -> NDVector:
        if isinstance(other, Real): # scalar division
            return NDVector([other / component for component in self.components])
        elif isinstance(other, NDVector): # vector division
            return NDVector([y / x for y, x in zip(other.components, self.components)])
        else:
            return NotImplemented

    def __matmul__(self, other: NDVector | Matrix) -> Matrix:
        if isinstance(other, NDVector): # Outer product
            return Matrix(array=outer_product(np.array(self.components), np.array(other.components)).tolist())
        elif isinstance(other, Matrix):
            return Matrix(array=vec_mat_mul(np.array(self.components), np.array(other._array)).tolist())
        else:
            return NotImplemented

    @overload
    def __rmatmul__(self, other: NDVector) -> NDVector: ...
    @overload
    def __rmatmul__(self, other: Matrix) -> Matrix: ...
    def __rmatmul__(self, other: NDVector | Matrix) -> NDVector | Matrix:
        if isinstance(other, NDVector):
            return other.__rmatmul__(self) # Same as __matmul__, but with the arguments reversed
        elif isinstance(other, Matrix):
            return other.__matmul__(self)
        else:
            return NotImplemented

class Matrix:
    def __init__(self,
        array: list[list[float]]  | None = None,
        shape: tuple[int, int]    | None = None,
        randomfill: bool          | None = False,
        randtype:   type  = float,
        randrange:  tuple = (-1, 1),
        fill:       float = 0,
    ) -> None:
        """
        N*M-dimensional Matrix.

        Args
        ----
        `array`: list[list[float]] - The data to create the matrix from, unless empty or random values are preferred.

        `shape`: tuple[int, int] - Create an empty matrix with dimensions `Rows` x `Cols`

        `randomfill`: bool - Create a matrix filled with uniform values ranging from -1 and 1 unless otherwise specified with the `randrange` parameter.

        `randtype`: type - Specifies if the matrix should be filled with random integers or floats.

        `randrange`: tuple - Specifies the range for the `random`.`uniform` function.

        `fill`: float - Specifies what value to fill the matrix with, if not random.
        """
        if shape == (0, 0):
            raise ValueError("Matrix can't have 0 rows or columns!")

        if array and shape:
            raise ValueError("Both array and size parameters are provided! Only one should be specified.")

        if array is not None:
            if len(array) == 0 or any(len(row) != len(array[0]) for row in array):
                raise ValueError("Matrix must be rectangular and non-empty")

        if not shape and not array:
            raise ArgumentError("Missing array and size parameters! Matrix() needs atleast 1!")

        if array is not None:
            if len(array) == 0 or any(len(row) != len(array[0]) for row in array):
                raise ValueError("Matrix must be rectangular and non-empty")

        if array is None and shape:
            rows, cols = shape
            if randomfill:
                if randtype is float:
                    array = [[random.uniform(*randrange) for _ in range(cols)] for _ in range(rows)]
                elif randtype is int:
                    array = [[random.randint(*randrange) for _ in range(cols)] for _ in range(rows)]
                else:
                    array = [[0 for _ in range(cols)] for _ in range(rows)]

            else:
                array = [[fill for _ in range(cols)] for _ in range(rows)]

        self._array = array if array else [[0.0, 0.0], [0.0, 0.0]]
        self._rows = len(self._array)
        self._cols = len(self._array[0]) if self._rows > 0 else 0

    @property
    def shape(self) -> tuple[int, int]:
        """Returns the dimensions of the matrix in the format: (`rows`,`cols`)"""
        return self._rows, self._cols

    @property
    def elements(self) -> int:
        """Returns the total number of elements in the matrix."""
        return self._rows * self._cols

    @property
    def zeros(self) -> int:
        """Returns the number of elements which are zero."""
        _zeros = 0
        for row in self._array:
            for element in row:
                _zeros += 1 if element == 0 else 0
        return _zeros
    @property
    def nonzeros(self) -> int:
        """Returns the number of elements which are not zero."""
        _nonzeros = 0
        for row in self._array:
            for element in row:
                _nonzeros += 1 if element != 0 else 0
        return _nonzeros

    def __getitem__(self, idx: int) -> list:
        return self._array[idx]
    def __setitem__(self, key: int, value: list[float]) -> None:
        self._array[key] = value

    def set_row(self, idx: int, newrow: list) -> None:
        if len(newrow) != self._cols:
            raise ValueError("New row length doesn't match the dimensions of the matrix!")
        self[idx] = newrow
    def row(self, idx: int) -> list:
        return self[idx]
    def set_column(self, idx: int, newcolumn: list) -> None:
        if len(newcolumn) != self._rows:
            raise ValueError("New column length doesn't match the dimensions of the matrix!")
        for j in range(len(self._array)):
            self[j][idx] = newcolumn[j]
    def column(self, idx: int) -> list:
        return [self[j][idx] for j in range(len(self[0]))]

    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case '':
                return str(self)
            case '_':
                return str(self)
        return str(self)
    def __bool__(self) -> bool:
        return any(any(cell != 0 for cell in row) for row in self._array)
    def __iter__(self):
        return iter(self._array)
    def __repr__(self) -> str:
        return f"Matrix({self._array!r})"
    def __str__(self) -> str:
        return_str = ""
        for row in self:
            return_str += str(row) + "\n"

        return return_str
    def __neg__(self) -> Matrix:
        return Matrix([[-(self[idx1][idx2]) for idx2 in range(self._cols)] for idx1 in range(self._rows)])
    def __len__(self) -> int:
        return self._rows
    def __abs__(self) -> float:
        return math.sqrt(sum(cell * cell for row in self._array for cell in row))
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Matrix):
            return is_close(self._array, other._array) and self._rows == other._rows and self._cols == other._cols
        else:
            return self._array == other

    def __add__(self, other: Matrix | int | float) -> Matrix:
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrix summation only takes same-size dimensions!")
            return Matrix([[self[i][j] + other[i][j] for j in range(self._cols)] for i in range(self._rows)])
        elif isinstance(other, (int, float)):
            return Matrix([[self[i][j] + other for j in range(self._cols)] for i in range(self._rows)])
        return NotImplemented
    def __radd__(self, other: Matrix | int | float) -> Matrix:
        return self.__add__(other)

    def __sub__(self, other: Matrix | int | float) -> Matrix:
        if isinstance(other, Matrix):
            if self._rows != other._rows or self._cols != other._cols:
                raise ValueError("Matrix subtraction only takes same-size dimensions!")
            return Matrix([[self[i][j] - other[i][j] for j in range(self._cols)] for i in range(self._rows)])
        elif isinstance(other, (int, float)):
            return Matrix([[self[i][j] - other for j in range(self._cols)] for i in range(self._rows)])
        return NotImplemented
    def __rsub__(self, other: Matrix | int | float) -> Matrix:
        if not isinstance(other, Matrix):
            return NotImplemented # Cant subtract a matrix from a int/float
        return other.__sub__(self)

    def __mul__(self, other: int | float) -> Matrix:
        if isinstance(other, (int, float)):
            return Matrix([[self[i][j] * other for j in range(self._cols)] for i in range(self._rows)])
        return NotImplemented
    def __rmul__(self, other: int | float) -> Matrix:
        if isinstance(other, (int, float)):
            return self.__mul__(other) # Commutative
        return NotImplemented

    def __truediv__(self, other: int | float) -> Matrix:
        if isinstance(other, (int, float)):
            return Matrix([[self[i][j] / other for j in range(self._cols)] for i in range(self._rows)])
        return NotImplemented
    def __rtruediv__(self, other: Any):
        return NotImplemented # Cant divide something by a matrix

    @overload
    def __matmul__(self, other: Matrix) -> Matrix: ...
    @overload
    def __matmul__(self, other: NDVector) -> NDVector: ...
    def __matmul__(self, other: Matrix | NDVector) -> Matrix | NDVector:
        if isinstance(other, Matrix):
            return Matrix(array=mat_mat_mul(np.array(self._array), np.array(other._array)).tolist())

        elif isinstance(other, NDVector):
            return NDVector(components=mat_vec_mul(np.array(self._array), np.array(other.components)).tolist())

        else:
            return NotImplemented

    @overload
    def __rmatmul__(self, other: Matrix) -> Matrix: ...
    @overload
    def __rmatmul__(self, other: NDVector) -> NDVector: ...
    def __rmatmul__(self, other: Matrix | NDVector) -> Matrix | NDVector:
        return other.__matmul__(self) # only need to define one method

    @staticmethod
    def __sign(expr: float, idx: int) -> float:
        return expr * (-1) ** abs(idx)
    @staticmethod
    def __2x2_det(_array: list[list[float]]) -> float:
        if len(_array) == 2 and all(len(row) == 2 for row in _array):
            A, B, C, D = _array[0][0], _array[0][1], _array[1][0], _array[1][1]
            return (A * D) - (B * C)
        raise ValueError("Can't calculate a base case 2x2 determinant of a non-2x2 matrix!")
    @staticmethod
    def __minor_extract(arr: list[list[float]], row_idx: int, col_idx: int) -> Matrix:
        """Extracts the minor matrix by removing the specified row and column from the given array."""
        without_row = [arr[idx] for idx in range(len(arr)) if idx != row_idx]
        without_col = [[without_row[idx1][idx2] for idx2 in range(len(without_row[idx1])) if idx2 != col_idx] for idx1 in range(len(without_row))]
        return Matrix(array=without_col)

    @requires_square
    def _det(self) -> float:
        if self.shape == 2:
            return self.__2x2_det(self._array)
        if self.shape == 1:
            return self._array[0][0]

        detsum = 0.0

        for idx1, _ in enumerate(self[0]):
            minor = self.__minor_extract(self._array, 0, idx1)
            detsum += self.__sign((self[0][idx1] * self._det(minor)), idx1)

        return detsum

    @property
    def det(self) -> float:
        """
        Returns the determinant of the matrix through Laplace Expansion.

        The determinant is used to determine if the Matrix is invertible or singular (collapses space).
        """
        return self._det()

    def _T(self) -> Matrix:
        rows, cols = self.shape
        transpose = Matrix(shape=(cols, rows))
        for i in range(rows):
            for j in range(cols):
                transpose[i][j] = self[j][i]

        return transpose
    @property
    def T(self) -> Matrix:
        """
        Returns the transposed matrix of itself.

        A transposed matrix is the original matrix but with its rows and columns swapped,
        so one element in the original matrix - `A[I][J]` becomes `A[J][I]` in the transpose.
        It is as if the matrix was rotated around its diagonal from the top-left to bottom-right.
        """
        return self._T()


    def __build_augmented(self) -> Matrix:
        """Builds the augmented matrix by concatenating the original matrix with its identity matrix."""
        n = self.shape[0]
        i = self.to_identity()

        aug = Matrix(
            array = [[0 for _ in range(2 * n)] for _ in range(n)],
        )

        for j in range(n):
            for k in range(n):
                aug[j][k] = self[j][k]
                aug[j][k + n] = i[j][k]

        return aug

    @requires_square
    def _inverse(self) -> Matrix | None:
        if self.det == 0:
            return None

        n = self.shape[0]
        aug = self.__build_augmented()


        for i in range(n):
            pivot = aug[i][i]

            if pivot == 0:
                for j in range(i + 1, n):
                    if aug[j][i] != 0:
                        aug[i], aug[j] = aug[j], aug[i]
                        pivot = aug[i][i]
                        break

            if pivot == 0:
                return None

            aug[i] = [x / pivot for x in aug[i]]

            for j in range(n):
                if j != i:
                    factor = aug[j][i]
                    aug[j] = [aug[j][k] - factor * aug[i][k] for k in range(2 * n)]

        inverse = [row[n:] for row in aug]
        return Matrix(inverse)
    @property
    def inverse(self) -> Matrix | None:
        """
        Returns the inverse of the matrix through Gauss-Jordan elimination.

        The inverse of a matrix `A`, `A^-1`, satisfies the following equation:

        `A` * `A^-1` = `A^-1` * `A` = `I`,

        where `I` is the identity matrix of the same dimensions.
        """
        return self._inverse()

    @requires_square
    def _rank(self) -> int:
        """
        Returns the rank of the matrix via Gaussian Elimination.

        The rank is the number of linearly independent rows or columns in the matrix.
        """
        A = copy.deepcopy(self)
        N = A.shape[0]

        rank, row_idx = N, 0

        for col in range(N):
            pivot_row_idx = row_idx
            while pivot_row_idx < N and abs(A[pivot_row_idx][col]) < EPSILON:
                pivot_row_idx += 1

            if pivot_row_idx == N:
                rank -= 1
                continue

            if pivot_row_idx != row_idx:
                A[row_idx], A[pivot_row_idx] = A[pivot_row_idx], A[row_idx]

            for i in range(row_idx + 1, N):
                factor = (A[i][col] / A[row_idx][col])
                for J in range(col, N):
                    A[i][J] -= factor * A[row_idx][J]

            row_idx += 1

            if row_idx == N:
                break

        return rank
    @property
    def rank(self) -> int:
        """The Matrix Rank. Uses Gaussian Elimination to find the number of linearly independent rows."""
        return self._rank()

    @staticmethod
    def __QR_decomp(A: Matrix) -> tuple[Matrix, Matrix]:
        """QR decomposition via modified Gram-Schmidt process."""
        N = A.shape[0]
        Q = Matrix(shape=(N, N))
        R = Matrix(shape=(N, N))

        # Iteratively build Q and R matrices
        for J in range(N):
            v = A.column(J)

            # Orthogonalize v against previous columns in Q
            for i in range(J):
                QI = Q.column(i)
                R[i][J] = sum(x * y for x, y in zip(QI, A.column(J)))
                v = [(v[idx] - R[i][J] * QI[idx]) for idx in range(N)]

            # Normalize v to get the next column of Q and R
            norm = math.sqrt(sum(x**2 for x in v))
            R[J][J] = norm

            # Set the next column of Q to the normalized v, or zero if norm is too small
            if norm > 1e-12:
                Q.set_column(J, [x / norm for x in v])
            else:
                Q.set_column(J, [0.0] * N)

        # Return the Q and R matrices
        return Q, R

    @requires_square
    def _eigen(self, max_iters: int = 150) -> tuple[list[float], Matrix]:
        n = self.shape[0]
        Ak = Matrix([[self[r][c] for c in range(n)] for r in range(n)])
        i = Matrix(shape=(n, n)).to_identity()

        # Iteratively apply QR decomposition to converge on eigenvalues
        for _ in range(max_iters):
            Q, R = self.__QR_decomp(Ak)

            # Update Ak and i to converge on eigenvalues
            Ak = R @ Q
            i = i @ Q

            # Check for convergence (off-diagonal elements should be small)
            off_diagonal_sum = 0.0
            for r in range(n):
                for c in range(n):
                    if r != c:
                        off_diagonal_sum += abs(Ak[r][c])

            # If off-diagonal elements are small, we've converged
            if off_diagonal_sum < EPSILON:
                break

        # Extract eigenvalues and eigenvectors
        eigenvals = [Ak[i][i] for i in range(n)]
        return eigenvals, i
    @property
    def eigen(self) -> tuple[list[float], Matrix]:
        """
        Computes eigenvalues and eigenvectors using the iterative QR algorithm.

        Returns
        -------
        - `list[float]`: The eigenvalues
        - `SquareMatrix`: A matrix where columns represent the corresponding eigenvectors
        """
        return self._eigen()

    @requires_square
    def _trace(self) -> float:
        return sum(self[idx][idx] for idx in range(len(self._array)))

    @property
    def trace(self) -> float:
        """
        Returns the trace of the matrix.

        The trace is defined as the sum of all the elements on the diagonal, e. g. `A_00`, `A_11`, `A_22`, etc.
        """
        return self._trace()

    @property
    def diagonal(self) -> list:
        """Returns the diagonal of the matrix as a list."""
        return [self[idx][idx] for idx in range(self.shape[0])]

    @requires_square
    def to_identity(self) -> Matrix:
        """Matrix constructor that returns the identity matrix of the given size."""
        matrix = Matrix(shape=self.shape)
        for idx in range(self.shape[0]):
            matrix[idx][idx] = 1

        return matrix

    @requires_square
    def is_singular(self) -> bool:
        """Returns if the matrix is singular, which is a matrix with a determinant of 0."""
        return (self.det == 0)
    @requires_square
    def is_identity(self) -> bool:
        """Returns if the matrix is equal to the identity matrix of the same dimension."""
        return self == Matrix(shape=self.shape).to_identity()
    @requires_square
    def is_diagonal(self) -> bool:
        """Returns if the matrix is diagonal.

        A diagonal matrix is a matrix where all the elements outside of the leading diagonal is 0.
        The identity matrix is a common example.
        """
        for idx1 in range(self.shape[0]):
            for idx2 in range(self.shape[1]):
                if idx1 != idx2 and self[idx1][idx2] != 0:
                    return False
                else:
                    continue
        return True
    @requires_square
    def is_symmetric(self) -> bool:
        """Returns if the matrix is symmetric, which is a matrix that is equal to its transpose."""
        return (self == self.T)
    @requires_square
    def is_nilpotent(self) -> bool:
        """Returns True if the matrix raised to some power becomes a zero matrix."""
        return all(value == 0 for value in self.eigen[0]) and self.det == 0
    @requires_square
    def is_idempotent(self) -> bool:
        """Returns True if the matrix multiplied by itself equals itself: `A^2` = `A`."""
        return (self == self @ self)
    @requires_square
    def is_orthogonal(self) -> bool:
        """Returns if the matrix is orthogonal, which is a matrix whose transpose is equal to its inverse."""
        return (self.T == self.inverse)
    @requires_square
    def is_invertible(self) -> bool:
        """Returns if the matrix is invertible, which is a matrix whose determinant is not 0."""
        return (self.det != 0)
    @requires_square
    def is_skew_symmetric(self) -> bool:
        """
        Returns if the matrix is skew-symmetric.

        A skew-symmetric matrix is a matrix whose transpose is equal to its negative.
        """
        return (self.T == -(self))
    @requires_square
    def is_upper_triangular(self) -> bool:
        """
        Returns if the matrix is upper triangular.

        An upper triangular matrix is a matrix whose elements below the leading diagonal are all 0.
        """
        for idx1 in range(1, self.shape[0]):
            for idx2 in range(idx1):
                if self[idx1][idx2] != 0:
                    return False
        return True
    @requires_square
    def is_lower_triangular(self) -> bool:
        """
        Returns if the matrix is lower triangular.

        An lower triangular matrix is a matrix whose elements above the leading diagonal are all 0.
        """
        for idx1 in range(self.shape[0]):
            for idx2 in range(idx1 + 1, self.shape[1]):
                if self[idx1][idx2] != 0:
                    return False
        return True
    @requires_square
    def is_positive_definite(self) -> bool:
        """
        Returns True if all eigenvalues are strictly positive.
        """
        return all(value > 0 for value in self.eigen[0])

class Tensor:
    def __init__(self, array: xp.ndarray, requires_grad: bool = False):
        """
        `Tensor` Dataclass for Machine Learning.

        Args
        ----
        `array`: xp.ndarray - The data to create the matrix from.
        """
        if array.ndim != 4 or array.size == 0:
            raise ValueError("Tensor must be 4-dimensional and non-empty")

        self.array = array
        self.requires_grad = requires_grad
        self.grad = xp.zeros_like(array) if requires_grad else None

        self._parents = []
        self._backward = lambda: None

    def __getitem__(self, idx: int) -> list:
        return self.array[idx]
    def __setitem__(self, key: int, value: list[float]) -> None:
        self.array[key] = value
    def __bool__(self) -> bool:
        return bool(xp.any(self.array != 0))
    def __iter__(self):
        return iter(self.array)
    def __repr__(self) -> str:
        return f"D4Tensor({self.array!r})"
    def __len__(self) -> int:
        return len(self.array)
    def __abs__(self) -> float:
        return float(xp.linalg.norm(self.array))
    def __neg__(self) -> Tensor:
        return Tensor(-self.array)
    def __eq__(self, other) -> bool:
        if isinstance(other, Tensor):
            return is_close(self.array, other.array) and self.dim == other.dim
        else:
            return self.array == other

    def __add__(self, other) -> Tensor:
        if isinstance(other, Tensor):
            if self.dim != other.dim:
                raise ValueError("Tensor summation only takes same-size dimensions!")
            return Tensor(self.array + other.array)
        return NotImplemented
    def __radd__(self, other) -> Tensor:
        return self.__add__(other)
    def __sub__(self, other) -> Tensor:
        if isinstance(other, Tensor):
            if self.dim != other.dim:
                raise ValueError("Tensor subtraction only takes same-size dimensions!")
            return Tensor(self.array - other.array)
        return NotImplemented
    def __rsub__(self, other) -> Tensor:
        if isinstance(other, Tensor):
            if self.dim != other.dim:
                raise ValueError("Tensor subtraction only takes same-size dimensions!")
            return Tensor(other.array - self.array)
        return NotImplemented
    def __mul__(self, other) -> Tensor:
        if isinstance(other, (int, float)):
            return Tensor(self.array * other)
        return NotImplemented
    def __rmul__(self, other) -> Tensor:
        if isinstance(other, (int, float)):
            return Tensor(self.array * other)
        return NotImplemented
    def __matmul__(self, other) -> Tensor:
        if isinstance(other, Tensor):
            return Tensor(self.array @ other.array)
        return NotImplemented
    def __rmatmul__(self, other) -> Tensor:
        if isinstance(other, Tensor):
            return Tensor(other.array @ self.array)
        return NotImplemented
    def __truediv__(self, other) -> Tensor:
        if isinstance(other, (int, float)):
            return Tensor(self.array / other)
        return NotImplemented
    def __rtruediv__(self, other):
        return NotImplemented

    @property
    def dim(self) -> xp.ndarray:
        """Returns the dimensions of the matrix."""
        return self.array.shape

    @property
    def elements(self) -> int:
        """Returns the total number of elements in the matrix."""
        return self.array.size

    @property
    def zeros(self) -> int:
        """Returns the number of elements which are zero."""
        return int(xp.sum(self.array == 0))

    @property
    def nonzeros(self) -> int:
        """Returns the number of elements which are not zero."""
        return int(xp.sum(self.array != 0))

def rot_x(θ: float) -> Matrix:
    """Returns the rotation matrix for a rotation around the x-axis by the given angle in degrees."""
    θ = math.radians(θ)
    return Matrix([
        [1, 0,            0          ],
        [0, math.cos(θ), -math.sin(θ)],
        [0, math.sin(θ),  math.cos(θ)]
    ])
def rot_y(θ: float) -> Matrix:
    """Returns the rotation matrix for a rotation around the y-axis by the given angle in degrees."""
    θ = math.radians(θ)
    return Matrix([
        [math.cos(θ),  0,  math.sin(θ)],
        [0,            1,  0          ],
        [-math.sin(θ), 0,  math.cos(θ)]
    ])
def rot_z(θ: float) -> Matrix:
    """Returns the rotation matrix for a rotation around the z-axis by the given angle in degrees."""
    θ = math.radians(θ)
    return Matrix([
        [math.cos(θ), -math.sin(θ), 0],
        [math.sin(θ),  math.cos(θ), 0],
        [0,            0,           1]
    ])
