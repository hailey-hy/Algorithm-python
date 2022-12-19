# 바닥 장식

from collections import deque

def bfs(a, b):
    deq = deque([(a, b)])
    while deq:
        x, y = deq.popleft()
        if room[x][y] == '-':
            room[x][y] = '1'
            if y + 1 < m and room[x][y + 1] == '-':
                deq.append((x, y + 1))
        elif room[x][y] == '|':
            room[x][y] = '1'
            if x + 1 < n and room[x + 1][y] == '|':
                deq.append((x + 1, y))

n, m = map(int, input().split())
room = [list(input()) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if room[i][j] != '1':
            bfs(i, j)
            cnt += 1

print(cnt)