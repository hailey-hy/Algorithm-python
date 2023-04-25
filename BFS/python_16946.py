# 벽 부수고 이동하기 4

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
array = []
for _ in range(n):
    array.append(list(sys.stdin.readline().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find_0(a, b):
    total = 1
    q = deque([(a, b)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < n and 0 <= n_y < m and array[n_x][n_y] == '0' and not visited[n_x][n_y]:
                visited[n_x][n_y] = True
                zero[n_x][n_y] = record
                total += 1
                q.append((n_x, n_y))
    return total

def find_path(a, b):
    total = 1
    q = deque([(a, b)])
    visited = ['1']
    while q:
        x, y = q.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < n and 0 <= n_y < m:
                target = zero[n_x][n_y]
                if target not in visited:
                    visited.append(target)
                    total += group[target]
                    q.append((n_x, n_y))
    return total

visited = [[False] * m for _ in range(n)]
zero = [['1'] * m for _ in range(n)]
group = dict()
record = 1
for i in range(n):
    for j in range(m):
        if array[i][j] == '0' and not visited[i][j]:
            visited[i][j] = True
            zero[i][j] = record
            group[record] = find_0(i, j)
            record += 1

for i in range(n):
    for j in range(m):
        if array[i][j] == '1':
            array[i][j] = find_path(i, j) % 10

for answer in array:
    print(''.join(map(str, answer)))