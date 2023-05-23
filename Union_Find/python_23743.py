# 방탈출

import sys

n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((c, a, b))

times = list(map(int, sys.stdin.readline().split()))
for index, time in enumerate(times):
    graph.append((time, index + 1, 0))

graph.sort(key=lambda x:x[0])

parent = [i for i in range(n + 1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same(a, b):
    return find(a) == find(b)

total = 0
for cost, a, b in graph:
    if not same(a, b):
        union(a, b)
        total += cost

print(total)
