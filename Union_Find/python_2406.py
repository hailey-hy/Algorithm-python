# 안정적인 네트워크

import sys

n, m = map(int, sys.stdin.readline().split())
graph_first = []

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph_first.append((0, x - 1, y - 1))

graph = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for index, t in enumerate(tmp):
        if 0 not in [i, index] and i < index:
            graph.append((t, i, index))

graph.sort(key=lambda x: x[0])
parent = [i for i in range(n)]

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

for cost, a, b in graph_first:
    if not same(a, b):
        union(a, b)

flag = True

total = 0
cnt = 0
answers = []
for cost, a, b in graph:
    if not same(a, b):
        flag = False
        union(a, b)
        total += cost
        cnt += 1
        answers.append((a + 1, b + 1))

if flag:
    print(0, 0)
else:
    print(total, cnt)
    for answer in answers:
        print(*answer)
