# LCS 2
import sys

word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()

length1 = len(word1)
length2 = len(word2)

LCS = [[''] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if word1[i - 1] == word2[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + word1[i - 1]
        else:
            if len(LCS[i - 1][j]) >= len(LCS[i][j - 1]):
                LCS[i][j] = LCS[i - 1][j]
            else:
                LCS[i][j] = LCS[i][j - 1]

print(len(LCS[-1][-1]))
print(LCS[-1][-1])