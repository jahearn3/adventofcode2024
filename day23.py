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

ans = 0
for s in connected_triplets:
    if any(cn.startswith('t') for cn in s):
        ans += 1
print(ans)

# Part 2


def bron_kerbosch(R, P, X):
    '''
    This recursive function finds all maximal cliques.
    `R` is the current set of nodes in the clique,
    `P` is the set of candidates for extending the clique, and
    `X` is the set of excluded nodes.
    When `P` and `X` are both empty, a maximal clique has been found.
    '''
    if not P and not X:
        yield R  # Found a maximal clique
    while P:
        v = P.pop()
        new_R = R | {v}
        yield from bron_kerbosch(new_R, P & graph[v], X & graph[v])
        X.add(v)


maximal_cliques = list(bron_kerbosch(set(), set(graph.keys()), set()))
largest_clique = max(maximal_cliques, key=len, default=set())

largest_clique_sorted = sorted(largest_clique)
print(','.join(largest_clique_sorted))
