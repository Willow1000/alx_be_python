import unittest
from simple_calculator import SimpleCalculator

class Calc_Test(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 0), "Error: Cannot divide by zero.")