# Day 10: Hoof It

import load_data as ld
import os
from collections import deque

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

ans = 0

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '0':
            # Breadth-first search algorithm
            start = (j, i, int(char))
            # print('start:', start)
            visited = []
            queue = deque([start])
            score = 0
            while queue:
                node = queue.popleft()
                x, y, alt = node
                if node not in visited:
                    visited.append(node)
                    neighbors = []
                    # Add neighbors
                    if y > 0 and int(data[y-1][x]) == alt + 1:
                        neighbors.append((x, y-1, alt+1))
                    if y < len(data) - 1 and int(data[y+1][x]) == alt + 1:
                        neighbors.append((x, y+1, alt+1))
                    if x > 0 and int(data[y][x-1]) == alt + 1:
                        neighbors.append((x-1, y, alt+1))
                    if x < len(data) - 1 and int(data[y][x+1]) == alt + 1:
                        neighbors.append((x+1, y, alt+1))
                    # print('neighbors:', neighbors)
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            queue.append(neighbor)
            for item in visited:
                x, y, alt = item
                # print('visited:', item)
                if alt == 9:
                    # If a trail ends with a 9, add 1 to the score
                    score += 1
            # print('score:', score)
            ans += score

print(ans)

# Part 2


def count_paths(graph, start, end, visited):
    if start == end:
        return 1
    visited.add(start)
    path_count = 0
    for neighbor in graph[start]:
        if neighbor not in visited:
            path_count += count_paths(graph, neighbor, end, visited)
    visited.remove(start)
    return path_count


ans = 0

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '0':
            # Breadth-first search algorithm
            start = (j, i, int(char))
            # print('start:', start)
            visited = []
            queue = deque([start])
            rating = 0
            graph = {}
            while queue:
                node = queue.popleft()
                graph[node] = []
                x, y, alt = node
                if node not in visited:
                    visited.append(node)
                    neighbors = []
                    # Add neighbors
                    if y > 0 and int(data[y-1][x]) == alt + 1:
                        neighbors.append((x, y-1, alt+1))
                    if y < len(data) - 1 and int(data[y+1][x]) == alt + 1:
                        neighbors.append((x, y+1, alt+1))
                    if x > 0 and int(data[y][x-1]) == alt + 1:
                        neighbors.append((x-1, y, alt+1))
                    if x < len(data) - 1 and int(data[y][x+1]) == alt + 1:
                        neighbors.append((x+1, y, alt+1))
                    # print('neighbors:', neighbors)
                    for neighbor in neighbors:
                        graph[node].append(neighbor)
                        if neighbor not in visited:
                            queue.append(neighbor)
            for item in visited:
                x, y, alt = item
                # print('visited:', item)
                if alt == 9:
                    # If a trail ends with a 9, find the rating
                    visited_path = set()
                    rating += count_paths(graph, start, item, visited_path)
            ans += rating
            print(start, rating)

print(ans)
# 196 too low
