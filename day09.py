# Day 9: Disk Fragmenter

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')[0]
data = ld.load_data(f'input{day}.txt')[0]

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
idx_to_move = -1
compact = False
left_idx = next((i for i, v in enumerate(layout) if v == '.'), -1)
right_idx = len(layout) - 1
while left_idx < right_idx:
    # Get next rightmost file
    char = layout[right_idx]
    if char != '.':
        size = 0
        right_idx2 = right_idx
        while char == layout[right_idx2]:
            size += 1
            right_idx2 -= 1
        slice_to_move_left = layout[right_idx2+1:right_idx+1]
        # Look for leftmost free space
        left_idx2 = left_idx
        while left_idx2 < right_idx:
            slice_to_move_right = layout[left_idx2:left_idx2+size]
            if slice_to_move_right == ['.'] * size:
                # Swap slices
                layout = layout[:left_idx2] + slice_to_move_left + layout[left_idx2+size:right_idx2+1] + slice_to_move_right + layout[right_idx+1:]
                left_idx = next((i for i, v in enumerate(layout) if v == '.'), -1)
                break
            else:
                left_idx2 += 1
        right_idx = right_idx2
    else:
        right_idx -= 1

ans = 0
for i in range(len(layout)):
    if layout[i] != '.':
        ans += i * int(layout[i])
print(ans)
