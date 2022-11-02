# 죽음의 게임

from collections import deque

n, k = map(int, input().split())
graph = [0 for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(n):
    num = int(input())
    graph[i] = num

q = deque([0])
cnt = 0

while True:
    now = q.popleft()
    if not visited[now]:
        visited[now] = True
        cnt += 1
        if graph[now] == k:
            break
        else:
            q.append(graph[now])
    else:
        cnt = -1
        break
    
print(cnt)