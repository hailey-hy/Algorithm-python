# 특정한 최단 경로

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
memo = [sys.maxsize] * (n + 1)

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    memo[x] = 0

    while q:
        now_cost, now = heapq.heappop(q)
        if memo[now] < now_cost:
            continue
        for i in graph[now]:
            new_cost = now_cost + i[0]
            if memo[i[1]] > new_cost:
                memo[i[1]] = new_cost
                heapq.heappush(q, (new_cost, i[1]))


dijkstra(1)
tmp1 = memo[v1]
tmp2 = memo[v2]
memo = [sys.maxsize] * (n + 1)

dijkstra(v1)
tmp1 += memo[v2]
tmp2 += memo[n]
memo = [sys.maxsize] * (n + 1)

dijkstra(v2)
tmp1 += memo[n]
tmp2 += memo[v1]

answer = min(tmp1, tmp2)

print(answer if answer < sys.maxsize else -1)