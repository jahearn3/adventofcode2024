# Day 18: RAM Run

import heapq
import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

corrupted_coords = []

for i, line in enumerate(data):
    x, y = line.split(',')
    corrupted_coords.append((int(x), int(y)))

x_grid, y_grid = 71, 71
t = 1024
example = False
if example:
    x_grid, y_grid = 7, 7
    t = 12

start = (0, 0)
end = (x_grid - 1, y_grid - 1)
grid = [['.' for _ in range(x_grid)] for _ in range(y_grid)]
c = 0
for x, y in corrupted_coords:
    if c >= t:
        break
    grid[y][x] = '#'
    c += 1

for row in grid:
    print(''.join(row))

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def is_valid_move(m, x, y):
    return 0 <= x < len(m[0]) and 0 <= y < len(m) and m[y][x] == '.'


def bfs(maze, start, end):
    start_x, start_y = start
    end_x, end_y = end

    # Priority queue for the BFS (min-heap)
    pq = []
    # (score, x, y)
    heapq.heappush(pq, (0, start_x, start_y))

    # Visited states: (x, y) -> minimum score
    visited = {}

    while pq:
        score, x, y = heapq.heappop(pq)

        # If we reached the end position
        if (x, y) == (end_x, end_y):
            return score

        # Check if we've visited this state with a lower score
        if (x, y) in visited and visited[(x, y)] <= score:
            continue
        visited[(x, y)] = score

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(maze, new_x, new_y):
                heapq.heappush(pq, (score + 1, new_x, new_y))

    return float('inf')  # If no path is found


print('Start:', start)
print('End:', end)

# Calculate minimum score
min_score = bfs(grid, start, end)
print("Minimum score to reach the end:", min_score)

# Part 2
# Find which byte cuts off the path to the exit
# Golden Section Search
a = t  # lower bound
b = len(corrupted_coords)  # upper bound
phi = (1 + 5 ** 0.5) / 2  # Golden ratio
resphi = 2 - phi  # 1 / phi^2 (reciprocal of the square of phi)
# Initial points
c = int(b - resphi * (b - a))
d = int(a + resphi * (b - a))


def update_grid(cutoff):
    grid = [['.' for _ in range(x_grid)] for _ in range(y_grid)]
    count = 0
    for x, y in corrupted_coords:
        if count >= cutoff:
            break
        grid[y][x] = '#'
        count += 1
    return grid


while abs(c - d) > 0.1:
    grid = update_grid(c)
    result_c = bfs(grid, start, end)
    grid = update_grid(d)
    result_d = bfs(grid, start, end)

    # Compare results to narrow down the search
    if result_c < float('inf') and result_d < float('inf'):
        # If both are valid integers, we can compare them
        if result_c < result_d:
            b = d  # Move upper bound down
        else:
            a = c  # Move lower bound up
    elif result_c < float('inf'):
        a = c  # Move lower bound up
    elif result_d < float('inf'):
        b = d  # Move upper bound down
    else:
        # Both results are float('inf'), which means we need to adjust bounds
        # This typically would mean we need to explore other indices
        # For the sake of this algorithm, we can continue with the outer bounds
        a = c  # or b = d, depending on your strategy

    # Recalculate c and d
    c = int(b - resphi * (b - a))
    d = int(a + resphi * (b - a))

cutoff_index = int((a + b) / 2)

# Double check and get coordinates
for i in range(cutoff_index - 3, len(corrupted_coords)):
    grid = update_grid(i)
    result = bfs(grid, start, end)
    # print(i, result)
    if result == float('inf'):
        print('Coords:', corrupted_coords[i-1])
        break
