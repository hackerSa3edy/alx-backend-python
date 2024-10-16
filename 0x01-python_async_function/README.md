# Project: 0x01. Python - Async

## Description

This directory contains projects that demonstrate the use of asynchronous programming in Python using the `asyncio` library. The tasks cover basic async syntax, executing multiple coroutines concurrently, measuring runtime, and creating and managing asyncio tasks.

## Resources

### Read or watch

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Tasks

| Task                                                             | File                                                       | Description                                                                  |
| ---------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 0. The basics of async                                           | [0-basic_async_syntax.py](./0-basic_async_syntax.py)       | A basic example of an asynchronous function using Python's asyncio library.  |
| 1. Let's execute multiple coroutines at the same time with async | [1-concurrent_coroutines.py](./1-concurrent_coroutines.py) | Executes multiple instances of a coroutine concurrently.                     |
| 2. Measure the runtime                                           | [2-measure_runtime.py](./2-measure_runtime.py)             | Measures the runtime of executing a coroutine multiple times.                |
| 3. Tasks                                                         | [3-tasks.py](./3-tasks.py)                                 | Creates an asyncio.Task from a coroutine.                                    |
| 4. Tasks                                                         | [4-tasks.py](./4-tasks.py)                                 | Executes multiple instances of a coroutine concurrently using asyncio tasks. |

## Detailed Descriptions

### 0. The basics of async

- **File:** [0-basic_async_syntax.py](./0-basic_async_syntax.py)
- **Description:** This script contains a basic example of an asynchronous function using Python's `asyncio` library. The function `wait_random` takes an integer `max_delay` and returns a random float between 0 and `max_delay`.

### 1. Let's execute multiple coroutines at the same time with async

- **File:** [1-concurrent_coroutines.py](./1-concurrent_coroutines.py)
- **Description:** This script contains a coroutine `wait_n` that executes multiple instances of the `wait_random` coroutine concurrently. It returns a list of the delays.

### 2. Measure the runtime

- **File:** [2-measure_runtime.py](./2-measure_runtime.py)
- **Description:** This script contains a function `measure_time` that measures the runtime of executing the `wait_n` coroutine multiple times and calculates the average time per call.

### 3. Tasks

- **File:** [3-tasks.py](./3-tasks.py)
- **Description:** This script contains a function `task_wait_random` that creates an `asyncio.Task` from the `wait_random` coroutine. It demonstrates how to create and manage asyncio tasks.

### 4. Tasks

- **File:** [4-tasks.py](./4-tasks.py)
- **Description:** This script contains a coroutine `task_wait_n` that executes multiple instances of the `task_wait_random` coroutine concurrently using asyncio tasks. It returns a sorted list of random delays.
