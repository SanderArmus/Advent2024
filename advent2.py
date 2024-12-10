filename = '/Users/sanderarmus/Kool/Advent/advent2.txt'
def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

matrix = read_matrix_from_file(filename)

safe_count = 0 
removable_count = 0 
def is_safe(row):
    for i in range(len(row) - 1):
        if not (1 <= abs(row[i] - row[i + 1]) <= 3):
            return False
    return row == sorted(row) or row == sorted(row, reverse=True)

for row in matrix:
    if is_safe(row):
        safe_count += 1
    else:
        for j in range(len(row)):
            modified_row = row[:j] + row[j + 1:]
            if is_safe(modified_row):
                removable_count += 1
                break 

print(safe_count)
print(removable_count) 
print(safe_count+removable_count)