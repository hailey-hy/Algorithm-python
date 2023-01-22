# 벽 부수고 이동하기

from collections import deque
import sys

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    q = deque([(a, b, 0)])
    visited[a][b][0] = 1
    while q:
        x, y, status = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][status]
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < n and 0 <= n_y < m and visited[n_x][n_y][status] == 0:
                if graph[n_x][n_y] == '0':
                    visited[n_x][n_y][status] = visited[x][y][status] + 1
                    q.append((n_x, n_y, status))
                if graph[n_x][n_y] == '1' and status == 0:
                    visited[n_x][n_y][1] = visited[x][y][status] + 1
                    q.append((n_x, n_y, 1))
    return -1

print(bfs(0, 0))