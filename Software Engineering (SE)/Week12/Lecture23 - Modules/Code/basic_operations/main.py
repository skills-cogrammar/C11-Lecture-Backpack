from math_operations.basic_operations import *
from string_operations.basic_string_operations import *

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    """
    This block executes the main operations of the script when run directly.
    It demonstrates basic mathematical and string operations using imported functions.
    """

    # Perform and print string concatenation
    # print(concatenate_strings(word_1, word_2))  # Concatenates word_1 and word_2
    # Call the calculator function to run the program
    calculator()