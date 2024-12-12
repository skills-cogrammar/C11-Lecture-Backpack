# --> Data Types & Input
name = input("Enter your name: ")  # String
age = int(input("Enter your age: "))  # Integer
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'  # Boolean

# --> Conditional Statements
if age < 18:
    print(f"Hello {name}, you are a minor.")
elif 18 <= age < 65:        # Note the noise. 18 lower range not required.
    print(f"Hello {name}, you are an adult.")
else:
    print(f"Hello {name}, you are a senior citizen.")

# --> While Loop: Countdown
count = 3
while count > 0:
    print(f"Starting in {count}...")
    count -= 1
print("Go!")

# --> For Loop: Sum of numbers in a fixed list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum using for loop: {total}")

# --> Use while loop in place of for loop as above
numbers = [1, 2, 3, 4, 5]
total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1
print(f"Sum using while loop: {total}")

# while loop with break statement: Handling User Input with break to Exit Loop
# --> Ask the user for input and break the loop if 'exit' is entered
while True:
    user_input = input("Enter something (type 'exit' to quit): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # Exit the loop when 'exit' is typed
    else:
        print(f"You entered: {user_input}")

# The loop keeps asking for user input until the user types "exit", 
# at which point the break statement terminates the loop abruptly.

# while True alternative: Ask for user input and exit gracefully when 'exit' is typed
user_input = ""

while user_input.lower() != 'exit':  # Keep asking until 'exit' is entered
    user_input = input("Enter something (type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting the loop. Goodbye!")
    else:
        print(f"You entered: {user_input}")

print("-- No more inputs!")

# ============= Understanding and Using the range() Function
# Example 1: Creating lists with the range function
# range(6) = [1, 2, 3, 4, 5] - natural list

for number in range(1, 6):
    print(number)

for number in range(0, 10, 2):
    print(number)

# ============= Use while True with break and consider alternative
numbers = []
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num == 'done':
        break
    numbers.append(int(num))

# Improve code above
numbers = []
num = ""
while num != "done":
    num = input("Enter a number (or 'done' to finish): ")
    if num != "done":
        numbers.append(int(num))
