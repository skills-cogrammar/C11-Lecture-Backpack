"""
This is a simple implementation of a Café Ordering System using the MVC (Model-View-Controller) architecture.
- **Model**: Defines the core data structures, such as Products, Orders, and Order Items, and includes methods to calculate totals and manage order status.
- **Controller**: Handles the business logic, such as creating orders, adding items, and updating order status.
- **View**: Provides a command-line interface to interact with the system, displaying menus and order summaries.

The system also demonstrates basic CRUD operations:
- **Create**: Create a new order and add items.
- **Read**: Retrieve and display order details.
- **Update**: Update order status or modify order contents.
- **Delete**: Not implemented here but can be added to remove items or orders.

This program uses Python's object-oriented principles to keep the system modular and maintainable.
"""

# ================== Models ==================

class OrderStatus:
    """
    Represents the possible statuses of an order.
    """
    PENDING = "PENDING"
    PREPARING = "PREPARING"
    READY = "READY"
    COMPLETED = "COMPLETED"

class PaymentStatus:
    """
    Represents the possible statuses of a payment.
    """
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Product:
    """
    Represents a product in the café menu.

    Attributes:
        id (int): The unique ID of the product.
        name (str): The name of the product.
        price (float): The price of the product.
    """
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

class OrderItem:
    """
    Represents an item in an order.

    Attributes:
        product (Product): The product being ordered.
        quantity (int): The quantity of the product.
    """
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        """
        Calculates the subtotal for this item.

        Returns:
            float: The subtotal for this item (price * quantity).
        """
        return self.product.price * self.quantity

class Order:
    """
    Represents an order containing multiple items.

    Attributes:
        order_id (int): The unique ID of the order.
        items (list[OrderItem]): The list of items in the order.
        status (str): The current status of the order.
        total_amount (float): The total amount for the order.
    """
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items = []
        self.status = OrderStatus.PENDING
        self.total_amount = 0.0

    def add_item(self, item: OrderItem):
        """
        Adds an item to the order and recalculates the total.

        Args:
            item (OrderItem): The item to add.
        """
        self.items.append(item)
        self.calculate_total()

    def calculate_total(self):
        """
        Recalculates the total amount for the order.
        """
        self.total_amount = sum(item.calculate_subtotal() for item in self.items)

    def update_status(self, status: OrderStatus):
        """
        Updates the status of the order.

        Args:
            status (str): The new status for the order.
        """
        self.status = status

# ================== Controllers ==================

class OrderController:
    """
    Manages the business logic for orders, acting as the controller in the MVC architecture.
    """
    def __init__(self):
        self.orders = {}
        self.next_order_id = 1

    def create_order(self) -> Order:
        """
        Creates a new order.

        Returns:
            Order: The newly created order.
        """
        order = Order(self.next_order_id)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        return order

    def add_item_to_order(self, order_id: int, product: Product, quantity: int):
        """
        Adds an item to an order.

        Args:
            order_id (int): The ID of the order.
            product (Product): The product to add.
            quantity (int): The quantity of the product.

        Returns:
            bool: True if the item was added successfully, False otherwise.
        """
        if order_id in self.orders:
            order = self.orders[order_id]
            item = OrderItem(product, quantity)
            order.add_item(item)
            return True
        return False

    def update_order_status(self, order_id: int, status: OrderStatus):
        """
        Updates the status of an order.

        Args:
            order_id (int): The ID of the order.
            status (str): The new status.

        Returns:
            bool: True if the status was updated, False otherwise.
        """
        if order_id in self.orders:
            self.orders[order_id].update_status(status)
            return True
        return False

    def get_order(self, order_id: int) -> Order:
        """
        Retrieves an order by ID.

        Args:
            order_id (int): The ID of the order.

        Returns:
            Order: The order with the specified ID, or None if not found.
        """
        return self.orders.get(order_id)

# ================== Views ==================

class CafeView:
    """
    Provides the user interface for the café ordering system.
    """
    def __init__(self, controller: OrderController):
        self.controller = controller
        self.menu = {
            1: Product(1, "Espresso", 2.50),
            2: Product(2, "Latte", 3.50),
            3: Product(3, "Cappuccino", 3.00),
            4: Product(4, "Tea", 2.00)
        }

    def display_menu(self):
        """
        Displays the café menu.
        """
        print("\n=== CAFÉ MENU ===")
        for id, product in self.menu.items():
            print(f"{id}. {product.name}: £{product.price:.2f}")

    def take_order(self):
        """
        Facilitates taking an order from the user.
        """
        order = self.controller.create_order()
        print(f"\nNew Order Created - Order #{order.order_id}")
        
        while True:
            self.display_menu()
            choice = input("\nEnter product number (or 'done' to finish): ")
            
            if choice.lower() == 'done':
                break

            try:
                product_id = int(choice)
                if product_id not in self.menu:
                    print("Invalid product number!")
                    continue

                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Invalid quantity!")
                    continue

                self.controller.add_item_to_order(
                    order.order_id, 
                    self.menu[product_id], 
                    quantity
                )
                print("Item added to order!")

            except ValueError:
                print("Invalid input!")

        self.display_order_summary(order.order_id)

    def display_order_summary(self, order_id: int):
        """
        Displays a summary of the specified order.

        Args:
            order_id (int): The ID of the order.
        """
        order = self.controller.get_order(order_id)
        if order:
            print("\n=== ORDER SUMMARY ===")
            print(f"Order #{order.order_id}")
            for item in order.items:
                print(f"{item.product.name} x{item.quantity}: £{item.calculate_subtotal():.2f}")
            print(f"Total: £{order.total_amount:.2f}")
            print(f"Status: {order.status}")

# ================== Main ==================

def main():
    """
    Entry point for the café ordering system.
    """
    controller = OrderController()
    view = CafeView(controller)
    
    while True:
        print("\n=== CAFÉ ORDER SYSTEM ===")
        print("1. New Order")
        print("2. View Order")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            view.take_order()
        elif choice == "2":
            try:
                order_id = int(input("Enter order number: "))
                view.display_order_summary(order_id)
            except ValueError:
                print("Invalid input!")
        elif choice == "3":
            print("Thank you for using our system!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()