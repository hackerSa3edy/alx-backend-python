#!/usr/bin/env python3
"""Run time for four parallel comprehensions

This script contains a coroutine that measures the total runtime of executing
four instances of async_comprehension concurrently.
"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of four calls to async_comprehension.

    This coroutine uses asyncio.gather to run four instances of
    async_comprehension concurrently and measures the total time taken for
    their execution.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
