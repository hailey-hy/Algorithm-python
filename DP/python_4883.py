# 삼각 그래프

import sys

case = 0

while True:
    n = int(sys.stdin.readline())
    case += 1
    if n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    dp = [[sys.maxsize] * 3 for _ in range(n)]
    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][2] + graph[0][1]

    for i in range(1, n):
        for j in range(3):
            if j == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + graph[i][j]
            elif j == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1], dp[i - 1][j - 1], dp[i][j - 1]) + graph[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + graph[i][j]
    
    print(str(case) + '. ' + str(dp[-1][1]))