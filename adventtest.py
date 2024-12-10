from collections import deque

def find_reachable_9s(mapmatrix, start_x, start_y):
    rows = len(mapmatrix)
    cols = len(mapmatrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    reachable_nines = 0
    queue = deque([(start_x, start_y, 0)]) 
    visited = set()
    visited.add((start_x, start_y))
    
    while queue:
        x, y, height = queue.popleft()
        if height == 9:
            reachable_nines += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                next_height = int(mapmatrix[nx][ny])
                if next_height == height + 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny, next_height))
    
    return reachable_nines
def sum_of_trailhead_scores(mapmatrix):
    rows = len(mapmatrix)
    cols = len(mapmatrix[0])
    total_score = 0

    for i in range(rows):
        for j in range(cols):
            if mapmatrix[i][j] == '0':
                score = find_reachable_9s(mapmatrix, i, j)
                total_score += score

    return total_score
with open('advent/advent10.txt', 'r') as f:
    hikeMap = f.readlines()
mapmatrix=[]
for line in hikeMap:
    line=line.strip()
    mapmatrix.append([])
    for char in line:
        mapmatrix[-1].append(char)
print (mapmatrix[0])

result = sum_of_trailhead_scores(mapmatrix)
print(result)
