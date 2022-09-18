# 인간-컴퓨터 상호작용

import sys

word = sys.stdin.readline().strip()

num = int(sys.stdin.readline())

word_sum = [0]
# a = 97 z = 122
for i in range(26):
    total = 0
    word_sum.append([0])
    for j in word:
        if ord(j) == i + 97:
            total += 1
            word_sum[i + 1].append(total)
        else:
            word_sum[i + 1].append(total)

for i in range(num):
    letter, x1, x2 = sys.stdin.readline().split()
    print(word_sum[ord(letter) - 96][int(x2) + 1] - word_sum[ord(letter) - 96][int(x1)])
