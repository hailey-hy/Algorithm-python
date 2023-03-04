# 민준이와 마산 그리고 건우

import heapq
import sys

v, e, p = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start, end):
    if start == end:
        return 0

    visited = [sys.maxsize] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0

    while q:
        cost, now= heapq.heappop(q)
        for i in graph[now]:
            new_cost = cost + i[0]
            if new_cost <= visited[i[1]]:
                heapq.heappush(q, (new_cost, i[1]))
                visited[i[1]] = new_cost

    return visited[end]

if dijkstra(1, v) == dijkstra(1, p) + dijkstra(p, v):
    print('SAVE HIM')
else:
    print('GOOD BYE')

    