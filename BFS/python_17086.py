# 아기 상어 2

from collections import deque
n, m = map(int, input().split())
space = []

for _ in range(n):
    space.append(list(map(int, input().split())))

tmp = max(n, m)

record = [[tmp] * m for _ in range(n)]
dx = [1, 0, 1, -1, -1, -1, 0, 1]
dy = [0, 1, 1, -1, 0, 1, -1, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        now_x, now_y = queue.popleft()
        if now_x < 0 or now_y < 0 or now_x >= n or now_y >= m:
            continue
        for i in range(8):
            if 0 <= now_x + dx[i] < n and 0 <= now_y + dy[i] < m and space[now_x + dx[i]][now_y + dy[i]] != 1:
                if record[now_x + dx[i]][now_y + dy[i]] > record[now_x][now_y] + 1:
                    record[now_x + dx[i]][now_y + dy[i]] = record[now_x][now_y] + 1
                    queue.append((now_x + dx[i], now_y + dy[i]))

for i in range(n):
    for j in range(m):
        if space[i][j] == 1:
            record[i][j] = 0
            bfs(i, j)

maximum = 0
for i in range(n):
    for j in range(m):
        maximum = max(maximum, record[i][j])

print(maximum)