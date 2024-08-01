#!/usr/bin/env python3
"""Contains definition for `sum_mixed_list` function"""
from typing import List, Union


MixedList = List[Union[int, float]]


def sum_mixed_list(mxd_lst: MixedList) -> float:
    """
    Returns the float sum of a mixed list of integers and floats

    Args:
        mxd_list <list>: A list containing a mixture of float and int values
    Return:
        <float>: The sum of elements in mxd_list
    """
    return sum(mxd_lst)
