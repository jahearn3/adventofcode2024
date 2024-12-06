# Day 1: Historian Hysteria

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

# data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans = 0

a = []
b = []

for line in data:
    a1, b1 = line.split('   ')
    a.append(int(a1))
    b.append(int(b1))

a = sorted(a)
b = sorted(b)

for i in range(len(a)):
    ans += abs(a[i] - b[i])

print(ans)

ans = 0

for i in range(len(a)):
    c = b.count(a[i])
    ans += a[i] * c

print(ans)
