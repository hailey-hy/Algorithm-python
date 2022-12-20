# 촌수계산

from collections import deque

n = int(input())
family = [[] for _ in range(n + 1)]

x, y = map(int, input().split())

relations = int(input())
for _ in range(relations):
    target, related = map(int, input().split())
    family[target].append(related)
    family[related].append(target)

visited = [-1 for _ in range(n + 1)]
visited[x] = 0

def bfs(a):
    queue = deque([a])
    while queue:
        now = queue.popleft()
        for i in family[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)

bfs(x)
print(visited[y])