# you can run your test with:
# py -m unittest -

# Import the unit testing framework from Python's standard library
import unittest

# Define a Calculator class with basic arithmetic operations
class Calculator:
    def add(self, a, b):
        pass
    
    def substract(self, a, b):
        pass

    def multiply(self, a, b):
        pass

    def divide(self, a, b):
        pass
        # if b == 0:
        #     raise ValueError("Cannot divide by zero")
        # return a / b

# Create a test class that inherits from unittest.TestCase
# This class will contain all our test methods for the Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        """
        Setup method that runs before EACH test.
        
        Creates a fresh Calculator instance for every test.
        This ensures each test starts with a clean slate and 
        prevents any interference between tests.
        """
        self.calculator = Calculator()
    
    # Test methods for addition
    def test_add_positive_numbers(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8, "Failed to add positive numbers correctly")
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        result = self.calculator.add(-3, -5)
        self.assertEqual(result, -8, "Failed to add negative numbers correctly")
    
    def test_add_mixed_numbers(self):
        """Test adding a negative and a positive number."""
        result = self.calculator.add(-3, 5)
        self.assertEqual(result, 2, "Failed to add mixed sign numbers correctly")
    
    def test_add_zero(self):
        """Test adding zero to a number."""
        result = self.calculator.add(0, 5)
        self.assertEqual(result, 5, "Failed to handle adding zero")
    
    # Test methods for subtraction
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        result = self.calculator.substract(10, 5)
        self.assertEqual(result, 5, "Failed to subtract positive numbers")
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        result = self.calculator.substract(-3, -5)
        self.assertEqual(result, 2, "Failed to subtract negative numbers")
    
    def test_subtract_mixed_numbers(self):
        """Test subtracting when numbers have different signs."""
        result = self.calculator.substract(10, -5)
        self.assertEqual(result, 15, "Failed to subtract with mixed signs")
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        result = self.calculator.multiply(3, 5)
        self.assertEqual(result, 15, "Failed to multiply positive numbers")
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        result = self.calculator.multiply(-3, -5)
        self.assertEqual(result, 15, "Failed to multiply negative numbers")
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        result = self.calculator.multiply(10, 0)
        self.assertEqual(result, 0, "Failed to multiply by zero")
    
    # Test methods for division
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5, "Failed to divide positive numbers")
    
    def test_divide_by_zero(self):
        """
        Test that dividing by zero raises an error.
        
        Uses a context manager to check if the correct error is raised.
        """
        # Check that a ValueError is raised when dividing by zero
        with self.assertRaises(ValueError, msg="Failed to raise error when dividing by zero"):
            self.calculator.divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        result = self.calculator.divide(0, 5)
        self.assertEqual(result, 0, "Failed to divide zero correctly")

# This block ensures tests only run when the script is executed directly
# It discovers and runs all test methods in the TestCalculator class
if __name__ == '__main__':
    unittest.main()