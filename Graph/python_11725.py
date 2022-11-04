# 트리의 부모 찾기
from collections import deque

n = int(input())
answer = [0] * (n + 1)

# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
tree = [[] for _ in range(n + 1)]
visited=[False] * (n + 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a] += [b]
    tree[b] += [a]

def bfs(graph, v, visited):
    que = deque([v])
    visited[v] = True
    while que:
        x = que.popleft()
        for i in graph[x]:
            if not visited[i]:
                answer[i] = x
                que.append(i)
                visited[i] = True

bfs(tree, 1, visited)

for i in range(2, n+1):
    print(answer[i])