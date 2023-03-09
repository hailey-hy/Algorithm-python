# 저울

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = -1

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if sys.maxsize > graph[i][k] > 0 and sys.maxsize > graph[k][j] > 0:
                graph[i][j] = graph[i][k] + graph[k][j]
            elif graph[i][k] < 0 and graph[k][j] < 0:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n + 1):
    print(graph[i].count(sys.maxsize) - 1)

