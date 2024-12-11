# Day 8: Resonant Collinearity

import load_data as ld
import math
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

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
                gcd = math.gcd(x_diff, y_diff)
                step_x = x_diff // gcd
                step_y = y_diff // gcd
                for k in range(-gcd * 50, gcd * 50 + 1):
                    x = x1 + k * step_x
                    y = y1 + k * step_y
                    if -1 < x < len(data[0]) and -1 < y < len(data):
                        antinode_locs.append(str(x) + ',' + str(y))

ans = len(set(antinode_locs))
print(ans)
