"""
Calculator functions
"""

from typing import Union


# Numeric type for python, using typing module.
Numeric = Union[int, float, complex]


def add(x: Numeric, y: Numeric) -> Numeric:
    """Add x and y and return result."""
    return x + y


def subtract(x: Numeric, y: Numeric) -> Numeric:
    """Subtract x from y and return result."""
    return y - x
