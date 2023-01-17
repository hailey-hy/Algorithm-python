# 케빈 베이컨의 6단계 법칙

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
answer = []

for i in range(m):
    a, b= map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(a, b):
    q = []
    for heap in graph[a]:
        heapq.heappush(q, (1, heap))
    visited = [False] * (n + 1)
    visited[a] = True
    while q:
        x = heapq.heappop(q)
        if x[1] == b:
            return x[0]
        if not visited[x[1]]:
            new_cost = x[0] + 1
            visited[x[1]] = True
            for heap in graph[x[1]]:
                heapq.heappush(q, (new_cost, heap))
    return 0

for i in range(1, n + 1):
    tmp = []
    for j in range(1, n + 1):
        if i != j:
            tmp.append(bfs(i, j))
    answer.append(sum(tmp))

print(answer.index(min(answer)) + 1)