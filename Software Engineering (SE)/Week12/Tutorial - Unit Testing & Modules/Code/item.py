from typing import Union
from decimal import Decimal


class Item:
    """
    Represents a product item that can be added to a shopping cart.

    This class stores details about an item, including its name, price, and quantity.

    Attributes:
        name (str): The name of the item.
        price (float): The price of a single unit of the item.
        quantity (int): The number of units of the item.
    """

    def __init__(self, name: str, price: Union[int, float, Decimal], quantity: int = 1) -> None:
        """
        Initialize an Item instance.

        Args:
            name (str): The name of the item.
            price (Union[int, float, Decimal]): The price of a single unit of the item.
            quantity (int, optional): The quantity of the item. Defaults to 1.

        Raises:
            ValueError: If price is negative or quantity is less than 1.

        Example:
            >>> item = Item("Laptop", 999.99, 1)
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")

        self.name: str = name
        self.price: Union[int, float, Decimal] = price
        self.quantity: int = quantity

    def total_price(self) -> float:
        """
        Calculate the total price for this item based on quantity.

        Returns:
            float: The total cost of this item (price * quantity).

        Example:
            >>> item = Item("Headphones", 50.00, 2)
            >>> item.total_price()
            100.00
        """
        return float(self.price) * self.quantity

    def apply_discount(self, discount_percentage: Union[int, float, Decimal]) -> float:
        """
        Apply a discount to the item's price.

        Args:
            discount_percentage (Union[int, float, Decimal]): The percentage discount (0-100).

        Returns:
            float: The new price after applying the discount.

        Raises:
            ValueError: If discount_percentage is not between 0 and 100.

        Example:
            >>> item = Item("Mouse", 20.00, 1)
            >>> item.apply_discount(10)  # 10% discount
            18.00
        """
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        self.price -= self.price * (discount_percentage / 100)
        return float(self.price)
