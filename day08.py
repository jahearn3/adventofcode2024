# Day 8: Resonant Collinearity

import load_data as ld
import numpy as np
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

antennas = {}
# Find antennas
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char != '.':
            if char not in antennas:
                antennas[char] = [(j, i)]
            else:
                antennas[char].append((j, i))

antinode_locs = []
# Place antinodes
for k, v in antennas.items():
    for vv in v:
        x1, y1 = vv
        for vvv in v:
            if vvv != vv:
                x2, y2 = vvv
                x_diff = x2 - x1
                y_diff = y2 - y1
                xa = x1 - x_diff
                ya = y1 - y_diff
                if -1 < xa < len(data[0]) and -1 < ya < len(data):
                    antinode_locs.append(str(xa) + ',' + str(ya))

ans = len(set(antinode_locs))
print(ans)

# Part 2

antinode_locs = []
# Place antinodes
for k, v in antennas.items():
    for vv in v:
        x1, y1 = vv
        for vvv in v:
            if vvv != vv:
                x2, y2 = vvv
                x_diff = x2 - x1
                y_diff = y2 - y1
                xa = x1 - x_diff
                ya = y1 - y_diff
                if -1 < xa < len(data[0]) and -1 < ya < len(data):
                    antinode_locs.append(str(xa) + ',' + str(ya))
                angle = np.arctan2(ya, xa)

ans = len(set(antinode_locs))
print(ans)
