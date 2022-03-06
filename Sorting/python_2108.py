# 통계학

import sys
from collections import Counter

n = int(sys.stdin.readline())

array = [int(input()) for i in range(n)]

array.sort()

total = sum(array)
if total >= 0:
    print(int(total/n + 0.5))
else:
    print(int(total/n - 0.5))

print(array[n//2])

cnt = Counter(array).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(array[-1] - array[0])