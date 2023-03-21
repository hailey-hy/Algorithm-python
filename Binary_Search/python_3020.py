# 개똥벌레

import sys
from bisect import bisect_left

n, h = map(int, sys.stdin.readline().split())
up = []
down = []
for i in range(1, n + 1):
    if i % 2 != 0:
        up.append(int(sys.stdin.readline()))
    else:
        down.append(int(sys.stdin.readline()))

up.sort()
down.sort()

start = 0
end = h - 1
cnt = 1
total = n

for i in range(1, h + 1):
    t, b = bisect_left(up, i), bisect_left(down, h - i + 1)
    tmp = n - (t + b)
    if tmp < total:
        total = tmp
        cnt = 1
    elif tmp == total:
        cnt += 1

print(total, cnt)

