# 서강그라운드

import sys
import heapq

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n)]
for _ in range(r):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a - 1].append((cost, b - 1))
    graph[b - 1].append((cost, a - 1))

def dijkstra(x):
    visited = [sys.maxsize] * n
    q = []
    heapq.heappush(q, (0, x))
    visited[x] = True
    while q:
        cost, now = heapq.heappop(q)
        for i in graph[now]:
            new_cost = cost + i[0]
            if new_cost <= m and visited[i[1]] > new_cost:
                visited[i[1]] = new_cost
                heapq.heappush(q, (new_cost, i[1]))

    total = 0
    for i in range(n):
        if visited[i] < sys.maxsize:
            total += items[i]

    return total

total = 0
for i in range(n):
    total = max(total, dijkstra(i))

print(total)
