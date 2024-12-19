# ====== Define and Call Functions with Parameters and Return Values

def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    numbers_sum = a + b
    return numbers_sum


# Calling the function with arguments
result = add_numbers(5, 10)
print(f"Sum: {result}")  # Output: Sum: 15

# ====== Implement Functions to Modularise and Organise Code Effectively

def get_user_input():
    """Gets input from the user."""
    return int(input("Enter a number: "))


def calculate_square(number):
    """Calculates the square of a number."""
    return number ** 2


def main():
    """Main function to organise the code."""
    num = get_user_input()
    squared = calculate_square(num)
    print(f"The square of {num} is {squared}")


# Calling the main function to run the program
# This block will only run if the script is executed directly and not when imported.
if __name__ == "__main__":
    main()

# ====== Apply Scope Rules to Avoid Common Errors Related to Variable Access and Modification

global_count = 0  # Global variable

def increment():
    global global_count  # Indicate we are modifying the global variable
    global_count += 1
    print(f"Global count inside function: {global_count}")


increment()
print(f"Global count outside function: {global_count}")

# ====== Apply Local Scope Rules to demonstrate it's purpose

def local_scope_example():
    local_variable = "I am local"  # Local variable defined inside the function
    print(local_variable)  # This works inside the function


local_scope_example()       # Call the function and then try to access the variable

# Trying to access the local variable outside the function
print(local_variable)  # This will raise a NameError: name 'local_variable' is not defined

# ====== Interpret Stack Traces to Debug and Identify the Source of Errors in Their Code

import traceback

def faulty_function():
    return 1 / 0  # This will cause a ZeroDivisionError

try:
    faulty_function()
except Exception as e:
    print("An error occurred:")
    traceback.print_exc()

# ====== Perform Basic String Operations such as Concatenation, Slicing, and Formatting

# String Concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"  # Concatenation
print(full_greeting)  # Output: Hello, Alice!

# String Slicing
sample_text = "Python Programming"
sliced_text = sample_text[7:18]  # Slicing
print(sliced_text)  # Output: Programming

# String Formatting with f-string
formatted_text = f"{name} loves {sliced_text}"  # Using f-strings for formatting
print(formatted_text)  # Output: Alice loves Programming

# String Formatting with .format() method
name = "Alice"
age = 30

# Using placeholders for formatting
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)    # Output: My name is Alice and I am 30 years old.

# ====== Use Built-in String Methods to Manipulate and Analyse Text Data

sample_text = "Python is fun!"

# Convert to uppercase
print(sample_text.upper())  # Output: PYTHON IS FUN!

# Replace a substring
print(sample_text.replace("fun", "awesome"))  # Output: Python is awesome!

# Check if text starts with a substring
print(sample_text.startswith("Python"))  # Output: True

# ====== Perform Basic List Operations such as Indexing, Slicing, Appending, and Removing Elements

fruits = ["apple", "banana", "cherry"]

# Indexing
print(fruits[0])  # Output: apple

# Find the index of the first occurrence of "apple"
index_apple = fruits.index("apple")
print(index_apple)  # Output: 0

# Slicing => list_str[start, end, direction]
print(fruits[1:])  # Output: ['banana', 'cherry']

# Appending
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Extend => 2 lists or strings can be combined with the + character
fruits_list1 = ["apple", "banana", "cherry"]
fruits_list2 = ["pineapple", "quava", "fig"]

all_fruits = fruits_list1 + fruits_list2
print(all_fruits)   # Output: ["apple", "banana", "cherry", "pineapple", "quava", "fig"]

# Removing by value
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'date']

# Removing by position
fruits = ["apple", "banana", "cherry", "date"]

# Remove the element at position 1 (second element)
removed_element = fruits.pop(1)
print(f"Removed element: {removed_element}")  # Output: Removed element: banana
print(fruits)  # Output: ['apple', 'cherry', 'date']

# ====== Use List Methods and Functions to Manipulate and Process List Data

numbers = [3, 1, 4, 1, 5, 9]

# Sorting the list
numbers.sort()  # not supported between instances of 'str' and 'int'
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

# Reversing the list
numbers.reverse()
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]

# Using `map` to apply a function to all elements. map() => Higher-order function (HOF)
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [81, 25, 16, 9, 1, 1]

# -- Without lambda
# def square(x):
#     return x * 2

# numbers = [9, 5, 4, 3, 1, 1]
# squared_numbers = map(square, numbers)
# print(list(squared_numbers))  # Output: [81, 25, 16, 9, 1, 1]

#--> Other HOF => filter(), reduce(), sorted(), any(), all()

# ====== Perform Basic Dictionary Operations such as Adding, Updating, and Removing Key-Value Pairs

student = {"name": "Alice", "age": 24}

# Adding a key-value pair
student["grade"] = "A"
print(student)  # Output: {'name': 'Alice', 'age': 24, 'grade': 'A'}

# Updating a key-value pair
student["age"] = 25
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A'}

#---------------------------
# another update method using .update()
# if the key exists, the value will be updated else key and value will be added
dict1 = {"name": "Alice"}

# Using update to add new key-value pairs
dict1.update({"age": 25, "city": "London"})
print(dict1)        # Output: {'name': 'Alice', 'age': 25, 'city': 'London'}
#---------------------------

# Removing a key-value pair from {'name': 'Alice', 'age': 25, 'grade': 'A'}
student.pop("grade")
print(student)  # Output: {'name': 'Alice', 'age': 25}

# ====== Use Dictionary Methods to Access and Manipulate Data Efficiently

person = {"name": "Bob", "city": "New York"}

# Accessing keys and values with keys and values methods
print(person.keys())  # Output: dict_keys(['name', 'city'])
print(person.values())  # Output: dict_values(['Bob', 'New York'])

# Using `get` to access a value with a default
print(person.get("age", "Not specified"))  # Output: Not specified since no "age" key.

# Checking for a key in the dictionary
print("name" in person)  # Output: True

# Use items() method to grab keys and values
# Iterating through the dictionary's keys and values
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

# ====== Perform Basic Operations on 2D Lists such as Accessing, Modifying, and Iterating Over Elements

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[1][2])  # Output: 6 (second row, third column)

# Modifying an element
matrix[0][0] = 10
print(matrix)  # Output: [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

# Iterating over elements
for row in matrix:
    for element in row:
        print(element, end=" ")  # Output: 10 2 3 4 5 6 7 8 9

