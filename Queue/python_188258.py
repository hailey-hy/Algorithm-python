# 큐 2

from collections import deque
import sys

integer = deque([])
n = int(sys.stdin.readline())

for i in range(n):
    order = list(sys.stdin.readline().split())
    if "push" in order:
        integer.append(order[1])
    elif "front" in order:
        if not integer:
            print(-1)
        else:
            print(integer[0])
    elif "back" in order:
        if not integer:
            print(-1)
        else:
            print(integer[-1])
    elif "size" in order:
        print(len(integer))
    elif "pop" in order:
        if not integer:
            print(-1)
        else:
            print(integer.popleft())
    elif "empty" in order:
        if not integer:
            print(1)
        else:
            print(0)
    