# 최소 스패닝 트리

import sys

v, e = map(int, sys.stdin.readline().split())
graph = []

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))
graph.sort(key=lambda x: x[2])

parent = [i for i in range(v + 1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, cost in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)