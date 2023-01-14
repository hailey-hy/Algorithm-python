# 신을 모시는 사당

import sys

n = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.readline().split()))
dp_max = [0] * n
dp_min = [0] * n

for i in range(n):
    if i == 0:
        if stones[i] == 1:
            dp_max[0] = 1
        else:
            dp_min[0] = 1
    else:
        if stones[i] == 1:
            dp_max[i] = max(dp_max[i - 1] + 1, dp_max[i])
            dp_min[i] = max(dp_min[i - 1] - 1, dp_min[i])
        else:
            dp_max[i] = max(dp_max[i - 1] - 1, dp_max[i])
            dp_min[i] = max(dp_min[i - 1] + 1, dp_min[i])

maximum = max(dp_max)
minimum = max(dp_min)
print(maximum if maximum > minimum else minimum)