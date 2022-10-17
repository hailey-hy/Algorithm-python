# 병사 배치하기

n = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * (n + 1)

for i in range(1, n):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

