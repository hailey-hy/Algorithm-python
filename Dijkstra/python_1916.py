# 최소 비용 구하기

import heapq
import sys

city = int(sys.stdin.readline())
bus = int(sys.stdin.readline())

graph = [[] for _ in range(city + 1)]
memo = [sys.maxsize for _ in range(city + 1)]

for i in range(bus):
    start, end, fee = map(int, sys.stdin.readline().split())
    graph[start].append((fee, end))

n, m = map(int, sys.stdin.readline().split())

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    memo[x] = 0
    while q:
        now_cost, now = heapq.heappop(q)

        if memo[now] < now_cost:
            continue
        
        for i in graph[now]:
            new_cost = i[0] + now_cost

            if memo[i[1]] > new_cost:
                memo[i[1]] = new_cost
                heapq.heappush(q, (new_cost, i[1]))

dijkstra(n)
print(memo[m])
