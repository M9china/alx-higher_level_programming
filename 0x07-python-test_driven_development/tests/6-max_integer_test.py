#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_max_integer_basic(self):
        """Test with a simple list of integers."""
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)  

    def test_max_integer_negative(self):
        """Test with negative numbers."""
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1) 

    def test_max_integer_mixed(self):
        """Test with a mix of positive, negative, and zero values."""
        result = max_integer([-10, 0, 10, -5, 5])
        self.assertEqual(result, 10)  

    def test_max_integer_empty_list(self):
        """Test with an empty list, which should return None."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_single_element(self):
        """Test with a list containing a single element."""
        result = max_integer([42])
        self.assertEqual(result, 42) 

    def test_max_integer_duplicate_values(self):
        """Test with a list containing duplicate maximum values."""
        result = max_integer([3, 3, 3, 3, 3])
        self.assertEqual(result, 3)  

    def test_max_integer_max_at_end(self):
        """Test with the maximum value at the end of the list."""
        result = max_integer([1, 2, 3, 4, 5, 10])
        self.assertEqual(result, 10)  

    def test_max_integer_max_at_beginning(self):
        """Test with the maximum value at the beginning of the list."""
        result = max_integer([100, 2, 3, 4, 5])
        self.assertEqual(result, 100)  

    def test_max_integer_max_in_middle(self):
        """Test with the maximum value in the middle of the list."""
        result = max_integer([1, 2, 99, 4, 5])
        self.assertEqual(result, 99) 

    def test_max_integer_one_negative_number(self):
        """Test with one negative number in the list."""
        result = max_integer([1, 2, -3, 4, 5])
        self.assertEqual(result, 5) 

    def test_max_integer_only_negative_numbers(self):
        """Test with only negative numbers in the list."""
        result = max_integer([-10, -20, -3, -4, -5])
        self.assertEqual(result, -3) 

if __name__ == '__main__':
    unittest.main()

