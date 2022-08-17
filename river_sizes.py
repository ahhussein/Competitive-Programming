# problem https://www.algoexpert.io/questions/river-sizes
# solution

from collections import deque

# Solution using BFS, trying every point as potential river starting point
def riverSizes(matrix):
    river_lengths = []
    visited = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue

            if (i,j) in visited:
                continue
                
            river_lengths.append(getRiverSize((i,j), visited, matrix))
    
    return river_lengths

def getRiverSize(starting_point, visited, matrix):
    q = deque()
    q.append(starting_point)
    visited.add(starting_point)
    
    river_length = 0
    while q:
        node_x, node_y = q.popleft()
        
        visited.add((node_x, node_y))

        river_length += 1
        
        # Try all adjacent points
        directions = [(-1,0), (0,-1), (1, 0), (0, 1)]
        for direction_x, direction_y in directions:
            child_x, child_y = (node_x + direction_x, node_y + direction_y)
            if child_x < 0 or child_x >= len(matrix):
                continue

            if child_y < 0 or child_y >= len(matrix[0]):
                continue

            if matrix[child_x][child_y] == 0:
                continue

            if (child_x, child_y) in visited:
                continue

            visited.add((child_x, child_y))
            q.append((child_x, child_y))

    return river_length

            
            
            
         
