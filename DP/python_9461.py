# 파도반 수열

import sys
t = int(sys.stdin.readline())

d = [0] * 100001

d[0] = 1
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 2

for i in range(t):
    n = int(sys.stdin.readline())
    for j in range(5, n):
        d[j] = d[j - 5] + d[j - 1]
    print(d[n - 1])
