# 섬의 개수

from collections import deque

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def bfs(graph, a, b):
    queue = deque()
    graph[a][b] = 0
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    
    island = []
    answer = 0
    for _ in range(h):
        island.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(island, i, j)
                answer += 1
    
    print(answer)