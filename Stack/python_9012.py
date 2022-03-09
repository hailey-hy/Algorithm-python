# 괄호

import sys

n = int(sys.stdin.readline())

def VPS(stack):
    if len(stack) = 0:
        return "YES"
    elif len(stack) == 1 and stack[0] == "(":
        stack.pop()
        return "YES"
    elif stack[-1] == ")":
        stack.pop()
        for k in range(len(stack)):
            if stack[-1] == "(":
                stack.pop()
                VPS(stack)
            else:
                stack.pop()
    else:
        return "NO"

for i in range(n):
    stack = []
    for j in input():
        stack.append(j)
    print(VPS(stack))