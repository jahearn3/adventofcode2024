# Day 5: Print Queue

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

rules = []
updates = []
blank = False
for line in data:
    if len(line) == 0:
        blank = True
    elif blank:
        page_numbers = line.split(',')
        updates.append([int(s) for s in page_numbers])
    else:
        a, b = line.split('|')
        rules.append((int(a), int(b)))

ans = 0

for u, update in enumerate(updates):
    rr = []
    for rule in rules:
        a, b = rule
        if a in update and b in update:
            a_i = update.index(a)
            b_i = update.index(b)
            if a_i < b_i:
                rr.append(1)
            else:
                rr.append(0)
    if sum(rr) == len(rr):
        mid = int((len(update) / 2) - 0.5)
        # print(update, mid)
        ans += update[mid]

print(ans)

# Part 2

