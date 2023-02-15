# 두 용액

import sys

n = int(sys.stdin.readline().rstrip())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

start = 0
end = n - 1

total = abs(liquid[start] + liquid[end])
final = [liquid[start], liquid[end]]

while start < end:
    start_val = liquid[start]
    end_val = liquid[end]
    result = start_val + end_val

    if abs(result) < total:
        total = abs(result)
        final = [start_val, end_val]
        if total == 0:
            break

    if result < 0:
        start += 1
    else:
        end -= 1

print(final[0], final[1])