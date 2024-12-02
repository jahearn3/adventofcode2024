# Day 2: Red-Nosed Reports

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans = 0

for line in data:
    line_lst = line.split(' ')
    levels = []
    for x in line_lst:
        levels.append(int(x))
    safe = True
    for i in range(1, len(levels)):
        if (abs(levels[i] - levels[i-1]) > 3) or (levels[i] == levels[i-1]):
            safe = False

    if safe and (levels == sorted(levels) or levels[::-1] == sorted(levels[::-1])):
        ans += 1

print(ans)

# Part 2
ans = 0

for line in data:
    line_lst = line.split(' ')
    levels = []
    for x in line_lst:
        levels.append(int(x))
    safe = True
    for i in range(1, len(levels)):
        if (abs(levels[i] - levels[i-1]) > 3) or (levels[i] == levels[i-1]):
            safe = False
    if safe and (levels == sorted(levels) or levels[::-1] == sorted(levels[::-1])):
        ans += 1
    else:
        counted = False
        for j in range(len(levels)):
            levels_minus_one = levels[:j] + levels[j+1:]
            safe = True
            for k in range(1, len(levels_minus_one)):
                if (abs(levels_minus_one[k] - levels_minus_one[k-1]) > 3) or (levels_minus_one[k] == levels_minus_one[k-1]):
                    safe = False
            if safe and (levels_minus_one == sorted(levels_minus_one) or levels_minus_one[::-1] == sorted(levels_minus_one[::-1])):
                if not counted:
                    ans += 1
                    counted = True

print(ans)
