# 백남이의 여행 준비

import sys
import decimal

n, m = map(int, sys.stdin.readline().split())
w = []
v = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    w.append(a)
    v.append(b)
bags = [int(sys.stdin.readline().rstrip()) for _ in range(m)]

t = max(bags)
dp = [0 for _ in range(t + 1)]
for j in range(1, n + 1):
    weight = w[j - 1]
    value = v[j - 1]
    for k in range(t, weight - 1, -1):
        dp[k] = max(dp[k], dp[k - weight] + value)

total = 0
answer = 0
for index, i in enumerate(bags):
    tmp = decimal.Decimal(str(dp[i] / i))
    if float(tmp - decimal.Decimal(str(total))) > 0:
        answer = index + 1

print(answer)

