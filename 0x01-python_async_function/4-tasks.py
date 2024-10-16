#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async

This script contains a coroutine that executes multiple instances of another
coroutine concurrently using asyncio tasks.
"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that calls task_wait_random n times and returns a list of
    the delays.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A sorted list of random delays.
    """
    random_delay_list: List[float] = []

    for i in range(n):
        random_delay_list.append(await task_wait_random(max_delay))

    return sorted(random_delay_list)
