# 안전 영역

from collections import deque

n = int(input())
land = []
maximum = 0
result = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    tmp = list(map(int, input().split()))
    land.append(tmp)
    maximum = max(maximum, max(tmp))

def bfs(x, y, h):
    queue = deque([(x, y)])
    while queue:
        now_x, now_y = queue.popleft()
        if 0 <= now_x < n and 0 <= now_y < n:
            for i in range(4):
                new_x = now_x + dx[i]
                new_y = now_y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y] and land[new_x][new_y] > h:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))

for k in range(1, maximum):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and land[i][j] > k:
                visited[i][j] = True
                bfs(i, j, k)
                cnt += 1
    result = max(result, cnt)

print(result)