#!/usr/bin/env python3
"""Complex types - list of floats

This module provides a function to calculate the sum of a list of floating-point numbers.
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the floating-point numbers in the list.
    """
    return sum(input_list)
