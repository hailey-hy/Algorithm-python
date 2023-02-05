# 비밀 모임

import heapq
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(n + 1)]
    for i in range(m):
        a, b, cost = map(int, sys.stdin.readline().split())
        graph[a].append((cost, b))
        graph[b].append((cost, a))
    
    friends_num = int(sys.stdin.readline())
    friends = list(map(int, sys.stdin.readline().split()))

    def dijkstra(x):
        q = []
        visited = [sys.maxsize] * (n + 1)
        visited[x] = 0
        heapq.heappush(q, (0, x))
        while q:
            cost, now = heapq.heappop(q)
            for i in graph[now]:
                if visited[i[1]] > cost + i[0]:
                    visited[i[1]] = cost + i[0]
                    heapq.heappush(q, (cost + i[0], i[1]))

        total = 0
        for i in friends:
            total += visited[i]
        return total
    
    answer = []
    for j in range(1, n + 1):
        answer.append(dijkstra(j))

    print(answer.index(min(answer)) + 1)
    