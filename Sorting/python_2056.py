# 작업

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)
indegree = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(n):
    tmp = list(map(int, input().split()))
    cost[i + 1] = tmp[0]
    num = tmp[1]
    if num >= 1:
        indegree[i + 1] += num
        tmp_word = tmp[2:]
        for j in tmp_word:
            graph[j].append(i + 1)

def topology():
    q = deque([])
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    
    result = []
    while q:
        now = q.popleft()
        result.append(cost[now])
        for i in graph[now]:
            dp[i] = max(dp[i], dp[now] + cost[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

topology()
print(max(dp))