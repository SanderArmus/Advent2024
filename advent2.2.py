filename = '/Users/sanderarmus/Kool/Advent/advent2.txt'
def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

matrix = read_matrix_from_file(filename)
print(matrix)
safe_count = 0 
for row in matrix:
    if (row == sorted(row) or row == sorted(row, reverse=True)):
        i = 0
        is_safe = True  
        while i < len(row) - 1: 
            if 1 <= abs(row[i] - row[i + 1]) <= 3: 
                i += 1
            else:
                is_safe = False 
                break 
        if is_safe:
            safe_count += 1
print(safe_count) 