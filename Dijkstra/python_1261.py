# 알고스팟

import sys
import heapq

n, m = map(int, input().split())

maze = []
for i in range(m):
    tmp = input()
    array = []
    for j in range(n):
        array.append(int(tmp[j]))
    maze.append(array)
memo = [[sys.maxsize] * n for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    memo[x][y] = 0

    while q:
        now_cost, now_x, now_y = heapq.heappop(q)
        if memo[now_x][now_y] < now_cost:
            continue
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n:
                new_cost = now_cost + maze[new_x][new_y]
                if new_cost < memo[new_x][new_y]:
                    memo[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))

dijkstra(0, 0)
print(memo[m - 1][n - 1])