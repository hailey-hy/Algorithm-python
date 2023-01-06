# 최단경로

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
memo = [sys.maxsize] * (n + 1)

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))


def dijkstra(x):
    q = []
    memo[k] = 0
    heapq.heappush(q, (0, x))
    while q:
        cost, now = heapq.heappop(q)

        if memo[now] < cost:
            continue

        for i in graph[now]:
            new_cost = cost + i[0]
            if memo[i[1]] > new_cost:
                memo[i[1]] = new_cost
                heapq.heappush(q, (new_cost, i[1]))

dijkstra(k)

for i in range(1, n + 1):
    if memo[i] < sys.maxsize:
        print(memo[i])
    else:
        print('INF')