# 공통 부분 문자열

import sys

word1 = list(sys.stdin.readline().rstrip())
word2 = list(sys.stdin.readline().rstrip())
dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
for i in range(1, len(word2) + 1):
    for j in range(1, len(word1) + 1):
        if word2[i - 1] == word1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

print(max(map(max, dp)))