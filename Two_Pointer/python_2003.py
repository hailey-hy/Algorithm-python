# 수들의 합 2

import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
start = 0
end = 0
answer = 0

while start < n and end < n:
    length = end - start + 1
    total = 0
    for i in range(length):
        total += array[start + i]
    if total == m:
        answer += 1
        start += 1
    elif total > m:
        start += 1
    else:
        end += 1

print(answer)