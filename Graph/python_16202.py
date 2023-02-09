# MST 게임

from collections import deque
import sys

n, m, k = map(int, sys.stdin.readline().split())
graph = deque([])
total = 0
for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    graph.append((a, b, i))
    total += i

for i in range(k):
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

    total = 0
    for a, b, cost in graph:
        if not same_parent(a, b):
            union_parent(a, b)
            total += cost
    
    check = set()
    for j in range(1, n + 1):
        if get_parent(j) not in check:
            check.add(get_parent(j))
    
    if len(check) > 1:
        print(0, end=' ')
    else:
        print(total, end= ' ')

    graph.popleft()