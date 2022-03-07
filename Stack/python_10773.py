# 제로

import sys
n = int(sys.stdin.readline())
stack = []

def total():
    money = int(sys.stdin.readline())
    if money == 0:
        stack.pop()
    else:
        stack.append(money)

for i in range(n):
    total()
    
print(sum(stack))