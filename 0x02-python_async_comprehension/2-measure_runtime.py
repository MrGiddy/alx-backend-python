#!/usr/bin/env python3
"""Contains the definition of `measure_runtime` coroutine"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures execution time of `async_comprehension` run 4 times in parallel
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
