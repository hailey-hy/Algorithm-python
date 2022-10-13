# 1, 2, 3 더하기 3

n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for j in range(4, 1000001):
    dp[j] = (dp[j - 3] + dp[j - 2] + dp[j - 1]) % 1000000009 

for i in range(n):
    num = int(input())
    print(dp[num])