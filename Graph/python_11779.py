# 최소 비용 구하기 2

import heapq
import sys
import copy

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([cost, end])

start, end = map(int, sys.stdin.readline().split())

def bfs(start, end):
    visited = [sys.maxsize for _ in range(n + 1)]
    visited[start] = 0
    heap = []
    heapq.heappush(heap, [0, start, [start]])
    while heap:
        cost, now, record= heapq.heappop(heap)
        if now == end:
            return cost, record
        for i in graph[now]:
            if visited[i[1]] > cost + i[0]:
                visited[i[1]] = cost + i[0]
                heapq.heappush(heap, [cost + i[0], i[1], record + [i[1]]])

cost, record = bfs(start, end)
print(cost)
print(len(record))
print(' '.join(map(str, record)))