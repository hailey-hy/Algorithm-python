# 점프 점프

n = int(input())

maze = list(map(int, input().split()))

dp = [n] * (n + 1) #점프한 횟수를 저장

dp[0] = 0

for i in range(n):
    for j in range(1, maze[i] + 1):
        if i + j < n: # 범위를 벗어나지 않도록 조절
            dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == n + 1:
	print(-1)
else:
	print(dp[n - 1])