# 오큰수

import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
result = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and array[stack[-1]] < array[i]:
        result[stack.pop()] = array[i]
    stack.append(i)

print(*result)
