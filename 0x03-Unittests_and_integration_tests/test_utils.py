#!/usr/bin/env python3
"""Tests the utils module"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from typing import (Dict, Mapping, Sequence, Any)
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """unit test for the `access_nested_map` function"""
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
        """paremeterized test case"""
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
        # Use assertRaises context manager to catch KeyError
        with self.assertRaises(expected) as context:
            access_nested_map(nested_map, path)
        # Test the exception message is as expected
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """unit test for the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            mocked_get) -> None:
        """
        test get_json returns correctly
        and that request.get is called correctly
        """
        # Create a mock resp. object with
        # a json method that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Set the mocked get to return mocked response
        mocked_get.return_value = mock_response

        # call the function and verify the behavior
        result = get_json(test_url)

        # check that request.get was called once with the correct URL
        mocked_get.assert_called_once_with(test_url)

        # check that the result of get_json is as expected
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Unit test for the `memoize` function"""
    def test_memoize(self):
        """
        Test that `a_property` is memoized and
        `a_method` is called only once
        """

        class TestClass:
            """A test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()

        with patch.object(
                TestClass,
                'a_method',
                return_value=42) as mocked_a_method:

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mocked_a_method.assert_called_once()
