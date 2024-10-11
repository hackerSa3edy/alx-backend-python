#!/usr/bin/env python3
"""Define Type Checking

This module provides a function to zoom into an array by
repeating its elements.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom into an array by repeating its elements.

    Args:
        lst (Tuple): The input tuple to zoom into.
        factor (int, optional): The factor by which to repeat each
        element. Defaults to 2.

    Returns:
        List: A list with elements of the input tuple repeated
        by the given factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


# Example usage
array = (12, 72, 91)

zoom_2x = zoom_array(array)
"""List: The array zoomed in by a factor of 2."""

zoom_3x = zoom_array(array, 3)
"""List: The array zoomed in by a factor of 3."""
