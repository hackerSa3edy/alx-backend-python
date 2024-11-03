#!/usr/bin/env python3
"""Defines test_utils module"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Class to test access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Test access_nested_map with valid inputs

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to access in the nested map.
            result: The expected result from accessing the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map with KeyError exception

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to access in the nested map.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to test get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload", True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, get_mock):
        """Test get_json with different URLs

        Args:
            test_url (str): The URL to fetch JSON from.
            test_payload (dict): The expected JSON payload.
            get_mock (Mock): The mock object for requests.get.
        """
        get_mock.json.return_value = test_payload
        get_mock.return_value = get_mock

        self.assertEqual(get_json(test_url), test_payload)
        get_mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Class to test memoize decorator"""

    def test_memoize(self):
        """Test memoize decorator functionality"""
        class TestClass:
            """Implement test class with memoized property"""

            def a_method(self):
                """Method that returns a constant value"""
                return 42

            @memoize
            def a_property(self):
                """Memoized property that calls a_method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as a_mock:
            a_mock.return_value = lambda: 42

            my_test = TestClass()
            self.assertEqual(my_test.a_property(), 42)
            self.assertEqual(my_test.a_property(), 42)

            a_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
