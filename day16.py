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


def is_valid_move(m, x, y):
    return 0 <= x < len(m[0]) and 0 <= y < len(m) and (m[y][x] == '.' or m[y][x] == 'E')


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

# Part 2


def bfs2(maze, start, end):
    start_x, start_y = start
    end_x, end_y = end

    # Priority queue for the BFS (min-heap)
    pq = []
    # (score, x, y, direction_index, path)
    heapq.heappush(pq, (0, start_x, start_y, 3, {(start_x, start_y)}))

    # Minimum score found
    min_score = float('inf')
    # Set to track unique tiles in the best paths
    unique_tiles = set()

    # Visited states: (x, y, direction_index) -> minimum score
    visited = {}

    while pq:
        score, x, y, dir_idx, path = heapq.heappop(pq)

        # If we reached the end position
        if (x, y) == (end_x, end_y):
            if score < min_score:
                min_score = score
                unique_tiles = path  # Update unique tiles on best path
            elif score == min_score:
                unique_tiles.update(path)  # Add tiles from another best path
            continue

        # Check if we've visited this state with a lower score
        if (x, y, dir_idx) in visited and visited[(x, y, dir_idx)] < score:
            continue
        visited[(x, y, dir_idx)] = score

        # Move forward in the current direction
        dx, dy = directions[dir_idx]
        new_x, new_y = x + dx, y + dy
        if is_valid_move(maze, new_x, new_y):
            new_path = path | {(new_x, new_y)}  # Add new tile to path
            heapq.heappush(pq, (score + 1, new_x, new_y, dir_idx, new_path))

        # Rotate left (counter-clockwise)
        new_dir_idx = (dir_idx + 1) % 4
        heapq.heappush(pq, (score + 1000, x, y, new_dir_idx, path))

        # Rotate right (clockwise)
        new_dir_idx = (dir_idx - 1) % 4
        heapq.heappush(pq, (score + 1000, x, y, new_dir_idx, path))

    return min_score, unique_tiles


# Calculate minimum score and unique tiles
min_score, unique_tiles = bfs2(data, start, end)
print("Minimum score to reach the end:", min_score)
print("Number of unique tiles part of the best paths:", len(unique_tiles))
