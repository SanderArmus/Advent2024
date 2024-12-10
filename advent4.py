def count_xmas_occurrences(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    found_patterns = []

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 'A':
                if (grid[r - 1][c - 1] == 'S' and
                    grid[r - 1][c + 1] == 'S' and
                    grid[r + 1][c - 1] == 'M' and
                    grid[r + 1][c + 1] == 'M'):
                    count += 1
                    found_patterns.append([(r - 1, c - 1), (r - 1, c + 1), (r, c), (r + 1, c - 1), (r + 1, c + 1)])

                if (grid[r - 1][c - 1] == 'M' and
                    grid[r - 1][c + 1] == 'M' and
                    grid[r + 1][c - 1] == 'S' and
                    grid[r + 1][c + 1] == 'S'):
                    count += 1
                    found_patterns.append([(r - 1, c - 1), (r - 1, c + 1), (r, c), (r + 1, c - 1), (r + 1, c + 1)])

                if (grid[r - 1][c - 1] == 'M' and
                    grid[r - 1][c + 1] == 'S' and
                    grid[r + 1][c - 1] == 'M' and
                    grid[r + 1][c + 1] == 'S'):
                    count += 1
                    found_patterns.append([(r - 1, c - 1), (r - 1, c + 1), (r, c), (r + 1, c - 1), (r + 1, c + 1)])

                if (grid[r - 1][c - 1] == 'S' and
                    grid[r - 1][c + 1] == 'M' and
                    grid[r + 1][c - 1] == 'S' and
                    grid[r + 1][c + 1] == 'M'):
                    count += 1
                    found_patterns.append([(r - 1, c - 1), (r - 1, c + 1), (r, c), (r + 1, c - 1), (r + 1, c + 1)])

    print(f"The 'X' formed by two MAS sequences appears {count} times.")

    output_grid = [['*' for _ in range(cols)] for _ in range(rows)]

    for pattern in found_patterns:
        for (row, col) in pattern:
            output_grid[row][col] = grid[row][col].lower()

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


filename = '/Users/sanderarmus/Kool/Advent/advent4.txt'
test_grid = read_grid_from_file(filename)

count_xmas_occurrences(test_grid)
