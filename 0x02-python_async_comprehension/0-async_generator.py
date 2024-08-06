#!/usr/bin/env python3
"""Contains the definiton of `async_generator` coroutine"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generates a random number between 0 and 10 asynchronously 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
