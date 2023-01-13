# 간선 이어가기 2

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
memo = [sys.maxsize] * (n + 1)
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))
s, t = map(int, sys.stdin.readline().split())

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    while q:
        now_cost, now = heapq.heappop(q)
        if memo[now] < now_cost:
            continue
        for i in graph[now]:
            new_cost = now_cost + i[0]
            if memo[i[1]] > new_cost:
                memo[i[1]] = new_cost
                heapq.heappush(q, (new_cost, i[1]))

dijkstra(s)
print(memo[t])
