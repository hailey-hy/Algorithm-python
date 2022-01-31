# 피보나치 수

d = [0] * 21
d[1] = 1

n = int(input())

for i in range(2, n + 1):
    d[i] = d[i - 2] + d[i - 1]

print(d[n])