# 연구소

from collections import deque
import sys

lab = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
max_result = 0

n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    lab.append(list(map(int, sys.stdin.readline().split())))

def bfs():
    global max_result
    copy = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = lab[i][j]
    result = 0
    arr = deque([])
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                arr.append((i, j))
    while arr:
        a, b = arr.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x and 0<= y and x < n and y < m:
                if copy[x][y] == 0:
                    copy[x][y] = 2
                    arr.append((x, y))
    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(max_result, result)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt + 1)
                lab[i][j] = 0

wall(0)
print(max_result)