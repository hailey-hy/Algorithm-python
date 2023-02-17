# 수강과목

import sys

n, k = map(int, sys.stdin.readline().split())
v = [0]
w = [0]
for _ in range(k):
    point, time = map(int, sys.stdin.readline().split())
    v.append(point)
    w.append(time)

dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        if j >= w[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[k][n])