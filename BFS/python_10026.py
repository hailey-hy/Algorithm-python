# 적록색약

from collections import deque

n = int(input())
colors = [list(input()) for _ in range(n)]
answer = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
red_green = ['R', 'G']

def bfs(x, y, blind):
    queue = deque([(x, y)])
    color = colors[x][y]
    while queue:
        now_x, now_y = queue.popleft()
        if 0 <= now_x < n and 0 <= now_y < n:
            for i in range(4):
                new_x = now_x + dx[i]
                new_y = now_y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                    if color == colors[new_x][new_y]:
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))
                    elif blind and color in red_green and colors[new_x][new_y] in red_green:
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))

for k in range(2):
    if k == 0:
        blind = False
    else:
        blind = True
    visited = [[False] * n for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                total += 1
                visited[i][j]
                bfs(i, j, blind)
    answer.append(total)
print(' '.join(map(str, answer)))
