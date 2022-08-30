# 이항 계수 2

n, k = map(int, input().split())

dp = [[1 for i in range(n + 2)] for i in range(n + 2)]

for j in range(1, n + 1):
    for i in range(1, j):
        dp[j][i] = dp[j - 1][i - 1] + dp[j - 1][i]

print(dp[n][k] % 10007)