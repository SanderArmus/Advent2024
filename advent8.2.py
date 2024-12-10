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
        r=pair[0][0]
        c=pair[0][1]
        while (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            antinodes.append((r,c))
            r+=pair[0][0]-pair[1][0]
            c+=pair[0][1]-pair[1][1]
        r=pair[1][0]
        c=pair[1][1]
        while (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            antinodes.append((r,c))
            r+=pair[1][0]-pair[0][0]
            c+=pair[1][1]-pair[0][1]
print (antinodes)
antinodes = list(set(tuple(antinode) for antinode in antinodes))
print (len(antinodes))