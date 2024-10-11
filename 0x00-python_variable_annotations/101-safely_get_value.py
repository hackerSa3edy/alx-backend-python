#!/usr/bin/env python3
"""More involved type annotations

This module provides a function to safely retrieve a value from a dictionary.
"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')
ret_t = Union[Any, T]
def_t = Optional[T]

def safely_get_value(dct: Mapping, key: Any, default: def_t = None) -> ret_t:
    """Return the value that corresponds to a specific key or a default value.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (def_t, optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        ret_t: The value corresponding to the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
