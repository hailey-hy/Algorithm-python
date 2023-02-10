# 트리의 지름

from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(x):
    answer = 0
    visited = [False] * (n + 1)
    q = deque([(x, 0)])
    visited[x] = True
    while q:
        now, cost = q.popleft()
        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append((i[0], i[1] + cost))
                answer = max(answer, i[1] + cost)
    return answer

result = 0
for i in range(1, n + 1):
    result = max(result, bfs(i))

print(result)