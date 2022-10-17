# 자원 캐기

n, m = map(int, input().split())
jems = []
for _ in range(n):
    jems.append(list(map(int, input().split())))

dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = jems[i][j]
        elif i == 0 and j > 0:
            dp[i][j] = dp[i][j - 1] + jems[i][j]
        elif i > 0 and j == 0:
            dp[i][j] = dp[i - 1][j] + jems[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + jems[i][j]

print(dp[n - 1][m - 1])
        