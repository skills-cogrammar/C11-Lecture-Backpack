# order.py
class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.status = "Placed"

    def update_items(self, new_items):
        self.items = new_items
