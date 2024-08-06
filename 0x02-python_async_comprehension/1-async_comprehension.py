#!/usr/bin/env python3
"""Contains the definition of `async_comprehension` coroutine"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns 10 random numbers collected using async comprehension"""
    return [n async for n in async_generator()]
