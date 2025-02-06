'''
Create a program that counts the number of even numbers in a list.
For example, [2, 1, 4, 5, 8] would return 3.
'''
import unittest

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

def count_evens(numbers):
    """Returns the count of even numbers in the list using recursion."""
    
    # Base case: If the list is empty, return 0
    if len(numbers) == 0:
        return 0

    # Check if the first number is even, then recurse on the rest
    return (1 if numbers[0] % 2 == 0 else 0) + count_evens(numbers[1:])

'''
Use recursion to reverse a list. 
For example, [5, 6, 7, 8] will become [8, 7, 6, 5]
             ["a", "b", "c"] will become ["c", "b", "a"]
'''

def reverse_list(lst):
    """Returns the reversed list using recursion."""
    
    # Base case: An empty list returns itself
    if len(lst) == 0:
        return []

    # Recursive case: Take the last element and append the reversed remainder
    return [lst[-1]] + reverse_list(lst[:-1])


if __name__ == '__main__':
    unittest.main(verbosity=3)

# NB NOTE: Run code with <python -m unittest test_single_file.py -v> in terminal