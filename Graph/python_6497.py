# 전력난

import sys

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    graph = []
    total = 0
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        total += c
        graph.append((a, b, c))
    graph.sort(key= lambda x: x[2])

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

    print(total - answer)