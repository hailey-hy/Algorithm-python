# Strahler 순서

from collections import deque

t = int(input())

for i in range(t):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    indegree = [0] * (m + 1)

    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    def topology():
        q = deque([])
        result = [0 for i in range(m + 1)]
        count = [[0, 0] for _ in range(m + 1)]
        for i in range(1, m + 1):
            if indegree[i] == 0:
                q.append(i)
                count[i] = [1, 1]
                result[i] = 1

        while q:
            now = q.popleft()

            for i in graph[now]:
                indegree[i] -= 1
                if count[i][0] < result[now]:
                    count[i] = [result[now], 1]
                elif count[i][0] == result[now]:
                    count[i][1] += 1
                if indegree[i] == 0:
                    q.append(i)
                    if count[i][1] > 1:
                        result[i] = count[i][0] + 1
                    else:
                        result[i] = count[i][0]

        return result[m]

    print(k, topology())