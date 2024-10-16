#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async

This script contains a coroutine that executes multiple instances of another
coroutine concurrently.
"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that calls wait_random n times and returns a list of the delays.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A sorted list of random delays.
    """
    random_delay_list: List[float] = []

    for i in range(n):
        random_delay_list.append(await wait_random(max_delay))

    return sorted(random_delay_list)
