# Day 23: LAN Party

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

graph = {}
for line in data:
    a, b = line.split('-')
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

connected_triplets = set()
for x in graph:
    for y in graph[x]:
        for z in graph[y]:
            if x != z and x in graph[z]:
                connected_triplets.add(tuple(sorted([x, y, z])))

print(len([s for s in connected_triplets if any(cn.startswith('t') for cn in s)]))

