# main.py
from order_system import CafeteriaOrderSystem

if __name__ == "__main__":
    system = CafeteriaOrderSystem()

    # Placing an order
    order_id = system.place_order("Alice", ["Burger", "Fries", "Soda"])
    print(f"Order ID: {order_id} placed successfully")

    # Viewing the order
    print(system.view_order(order_id))

    # Updating the order
    print(system.update_order(order_id, ["Salad", "Water"]))
    print(system.view_order(order_id))

    # Cancelling the order
    print(system.cancel_order(order_id))
    print(system.view_order(order_id))
