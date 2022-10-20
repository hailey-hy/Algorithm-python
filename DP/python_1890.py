# 점프

n = int(input())

game = []
for _ in range(n):
    game.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if game[i][j] > 0 and dp[i][j] > 0:
            if i + game[i][j] < n:
                tmp = True
                for k in range(1, game[i][j] + 1):
                    if game[i + k][j] == 0 and not(i  + k== n - 1 and j == n - 1):
                        tmp = False
                if tmp == True or i == n - 2 and j == n - 1:
                    dp[i + game[i][j]][j] += dp[i][j]
            if j + game[i][j] < n:
                tmp = True
                for k in range(1, game[i][j] + 1):
                    if game[i][j + k] == 0 and not(i == n - 1 and j + k == n - 1):
                        tmp = False
                if tmp == True or i == n - 1 and j == n - 2:
                    dp[i][j + game[i][j]] += dp[i][j]

print(dp[n - 1][n - 1])
