# Day 4: Ceres Search

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans = 0
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == 'X':
            # Horizontal forward
            if j + 3 < len(line) and line[j:j+4] == 'XMAS':
                ans += 1
            # Horizontal backward
            if j - 3 >= 0 and line[j-3:j+1] == 'SAMX':
                ans += 1
            # Vertical forward
            if i + 3 < len(data) and data[i][j] == 'X' and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
                ans += 1
            # Vertical backward
            if i - 3 >= 0 and data[i][j] == 'X' and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
                ans += 1
            # Diagonal forward up
            if i - 3 >= 0 and j + 3 < len(line) and data[i][j] == 'X' and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
                ans += 1
            # Diagonal forward down
            if i + 3 < len(data) and j + 3 < len(line) and data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
                ans += 1
            # Diagonal backward up
            if i - 3 >= 0 and j - 3 >= 0 and data[i][j] == 'X' and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
                ans += 1
            # Diagonal backward down
            if i + 3 < len(data) and j - 3 >= 0 and data[i][j] == 'X' and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
                ans += 1

print(ans)
# 2336 correct

# Part 2
ans = 0
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == 'M':
            # Diagonal forward up
            if i - 2 >= 0 and j + 2 < len(line) and data[i][j] == 'M' and data[i-1][j+1] == 'A' and data[i-2][j+2] == 'S':
                # Diagonal forward down
                if data[i-2][j] == 'M' and data[i][j+2] == 'S':
                    ans += 1
                # Diagonal backward up
                elif data[i-2][j] == 'S' and data[i][j+2] == 'M':
                    ans += 1
            # Diagonal forward down
            if i + 2 < len(data) and j + 2 < len(line) and data[i][j] == 'M' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S':
                # Diagonal forward up
                if data[i+2][j] == 'M' and data[i][j+2] == 'S':
                    ans += 1
                # Diagonal backward down
                elif data[i+2][j] == 'S' and data[i][j+2] == 'M':
                    ans += 1
            # Diagonal backward up
            if i - 2 >= 0 and j - 2 >= 0 and data[i][j] == 'M' and data[i-1][j-1] == 'A' and data[i-2][j-2] == 'S':
                # Diagonal forward up
                if data[i-2][j] == 'M' and data[i][j-2] == 'S':
                    ans += 1
                # Diagonal backward down
                elif data[i-2][j] == 'S' and data[i][j-2] == 'M':
                    ans += 1
            # Diagonal backward down
            if i + 2 < len(data) and j - 2 >= 0 and data[i][j] == 'M' and data[i+1][j-1] == 'A' and data[i+2][j-2] == 'S':
                if data[i+2][j] == 'M' and data[i][j-2] == 'S':
                    ans += 1
                # Diagonal backward up
                elif data[i+2][j] == 'S' and data[i][j-2] == 'M':
                    ans += 1

print(ans // 2)
