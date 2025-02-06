from cart import Cart
from item import Item


# Initialize a shopping cart
cart_1 = Cart()

# Create item instances
shoe = Item("Shoe", 100.0, 2)      # A pair of shoes priced at £100 each
t_shirt = Item("T-Shirt", 50.0, 6)  # Six t-shirts priced at £50 each
laptop = Item("Laptop", 1000.0, 6)  # Six laptops priced at £1000 each

# Add items to the shopping cart
for item in [shoe, t_shirt, laptop]:
    cart_1.add_item(item)

# Remove specific items from the cart
cart_1.remove_item(laptop)
cart_1.remove_item(shoe)

# Print the total price before applying any discounts
print("Total before discount:", cart_1.calculate_total())

# Apply a 100% discount (Free items)
cart_1.apply_discount(100)

# Print the total price after the discount is applied
print("Total after 100% discount:", cart_1.calculate_total())
