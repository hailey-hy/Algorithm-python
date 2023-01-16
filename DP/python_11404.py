# 플로이드

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = []
graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
answer = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j :
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == sys.maxsize:
            print('0', end=' ')
        else:
            print(str(graph[i][j]), end=' ')
    print()