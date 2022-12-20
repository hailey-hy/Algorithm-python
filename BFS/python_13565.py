# 침투

from collections import deque

n, m = map(int, input().split())
blocks = [list(input()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    answer = False
    while queue:
        now_x, now_y = queue.popleft()
        if now_x == n - 1:
            answer = True
            return answer
        for i in range(4):
            if not (0 <= now_x + dx[i] < n and 0 <= now_y + dy[i] < m):
                continue
            if blocks[now_x + dx[i]][now_y + dy[i]] == '0':
                blocks[now_x + dx[i]][now_y + dy[i]] = '1'
                queue.append((now_x + dx[i], now_y + dy[i]))

for i in range(m):
    if blocks[0][i] == '0':
        blocks[0][i] = '1'
        if bfs(0, i):
            print('YES')
            break
else:
    print('NO')