# AC

import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    order = sys.stdin.readline().strip()
    num = int(sys.stdin.readline())
    array = deque(eval(sys.stdin.readline()))

    r_num = 0
    e_num = 0
    answer = True

    for j in order:
        if j == 'R':
            r_num += 1
        else:
            if len(array)== 0:
                print('error')
                answer = False
                break
            if r_num % 2 == 0:
                array.popleft()
            else:
                array.pop()

    if r_num % 2 == 1:
        array.reverse()

    if answer:
        print("[" + ','.join(map(str, array)) + "]")