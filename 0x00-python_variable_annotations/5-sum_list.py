#!/usr/bin/env python3
"""Defines the `sum_list` function"""
from typing import List


FloatList = List[float]


def sum_list(input_list: FloatList) -> float:
    """Returns the sum of a list of floats"""
    return sum(input_list)
