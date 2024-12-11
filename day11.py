# Day 11: Plutonian Pebbles

import load_data as ld
import os

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
    print(i+1, len(prev_numbers))
ans = len(prev_numbers)

print(ans)

# Part 2
# for i in range(75):
