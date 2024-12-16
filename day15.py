# Day 15: Warehouse Woes

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}a.txt')
# data = ld.load_data(f'example{day}.txt')
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
            # Replace char with '.'
            map[i] = map[i][:j] + '.' + map[i][j+1:]

# Simulate moves according to instructions
pos = start
for line in instructions:
    for dir in line:
        x = pos[0]
        y = pos[1]

        if dir == '<':
            # Examine cells to the left
            left = map[y][:x]
            # Do nothing if there is no space
            if '.' in left:
                # Relevant string is from rightmost wall
                lefts = left.split('#')
                immediate_left = lefts[-1]
                if immediate_left[-1] == '.':
                    pos = (x-1, y)
                # Push boxes
                elif immediate_left == 'O':
                    b = immediate_left.count('O')
                    s = immediate_left.count('.')
                    print(b, s)
                    if s > 0:
                        # for i in range(len(immediate_left) - 2, -1, -1):
                        #todo: test below is waiting for an occurrence
                        for i in range(1, len(immediate_left)):
                            if immediate_left[i] == '.':
                                print('immediate left:', immediate_left)
                                print('Found space')
                                print(map[y])
                                print(map[y][:x])
                                print('O' * i)
                                print('.')
                                print(map[y][x:])
                                map[y] = map[y][:x] + ('O' * i) + '.' + map[y][x:]
        elif dir == '>':
            # Examine cells to the right
            right = map[y][x+1:]
            if '.' in right:
                rights = right.split('#')
                immediate_right = rights[0]
                # Move right
                if immediate_right[0] == '.':
                    pos = (x+1, y)
                # Push boxes
                elif immediate_right[0] == 'O':
                    # Count number of boxes to move and number of empty spaces
                    b = immediate_right.count('O')
                    s = immediate_right.count('.')
                    print(b, s)
                    # Do nothing if there is no space
                    if s > 0:
                        # immediate_right[0] becomes '.'; 
                        # in reality it is occupied by @
                        for i in range(1, len(immediate_right)):
                            # the first '.' in immediate_right becomes 'O'
                            if immediate_right[i] == '.':
                                map[y] = map[y][:x+1] + '.' + ('O' * i) + map[y][x+i+2:]
                                break
                        # Move because there was space
                        pos = (x+1, y)
        elif dir == '^':
            above = ''
            for i in range(y):
                above += map[i][x]
            if '.' in above:
                aboves = above.split('#')
                immediate_above = aboves[-1]
                if immediate_above == '.':
                    pos = (x, y-1)
                # TODO
        elif dir == 'v':
            below = ''
            for i in range(y+1, len(map)):
                below += map[i][x]
            if '.' in below:
                belows = below.split('#')
                immediate_below = belows[-1]
                if immediate_below == '.':
                    pos = (x, y+1)
                # TODO

ans = 0

for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == 'O':
            ans += 100 * i + j

print(ans)
print('Should be 2028')
