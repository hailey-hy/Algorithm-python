# 도넛 행성

from collections import deque

n, m = map(int, input().split())
donut = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False] * m for _ in range(n)]
cnt = 0

def bfs(a, b):
    q = deque([(a, b)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if not visited[new_x][new_y] and donut[new_x][new_y] == 0:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))
            else:
                if new_x < 0:
                    new_x += n
                else:
                    new_x -= n
                if new_y < 0:
                    new_y += m
                else:
                    new_y -= m
                if not visited[new_x][new_y] and donut[new_x][new_y] == 0:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))
                
for i in range(n):
    for j in range(m):
        if not visited[i][j] and donut[i][j] == 0:
            visited[i][j] = True
            bfs(i, j)
            cnt += 1

print(cnt)