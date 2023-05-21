# 중량제한

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

start, end = map(int, sys.stdin.readline().split())

def bfs(x, start, end):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    while q:
        now = q.popleft()
        if now == end:
            return x
        for new, new_cost in graph[now]:
            if new_cost >= x and not visited[new]:
                visited[new] = True
                q.append(new)
    return False

first = 1
second = 1000000000

while first <= second:
    mid = (first + second) // 2
    result = bfs(mid, start, end)
    if result:
        first = mid + 1
    else:
        second = mid - 1

print(second)

    