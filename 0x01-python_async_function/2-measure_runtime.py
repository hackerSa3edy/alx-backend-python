#!/usr/bin/env python3
"""Measure the runtime

This script contains a function to measure the runtime of executing
a coroutine multiple times.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that calls wait_n and calculates the average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for wait_n.

    Returns:
        float: The average time per call.
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - start

    return total_time / n
