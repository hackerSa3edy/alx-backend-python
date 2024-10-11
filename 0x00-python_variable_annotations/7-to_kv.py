#!/usr/bin/env python3
"""Complex types - string and int/float to tuple

This module provides a function to create a tuple from a string and the square of an integer or float.
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple from a string and the square of an integer or float.

    Args:
        k (str): The string to be used as the first element of the tuple.
        v (Union[int, float]): The number to be squared and used as the second element of the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k` and the second element is the square of `v`.
    """
    return k, v ** 2
