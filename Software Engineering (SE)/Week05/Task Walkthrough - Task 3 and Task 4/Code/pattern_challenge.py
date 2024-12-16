# Part2: Example
# Code to print the diamond pattern - Challenge

# Ask the user for the size of the diamond
max_width = int(input("Enter the max-width size of the diamond (Odd-number): "))

if max_width % 2 == 0:
    print("Please enter an odd number for the maximum width.")
else:
    # Calculate the size (half of max width + 1)
    size = (max_width // 2) + 1

    # Loop through all the rows
    for i in range(1, max_width + 1):
        # If i is less than or equal to size, it's the top half
        if i <= size:
            print(" " * (size - i) + "*" * ((2 * i) - 1))
        else:
            # Else, it's the bottom half of the diamond
            print(" " * (i - size) + "*" * (2 * (max_width - i) + 1))
