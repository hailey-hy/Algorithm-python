# 행성 연결

import sys

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if i != j:
            graph.append((i, j, tmp[j]))

graph.sort(key=lambda x:x[2])

parent = [i for i in range(n)]

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