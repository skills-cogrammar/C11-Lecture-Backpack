# testing the functionalities of our calc
import unittest
from utils.calc import Calc

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add_positive_number(self):
        num_1 = 5
        num_2 = 10
        result = self.calc.add(num_1, num_2)
        self.assertEqual(result, 15)

    def test_add_negative_number(self):
        num_1 = -5
        num_2 = -10
        result = self.calc.add(num_1, num_2)
        self.assertEqual(result, -15)

    def test_division(self):
        num_1 = 5
        num_2 = 10
        result = self.calc.div(num_1, num_2)
        self.assertEqual(result, 0.5)

    def test_divide_by_zero(self):
        num_1 = 5
        num_2 = 0
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(num_1, num_2)

    def test_divide_by_char(self):
        num_1 = 5
        num_2 = "e"
        with self.assertRaises(TypeError):
            self.calc.div(num_1, num_2)

