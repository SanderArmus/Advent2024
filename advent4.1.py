def count_xmas_occurrences(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Check for the X-MAS pattern centered at (r, c)
    for r in range(1, rows - 1):  # Start from 1 to avoid out-of-bounds
        for c in range(1, cols - 1):  # Start from 1 to avoid out-of-bounds
            # Check for the pattern M.S
            if (grid[r-1][c-1] == 'M' and grid[r][c] == 'A' and grid[r+1][c-1] == 'M' and
                grid[r-1][c+1] == 'S' and grid[r][c+1] == 'M' and grid[r+1][c+1] == 'S'):
                count += 1  # Found one X-MAS

            # Check for the pattern M.S (backwards)
            if (grid[r-1][c-1] == 'M' and grid[r][c] == 'A' and grid[r+1][c-1] == 'M' and
                grid[r-1][c+1] == 'S' and grid[r][c-1] == 'M' and grid[r+1][c-1] == 'S'):
                count += 1  # Found one X-MAS (backwards)

    print(count)  # Print the total count of occurrences


# Function to read the grid from a file
def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


# Read the grid from the file
test_grid = read_grid_from_file('/Users/sanderarmus/Kool/Advent/advent4.txt')

# Call the function with the new test grid
count_xmas_occurrences(test_grid)