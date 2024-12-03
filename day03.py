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
data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
ans = multiply(data)
ans = 0
data = ld.load_data(f'input{day}.txt')
for line in data:
    ans += multiply(line)
print(ans)


# Part 2 
def multiply3(s, mult):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    a = 0
    for i in range(4, len(s)):
        if s[i-4:i] == 'do()':
            mult = True
        elif i > 7 and s[i-7:i] == '''don't()''':
            mult = False
        elif mult and s[i-4:i] == 'mul(':
            ext = 9 if i + 9 < len(s) else len(s) - i
            st = s[i-4:i+ext]
            match = re.search(pattern, st)
            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                a += (x * y)
    return a, mult


ans = 0
data = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
ans = multiply3(data)
print(ans)

ans = 0
data = ld.load_data(f'input{day}.txt')
mult = True
for line in data:
    a, mult = multiply3(line, mult)
    ans += a
print(ans)
