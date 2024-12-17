# Day 11: Plutonian Pebbles

import load_data as ld
import os
from functools import cache

f = os.path.basename(__file__)
day = f[3:5]

# data = ld.load_data(f'example{day}.txt')[0]
data = ld.load_data(f'input{day}.txt')[0]
numbers = data.split(' ')
numbers = [int(num) for num in numbers]
prev_numbers = numbers
next_numbers = []
ans = 0
for i in range(25):
    for n in prev_numbers:
        if n == 0:
            next_numbers.append(1)
        elif len(str(n)) % 2 == 0:
            left, right = str(n)[:len(str(n))//2], str(n)[len(str(n))//2:]
            next_numbers.append(int(left))
            next_numbers.append(int(right))
        else:
            next_numbers.append(n * 2024)
    prev_numbers = next_numbers
    next_numbers = []
ans = len(prev_numbers)

print(ans)

# Part 2
# Following the solution from HyperNeutrino


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps-1)
    s = str(stone)
    lg = len(s)
    if lg % 2 == 0:
        return count(int(s[:lg//2]), steps-1) + count(int(s[lg//2:]), steps-1)
    return count(stone * 2024, steps-1)


print(sum(count(stone, 75) for stone in numbers))
