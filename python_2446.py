# 별 찍기

n = int(input())

for i in range(1, n + 1,):
    max = 2 * i - 1
    min = 2 * n - max
    print(" " * (max // 2) + "*" * min)

for i in range(2, n + 1):
    max = 2 * i - 1
    min = 2 * n - max
    print(" " * (min // 2) + "*" * max)
