#!/usr/bin/env python3
"""Asynchronous Tasks

This script contains a function that creates an asyncio.Task from a coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A task that will run the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
