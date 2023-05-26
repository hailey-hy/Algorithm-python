# 여행가자

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = []
for i in range(n):
    tmps = list(map(int, sys.stdin.readline().split()))
    for index, tmp in enumerate(tmps):
        if tmp == 1:
            graph.append((index, i))

plans = list(map(int, sys.stdin.readline().split()))

parent = [i for i in range(n)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def uinon(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same(a, b):
    return find(a) == find(b)

for a, b in graph:
    if not same(a, b):
        uinon(a, b)

flag = True
tmp = find(plans[0] - 1)
for plan in plans:
    if tmp != find(plan - 1):
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')