# 덱

import sys
from collections import deque

n = int(sys.stdin.readline())
array = deque([])

for i in range(n):
    statement = list(sys.stdin.readline().split())
    if "push_front" in statement:
        array.appendleft(int(statement[1]))
    elif "push_back" in statement:
        array.append(int(statement[1]))
    elif "pop_front" in statement:
        if array:
            print(array.popleft())
        else:
            print(-1)
    elif "pop_back" in statement:
        if array:
            print(array.pop())
        else:
            print(-1)
    elif "size" in statement:
        print(len(array))
    elif "empty" in statement:
        if array:
            print(0)
        else:
            print(1)
    elif "front" in statement:
        if array:
            print(array[0])
        else:
            print(-1)
    elif "back" in statement:
        if array:
            print(array[-1])
        else:
            print(-1)


    