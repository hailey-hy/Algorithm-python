# 녹색 옷 입은 애가 젤다지?

from collections import deque

cnt = 1

while True:
    n = int(input())

    if n > 0:
        cave = []
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        theif = [[99999] * n for _ in range(n)]
        visited = [[False for _ in range(n)] for _ in range(n)] 

        for i in range(n):
            cave.append(list(map(int, input().split())))
        
        theif[0][0] = cave[0][0]
        
        q = deque()
        q.append((0, 0))



        while q:
            i, j = q.popleft()
            visited[0][0]=True

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny]:
                        if theif[nx][ny] > theif[i][j] + cave[nx][ny]:
                            theif[nx][ny] = theif[i][j] + cave[nx][ny]
                            q.append((nx,ny))
        
        print("Problem " + str(cnt) + ": " + str(theif[n - 1][n - 1]))
        cnt += 1
    else:
        break
