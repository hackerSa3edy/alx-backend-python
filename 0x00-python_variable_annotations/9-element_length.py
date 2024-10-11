#!/usr/bin/env python3
"""Duck type an iterable object

This module provides a function to calculate the length of elements in an iterable of sequences.
"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each sequence in an iterable.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence from the iterable and its length.
    """
    return [(i, len(i)) for i in lst]
