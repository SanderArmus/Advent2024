from collections import defaultdict

def can_guard_get_stuck(lab_map, guard_start, obstruction_position):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    direction_index = 0  # Start facing up
    visited_positions = set()  # Track (position, direction) to detect loops
    guard_position = guard_start

    # Place the obstruction temporarily
    r, c = obstruction_position
    lab_map[r][c] = '#'

    while True:
        r, c = guard_position
        # Track both position and direction
        if (guard_position, direction_index) in visited_positions:
            # The guard is stuck in a loop
            lab_map[r][c] = '.'  # Restore the original state
            return True
        visited_positions.add((guard_position, direction_index))
        
        # Calculate the next position
        next_r = r + directions[direction_index][0]
        next_c = c + directions[direction_index][1]

        # Check if next position is within bounds
        if 0 <= next_r < len(lab_map) and 0 <= next_c < len(lab_map[0]):
            if lab_map[next_r][next_c] == '#':
                direction_index = (direction_index + 1) % 4  # Turn right if obstacle
            else:
                guard_position = (next_r, next_c)
        else:
            # Out of bounds, stop the simulation
            break
    
    lab_map[r][c] = '.'  # Restore the original state
    return False


def count_obstruction_positions(lab_map, guard_start):
    count = 0
    for r in range(len(lab_map)):
        for c in range(len(lab_map[r])):
            if (r, c) != guard_start and lab_map[r][c] == '.':
                # Temporarily place an obstruction
                lab_map[r][c] = '#'
                if can_guard_get_stuck(lab_map, guard_start, (r, c)):
                    count += 1
                # Restore the original state
                lab_map[r][c] = '.'  
    return count


def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]  # Read and return the matrix


# Example usage
filename = '/Users/sanderarmus/Kool/Advent/advent6.1.txt'
matrix = read_matrix_from_file(filename)

# Find the guard's starting position
guard_start = None
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == '^':
            guard_start = (r, c)
            break
    if guard_start:
        break

valid_positions_count = count_obstruction_positions(matrix, guard_start)
print(valid_positions_count)  # Should output the number of valid obstruction positions
