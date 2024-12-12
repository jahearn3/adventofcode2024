# Day 12: Garden Groups

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}a.txt')
# data = ld.load_data(f'example{day}b.txt')
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
    def calculate_region_properties(start_r, start_c):
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
                        cell_perimeter -= 1  # Shared side with the same plant
                        stack.append((nr, nc))  # Add connected cell for further exploration
                    else:
                        # If the neighbor is not the same plant type, it contributes to perimeter
                        continue
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
                region_perimeter, region_area = calculate_region_properties(r, c)

                # Initialize the list if the plant type is not already in the dictionary
                if plant_type not in regions:
                    regions[plant_type] = []

                # Append the (perimeter, area) tuple to the list for the plant type
                regions[plant_type].append((region_perimeter, region_area))

    return regions


regions = calculate_perimeters_and_areas(data)

ans = 0

for k, v in regions.items():
    for r in v:
        perimeter, area = r
        ans += perimeter * area

print(ans)
