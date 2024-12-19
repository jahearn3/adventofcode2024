# Day 19: Linen Layout

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

patterns = data[0]
designs = data[2:]

ans = 0
for design in designs:
    # Attempt to build design from patterns
    while True:
        reconstructed = ''
    # If successful, increment ans
        if reconstructed == design:
            ans += 1
            break


print(ans)
