# Coins

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    coins = [0] + list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    dp = [[0] * (m + 1) for i in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            if coins[i] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[-1][-1])