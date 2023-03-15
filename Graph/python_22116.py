# 창영이와 퇴근

import heapq
import sys

n = int(sys.stdin.readline().rstrip())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    visited = [[sys.maxsize] * n for _ in range(n)]
    visited[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                new_cost = max(abs(graph[x][y] - graph[new_x][new_y]), cost)
                if new_cost < visited[new_x][new_y]:
                    visited[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))
    
    print(visited[n - 1][n - 1])

dijkstra()

