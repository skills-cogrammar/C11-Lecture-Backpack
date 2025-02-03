'''
In this example, we will explore a simplified implementation of a Minesweeper-style
grid processing algorithm using a fixed 3x3 grid. Our goal is to replace each zero 
with a count of adjacent non-zero values. For example:

The 3x3 grid
[[0, 2, 0],
 [4, 0, 1],
 [0, 5, 0]]

Results in
[2, 2, 2]
[4, 4, 1]
[2, 5, 2]
'''


def process_grid(grid):
    # Because we are assuming the input grid is always 3x3, the resulting grid 
    # will also be 3x3 

    # Create resulting grid
    result_grid = [[0, 0, 0],
                   [0, 0, 0],  
                   [0, 0, 0]] 

    # These for loops allow us to iterate over grid values 
    for row in range(3): # row = 0 first row
        for col in range(3):   # col = 0 first column

            # Check if grid values is a 0 or not
            if grid[row][col] == 0:  # grid[0][0] = 0
                # We call on the function that counts the surrounding non-zero values
                surrounding_count = count_surrounding_non_zero(grid, row, col)

                # Replace 0 in result_grid with the count of non-zero values
                result_grid[row][col] = surrounding_count  
            else:
                # If grid value is NOT a zero, we simply replace the item in the result_grid 
                # with the number itself (we do nothing to non-zero values)
                result_grid[row][col] = grid[row][col] 

    return result_grid


def count_surrounding_non_zero(grid, row = 1, col = 1):
    # Possible directions for neighbors 
    # List items displayed to show where they sit (top left, top, top right, to the left, and so on respectively)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    count = 0 

    # Neighbours directions
    for direct_row, direct_column in directions: # (-1, -1)
        new_row = row + direct_row
        new_col = col + direct_column 
        
        # Make sure the new position for neighbour is within the bounds of our grid
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            if grid[new_row][new_col] != 0: 
                count += 1  

    return count

grid = [[0, 2, 0],
        [4, 0, 1],
        [0, 5, 9]]

# Simply call on process grid and it will take care of calling count_surrounding_non_zero() when necessary
result = process_grid(grid)

# Iterate over result_grid to display row items (the lists inside the main list)
for row in result:
    print(row)
