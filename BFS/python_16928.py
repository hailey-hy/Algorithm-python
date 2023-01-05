# 뱀과 사다리 게임

from collections import deque
import sys

n, m = map(int, input().split())
move = {}

for i in range(n):
    a, b = map(int, input().split())
    move[a] = b

for i in range(m):
    a, b = map(int, input().split())
    move[a] = b

visited = [sys.maxsize] * 101
queue = deque([(1, 0)])
while queue:
    now, dice = queue.popleft()
    for i in range(1, 7):
        if now + i <= 100:
            if now + i in move:
                if visited[move[now + i]] > dice + 1:
                    visited[move[now + i]] = dice + 1
                    queue.append((move[now + i], dice + 1))
            else:
                if visited[now + i] > dice + 1:
                    visited[now + i] = dice + 1
                    queue.append((now + i, dice + 1))
            
print(visited[100])