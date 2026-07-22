# src/unimath/_maxcompute.pyi

import numpy as np
import numpy.typing as npt

ndarray_ = npt.NDArray[np.float64]

"""MX | MaxCompute C++ Accelerated Computation Platform"""

def mat_mat_mul(a: ndarray_, b: ndarray_) -> ndarray_:
    """Matrix-Matrix multiplication accelerated natively in C++.

    Expects two 2D NumPy arrays of float64.
    """
    ...

def mat_vec_mul(a: ndarray_, b: ndarray_) -> ndarray_:
    """Matrix-Vector multiplication accelerated natively in C++.

    Expects a 2D matrix array and a 1D vector array.
    """
    ...

def vec_mat_mul(a: ndarray_, b: ndarray_) -> ndarray_:
    """Vector-Matrix multiplication accelerated natively in C++.

    Expects a 1D vector array and a 2D matrix array.
    """
    ...

def dot_product(a: ndarray_, b: ndarray_) -> float:
    """Vector-dot product accelerated natively in C++.

    Expects two 1D vector arrays and returns a scalar float.
    """
    ...

def outer_product(a: ndarray_, b: ndarray_) -> ndarray_:
    """Vector-outer product accelerated natively in C++.

    Expects two 1D vector arrays and returns a 2D matrix array.
    """
    ...
