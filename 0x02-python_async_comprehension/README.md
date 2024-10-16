# Project: 0x02. Python - Async Comprehension

## Description

This directory contains projects that demonstrate the use of asynchronous comprehensions in Python. The tasks cover creating asynchronous generators, using async comprehensions to collect data, and measuring the runtime of concurrent async comprehensions.

## Resources

### Read or watch

- [PEP 530 -- Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep530)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Tasks

| Task                                         | File                                                   | Description                                                                            |
| -------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| 0. Async Generator                           | [0-async_generator.py](./0-async_generator.py)         | Creates an asynchronous generator that yields random numbers.                          |
| 1. Async Comprehensions                      | [1-async_comprehension.py](./1-async_comprehension.py) | Uses an async comprehension to collect random numbers from an async generator.         |
| 2. Run time for four parallel comprehensions | [2-measure_runtime.py](./2-measure_runtime.py)         | Measures the runtime of executing four instances of async comprehensions concurrently. |

## Detailed Descriptions

### 0. Async Generator

- **File:** [0-async_generator.py](./0-async_generator.py)
- **Description:** This script contains an asynchronous generator function `async_generator` that yields random numbers between 0 and 10. The function loops 10 times, each time asynchronously waiting for 1 second before yielding a random number.

### 1. Async Comprehensions

- **File:** [1-async_comprehension.py](./1-async_comprehension.py)
- **Description:** This script contains a coroutine `async_comprehension` that collects 10 random numbers using an async comprehension over the `async_generator` coroutine. It demonstrates how to use asynchronous comprehensions to gather data from an async generator.

### 2. Run time for four parallel comprehensions

- **File:** [2-measure_runtime.py](./2-measure_runtime.py)
- **Description:** This script contains a coroutine `measure_runtime` that measures the total runtime of executing four instances of `async_comprehension` concurrently. It uses `asyncio.gather` to run the instances in parallel and calculates the total time taken for their execution.
