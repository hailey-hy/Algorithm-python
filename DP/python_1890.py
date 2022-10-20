# 점프

n = int(input())

game = []
for _ in range(n):
    game.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if game[i][j] > 0 and dp[i][j] > 0:
            if i + game[i][j] < n:
                dp[i + game[i][j]][j] += 1
            if j + game[i][j] < n:
                dp[i][j + game[i][j]] += 1

print(dp[n - 1][n - 1])