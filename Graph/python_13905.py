# 세부

import sys

n, m = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
graph = []
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))
graph.sort(key=lambda x:x[2], reverse=True)

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
        if get_parent(s) == get_parent(e):
            answer.append(cost)

if answer:
    print(max(answer))
else:
    print(0)