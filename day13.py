# Day 13: Claw Contraption

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

prizes = []
prize = {}

for line in data:
    if len(line) > 0:
        left, right = line.split(': ')
        x, y = right.split(',')
        if left[:6] == 'Button':
            dx = int(x.split('+')[1])
            dy = int(y.split('+')[1])
            prize[left[-1]] = (dx, dy)
        elif left == 'Prize':
            x_loc = int(x.split('=')[1])
            y_loc = int(y.split('=')[1])
            prize['loc'] = (x_loc, y_loc)
        else:
            print(left, 'not found')
    else:
        prizes.append(prize)
        prize = {}
prizes.append(prize)

ans = 0

for prize in prizes:
    a = 0  # number of times Button A is pushed
    solutions = []
    while a < 101:
        b = 0  # number of times Button B is pushed
        while b < 101:
            x_f = a * prize['A'][0] + b * prize['B'][0]
            y_f = a * prize['A'][1] + b * prize['B'][1]
            if x_f == prize['loc'][0] and y_f == prize['loc'][1]:
                cost = 3 * a + b
                solutions.append((a, b, cost))
                break
            elif x_f > prize['loc'][0] and y_f > prize['loc'][1]:
                break
            else:
                b += 1
        a += 1
    if len(solutions) > 0:
        min_cost = solutions[0][2]
        if len(solutions) > 1:
            for i in range(1, len(solutions)):
                if solutions[i][2] < min_cost:
                    min_cost = solutions[i][2]
        ans += min_cost

print(ans)
