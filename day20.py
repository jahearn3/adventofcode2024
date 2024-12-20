# Day 20: Race Condition

import load_data as ld
import os
from collections import deque

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == 'S':
            start = (j, i)
        elif char == 'E':
            end = (j, i)

print('start:', start)
print('end:', end)

cheat_start = (-1, -1)
cheat_end = (-1, -1)

# Count number of cheats that save at least 100 steps
limit = 100
limit = 15  # for the example
ans = 0

cheat_used = False

# print(ans)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up


def is_within_bounds(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def bfs_without_cheats(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = set()
    visited.add((start[0], start[1]))  # Only track (x, y)

    while queue:
        x, y, distance = queue.popleft()
        
        # If we reached the end, return the distance
        if (x, y) == end:
            return distance, visited
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if is_within_bounds(nx, ny, rows, cols):
                if grid[nx][ny] == '.' or grid[nx][ny] == 'E':
                    # Normal move
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, distance + 1))
    
    return float('inf'), visited  # If we cannot reach the end


def count_successful_cheats(grid):
    # Find start and end positions
    start = end = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)

    # Calculate distance without cheating
    normal_distance, _ = bfs_without_cheats(grid, start, end)

    # successful_cheats = 0
    successful_cheat_paths = set()

    # We need to check using 2 consecutive cheats
    rows, cols = len(grid), len(grid[0])

    # Check horizontal pairs
    for i in range(rows):
        for j in range(cols - 1):
            if grid[i][j] == '#' or grid[i][j + 1] == '#':
                # Temporarily replace with track
                gridij = grid[i][j]
                gridijp1 = grid[i][j + 1]
                grid[i][j] = '.'
                grid[i][j + 1] = '.'

                # Calculate distance after the cheat
                cheat_distance, cheat_visited_nodes = bfs_without_cheats(grid, start, end)
                
                if normal_distance - cheat_distance >= 15:
                    successful_cheat_paths.add(tuple(sorted(cheat_visited_nodes)))
                    print('cheat saves', normal_distance - cheat_distance, 'steps')
                
                # Restore the walls
                grid[i][j] = gridij
                grid[i][j + 1] = gridijp1

    # Check vertical pairs
    for i in range(rows - 1):
        for j in range(cols):
            if grid[i][j] == '#' or grid[i + 1][j] == '#':
                # Temporarily replace with track
                gridij = grid[i][j]
                gridip1j = grid[i + 1][j]
                grid[i][j] = '.'
                grid[i + 1][j] = '.'
                
                # Calculate distance after the cheat
                cheat_distance, cheat_visited_nodes = bfs_without_cheats(grid, start, end)
                if normal_distance - cheat_distance >= 15:
                    successful_cheat_paths.add(tuple(sorted(cheat_visited_nodes)))
                    print('cheat saves', normal_distance - cheat_distance, 'steps')
                
                # Restore the walls
                grid[i][j] = gridij
                grid[i + 1][j] = gridip1j

    return len(successful_cheat_paths)


# Example grid
racetrack = [
    "###############",
    "#...#...#.....#",
    "#.#.#.#.#.###.#",
    "#S#...#.#.#...#",
    "#######.#.#.###",
    "#######.#.#...#",
    "#######.#.###.#",
    "###..E#...#...#",
    "###.#######.###",
    "#...###...#...#",
    "#.#####.#.###.#",
    "#.#...#.#.#...#",
    "#.#.#.#.#.#.###",
    "#...#...#...###",
    "###############"
]

# Convert to list of lists
racetrack_list = [list(row) for row in racetrack]

# Count successful cheats
print(count_successful_cheats(racetrack_list))  # Should output 5
