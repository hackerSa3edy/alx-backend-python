#!/usr/bin/env python3
"""The basics of async

This script contains a basic example of an asynchronous function using
Python's asyncio library.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine that takes an integer max_delay and returns a random float
    between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: A random delay time between 0 and max_delay.
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
