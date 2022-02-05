# 하노이의 탑

from pickle import APPEND


def hanoi(n):
    stack1 = [i for i in range(1, n + 1)]
    if len(stack2) == 0 and len(stack3) == 0:
        out = stack1.pop()
        stack3.append(out)
        out = stack1.pop()
        stack2.append(out)
        n -= 2
        return hanoi(n)
    elif len(stack2) != 0 or len(stack3) != 0:
        if stack2[-1] > stack3[-1]:
            out = stack3.pop()
            stack2.append(out)
            return hanoi(n)
        else:
            out = stack2.pop()
            stack3.append(out)
            return hanoi(n)

    elif len(stack1) == 0 and len(stack2) == 0 and stack3 == sorted(stack3): 
        return 
        


n = int(input())
stack2 = []
stack3 = []