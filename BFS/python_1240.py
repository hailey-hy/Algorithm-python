# 노드사이의 거리

from collections import deque
import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, distance = map(int, input().split())
    graph[a].append((b, distance))
    graph[b].append((a, distance))

def bfs(a, b):
    q = deque([(a, 0)])
    visited = [sys.maxsize] * (n + 1)
    visited[a] = 0
    while q:
        now, distance = q.popleft()
        for i in graph[now]:
            if i[1] + distance < visited[i[0]]:
                visited[i[0]] = i[1] + distance
                q.append((i[0], i[1] + distance))
    return visited[b]

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))