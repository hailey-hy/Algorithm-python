# 회전하는 큐

import sys

n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
array = [i + 1 for i in range(n)]
trial = 0

while targets:
    if array[0] == targets[0]:
        targets.pop(0)
        array.append(array.pop(0))
    elif array.index(targets[0]) < (n // 2):
        
