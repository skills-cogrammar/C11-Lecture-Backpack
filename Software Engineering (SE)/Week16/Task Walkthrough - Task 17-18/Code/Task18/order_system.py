# order_system.py
from order import Order


class CafeteriaOrderSystem:
    def __init__(self):
        self.orders = {}  # Store orders with order_id as key
        self.order_id_counter = 1

    def place_order(self, customer_name, items):
        order_id = self.order_id_counter
        self.orders[order_id] = Order(order_id, customer_name, items)
        self.order_id_counter += 1
        return order_id

    def view_order(self, order_id):
        order = self.orders.get(order_id)
        return vars(order) if order else "Order not found"

    def update_order(self, order_id, new_items):
        if order_id in self.orders:
            self.orders[order_id].update_items(new_items)
            return "Order updated successfully"
        return "Order not found"

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            return "Order cancelled successfully"
        return "Order not found"
