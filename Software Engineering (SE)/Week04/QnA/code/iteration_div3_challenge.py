""""
Write a program to find and print the sum of numbers 
from 1 to 100 that are divisible by 3. 
"""

# --- Program to calculate the sum of numbers from 1 to 100 divisible by 3

# ---> Solution with %
# Step 1: Initialise a variable to store the sum
sum_divisible_by_3 = 0

# Step 2: Loop through numbers from 1 to 100
for number in range(1, 101):
    # Step 3: Check if the number is divisible by 3
    if number % 3 == 0:
        # Step 4: Add the number to the sum
        sum_divisible_by_3 += number

# Step 5: Print the result
print("The sum of numbers from 1 to 100 that are divisible by 3 is:", 
        sum_divisible_by_3)
# OUTPUT: The sum of numbers from 1 to 100 that are divisible by 3 is: 1683

# --- Program to calculate the sum of numbers from 1 to 100 
# divisible by 3 (without modulo)

# Step 1: Initialise a variable to store the sum
sum_divisible_by_3 = 0

# Step 2: Loop through numbers that are divisible by 3
# Start from 3, end at 100, and increment by 3
for number in range(3, 101, 3):
    # Step 3: Add the number to the sum
    sum_divisible_by_3 += number

# Step 4: Print the result
print("The sum of numbers from 1 to 100 that are divisible by 3 is:", 
        sum_divisible_by_3)
# OUTPUT: The sum of numbers from 1 to 100 that are divisible by 3 is: 1683
