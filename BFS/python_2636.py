# 치즈

from collections import deque

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0
leftover = []

def bfs(a, b):
    q = deque([(a, b)])
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True
    state = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                if cheese[new_x][new_y] == 1:
                    state += 1
                    cheese[new_x][new_y] = 0
                else:
                    q.append((new_x, new_y))

    leftover.append(state)
    return state
                
while True:
    bfs(0, 0)
    if leftover[-1] == 0:
        break
    else:
        answer += 1

print(answer)
print(leftover[-2] if len(leftover) >= 2 else 0)
