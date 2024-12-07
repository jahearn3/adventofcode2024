# Day 7: Bridge Repair

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans = 0
for line in data:
    a, b = line.split(':')
    bs = b.strip().split(' ')
    test_value = int(a)
    numbers = [int(n) for n in bs]
    calculations = []
    prev_q = []
    next_q = []
    for i in range(1, len(numbers)):
        # Add
        if i == 1:
            if i == len(numbers) - 1:
                calculations.append(numbers[i-1] + numbers[i])
            else:
                next_q.append(numbers[i-1] + numbers[i])
        else:
            for res in prev_q:
                if i == len(numbers) - 1:
                    calculations.append(res + numbers[i])
                else:
                    next_q.append(res + numbers[i])
        # Multiply
        if i == 1:
            if i == len(numbers) - 1:
                calculations.append(numbers[i-1] * numbers[i])
            else:
                next_q.append(numbers[i-1] * numbers[i])
        else:
            for res in prev_q:
                if i == len(numbers) - 1:
                    calculations.append(res * numbers[i])
                else:
                    next_q.append(res * numbers[i])
        prev_q = next_q
        next_q = []

    if test_value in calculations:
        ans += test_value

print(ans)

# Part 2
ans = 0
for line in data:
    a, b = line.split(':')
    bs = b.strip().split(' ')
    test_value = int(a)
    numbers = [int(n) for n in bs]
    calculations = []
    prev_q = []
    next_q = []
    for i in range(1, len(numbers)):
        # Add
        if i == 1:
            if i == len(numbers) - 1:
                calculations.append(numbers[i-1] + numbers[i])
            else:
                next_q.append(numbers[i-1] + numbers[i])
        else:
            for res in prev_q:
                if i == len(numbers) - 1:
                    calculations.append(res + numbers[i])
                else:
                    next_q.append(res + numbers[i])
        # Multiply
        if i == 1:
            if i == len(numbers) - 1:
                calculations.append(numbers[i-1] * numbers[i])
            else:
                next_q.append(numbers[i-1] * numbers[i])
        else:
            for res in prev_q:
                if i == len(numbers) - 1:
                    calculations.append(res * numbers[i])
                else:
                    next_q.append(res * numbers[i])
        # Concatenate
        if i == 1:
            if i == len(numbers) - 1:
                calculations.append(int(str(numbers[i-1]) + str(numbers[i])))
            else:
                next_q.append(int(str(numbers[i-1]) + str(numbers[i])))
        else:
            for res in prev_q:
                if i == len(numbers) - 1:
                    calculations.append(int(str(res) + str(numbers[i])))
                else:
                    next_q.append(int(str(res) + str(numbers[i])))
        prev_q = next_q
        next_q = []

    if test_value in calculations:
        ans += test_value

print(ans)
