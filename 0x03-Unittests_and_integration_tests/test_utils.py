#!/usr/bin/env python3
"""Parameterize a unittest"""
from parameterized import parameterized
import unittest
from typing import (Mapping, Sequence, Any)
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """parameterized unittest for `access_nested_map` function"""
    @parameterized.expand([
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any) -> None:
        """test case for the function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
