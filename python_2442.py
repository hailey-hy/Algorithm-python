#  첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제

n = int(input())
l = 2 * n - 1 #9

for i in range(1, n + 1):
    m = 2 * i - 1
    k = (l - m) // 2
    print(" " * k + "*" * m + " " * k)
