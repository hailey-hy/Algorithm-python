# 요세푸스 문제 0

import sys
from collections import deque
numbers = deque([])

n, k = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    numbers.append(i)

print("<", end="")
for i in range(n):
    cnt = 1
    while cnt < k:
        numbers.append(numbers.popleft())
        cnt += 1
    if n <= 1:
        print(numbers.popleft(), end="")
    else:
        if i == n - 1:
            print(numbers.popleft(), end="")
        else:
            print(str(numbers.popleft()) + ",", end=" ")
print(">")