# Day 12: Garden Groups

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}a.txt')
data = ld.load_data(f'example{day}b.txt')
# data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

areas = {}
perimeters = {}
visited = set()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
rows = len(data)
cols = len(data[0]) if rows > 0 else 0


def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols


def calculate_region_perimeter(start_r, start_c):
    plant_type = data[start_r][start_c]
    stack = [(start_r, start_c)]
    region_perimeter = 0

    while stack:
        r, c = stack.pop()

        # If this cell has already been visited, skip it
        if (r, c) in visited:
            continue

        # Mark the cell as visited
        visited.add((r, c))

        # Start with 4 sides for the current cell
        cell_perimeter = 4

        # Check all four directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # If the neighbor is valid and has the same plant type
            if is_valid(nr, nc):
                if data[nr][nc] == plant_type:
                    cell_perimeter -= 1
                    stack.append((nr, nc))

        # Add the cell's perimeter to the region's total perimeter
        region_perimeter += cell_perimeter

    return region_perimeter


for i, line in enumerate(data):
    for j, char in enumerate(line):
        if (j, i) not in visited:
            if char not in areas:
                areas[char] = 0
            areas[char] += 1
            region_perimeter = calculate_region_perimeter(j, i)
            if char not in perimeters:
                perimeters[char] = 0
            perimeters[char] += region_perimeter

            cell_perimeter = 4
            # Left side
            if j > 0 and data[i][j-1] == char:
                cell_perimeter -= 1
            # Right side
            if j < len(data[0]) - 1 and data[i][j+1] == char:
                cell_perimeter -= 1
            # Top side
            if i > 0 and data[i-1][j] == char:
                cell_perimeter -= 1
            # Bottom side
            if i < len(data) - 1 and data[i+1][j] == char:
                cell_perimeter -= 1
            perimeters[char] += cell_perimeter

ans = 0
for k in areas.keys():
    print(areas[k], perimeters[k])
    ans += areas[k] * perimeters[k]

print(ans)
