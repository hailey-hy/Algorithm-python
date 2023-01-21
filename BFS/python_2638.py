# 치즈

from collections import deque

n, m = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1] #오른쪽 왼쪽 아래 위
dy = [1, -1, 0, 0]
vector = {(0, 1): 3, (0, -1): 2, (1, 0): 1, (-1, 0): 0}
answer = 0

def bfs():
    q = deque([(0, 0)])
    visited = [[[0, 0, 0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0] = [0, 0, 0, 0]
    status = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < n and 0 <= n_y < m:
                if visited[n_x][n_y][vector[(dx[i], dy[i])]] == 0:
                    if cheese[n_x][n_y] == 0:
                        visited[n_x][n_y][vector[(dx[i], dy[i])]] = 1
                        q.append((n_x, n_y))
                    else:
                        visited[n_x][n_y][vector[(dx[i], dy[i])]] = 1
    for i in range(n):
        for j in range(m):
            if sum(visited[i][j]) >= 2 and cheese[i][j] == 1:
                cheese[i][j] = 0
                status = True

    return status

while True:
    if not bfs():
        break
    answer += 1
        

print(answer)
                    