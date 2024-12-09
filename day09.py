# Day 9: Disk Fragmenter

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')[0]
# data = ld.load_data(f'input{day}.txt')[0]

layout = []
file_length = True
id = 0
free_space = 0
for char in data:
    if not file_length:
        for j in range(int(char)):
            layout.append('.')
        file_length = True
        free_space += int(char)
    else:
        for j in range(int(char)):
            layout.append(str(id))
        file_length = False
        id += 1

compact_file = []
idx_to_move = -1
for i in range(len(layout) - free_space):
    if layout[i] != '.':
        compact_file.append(int(layout[i]))
    else:
        while layout[idx_to_move] == '.':
            idx_to_move -= 1
        compact_file.append(int(layout[idx_to_move]))
        idx_to_move -= 1

ans = 0
for i in range(len(compact_file)):
    ans += i * compact_file[i]
print(ans)

# Part 2
compact_file = []
idx_to_move = -1
for i in range(len(layout) - free_space):
    if layout[i] != '.':
        compact_file.append(int(layout[i]))
    else:
        # See how much free space in this slot
        j = i
        while layout[j] == '.':
            j += 1
        # Find next available files to move
        # TODO- Here
        while layout[idx_to_move] == '.':
            idx_to_move -= 1

        compact_file.append(int(layout[idx_to_move]))
        idx_to_move -= 1

ans = 0
for i in range(len(compact_file)):
    ans += i * compact_file[i]
print(ans)
