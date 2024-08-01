#!/usr/bin/env python3
"""Contains the definition of `element_length` function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of elements and their length"""
    return [(i, len(i)) for i in lst]
