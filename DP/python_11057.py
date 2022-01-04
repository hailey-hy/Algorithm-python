import sys

n = int(sys.stdin.readline())
total = 0
d = [[0] * 10 for j in range(n + 1)]

for i in range(10):
    d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j > 1:
            d[i][j] = d[i - 1][j] + d[i][j - 1]
        elif j == 1:
            d[i][j] = 1
        else:
            d[i][j] = sum(d[i - 1])

print(sum(d[n])%10007)
