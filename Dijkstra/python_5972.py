# 택배 배송

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
memo = [sys.maxsize for _ in range(n + 1)]

for _ in range(m):
    start, end, fee = map(int, sys.stdin.readline().split())
    graph[start].append((end, fee))
    graph[end].append((start, fee))

def dijkstra(x):
    q = []
    heapq.heappush(q, (x, 0))

    while q:
        now, now_cost = heapq.heappop(q)

        if memo[now] < now_cost:
            continue

        for togo, fee in graph[now]:
            new_fee = fee + now_cost
            if memo[togo] > new_fee:
                memo[togo] = new_fee
                heapq.heappush(q, (togo, new_fee))

dijkstra(1)
print(memo[n])
