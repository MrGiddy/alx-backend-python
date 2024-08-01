#!/usr/bin/env python3
"""Contains the definition of `make_multiplier` function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by `multiplier` arg"""
    def multiplier_func(value: float) -> float:
        return multiplier * value
    return multiplier_func
