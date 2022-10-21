# 기타리스트

n, start, maximum = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [[0] * (maximum + 1) for _ in range(n + 1)]

dp[0][start] = 1

for i in range(1, n + 1):
    for j in range(maximum + 1):
        if dp[i - 1][j] != 0:
            if 0 <= j + volumes[i - 1] <= maximum:
                dp[i][j + volumes[i - 1]] = 1
            if 0 <= j - volumes[i - 1] <= maximum:
                dp[i][j - volumes[i - 1]] = 1

result = -1

for i in range(maximum, -1, -1):
    if dp[n][i] == 1:
        result = i
        break

print(result)