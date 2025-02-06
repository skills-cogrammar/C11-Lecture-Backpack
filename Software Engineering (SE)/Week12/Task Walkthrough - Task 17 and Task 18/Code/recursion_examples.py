'''
Create a program that counts the number of even numbers in a list.
For example, [2, 1, 4, 5, 8] would return 3.
'''

def count_evens(num_list):

    # base case is when the list is empty
    if not num_list:
        return 0

    # Recursive case
    # Check if the first item is even or not
    if num_list[0] % 2 == 0:
        return count_evens(num_list[1:]) + 1
    else:
        return count_evens(num_list[1:])
   
'''
Use recursion to reverse a list. 
For example, [5, 6, 7, 8] will become [8, 7, 6, 5]
             ["a", "b", "c"] will become ["c", "b", "a"]

             
[5, 6, 7, 8]

[8] + reverse_list([5, 6, 7])
[8] + [7] + reverse_list([5, 6])
[8] + [7] + [6] + reverse_list([5])
[8] + [7] + [6] + [5] + reverse_list([])
[8, 7, 6, 5]
'''

def reverse_list(input_list):
    """Returns the reversed list using recursion."""
    
    # Base case: An empty list returns itself
    if len(input_list) == 0:
        return []

    # Recursive case: Take the last element and append the reversed remainder
    return [input_list[-1]] + reverse_list(input_list[:-1])
