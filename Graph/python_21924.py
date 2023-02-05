# 도시 건설

import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
total = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))
    total += c
graph.sort(key=lambda x:x[2])

parent = [i for i in range(n + 1)]

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

answer = []
for a, b, cost in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        answer.append(cost)

if len(answer) == n - 1:
    print(total - sum(answer))
else:
    print(-1)