# 백도어

import sys
import heapq

n, m = map(int, input().split())

see = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
memo = [sys.maxsize for _ in range(n + 1)]

for i in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    memo[x] = 0
    while q:
        now_cost, now = heapq.heappop(q)
        if memo[now] < now_cost:
            continue
        for i in graph[now]:
            if see[i[1]] == 1 and i[1] != n - 1:
                continue
            new_cost = i[0] + now_cost
            if memo[i[1]] > new_cost:
                memo[i[1]] = new_cost
                heapq.heappush(q, (new_cost, i[1]))

dijkstra(0)
if memo[n - 1] < sys.maxsize:
    print(memo[n - 1])
else:
    print(-1)