# 호텔

import sys

c, n = map(int, sys.stdin.readline().split())
pr = []
for _ in range(n):
    cost, customer = map(int, sys.stdin.readline().split())
    pr.append((cost, customer))
pr.sort(key=lambda x:x[0])

dp = [sys.maxsize] * (c + 100)
dp[0] = 0
for cost, customer in pr:
    for i in range(customer, c + 100):
        dp[i] = min(dp[i - customer] + cost, dp[i])

print(min(dp[c:]))