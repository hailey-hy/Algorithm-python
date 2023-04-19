# 타임머신

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

visited = [sys.maxsize] * (n + 1)
visited[1] = 0

def belman():
    for i in range(1, n + 1):
        for start in range(1, n + 1):
            for end, cost in graph[start]:
                if visited[start] < sys.maxsize and visited[end] > visited[start] + cost:
                    visited[end] = visited[start] + cost
                    if i == n:
                        return -1
    return visited

answers = belman()
if answers == -1:
    print(-1)
else:
    for i in range(2, n + 1):
        if visited[i] < sys.maxsize:
            print(visited[i])
        else:
            print(-1)