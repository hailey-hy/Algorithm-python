# 스택

import sys

n = int(sys.stdin.readline())
stack = []

def stack_print():
    order = list(sys.stdin.readline().split())
    if "push" == order[0]:
        stack.append(int(order[1]))
    elif "top" == order[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif "size" == order[0]:
        print(len(stack))
    elif "empty" == order[0]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "pop" == order[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

for i in range(n):
    stack_print()