# 벼락치기

n, t = map(int, input().split())
w = []
v = []
for i in range(n):
    time, point = map(int, input().split())
    w.append(time)
    v.append(point)

dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        if j >= w[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][t])

# n, t = map(int, input().split())
# dp = [0] * (t + 1)
# for _ in range(n):
#     w, v = map(int, input().split())
#     for i in range(t, w - 1, -1):
#         dp[i] = max(dp[i], dp[i - w] + v)

# print(dp[t])