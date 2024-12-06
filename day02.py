# Day 2: Red-Nosed Reports

import load_data as ld
import os


def identify_unsafe_reports(levels):
    safe = True
    for i in range(1, len(levels)):
        if (abs(levels[i] - levels[i-1]) > 3) or (levels[i] == levels[i-1]):
            safe = False
    return safe


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
    safe = identify_unsafe_reports(levels)

    if safe and (levels == sorted(levels)
                 or levels[::-1] == sorted(levels[::-1])):
        ans += 1

print(ans)

# Part 2
ans = 0

for line in data:
    line_lst = line.split(' ')
    levels = []
    for x in line_lst:
        levels.append(int(x))
    safe = identify_unsafe_reports(levels)
    if safe and (levels == sorted(levels)
                 or levels[::-1] == sorted(levels[::-1])):
        ans += 1
    else:
        for j in range(len(levels)):
            levels_s = levels[:j] + levels[j+1:]
            safe = identify_unsafe_reports(levels_s)
            if safe and (levels_s == sorted(levels_s)
                         or levels_s[::-1] == sorted(levels_s[::-1])):
                ans += 1
                break

print(ans)
