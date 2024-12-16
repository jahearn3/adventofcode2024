# Day 16: Reindeer Maze

import heapq
import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'example{day}b.txt')
data = ld.load_data(f'input{day}.txt')

# Directions: East, North, West, South (clockwise)
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # (dy, dx)


def is_valid_move(maze, x, y):
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and (maze[y][x] == '.' or maze[y][x] == 'E')


def bfs(maze, start, end):
    start_x, start_y = start
    end_x, end_y = end

    # Priority queue for the BFS (min-heap)
    pq = []
    # (score, x, y, direction_index)
    heapq.heappush(pq, (0, start_x, start_y, 3))  # starting facing East

    # Visited states: (x, y, direction_index) -> minimum score
    visited = {}

    while pq:
        score, x, y, dir_idx = heapq.heappop(pq)

        # If we reached the end position
        if (x, y) == (end_x, end_y):
            return score

        # Check if we've visited this state with a lower score
        if (x, y, dir_idx) in visited and visited[(x, y, dir_idx)] <= score:
            continue
        visited[(x, y, dir_idx)] = score

        # Move forward in the current direction
        dx, dy = directions[dir_idx]
        new_x, new_y = x + dx, y + dy
        if is_valid_move(maze, new_x, new_y):
            heapq.heappush(pq, (score + 1, new_x, new_y, dir_idx))

        # Rotate left (counter-clockwise)
        new_dir_idx = (dir_idx + 1) % 4
        heapq.heappush(pq, (score + 1000, x, y, new_dir_idx))

        # Rotate right (clockwise)
        new_dir_idx = (dir_idx - 1) % 4
        heapq.heappush(pq, (score + 1000, x, y, new_dir_idx))

    return float('inf')  # If no path is found


# Find start and end positions
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'S':
            start = (x, y)
        elif data[y][x] == 'E':
            end = (x, y)

print('Start:', start)
print('End:', end)

# Calculate minimum score
min_score = bfs(data, start, end)
print("Minimum score to reach the end:", min_score)
