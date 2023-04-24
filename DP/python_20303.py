# 할로윈의 양아치

from collections import deque
import sys

n, m, k = map(int,sys.stdin.readline().split())
candies = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
total = sum(candies)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
def bfs(x):
    visited[x] = True
    cnt = 0
    candy = 0
    q = deque([x])
    while q:
        now = q.popleft()
        candy += candies[now]
        cnt += 1
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return [cnt, candy]

group = []
for kid in range(1, n + 1):
    if not visited[kid]:
        group.append(bfs(kid))

dp = [0 for i in range(k)]

for i, (cost, candy) in enumerate(group):
    for j in range(k - 1, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + candy)

print(dp[-1])