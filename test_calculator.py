'''
Created on Jul. 23, 2023

@author: tonyp
'''
# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = self.calculator.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
