#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 20, 30, 5]), 30)

    def test_unsorted_list(self):
        """Test with an unsorted list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_single_element_list(self):
        """Test with a single element in the list"""
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7]), -7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-10, -20, -3, -4]), -3)

    def test_mixed_numbers(self):
        """Test with a mix of positive, negative, and zero"""
        self.assertEqual(max_integer([0, -1, 1, -2, 2]), 2)

    def test_duplicates(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_large_numbers(self):
        """Test with LARGE numbers"""
        self.assertEqual(max_integer([1, 1000000000, 999999999]), 1000000000)

    def test_floats(self):
        """Test with floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_float(self):
        """Test with a mix of integers and floats"""
        self.assertEqual(max_integer([1, 2.7, 3]), 3)

    def test_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['apple', 'banana', 'cantaloupe']), 'cantaloupe')

    def test_single_string(self):
        """Test with a single string"""
        self.assertEqual(max_integer("abcde"), 'e')

    def test_none(self):
        """Test with None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        """Test with non-iterables"""
        with self.assertRaises(TypeError):
            max_integer(123)

    if __name__ == '__main__':
        unittest.main()
