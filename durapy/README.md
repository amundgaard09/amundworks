# DuraPy - The Durendal Python Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

DuraPy is a growing toolbox for science, engineering, and STEMP workflows. It brings together helpful utilities for mathematics, physics, robotics, chemistry-adjacent calculations, and more under one Python package.

## What makes it useful

- A practical math layer for geometry, trigonometry, and algebra
- Physics constants and helper modules for scientific exploration
- A lightweight foundation for future CLI tools and engineering utilities
- A simple package structure that is easy to extend

## Installation

```bash
pip install durapy
```

## Quick start

```python
from durapy import unimath

print(unimath.pythagoras(A=3, B=4))
```

Output:

```text
5.0
```

## Example: constants and units

```python
from durapy import constants

print(constants.PI.value)
print(constants.C.value)
```

## Suggested next improvements

If you want to evolve the package further, the most impactful next steps are:

- Add more polished examples and tutorials
- Create a small CLI for common calculations
- Add documentation pages for each submodule
- Introduce a richer test suite and versioned release workflow

DuraPy is intentionally open-ended, so it can grow into whatever your STEMP projects need next.
