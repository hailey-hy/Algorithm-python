# 구간 합 구하기 4

import sys

n, m = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))
array_sum = []
for i in range(n):
    if i == 0:
        array_sum.append(array[0])
    else:
        array_sum.append(array[i] + array_sum[i - 1])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a > 1:
        print(array_sum[b - 1] - array_sum[a - 2])
    else:

        print(array_sum[b - 1])