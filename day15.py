# Day 15: Warehouse Woes

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

map = []
instructions = []
blank = False
for line in data:
    if len(line) == 0:
        blank = True
    elif blank:
        instructions.append(line)
    else:
        map.append(line)

# Find robot
for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == '@':
            start = (j, i)
            print('start:', start)

# Simulate moves according to instructions
for line in instructions:
    for dir in line:
        # TODO
        pass

ans = 0

for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == 'O':
            ans += 100 * i + j

print(ans)
