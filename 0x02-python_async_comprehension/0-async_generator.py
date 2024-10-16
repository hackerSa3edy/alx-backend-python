#!/usr/bin/env python3
"""Async Generator

This script contains an asynchronous generator function that yields
random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This function loops 10 times, each time asynchronously waiting
    for 1 second,
    then yielding a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
