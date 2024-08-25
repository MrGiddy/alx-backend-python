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
        """paremeterized test case for the function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Exception) -> None:
        """test KeyError is raised for given inputs"""
        with self.assertRaises(expected) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[-1]))
