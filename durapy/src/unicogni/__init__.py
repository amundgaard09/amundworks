"""
The `DuraPy` `UniPy` `UniCogni` module provides a collection of functions and classes for Machine Learning.
"""

from .unicogni import (
    relu, d_relu, leaky_relu, d_leaky_relu,
    gelu, d_gelu,
    silu, d_silu,
    prelu, dx_prelu, da_prelu,
    cdelu, d_cdelu,
    sigmoid, d_sigmoid,
    tanh, d_tanh,
    swish, d_swish,
    mish, d_mish,
    softmax,
    mae, mse, rmse,
    cross_entropy_loss,
)


__all__ = [
    "relu", "d_relu", "leaky_relu", "d_leaky_relu",
    "gelu", "d_gelu",
    "silu", "d_silu",
    "prelu", "dx_prelu", "da_prelu",
    "cdelu", "d_cdelu",
    "sigmoid", "d_sigmoid",
    "tanh", "d_tanh",
    "swish", "d_swish",
    "mish", "d_mish",
    "softmax",
    "mae", "mse", "rmse",
    "cross_entropy_loss",
]
