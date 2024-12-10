def count_distinct_trails(mapmatrix, x, y, memo):
    rows = len(mapmatrix)
    cols = len(mapmatrix[0])
    
    # If this position has been computed before, return the result
    if (x, y) in memo:
        return memo[(x, y)]
    
    # If we've reached a '9', it's a valid trail end
    if mapmatrix[x][y] == '9':
        return 1
    
    # Directions to move (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    trails_count = 0
    
    # Explore all 4 directions (up, down, left, right)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # Check if the new position is within bounds and has the next height (+1)
        if 0 <= nx < rows and 0 <= ny < cols and int(mapmatrix[nx][ny]) == int(mapmatrix[x][y]) + 1:
            trails_count += count_distinct_trails(mapmatrix, nx, ny, memo)
    
    # Memoize the result for this position
    memo[(x, y)] = trails_count
    return trails_count

def sum_of_trailhead_ratings(mapmatrix):
    rows = len(mapmatrix)
    cols = len(mapmatrix[0])
    total_rating = 0
    memo = {}  # Memoization dictionary to store results for subproblems
    
    # Traverse the map and find all trailheads (positions with height '0')
    for i in range(rows):
        for j in range(cols):
            if mapmatrix[i][j] == '0':  # A trailhead is a position with height '0'
                rating = count_distinct_trails(mapmatrix, i, j, memo)
                total_rating += rating
    
    return total_rating

with open('advent/advent10.txt', 'r') as f:
    hikeMap = f.readlines()
mapmatrix=[]
for line in hikeMap:
    line=line.strip()
    mapmatrix.append([])
    for char in line:
        mapmatrix[-1].append(char)
print (mapmatrix[0])

result = sum_of_trailhead_ratings(mapmatrix)
print(result)