# Day 5: Print Queue

import load_data as ld
import os
from collections import defaultdict, deque

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

rules = []
updates = []
blank = False
for line in data:
    if len(line) == 0:
        blank = True
    elif blank:
        page_numbers = line.split(',')
        updates.append([int(s) for s in page_numbers])
    else:
        a, b = line.split('|')
        rules.append((int(a), int(b)))

ans = 0

for u, update in enumerate(updates):
    rr = []
    for rule in rules:
        a, b = rule
        if a in update and b in update:
            a_i = update.index(a)
            b_i = update.index(b)
            if a_i < b_i:
                rr.append(1)
            else:
                rr.append(0)
    if sum(rr) == len(rr):
        mid = int((len(update) / 2) - 0.5)
        ans += update[mid]

print(ans)


# Part 2
def reorder_list(elements, rules):
    # Step 1: Create a graph and in-degree count
    graph = defaultdict(list)
    in_degree = {elem: 0 for elem in elements}

    # Step 2: Build the graph and in-degree counts
    for a, b in rules:
        graph[a].append(b)
        in_degree[b] += 1

    # Step 3: Initialize the queue with all elements that have in-degree of 0
    queue = deque([elem for elem in elements if in_degree[elem] == 0])

    # Step 4: Perform topological sort
    ordered_list = []

    while queue:
        current = queue.popleft()
        ordered_list.append(current)

        # Decrease the in-degree of the neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_list


ans = 0

for u, update in enumerate(updates):
    rr = []
    relevant_rules = []
    for rule in rules:
        a, b = rule
        if a in update and b in update:
            relevant_rules.append(rule)
            a_i = update.index(a)
            b_i = update.index(b)
            if a_i < b_i:
                rr.append(1)
            else:
                rr.append(0)
    if sum(rr) != len(rr):
        # Re-order
        disordered = True
        ordered_update = reorder_list(update, relevant_rules)
        mid = int((len(ordered_update) / 2) - 0.5)
        ans += ordered_update[mid]

print(ans)
