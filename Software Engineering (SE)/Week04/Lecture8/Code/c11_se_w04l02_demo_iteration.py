# ============= While loop Examples
 
# Example 1 - Printing a count up to 4
count = 1

while count < 5:
    print(count)
    # count += 1
    count = count + 1

"""
This while loop continues to execute as long as the condition (count <= 5) 
is true, illustrating how a while loop can repeatedly execute a block of code.
Since we can change the initial value of count, the number of times the loop
iterates is not consistent. 
"""
# Example 2 - Counting down from 5
count = 5

while count > 0:
    print(count)
    count -= 1
print("takeoff!")

# Example 3: Menu example

# Initialise the choice variable
choice = ""

# Continue looping until the user chooses to exit
while choice != "3":
    # Display the menu
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Calculate Sum")
    print("3. Exit")

    # Get the user's choice - NOTE: input is always of type string
    choice = input("Please choose an option (1-3): ")

    # Process the user's choice
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        # Calculate the sum of two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

# ============= For loop Examples

# Example 1: Iterating Over a List of Fruits
fruit_list = ["apple", "orange", "strawberry", "litchi"]

print(fruit_list)
print("This is the list 👆")

for fruit in fruit_list:
    print("Current fruit: ", fruit)

""" 
This for loop iterates over each element in the fruits list and prints it, 
demonstrating the use of iteration to automate repetitive tasks.
"""

# Example 2: Iterating Over a String (Character by Character)
random_sent = "Hello there General Kenobi"

for letter in random_sent:
    print(letter)

# Example 3: Splitting a String and Iterating Over Words
random_sent = "Well, of course I know him. He's me!"
random_sent_split = random_sent.split(' ')
print(random_sent_split)

for word in random_sent_split:
    print(word)

# ============= Implementing break and continue Statements

# Example 1: Breaking out of a loop after a specific condition is met
# --> Find the first number greater than 10 in a list and stop further iteration
numbers = [4, 7, 9, 12, 15]

for num in numbers:
    # Check if the number is greater than 10
    if num > 10:
        print(f"First number greater than 10: {num}")
        break  # Exit the loop once the condition is met

# The loop will stop as soon as it finds a number greater than 10, 
# avoiding unnecessary iterations over the rest of the list.

# Example 2: Skipping Specific Values with continue
# --> Skip even numbers and print only odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for num in numbers:
    # If the number is even, skip it
    if num % 2 == 0:
        continue  # Skip the rest of the loop and move to the next iteration
    print(f"Odd number: {num}")

# ============= Understanding and Using the range() Function
# Example 1: Creating lists with the range function
# range(6) = [1, 2, 3, 4, 5] - natural list

for number in range(1, 6):
    print(number)

for number in range(0, 10, 2):
    print(number)

# ============= Nested For loop Examples

# Example 1:
for i in range(1, 4):
    # print("Outer Loop postion: ", i)
    for j in range(1, 4):
        # print("Inner Loop position", j)
        print(i * j, end=" ")
    print()

# Example 2: Nested for loops to iterate over a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for value in row:
        print(value)

# Example 3: Nested Loop with break to Exit Inner Loop
# --> Stop the inner loop when a condition is met
for i in range(5):
    for j in range(5):
        if j == 3:  # Exit inner loop when j is 3
            print(f"Breaking inner loop when i = {i}, j = {j}")
            break  # Break the inner loop
