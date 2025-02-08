# currency_converter.py
from typing import Dict, Optional

class CurrencyConverter:
    def __init__(self, exchange_rates: Dict[str, float]):
        """
        Initialize the converter with exchange rates.
        
        Args:
            exchange_rates: Dictionary of currency rates (e.g., {'USD': 1.0, 'EUR': 0.85})
        """
        self.exchange_rates = exchange_rates
    
    def convert(self, amount: float, from_currency: str, to_currency: str) -> Optional[float]:
        """
        Convert an amount from one currency to another.
        
        Args:
            amount: The amount to convert
            from_currency: Source currency code (e.g., 'USD')
            to_currency: Target currency code (e.g., 'EUR')
            
        Returns:
            Converted amount or None if conversion not possible
        """
        # Check if currencies exist in our rates
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            return None
            
        # Handle same currency conversion
        if from_currency == to_currency:
            return round(amount, 2)
            
        try:
            # Convert to USD first (our base currency)
            usd_amount = amount / self.exchange_rates[from_currency]
            
            # Convert from USD to target currency
            result = usd_amount * self.exchange_rates[to_currency]
            
            # Round to 2 decimal places
            return round(result, 2)
            
        except (TypeError, ZeroDivisionError):
            return None