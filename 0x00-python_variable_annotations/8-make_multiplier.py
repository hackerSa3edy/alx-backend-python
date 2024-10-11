#!/usr/bin/env python3
"""Complex types - functions

This module provides a function to create a multiplier function.
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and returns it multiplied by the multiplier.
    """
    return lambda num: num * multiplier
