# Task 1 Examples: While Loop for User Input and Average Calculation

# Example 1: Continuously Prompting for Input
print("Example 1: Continuously Prompting for Input")
while True:
    user_input = input("Enter a number (or type 'stop' to end): ")
    if user_input.lower() == "stop":
        print("Stopping...")
        break  # Exit the loop when the user types 'stop'
    print(f"You entered: {user_input}")
print()

# Example 2: Summing Numbers Dynamically
print("Example 2: Summing Numbers Dynamically")
total = 0
numbers_entered = 0

while numbers_entered < 5:  # Limit input to 5 numbers
    num = int(input("Enter a number: "))
    total += num  # Add the input to the total
    numbers_entered += 1  # Increment the count of numbers entered

print(f"Sum of numbers entered: {total}")
print()

# Example 3: Skipping a Specific Value
print("Example 3: Skipping a Specific Value")
forbidden_value = 0
total = 0

# if we need a variable for the sintax but we never use the variable then we can use an "_"
for _ in range(3):  # Limit input to 3 numbers for simplicity
    num = int(input("Enter a number: "))
    if num == forbidden_value:  # Check if the input matches the forbidden value
        print(f"{forbidden_value} is not allowed, skipping...")
        continue  # Skip the rest of the loop for this iteration
    total += num  # Add the number to the total if it's valid

print(f"Total: {total}")
