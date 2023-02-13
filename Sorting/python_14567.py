# 선수과목

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
dp = [1] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    indegree[b] += 1
    graph[a].append(b)

def topology():
    q = deque([])
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + 1, dp[i])
            if indegree[i] == 0:
                q.append(i)
    return dp

print(' '.join(map(str, topology()[1:])))
