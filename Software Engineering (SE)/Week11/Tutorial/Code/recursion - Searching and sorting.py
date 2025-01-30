import random
import time

##################################### Recursion #####################################

# 0 + 1 + 2 + 3 + 4 + 5 = 15

def summ(n):
    # Summ for the first n natural number iteration
    total = 0
    # the last number is not taken, so you need to increase the upper
    # bound by one
    for i in range(n + 1):
        total += i
    return total

def summ(n):
# Summ for the first n natural number recursion
    if n == 0:
        return 0
    return n + summ(n-1)

print(summ(5))

# Example usage
print(summ(5))  # Output: 15 (1+2+3+4+5)

##################################### Search Algorithms #####################################

def linear_search(arr, target):
    """
    Performs linear search by checking each element sequentially.
    Time Complexity: O(n) - must check each element in worst case
    Space Complexity: O(1) - uses constant extra space
    
    Args:
        arr: List of comparable elements
        target: Element to find
    Returns:
        Index of target if found, -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Performs binary search on a sorted array by repeatedly dividing search interval in half.
    Time Complexity: O(log n) - search space is halved in each step
    Space Complexity: O(1) - uses constant extra space
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to find
    Returns:
        Index of target if found, -1 if not found
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        # Find middle element
        mid = (low + high) // 2
        # If target is found at mid, return it
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1
    return -1

# Commented out recursive version of binary search
# def binary_search(arr, low, high, target):
#     """
#     Recursive implementation of binary search
#     Same time complexity as iterative version but uses O(log n) space due to recursion stack
#     """
#     if high >= low:
#         mid = low + (high - low) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             return binary_search(arr, low, mid-1, target)
#         else:
#             return binary_search(arr, mid + 1, high, target)
#     else:
#         return -1

##################################### Sort Algorithms #####################################

def bubble_sort(array):
    """
    Repeatedly steps through the list, compares adjacent elements and swaps them if in wrong order.
    Time Complexity: O(n²) in worst and average cases, O(n) in best case (already sorted)
    Space Complexity: O(1) - sorts in-place
    
    Args:
        array: List of comparable elements
    Returns:
        Sorted list
    """
    length = len(array)
    swapped = True
    while swapped:  # Continue until no swaps needed (list is sorted)
        swapped = False
        for i in range(0, length - 1):
            # Compare adjacent elements
            if array[i] > array[i + 1]:
                # Swap if they are in wrong order
                array[i + 1], array[i] = array[i], array[i + 1]
                swapped = True  # Mark that we did a swap
    return array

def selection_sort(array):
    """
    Divides input into sorted and unsorted regions, repeatedly selects minimum element 
    from unsorted region and adds it to sorted region.
    Time Complexity: O(n²) in all cases
    Space Complexity: O(1) - sorts in-place
    
    Args:
        array: List of comparable elements
    Returns:
        Sorted list
    """
    length = len(array)
    for i in range(length):
        # Find minimum element in unsorted portion
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        # Swap minimum element with first element of unsorted portion
        array[i], array[min_index] = array[min_index], array[i]
    return array

def insertion_sort(array):
    """
    Builds final sorted array one item at a time, by repeatedly inserting a new element
    into the sorted portion of the array.
    Time Complexity: O(n²) worst/average case, O(n) best case (already sorted)
    Space Complexity: O(1) - sorts in-place
    
    Args:
        array: List of comparable elements
    Returns:
        Sorted list
    """
    i = 1
    length = len(array)
    while i < length:
        j = i
        # Move elements greater than current element one position ahead
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        i = i + 1
    return array

##################################### Testing Code #####################################

# Test sorting algorithms with small list
small_list = [34, 7, 23, 32, 5, 62, 32, 1, 12, 45]
print("Insertion Sort:", insertion_sort(small_list.copy()))
print("Selection Sort:", selection_sort(small_list.copy()))
print("Bubble Sort:", bubble_sort(small_list.copy()))

# Test sorting algorithms with large list (10000 elements)
large_list = random.sample(range(1, 10001), 10000)

# Measure execution time for each sorting algorithm
start_time = time.time()
insertion_sort(large_list.copy())
print("Insertion Sort on large list Time:", time.time() - start_time)

start_time = time.time()
selection_sort(large_list.copy())
print("Selection Sort on large list Time:", time.time() - start_time)

start_time = time.time()
bubble_sort(large_list.copy())
print("Bubble Sort on large list Time:", time.time() - start_time)

# Test search algorithms
sorted_small_list = bubble_sort(small_list)
target = 32

# Test linear search
start_time = time.time()
print(f"Linear Search (target {target}):", linear_search(sorted_small_list, target))
print("Linear Search on small list Time:", time.time() - start_time)

# Test binary search
start_time = time.time()
print(f"Binary Search (target {target}):", binary_search(sorted_small_list, target))
print("Binary Search on small list Time:", time.time() - start_time)

# Test search algorithms with large list
start_time = time.time()
large_list_for_search = random.sample(range(1, 10001), 10000)
sorted_large_list = bubble_sort(large_list_for_search)
print("Bubble Sort Time:", time.time() - start_time)
target_large = sorted_large_list[50]

# Compare linear vs binary search performance on large list
start_time = time.time()
linear_search_result = linear_search(large_list_for_search, target_large)
print("Linear Search Result:", linear_search_result)
print("Linear Search Time:", time.time() - start_time)

start_time = time.time()
binary_search_result = binary_search(sorted_large_list, target_large)
print("Binary Search Result:", binary_search_result)
print("Binary Search Time:", time.time() - start_time)