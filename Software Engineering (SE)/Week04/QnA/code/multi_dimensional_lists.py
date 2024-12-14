# ============= Nested For loop Examples

# Example 1: Nested for loops to iterate over a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for value in row:
        print(value)

# Example 2: Nested Loop with break to Exit Inner Loop
# --> Stop the inner loop when a condition is met
for i in range(5):
    for j in range(5):
        if j == 3:  # Exit inner loop when j is 3
            print(f"Breaking inner loop when i = {i}, j = {j}")
            break  # Break the inner loop

# Example 3: For Loop Multiplication Table
print("\nMultiplication Table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("")  # Blank line for separation

# ----> Multi-dimentional list challenge
"""
You are tasked with simulating a classroom seating arrangement 
using a multi-dimensional list in Python. 
Each row in the classroom can hold 4 seats, and the seats can 
either be occupied (represented by 1) or empty (represented by 0).

Write a Python program that:

- Creates a 2D list to represent the classroom's 
seating arrangement with 4 rows and 4 columns.
- Calculates the total number of occupied seats 
(i.e., the number of 1s in the list).
- Displays the classroom seating arrangement and the 
total number of students present based on the occupied seats.
- Requirements:
Ensure that the seating arrangement is displayed in a readable format 
and the total number of students present is printed at the end.
"""

# Multi-dimensional list representing a classroom seating arrangement
classroom = [
    [1, 1, 0, 1],  # Row 1 (1 = occupied, 0 = empty)
    [0, 1, 1, 1],  # Row 2
    [1, 0, 1, 0],  # Row 3
    [1, 1, 1, 0]   # Row 4
]

# Main logic to count the number of students (occupied seats)
student_count = 0

# Iterate through each row and count occupied seats (1s)
for row in classroom:
    student_count += sum(row)  # sum(row) gives the number of occupied seats in that row

# Display the seating arrangement
print("Classroom seating arrangement:")
for row in classroom:
    print(row)

# Display the total number of students present
print(f"\nTotal students present: {student_count}")
