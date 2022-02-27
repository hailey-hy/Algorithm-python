# 포도주 시식

n = int(input())

d = [0] * 10001
wine = [0] * 10001

for i in range(1, n + 1):
    wine[i] = int(input())

d[1] = wine[1]
d[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    d[i] = max(d[i - 2] + wine[i], d[i - 1], d[i - 3] + wine[i - 1] + wine[i])

print(d[n])