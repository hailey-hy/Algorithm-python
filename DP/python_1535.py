# 안녕

n = int(input())

hearts = list(map(int, input().split()))
joys = list(map(int, input().split()))

dp = [0] * (101)

heart = 100

for i in range(n):
    for j in range(99, 0, -1):
        if hearts[i] <= j:
            dp[j] = max(dp[j], dp[j-hearts[i]] + joys[i])

print(max(dp))