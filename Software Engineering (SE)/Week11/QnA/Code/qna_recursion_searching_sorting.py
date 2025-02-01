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
print(sum_natural(5))  # Output: 15 (1+2+3+4+5)

##################################### Search #####################################

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Recursive
def binary_search_recursive(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid-1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1
##################################### Search #####################################


##################################### Sort #####################################

def bubble_sort(array):
    length = len(array)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, length - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                swapped = True
    return array

def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def insertion_sort(array):
    i = 1
    length = len(array)
    while i < length:
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        i = i + 1
    return array

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Choosing the middle element as pivot
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]  
    return quick_sort(left) + middle + quick_sort(right)

##################################### Sort #####################################



# Test the algorithms

small_list = [34, 7, 23, 32, 5, 62, 1, 12, 45]
print("Insertion Sort:", insertion_sort(small_list.copy()))
print("Selection Sort:", selection_sort(small_list.copy()))
print("Bubble Sort:", bubble_sort(small_list.copy()))
print("Bubble Recursive Sort:", binary_search_recursive(small_list.copy(), 0, len(small_list.copy()) - 1, target))

large_list = random.sample(range(1, 10001), 10000)

start_time = time.time()
insertion_sort(large_list.copy())
print("Insertion Sort on large list Time:", time.time() - start_time)

start_time = time.time()
selection_sort(large_list.copy())
print("Selection Sort on large list Time:", time.time() - start_time)

start_time = time.time()
bubble_sort(large_list.copy())
print("Bubble Sort on large list Time:", time.time() - start_time)

sorted_small_list = bubble_sort(small_list)
target = 32
start_time = time.time()
print(f"Linear Search (target {target}):", linear_search(sorted_small_list, target))
print("Linear Search on small list Time:", time.time() - start_time)

start_time = time.time()
print(f"Binary Search (target {target}):", binary_search(sorted_small_list, target))
print("Binary Search on small list Time:", time.time() - start_time)

start_time = time.time()
print(f"Binary Search Recursive(target {target}):", binary_search_recursive(sorted_small_list, 0, len(sorted_small_list) - 1, target))
print("Binary Search Recursive on small list Time:", time.time() - start_time)

start_time = time.time()
large_list_for_search = random.sample(range(1, 10001), 10000)
sorted_large_list = bubble_sort(large_list_for_search)
print("Bubble Sort Time:", time.time() - start_time)
target_large = sorted_large_list[50]

start_time = time.time()
linear_search_result = linear_search(large_list_for_search, target_large)
print("Linear Search Result:", linear_search_result)
print("Linear Search Time:", time.time() - start_time)

start_time = time.time()
binary_search_result = binary_search(sorted_large_list, target_large)
print("Binary Search Result:", binary_search_result)
print("Binary Search Time:", time.time() - start_time)