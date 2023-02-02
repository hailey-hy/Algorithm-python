# 아기 상어

from collections import deque

n = int(input())
a = -1
b = -1
space = []
for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        a = i
        b = tmp.index(9)
    space.append(tmp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque([(a, b, 2)])
    while q:
        x, y, shark, time, tmp = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and :
