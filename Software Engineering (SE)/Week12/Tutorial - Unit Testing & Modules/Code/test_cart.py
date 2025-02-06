import unittest
from cart import Cart
from item import Item

class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.item1 = Item('Book', 10.0, 2)
        self.item2 = Item('Pen', 2.0, 5)

    def test_add_item(self):
        self.cart.add_item(self.item1)
        self.assertEqual(len(self.cart.items), 1)
        self.cart.add_item(self.item2)
        self.assertEqual(len(self.cart.items), 2)

    def test_remove_item(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.cart.remove_item(self.item1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, 'Pen')

    def test_calculate_total(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        total = self.cart.calculate_total()
        self.assertEqual(total, 30.0)

    def test_apply_discount(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.cart.apply_discount(10)
        total = self.cart.calculate_total()
        self.assertEqual(total, 27.0)

    def test_add_multiple_items(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.cart.add_item(Item('Notebook', 3.0, 4))
        self.assertEqual(len(self.cart.items), 3)

    def test_handle_discount_edge_case(self):
        self.cart.add_item(self.item1)
        self.cart.apply_discount(100)  # Apply 100% discount
        total = self.cart.calculate_total()
        self.assertEqual(total, 0.0)

if __name__ == '__main__':
    unittest.main()
