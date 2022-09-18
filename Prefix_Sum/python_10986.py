# 나머지 합

import sys

n, m = map(int, sys.stdin.readline().split())



array = list(map(int, sys.stdin.readline().split())) + [0]
r = [0] * m


for i in range(n):
    array[i] += array[i - 1]
    r[array[i] % m] += 1

total = r[0]

for i in r:
    total += i * (i - 1) // 2

print(total)