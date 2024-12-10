import itertools
count = 0
with open('advent/advent8.txt', 'r') as f:
    grid = [list(line.strip()) for line in f]
print(grid)
indexes = []
antinodes=[]
for row_index, row in enumerate(grid):
    for col_index, char in enumerate(row):
        if char != '.':
            indexes.append((row_index, col_index))
indexes.sort(key=lambda index: grid[index[0]][index[1]])

char_indexes = {}
for index in indexes:
    char = grid[index[0]][index[1]]
    if char not in char_indexes:
        char_indexes[char] = set()
    char_indexes[char].add(index)
for char in char_indexes:
    char_indexes[char] = list(char_indexes[char])
char_pairs = {}
for char, indexes_list in char_indexes.items():
    pairs = list(itertools.combinations(indexes_list, 2))
    char_pairs[char] = pairs
for char in char_pairs:
    for pair in char_pairs[char]:
        if (0 <= pair[0][0] + (pair[0][0] - pair[1][0]) < len(grid) and 
            0 <= pair[0][1] + (pair[0][1] - pair[1][1]) < len(grid[0])):
            antinodes.append([pair[0][0]+(pair[0][0]-pair[1][0]), pair[0][1]+(pair[0][1]-pair[1][1])])

        
        if (0 <= pair[1][0] + (pair[1][0] - pair[0][0]) < len(grid) and 
            0 <= pair[1][1] + (pair[1][1] - pair[0][1]) < len(grid[0])):
            antinodes.append([pair[1][0]+(pair[1][0]-pair[0][0]), pair[1][1]+(pair[1][1]-pair[0][1])])
print (antinodes)

#for antinode in antinodes:
#    for index in indexes:
#        if antinode[0] == index[0] and antinode[1]==index[1]:
#            antinodes.remove(antinode)


# Remove duplicates from antinodes
antinodes = list(set(tuple(antinode) for antinode in antinodes))  # Convert to set and back to list
print (len(antinodes))