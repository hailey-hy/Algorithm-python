# 카우버거 알바생

import sys

n, m, k = map(int, sys.stdin.readline().split())

dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

bur = []
fri = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    bur.append(a)
    fri.append(b)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1, k + 1):
            if bur[i - 1] <= j and fri[i - 1] <= k:
                dp[i][j][k] = max(1 + dp[i - 1][j - bur[i - 1]][k - fri[i - 1]], dp[i - 1][j][k])
            else:
                dp[i][j][k] = dp[i - 1][j][k]

print(dp[n][m][k])