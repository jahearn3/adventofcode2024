# Day 22: Monkey Market

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')


def mix(n, val):
    return n ^ val


def prune(n):
    return n % 16777216


def next_secret_number(n):
    n = mix(n * 64, n)
    n = prune(n)
    n = mix(n // 32, n)
    n = prune(n)
    n = mix(n * 2048, n)
    n = prune(n)
    return n


# secret_number = 123
# for i in range(10):
#     secret_number = next_secret_number(secret_number)
#     print(secret_number)


ans = 0

for line in data:
    secret_number = int(line)
    for j in range(2000):
        secret_number = next_secret_number(secret_number)
    ans += secret_number

print(ans)
