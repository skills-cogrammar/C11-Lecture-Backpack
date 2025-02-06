from typing import List, Union
from decimal import Decimal


class Cart:
    """
    A shopping cart that manages items and their associated operations.

    This class provides functionality to add/remove items, calculate totals,
    and apply discounts to items in the cart.

    Attributes:
        items (List[Item]): A list containing the items in the cart.
    """

    def __init__(self) -> None:
        """Initialize an empty shopping cart."""
        self.items: List['Item'] = []

    def add_item(self, item: 'Item') -> List['Item']:
        """
        Add an item to the shopping cart.

        Args:
            item (Item): The item object to be added to the cart.

        Returns:
            List[Item]: The updated list of items in the cart.

        Example:
            >>> cart = Cart()
            >>> item = Item("Book", 10.99, 1)
            >>> cart.add_item(item)
        """
        self.items.append(item)
        return self.items

    def remove_item(self, item: 'Item') -> None:
        """
        Remove a specific item from the shopping cart.

        Args:
            item (Item): The item object to be removed from the cart.

        Raises:
            ValueError: If the item is not found in the cart.

        Example:
            >>> cart = Cart()
            >>> item = Item("Book", 10.99, 1)
            >>> cart.add_item(item)
            >>> cart.remove_item(item)
        """
        self.items.remove(item)

    def calculate_total(self) -> float:
        """
        Calculate the total cost of all items in the cart.

        Returns:
            float: The total cost of all items, considering their quantities.

        Example:
            >>> cart = Cart()
            >>> item = Item("Book", 10.99, 2)
            >>> cart.add_item(item)
            >>> cart.calculate_total()
            21.98
        """
        return sum(item.price * item.quantity for item in self.items)

    def apply_discount(self, discount_percentage: Union[int, float, Decimal]) -> float:
        """
        Apply a discount percentage to all items in the cart.

        Args:
            discount_percentage (Union[int, float, Decimal]): The percentage discount
                to apply (0-100).

        Returns:
            float: The total cost after applying the discount.

        Raises:
            ValueError: If discount_percentage is not between 0 and 100.

        Example:
            >>> cart = Cart()
            >>> item = Item("Book", 10.00, 1)
            >>> cart.add_item(item)
            >>> cart.apply_discount(10)  # 10% discount
            9.00
        """
        # Validate discount percentage
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        # Apply discount to each item
        for item in self.items:
            item.price -= item.price * (discount_percentage / 100)

        return self.calculate_total()