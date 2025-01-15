import unittest
from simple_calculator import SimpleCalculator

class Calc_Test(unittest.TestCase):
    def test_add(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(1, 2), 3)

    def test_subtract(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(4, 2), 2)

    def test_multiply(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.multiply(3, 3), 9)

    def test_divide(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(5, 0), "Error: Cannot divide by zero.")