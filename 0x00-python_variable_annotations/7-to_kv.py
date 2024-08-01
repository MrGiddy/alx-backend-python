#!/usr/bin/env python3
"""Contains the definition of `to_kv` function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Makes a (str, float) tuple with the number part squared

    Args:
        k <str> : A string
        v <str> or <float> : Could be a string or a float type
    Return:
        <tuple>: A tuple
    """
    return (k, (v ** 2))
