# Day 12: Garden Groups

import load_data as ld
import os
from collections import deque

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}a.txt')
data = ld.load_data(f'example{day}b.txt')
data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')


def calculate_perimeters_and_areas(grid):
    # Create a dictionary to store perimeters and areas
    regions = {}

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # To track visited cells
    visited = set()

    # Directions for neighboring cells (left, right, up, down)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Function to calculate perimeter and area for a region using DFS
    def calc_region_properties(start_r, start_c):
        plant_type = grid[start_r][start_c]
        stack = [(start_r, start_c)]
        region_perimeter = 0
        region_area = 0

        while stack:
            r, c = stack.pop()

            # If this cell has already been visited, skip it
            if (r, c) in visited:
                continue

            # Mark the cell as visited
            visited.add((r, c))
            region_area += 1  # Each cell contributes to the area

            # Start with 4 sides for the current cell
            cell_perimeter = 4

            # Check all four directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # If the neighbor is valid
                if is_valid(nr, nc):
                    if grid[nr][nc] == plant_type:
                        # Shared side with the same plant
                        cell_perimeter -= 1
                        # Add connected cell for further exploration
                        stack.append((nr, nc))
                    else:
                        # If the neighbor is not the same plant type,
                        continue  # it contributes to perimeter
                else:
                    # If out of bounds, contributes to perimeter
                    continue

            # Add the cell's perimeter to the region's total perimeter
            region_perimeter += cell_perimeter

        return region_perimeter, region_area

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant_type = grid[r][c]
                # Calculate the perimeter and area for this region
                region_perimeter, region_area = calc_region_properties(r, c)

                # Initialize the list if not already in the dictionary
                if plant_type not in regions:
                    regions[plant_type] = []

                # Append (perimeter, area) to the list for the plant type
                regions[plant_type].append((region_perimeter, region_area))

    return regions


regions = calculate_perimeters_and_areas(data)

ans = 0

for k, v in regions.items():
    for r in v:
        perimeter, area = r
        ans += perimeter * area

print(ans)

# Part 2
# Solution from HyperNeutrino
regions = []

# Get the dimensions of the grid
rows = len(data)
cols = len(data[0])

# To track visited cells
seen = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        region = {(r, c)}
        q = deque([(r, c)])
        crop = data[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if data[nr][nc] != crop:
                    continue
                if (nr, nc) in region:
                    continue
                region.add((nr, nc))
                q.append((nr, nc))
        seen |= region  # updates the seen set
        regions.append(region)


def sides(region):
    # Number of sides is the numbers of corners
    corner_candidates = set()
    for r, c in region:
        for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corner_candidates.add((cr, cc))
    corners = 0
    for cr, cc in corner_candidates:
        config = [(sr, sc) in region for sr, sc in [(cr - 0.5, cc - 0.5), (cr + 0.5, cc - 0.5), (cr + 0.5, cc + 0.5), (cr - 0.5, cc + 0.5)]]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif number == 3:
            corners += 1
    return corners


print(sum(len(region) * sides(region) for region in regions))
