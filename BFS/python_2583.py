# 영역 구하기

from collections import deque

n, m, k = map(int, input().split())
box = [[0] * m for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x2 - x1):
        for j in range(y2 - y1):
            box[y1 + j][x1 + i] = 1

visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
answer = []

def bfs(a, b):
    q = deque([(a, b)])
    tmp = 1
    while q:
        x_now, y_now = q.popleft()

        if 0 <= x_now < n and 0 <= y_now < m:            
            for i in range(4):
                x_new = x_now + dx[i]
                y_new = y_now + dy[i]
                if 0 <= x_new < n and 0 <= y_new < m and box[x_new][y_new] == 0:
                    # visited[x_new][y_new] = True
                    box[x_new][y_new] = 1
                    q.append((x_new, y_new))
                    tmp += 1

    answer.append(tmp)
        

for i in range(n):
    for j in range(m):
        if not visited[i][j] and box[i][j] == 0:
            box[i][j] = 1
            bfs(i, j)
            cnt += 1

print(cnt)
answer.sort()
print(' '.join(map(str, answer)))
            