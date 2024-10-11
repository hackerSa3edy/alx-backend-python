#!/usr/bin/env python3
"""Complex types - mixed list

This module provides a function to calculate the sum of a list
containing both integers and floating-point numbers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing
        integers and floating-point numbers.

    Returns:
        float: The sum of the numbers in the list as a floating-point number.
    """
    return sum(mxd_lst)
