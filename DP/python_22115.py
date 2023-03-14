# 창영이와 커피

import sys

n, k = map(int, sys.stdin.readline().split())
coffees = list(map(int, sys.stdin.readline().split()))

dp = [0] + [sys.maxsize] * k

for coffee in coffees:
    dp_max = dp.copy()
    for i in range(coffee, k + 1):
        dp[i] = min(dp[i], dp_max[i - coffee] + 1)

if dp[k] >= sys.maxsize:
    print(-1)
else:
    print(dp[k])