# Day 25: Code Chronicle

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

keys = []
locks = []


for i in range(0, len(data), 8):
    lock = None
    if data[i] == '.....':
        lock = False
    elif data[i] == '#####':
        lock = True
    cc = [0] * 5
    for j in range(8):
        if i + j >= len(data):
            break
        if len(data[i+j]) > 0:
            row = data[i+j]
            for idx, char in enumerate(row):
                if char == '#':
                    cc[idx] += 1
    result = tuple(c - 1 for c in cc)
    if lock:
        locks.append(result)
    else:
        keys.append(result)

ans = 0
for k in keys:
    for lock in locks:
        fit = True
        for c in range(5):
            if k[c] + lock[c] > 5:
                fit = False
                break
        if fit:
            ans += 1

print(ans)
