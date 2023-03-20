# 소수 경로

from collections import deque
import math

dp = [True] * (10001)
for i in range(2, int(math.sqrt(10000)) + 1):
    if dp[i]:
        j = 2
        while i * j <= 10000:
            dp[i * j] = False
            j += 1

def bfs(a, b):
    q = deque([(a, 0)])
    visited = [False] * (10000)
    visited[a] = True
    while q:
        now, total = q.popleft()
        if now == b:
            return total
        now = str(now)
        for i in range(4):
            for j in range(10):
                tmp = int(now[:i] + str(j) + now[i + 1:])
                if not visited[tmp] and dp[tmp] and tmp >= 1000:
                    visited[tmp] = True
                    q.append((tmp, total + 1))

    return 'Impossible'

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))