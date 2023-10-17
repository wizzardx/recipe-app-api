"""
Calculator functions
"""

from typing import Union


# Numeric type for python, using typing module.
from typeguard import typechecked

Numeric = Union[int, float, complex]


@typechecked
def add(x: Numeric, y: Numeric) -> Numeric:
    """Add x and y and return result."""
    return x + y


@typechecked
def subtract(x: Numeric, y: Numeric) -> Numeric:
    """Subtract x from y and return result."""
    return y - x
