# 다리 놓기

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    num1 = 1
    num2 = 1
    for j in range(m, m - n, -1):
        num1 *= j
    for k in range(n, 1, -1):
        num2 *= k
    print(num1//num2)