# 부분합

import sys

n, s = map(int, sys.stdin.readline().split())
graph = list(map(int, sys.stdin.readline().split()))

answer = 0
length = sys.maxsize
start, end = 0, 0

while True:
    if answer >= s:
        length = min(length, end - start)
        answer -= graph[start]
        start += 1
    elif end == n:
        break
    else:
        answer += graph[end]
        end += 1


print(length if length < sys.maxsize else 0)