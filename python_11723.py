# 집합

import sys

n = int(sys.stdin.readline())
result = set()

for i in range(n):
    order = list(sys.stdin.readline().split())

    if order[0] == 'all':
        result = set([i for i in range(1, 21)])

    elif order[0] == 'empty':
        result = set()

    elif order[0] == 'add':
        result.add(int(order[-1]))
    
    elif order[0] == 'check':
        print(1 if int(order[-1]) in result else 0)
    
    elif order[0] == 'remove':
        result.discard(int(order[-1]))
    
    elif order[0] == 'toggle':
        if int(order[-1]) in result:
            result.discard(int(order[-1]))
        else:
            result.add(int(order[-1]))
                