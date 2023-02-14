# 한글 LCS

import sys

word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()

length1 = len(word1)
length2 = len(word2)

LCS = [[0] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if word1[i - 1] == word2[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i][j - 1], LCS[i - 1][j])

print(LCS[-1][-1])