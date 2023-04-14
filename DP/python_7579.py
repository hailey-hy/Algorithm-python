# 앱

import sys

n, m = map(int, sys.stdin.readline().split())
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

total = sum(c)
result = sum(c)

dp = [0] * (total + 1)

for i in range(n):
    bite = b[i]
    cost = c[i]
    for j in range(total, cost - 1, -1):
        if cost <= j:
            dp[j] = max(dp[j], dp[j - cost] + bite)
        if dp[j] >= m:
            result = min(result, j)

if m != 0:
    print(result)
else:
    print(0)