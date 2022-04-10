# 프린터 큐

import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    array_priorities = [i + 1 for i in range(n)]
    array_printed = []
    target = array_priorities[m]
    while array:
        first = array.pop(0)
        if (len(array) == 0) or (first >= max(array)):
            array_printed.append(first)
            if target == array_priorities[0]:
                print(len(array_printed))
                break
            else:
                array_priorities.pop(0)
        else:
            array.append(first)
            array_priorities.append(array_priorities.pop(0))
