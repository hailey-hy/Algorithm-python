# 수도배관공사

import sys

d, p = map(int, input().split())
dp = [sys.maxsize] + [0] * d

for _ in range(p):
    dp_max = dp.copy()
    l, v = map(int, input().split())
    for i in range(l, d + 1):
        if dp_max[i - l]:
            dp[i] = max(dp[i], min(dp_max[i - l], v))

print(dp[d])