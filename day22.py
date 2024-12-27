# Day 22: Monkey Market

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')


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

# Part 2
seq = [None, None, None, None]  # last 4 changes
best_seq = seq
max_bananas = 0
for a in range(-3, 0):
    for b in range(0, 2):
        for c in range(-2, 0):
            for d in range(2, 4):
                bananas = 0
                for line in data:
                    secret_number = int(line)
                    prev_price = 0
                    for j in range(2000):
                        secret_number = next_secret_number(secret_number)
                        price = int(str(secret_number)[-1])
                        change = price - prev_price
                        seq.pop(0)
                        seq.append(change)
                        prev_price = price
                        if seq == [a, b, c, d]:
                            print(seq, price)
                            bananas += price
                            break
                if bananas > max_bananas:
                    best_seq = [a, b, c, d]
                    max_bananas = bananas


print(best_seq, max_bananas)
