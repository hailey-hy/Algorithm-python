# 호석이 두 마리 치킨

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = [0, 0, sys.maxsize]
for i in range(1, n):
    for j in range(i + 1, n + 1):
        total = [0] * (n + 1)
        for k in range(1, n + 1):
            if k == i or k == j:
                total[k] == 0
            else:
                total[k] = min(graph[i][k], graph[j][k])
        if answer[-1] > sum(total):
            answer = [i, j, sum(total)]

print(answer[0], answer[1], answer[2] * 2)