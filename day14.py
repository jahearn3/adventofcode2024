# Day 14: Restroom Redoubt

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

grid_x = 101
grid_y = 103
# grid_x = 11
# grid_y = 7
seconds = 100

robots = []
for line in data:
    p, v = line.split(' ')
    pos = p.split('=')[1]
    vel = v.split('=')[1]
    x, y = pos.split(',')
    vx, vy = vel.split(',')
    robots.append((int(x), int(y), int(vx), int(vy)))

# print(robots)
prev_robots = robots
# prev_robots = [(2, 4, 2, -3)]
# print(prev_robots)
for t in range(seconds):
    next_robots = []
    for r in prev_robots:
        x, y, vx, vy = r
        x = (x + vx) % grid_x
        y = (y + vy) % grid_y
        next_robots.append((x, y, vx, vy))
    # print(next_robots)
    prev_robots = next_robots


half_x = grid_x // 2
half_y = grid_y // 2

q1, q2, q3, q4 = 0, 0, 0, 0

for r in next_robots:
    x, y, vx, vy = r
    # print(r)
    if x < half_x and y < half_y:
        q1 += 1
    elif x > half_x and y < half_y:
        q2 += 1
    elif x < half_x and y > half_y:
        q3 += 1
    elif x > half_x and y > half_y:
        q4 += 1
print(q1, q2, q3, q4)
ans = q1 * q2 * q3 * q4
print(ans)


# Part 2
min_safety_factor = ans
prev_robots = robots
seconds = 10
t = 0
while True:
    anomaly = False
    t += 1
    next_robots = []
    for r in prev_robots:
        x, y, vx, vy = r
        x = (x + vx) % grid_x
        y = (y + vy) % grid_y
        next_robots.append((x, y, vx, vy))
    q1, q2, q3, q4 = 0, 0, 0, 0
    for r in next_robots:
        x, y, vx, vy = r
        if x < half_x and y < half_y:
            q1 += 1
        elif x > half_x and y < half_y:
            q2 += 1
        elif x < half_x and y > half_y:
            q3 += 1
        elif x > half_x and y > half_y:
            q4 += 1
    safety_factor = q1 * q2 * q3 * q4
    if safety_factor < min_safety_factor:
        min_safety_factor = safety_factor
        print(f'New min safety factor {safety_factor} after {t} seconds')
    if (t % 500) == 0:
        print(f'{t} seconds have elapsed.')
    # Already looked at first 1814 seconds
    # and 7000 < t < 7200
    if t > 6240 and safety_factor / min_safety_factor < 1.1:
        for i in range(grid_y):
            row = ''
            for j in range(grid_x):
                c = 0
                for rob in next_robots:
                    xx, yy, _, _ = rob
                    if j == xx and i == yy:
                        c += 1
                if c == 0:
                    row += '.'
                else:
                    row += '#'
            if not anomaly and ('#' * 9) in row:
                anomaly = True
                print(f'After {t} seconds')
            if anomaly:
                print(row)

    prev_robots = next_robots
    if anomaly:
        break
