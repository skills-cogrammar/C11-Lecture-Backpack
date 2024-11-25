# Task 2 Examples: Pattern Creation with For Loop and If-Else

# Example 1: Generating Patterns with For Loop
print("Example 1: Generating Patterns with For Loop")
for i in range(1, 6):  # Loop from 1 to 5
    print("*" * i)  # Print '*' repeated 'i' times
print()

# Example 2: Conditional Output Based on Loop Index
print("Example 2: Conditional Output Based on Loop Index")
for i in range(5):  # Loop through indices 0 to 4
    if i % 2 == 0:  # Check if the index is even
        print("Even Row")
    else:  # If the index is odd
        print("Odd Row")
print()

# Example 3: Combining Strings in a Pattern
print("Example 3: Combining Strings in a Pattern")
for i in range(1, 6):  # Loop from 1 to 5
    line = "Row " + str(i) + ": " + "*" * i  # Create a dynamic string
    print(line)  # Print the formatted string
print()

# Example 4: Single For Loop with Multiple Conditions
print("Example 4: Single For Loop with Multiple Conditions")
for i in range(6):  # Loop from 0 to 5
    if i == 0:  # Special condition for the first iteration
        print("Start")
    elif i == 5:  # Special condition for the last iteration
        print("End")
    else:  # Default case for the other iterations
        print("*" * i)  # Print '*' repeated 'i' times
