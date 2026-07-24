# setup.py

import sys

from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup

if sys.platform == "win32":
    extra_compile_args = ["/O2", "/std:c++17"]
else:
    extra_compile_args = ["-O3", "-std=c++17"]

ext_modules = [
    Pybind11Extension(
        "unimath._maxcompute", # Target name for the extension
        ["src/maxcompute/maxcompute.cpp"], # Path to the C++ source file
        extra_compile_args=extra_compile_args,
    ),
]

setup(
    ext_modules=ext_modules,
)
