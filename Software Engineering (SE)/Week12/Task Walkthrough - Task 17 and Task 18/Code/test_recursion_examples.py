import unittest
from recursion_examples import count_evens, reverse_list

class TestRecursionFunctions(unittest.TestCase):

    # Testing count_evens 
    def test_only_even_numbers(self):
        self.assertEqual(count_evens([1, 2, 3, 4, 5]), 2)

    def test_only_odd_numbers(self):
        self.assertEqual(count_evens([1, 3, 5, 7]), 0)
    
    def test_empty_list(self):
        self.assertEqual(count_evens([]), 0)

    def test_reverse_list_numbers(self):
        self.assertEqual(reverse_list([5, 6, 7, 8]), [8, 7, 6, 5])

    def test_reverse_list_strings(self):
        self.assertEqual(reverse_list(["a", "b", "c"]), ["c", "b", "a"])

if __name__ == '__main__':
    unittest.main(verbosity=5)
        