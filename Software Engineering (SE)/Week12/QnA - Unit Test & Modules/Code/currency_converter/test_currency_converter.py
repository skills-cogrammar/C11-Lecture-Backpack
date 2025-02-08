# test_currency_converter.py
import unittest
from currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        """Set up test data before each test"""
        self.rates = {
            'USD': 1.0,   # Base currency
            'EUR': 0.85,  # 1 USD = 0.85 EUR
            'GBP': 0.73,  # 1 USD = 0.73 GBP
        }
        self.converter = CurrencyConverter(self.rates)

    def test_simple_conversion(self):
        """Test converting USD to EUR"""
        # Arrange
        amount = 100  # $100
        
        # Act
        result = self.converter.convert(amount, 'USD', 'EUR')
        
        # Assert
        self.assertEqual(result, 85.00)  # $100 = €85.00

    def test_reverse_conversion(self):
        """Test converting EUR to USD"""
        # Arrange
        amount = 85  # €85
        
        # Act
        result = self.converter.convert(amount, 'EUR', 'USD')
        
        # Assert
        self.assertEqual(result, 100.00)  # €85 = $100.00

    def test_same_currency(self):
        """Test converting USD to USD"""
        # Arrange
        amount = 100
        
        # Act
        result = self.converter.convert(amount, 'USD', 'USD')
        
        # Assert
        self.assertEqual(result, 100.00)

    def test_invalid_currency(self):
        """Test conversion with invalid currency code"""
        # Arrange
        amount = 100
        
        # Act
        result = self.converter.convert(amount, 'XXX', 'EUR')
        
        # Assert
        self.assertIsNone(result)

    def test_invalid_amount(self):
        """Test conversion with invalid amount"""
        # Arrange
        amount = "not a number"
        
        # Act
        result = self.converter.convert(amount, 'USD', 'EUR')
        
        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()