# 음악프로그램

from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(2, len(tmp)):
        a, b = tmp[i - 1], tmp[i]
        graph[a].append(b)
        indegree[b] += 1

def topology():
    q = deque()
    result = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) == n:
        for i in result:
            print(i)
    else:
        print(0)

topology()