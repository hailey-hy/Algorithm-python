# 파이프 옮기기 1

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = []
for _ in range(n):
    tmp = []
    for t in range(n):
        tmp.append([0, 0, 0]) #-|/
    dp.append(tmp)

dp[0][1][0] = 1


for i in range(n):
    for j in range(n):
        if house[i][j] == 0:
            if i == 0 and 0 < j < n - 1:
                dp[i][j][0] += dp[i][j - 1][0]
 
            elif i > 0 and j > 0:
                #세로
                if house[i - 1][j] == 0:
                    if dp[i - 1][j][1] > 0:
                        dp[i][j][1] += dp[i - 1][j][1]
                    if dp[i - 1][j][2] > 0:
                        dp[i][j][1] += dp[i - 1][j][2]
                    
                #가로
                if house[i][j - 1] == 0:
                    if dp[i][j - 1][0] > 0:
                        dp[i][j][0] += dp[i][j - 1][0]
                    if dp[i][j - 1][2] > 0:
                        dp[i][j][0] += dp[i][j - 1][2]
                    
                #대각선
                if house[i - 1][j] == 0 and house[i][j - 1] == 0:
                    if dp[i - 1][j - 1][1] > 0:
                        dp[i][j][2] += dp[i - 1][j - 1][1]
                    if dp[i - 1][j - 1][0] > 0:
                        dp[i][j][2] += dp[i - 1][j - 1][0]
                    if dp[i - 1][j - 1][2] > 0:
                        dp[i][j][2] += dp[i - 1][j - 1][2]
        else:
            dp[i][j][0] = 0
        
print(sum(dp[n - 1][n - 1]))