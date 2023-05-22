# 유닛 이동시키기

from collections import deque
import sys

n, m, a, b, k = map(int, sys.stdin.readline().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x - 1][y - 1] = -1

start_x, start_y = map(int, sys.stdin.readline().split()) #왼쪽 제일 위
end_x, end_y = map(int, sys.stdin.readline().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[sys.maxsize] * m for _ in range(n)]
visited[start_x - 1][start_y - 1] = 0

def units(x, y):
    units = []
    for i in range(a):
        for j in range(b):
            if graph[x + i][y + j] == -1:
                return False
    return True


def bfs():
    q = deque([(start_x - 1, start_y - 1)])
    while q:
        x, y = q.popleft()
        if x == end_x - 1 and y == end_y - 1:
            return visited[end_x - 1][end_y - 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n - a and 0 <= ny <= m - b: #영역 밖 예외처리
                if not units(nx, ny): # 장애물 예외처리
                    continue
                if visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))     
    return -1
print(bfs())

