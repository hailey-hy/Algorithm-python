# 인구 이동

from collections import deque

n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    ally = 0
    ally_arry = []
    memo = [[-1] * n for _ in range(n)]
    tmp = False
    for i in range(n):
        for j in range(n):
            if memo[i][j] == -1:
                q = deque([(i, j)])
                visited = [[False] * n for _ in range(n)]
                visited[i][j] = True
                memo[i][j] = ally
                total = 0
                num = 0
                while q:
                    x, y = q.popleft()
                    total += graph[x][y]
                    num += 1
                    for k in range(4):
                        new_x = dx[k] + x
                        new_y = dy[k] + y
                        if 0 <= new_x < n and 0 <= new_y < n:
                            if L <= abs(graph[x][y] - graph[new_x][new_y]) <= R and not visited[new_x][new_y]:
                                visited[new_x][new_y] = True
                                memo[new_x][new_y] = ally
                                q.append((new_x, new_y))
                                tmp = True
                ally += 1
                ally_arry.append(int(total / num))

    if tmp:
        for i in range(n):
            for j in range(n):
                if memo[i][j] > -1:
                    graph[i][j] = ally_arry[memo[i][j]]
        return True

    else:
        return False
    

while True:
    if not bfs():
        break
    else:
        answer += 1

print(answer)