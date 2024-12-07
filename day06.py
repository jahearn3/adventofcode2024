# Day 6: Guard Gallivant

import copy
import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans = 0

# Find guard
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '^' or char == '>' or char == '<' or char == 'v':
            pos = [j, i]
            dir = char

print('start:', pos, dir)
x, y = pos[0], pos[1]
print(data[y][x])

on_map = True
visited = []
limit = 9999
loops = 0

while on_map:
    x, y = pos[0], pos[1]
    loops += 1
    if loops >= limit:
        on_map = False
        print(f'Limit {limit} reached')
        break
    if dir == '^':
        if y-1 < 0:
            on_map = False
            visited.append(pos)
        else:
            if data[y-1][x] == '#':
                dir = '>'
            else:
                visited.append(pos)
                pos = [x, y-1]
    elif dir == '>':
        if x+1 >= len(data[y]):
            on_map = False
            visited.append(pos)
        else:
            if data[y][x+1] == '#':
                dir = 'v'
            else:
                visited.append(pos)
                pos = [x+1, y]
    elif dir == 'v':
        if y+1 >= len(data):
            on_map = False
            visited.append(pos)
        else:
            if data[y+1][x] == '#':
                dir = '<'
            else:
                visited.append(pos)
                pos = [x, y+1]
    elif dir == '<':
        if x-1 < 0:
            on_map = False
            visited.append(pos)
        else:
            if data[y][x-1] == '#':
                dir = '^'
            else:
                visited.append(pos)
                pos = [x-1, y]

# print(visited)
visited_tuples = [tuple(lst) for lst in visited]
ans = len(set(visited_tuples))
print(ans)

# Part 2

# Loop through all positions where there is a '.'
# Simulate guard's path and see if a limit is reached


def patrol(pos, grid):
    on_map = True
    visited = []
    limit = 9999
    loops = 0
    loop = False

    while on_map:
        visited.append(pos)
        x, y, dir = pos[0], pos[1], pos[2]
        loops += 1
        if loops >= limit:
            on_map = False
            loop = True
            break
        if dir == '^':
            if y-1 < 0:
                on_map = False
            else:
                if grid[y-1][x] == '#':
                    pos = [x, y, '>']
                else:
                    pos = [x, y-1, dir]
        elif dir == '>':
            if x+1 >= len(data[y]):
                on_map = False
            else:
                if grid[y][x+1] == '#':
                    pos = [x, y, 'v']
                else:
                    pos = [x+1, y, dir]
        elif dir == 'v':
            if y+1 >= len(data):
                on_map = False
            else:
                if grid[y+1][x] == '#':
                    pos = [x, y, '<']
                else:
                    pos = [x, y+1, dir]
        elif dir == '<':
            if x-1 < 0:
                on_map = False
            else:
                if grid[y][x-1] == '#':
                    pos = [x, y, '^']
                else:
                    pos = [x-1, y, dir]

    return loop


ans = 0
# Find guard
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '^':
            pos = [j, i, '^']

# Explore obstacles
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char != '#' and char != '^':
            grid = copy.deepcopy(data)
            grid[i] = grid[i][:j] + "#" + grid[i][j+1:]
            loop = patrol(pos, grid)
            if loop:
                ans += 1

print(ans)
