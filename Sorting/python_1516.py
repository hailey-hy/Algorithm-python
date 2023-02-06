# 게임 개발

from collections import deque

n = int(input())
graph = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
cost = [0] * (n + 1)
for j in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for index, i in enumerate(tmp):
        if i == -1:
            break
        if index > 0:
            graph[i].append(j)
            indegree[j] += 1
        if index == 0:
            cost[j] = i

def topology():
    q = deque()
    for k in range(1, n + 1):
        if indegree[k] == 0:
            q.append(k)

    cnt = 1
    result = [0] * (n + 1)
    while q:
        now = q.popleft()
        result[now] += cost[now]
        for l in graph[now]:
            indegree[l] -= 1
            result[l] = max(result[l], result[now])
            if indegree[l] == 0:
                q.append(l)

    for i in result[1:]:
        print(i)
topology()
