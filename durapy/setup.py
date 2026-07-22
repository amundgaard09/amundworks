# setup.py
from setuptools import setup, Extension
import sys

# Secure compilation flags depending on the OS compiler detected
if sys.platform == "win32":
    extra_compile_args = ["/O2", "/std:c++17"] # Optimizations for MSVC on Windows
else:
    extra_compile_args = ["-O3", "-std=c++17"]  # Optimizations for GCC/Clang on Mac/Linux

class Pybind11Extension(Extension):
    """A helper class that defers resolving pybind11 include paths until build time."""
    def __init__(self, name, sources, *args, **kwargs):
        super().__init__(name, sources, *args, **kwargs)

    @property
    def include_dirs(self):
        import pybind11
        return [pybind11.get_include()]

# Define the C++ extension module
ext_modules = [
    Pybind11Extension(
        name="src.unimath._maxcompute",               # Target path where the .pyd/.so file lands
        sources=["maxcompute/maxcompute.cpp"],         # Path to your C++ source file
        extra_compile_args=extra_compile_args,
        language="c++",
    ),
]

setup(ext_modules=ext_modules)
