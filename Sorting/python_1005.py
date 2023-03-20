# ACM Craft

import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    target = int(sys.stdin.readline())
    dp = [0] * (n + 1)

    def topology():
        global indegree
        q = deque([])
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = time[i - 1]

        while q:
            now = q.popleft()
            for i in graph[now]:
                indegree[i] -= 1
                dp[i] = max(dp[i], dp[now] + time[i - 1])
                if indegree[i] == 0:
                    q.append(i)

    topology()
    print(dp[target])