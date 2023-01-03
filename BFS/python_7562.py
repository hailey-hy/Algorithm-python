# 나이트의 이동

from collections import deque
import sys

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, 1, -1]

t = int(sys.stdin.readline())
for _ in range(t):
    board = int(sys.stdin.readline())
    now_x, now_y = map(int, sys.stdin.readline().split())
    togo_x, togo_y = map(int, sys.stdin.readline().split())
    visited = [[False] * board for _ in range(board)]
    now_cnt = 0
    answer = sys.maxsize

    queue = deque([(now_x, now_y, now_cnt)])
    while queue:
        x, y, cnt = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            if x < 0 or y < 0 or x >= board or y >= board:
                continue
            if x == togo_x and y == togo_y:
                answer = min(answer, cnt)
                continue
            for i in range(8):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x >= 0 and new_y >= 0 and new_x < board and new_y < board:
                    queue.append((new_x, new_y, cnt + 1))

    print(answer)