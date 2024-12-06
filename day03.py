# Day 03: Mull It Over

import load_data as ld
import os
import re


f = os.path.basename(__file__)
day = f[3:5]


# Part 1
def multiply(s):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, s)
    a = 0
    for match in matches:
        x = int(match[0])
        y = int(match[1])
        a += (x * y)
    return a


ans = 0
data = ld.load_data(f'example{day}a.txt')
data = ld.load_data(f'input{day}.txt')
for line in data:
    ans += multiply(line)
print(ans)


# Part 2
def multiply2(s, multiplication):
    a = 0
    for i in range(4, len(s)):
        # Turn on multiplication if do() occurs
        if s[i-4:i] == 'do()':
            multiplication = True
        # Turn off multiplication if don't() occurs
        elif i > 7 and s[i-7:i] == '''don't()''':
            multiplication = False
        # Multiply if multiplication is on and mul(x,y) occurs
        elif multiplication and s[i-4:i] == 'mul(':
            # Extend string by 9 chars or to end of line
            ext = 9 if i + 9 < len(s) else len(s) - i
            st = s[i-4:i+ext]
            # Search for a match in the abbreviated string
            a += multiply(st)
    return a, multiplication


ans = 0
data = ld.load_data(f'example{day}b.txt')
data = ld.load_data(f'input{day}.txt')
multiplication = True
for line in data:
    a, multiplication = multiply2(line, multiplication)
    ans += a
print(ans)
