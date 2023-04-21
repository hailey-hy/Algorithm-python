# 세 용액

import sys

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

result = sys.maxsize
answer = []

for i in range(n - 2):
    left = i + 1
    right = n - 1
    while left < right:
        tmp = liquid[left] + liquid[right] + liquid[i]
        if abs(tmp) < result:
            result = abs(tmp)
            answer = [liquid[i], liquid[left], liquid[right]]
        if tmp < 0:
            left += 1
        elif tmp > 0:
            right -= 1
        else:
            break

print(*answer)