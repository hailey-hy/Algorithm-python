# 1, 2, 3 더하기

import sys

a = int(sys.stdin.readline())
d = [1] * (12)
d[2] = 2
d[3] = 4

for i in range(a):
    n = int(sys.stdin.readline())
    for i in range(4, n + 1):
        d[i] = d[i - 3] + d[i - 2] + d[i - 1]
    print(d[n])
