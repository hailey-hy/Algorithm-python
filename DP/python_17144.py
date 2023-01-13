# 미세먼지 안녕!

from collections import deque

n, m, t = map(int, input().split())
room = []
air_n = []
air_m = []
for i in range(n):
    tmp = list(map(int, input().split()))
    if -1 in tmp:
        air_n.append(i)
        air_m.append(0)
    room.append(tmp)

dx = [0, 0, 1, -1] #오른/왼/아래/위
dy = [1, -1, 0, 0]

def dust():
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if room[i][j] > 0:
                now = room[i][j]
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < m and room[x][y] > -1:
                        new = int(room[i][j] / 5)
                        dp[x][y] += new
                        now -= new
                dp[i][j] += now
            elif room[i][j] == -1:
                dp[i][j] = -1
    return dp

    
def clean():
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if room[i][j] > -1:
                #위쪽 순환 아래쪽 모서리, 아래쪽 순환 위쪽 모서리
                if room[i][j - 1] > -1 and ((i == air_n[0] and j <= m - 1) or (i == air_n[1] and j <= m - 1)):
                    dp[i][j] = room[i][j - 1]
                #위쪽 순환 오른쪽 모서리, 아래쪽 순환 왼쪽 모서리
                elif (0 <= i < air_n[0] and j == m - 1) or (air_n[1] <= i < n - 1 and j == 0):
                    dp[i][j] = room[i + 1][j]
                #위쪽 순환 위쪽 모서리, 아래쪽 순환 아래쪽 모서리
                elif ((i == 0 and 0 <= j < m - 1) or (i == n - 1 and j < m - 1)) and room[i][j + 1] > -1:
                    dp[i][j] = room[i][j + 1]
                #위쪽 순환 왼쪽 모서리, 아래쪽 순환 오른쪽 모서리
                elif (0 < i <= air_n[0] and j == 0) or (air_n[1] <= i < n and j == m - 1):
                    dp[i][j] = room[i - 1][j]
                else:
                    if i not in air_n:
                        dp[i][j] = room[i][j]
            else:
                dp[i][j] = room[i][j]
    return dp

    

for _ in range(t):
    room = dust()
    room = clean()

total = 0
for i in range(n):
    total += sum(room[i])

print(total + 2)