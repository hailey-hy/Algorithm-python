# 점프왕 쩰리 (Small)

from collections import deque
import sys

n = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        now_x, now_y = queue.popleft()
        if not visited[now_x][now_y]:
            moved = game[now_x][now_y]
            visited[now_x][now_y] = True
            if moved == -1:
                return 'HaruHaru'
            else:
                if now_x + moved < n:
                    queue.append((now_x + moved, now_y))
                if now_y + moved < n:
                    queue.append((now_x, now_y + moved))
    return 'Hing'

print(bfs(0, 0))