# 수 정렬하기 3

import sys

n = int(sys.stdin.readline())
counts = [0] * 10001

for i in range(n):
    counts[int(sys.stdin.readline())] += 1

for i in range(10001):
    if counts[i] != 0:
        for j in range(counts[i]):
            print(i)
