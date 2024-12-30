# Day 15: Warehouse Woes

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}a.txt')
# data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

grid = []
instructions = []
blank = False
for line in data:
    if len(line) == 0:
        blank = True
    elif blank:
        instructions.append(line)
    else:
        # converting to list to allow modifications
        # by assignment (str does not support that)
        grid.append(list(line))

# Find robot
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == '@':
            start = (r, c)
            print('start:', start)
            break
    else:
        continue
    break

# Using solution from HyperNeutrino
# Simulate moves according to instructions
pos = start
for line in instructions:
    for dir in line:
        dr = {'^': -1, 'v': 1}.get(dir, 0)
        dc = {'<': -1, '>': 1}.get(dir, 0)
        targets = [(r, c)]
        cr = r
        cc = c
        go = True  # Empty space to move
        while True:
            cr += dr
            cc += dc
            char = grid[cr][cc]
            if char == '#':
                go = False
                break
            if char == 'O':
                targets.append((cr, cc))
            if char == '.':
                break
        if not go: # No empty space; no updates
            continue
        # Moving the robot
        grid[r][c] = '.'
        grid[r + dr][c + dc] = '@'
        # Moving the boxes
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = 'O'
        # Updating the robot's position
        r += dr
        c += dc

ans = 0

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == 'O':
            ans += 100 * i + j

print(ans)
